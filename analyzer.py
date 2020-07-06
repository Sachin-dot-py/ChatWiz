import pandas as pd
from datetime import datetime


class WhatsAppAnalyzer():
    """ Analyze WhatsApp data and get statistics """
    def __init__(self, content=None, df=None, file=None):
        """
        Either content or dataframe is required
        """
        if df:
            self.df = df
        elif not content and not df and not file:
            raise AssertionError("No Dataframe or content passed")
        else:
            if file:
                with open(file) as f:
                    content = f.read()
            self.df = self.parse_chat(content)
        self.userdf = self.parse_user()

    def parse_chat(self, content) -> pd.DataFrame:
        """ Parses content and returns a Dataframe with contact, datetime object and message """
        lines = content.splitlines()
        if "end-to-end encryption" in lines[0]:
            lines.pop(0)  # Remove message about end-to-end encryption
        messages = []
        for line in lines:
            try:
                media = 0
                date_str = line.split(' - ')[0]
                contact = line.split(' - ')[1].split(':')[0]
                try:
                    message = line.split(':')[2].lstrip(' ')
                except:
                    continue  # Automatic messages such as "XX person left", "XX added YY" etc.
                if message == "<Media omitted>":
                    media = 1
                    message = ""
                date = datetime.strptime(date_str, "%d/%m/%Y, %I:%S %p")
                words = len(message.split())
                letters = len(message.replace(" ", "").replace("\n", ""))
            except:  # For multi-line messages
                prev_msg = messages[-1].get('message') + "\n"
                new_msg = prev_msg + line
                messages[-1]['message'] = new_msg
                messages[-1]['words'] = len(new_msg.split())
                messages[-1]['letters'] = len(
                    new_msg.replace(" ", "").replace("\n", ""))
            else:
                message_data = {
                    'contact': contact,
                    'date': date,
                    'media': media,
                    'message': message,
                    'words': words,
                    'letters': letters
                }
                messages.append(message_data)
        df = pd.DataFrame(messages)
        return df

    def parse_user(self) -> dict:
        """ Parse dataframe to get user dataframe with count of messages, media and more per user """
        user_table = {k: table for k, table in self.df.groupby("contact")}
        return user_table

    @property
    def first_message_date(self) -> pd.Timestamp:
        """
        Get day of first message as a pandas Timestamp object
        """
        first = self.df.at[0, 'date']
        return first

    @property
    def last_message_date(self) -> pd.Timestamp:
        """
        Get day of last message as a pandas Timestamp object
        """
        last = self.df.at[len(self.df) - 1, 'date']
        return last

    @property
    def total_days(self) -> int:
        """
        Get total number of days between first and last message
        """
        days = (self.last_message_date - self.first_message_date).days
        return days

    @property
    def total_messages(self) -> int:
        """ Get total number of messages """
        return len(self.df)

    @property
    def total_words(self) -> int:
        """ Get total number of words """
        return self.df['words'].sum()

    @property
    def total_letters(self) -> int:
        """ Get total number of letters """
        return self.df['letters'].sum()

    @property
    def total_media(self) -> int:
        """ Gets total number of media """
        return self.df['media'].sum()

    def get_user(self, name) -> dict:
        """ Returns dict of statistics for the given user name """
        try:
            user = self.userdf[name]
        except:
            raise AssertionError(f"User {name} does not exist")
        media = user['media'].sum()
        words = user['words'].sum()
        letters = user['letters'].sum()
        messages = len(user) - media
        words_per_message = int(words / messages)
        letters_per_word = int(letters / words)
        userdict = {
            'messages': messages,
            'media': media,
            'words': words,
            'letters': letters,
            'words_per_message': words_per_message,
            'letters_per_word': letters_per_word
        }
        return userdict


if __name__ == "__main__":
    file = 'sample_chat/sample_chat.txt'  # Chat data exported from WhatsApp
    with open(file) as f:
        content = f.read()
    analyzer = WhatsAppAnalyzer(content)
