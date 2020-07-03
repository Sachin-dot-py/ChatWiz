import pandas as pd
from datetime import datetime


class WhatsAppAnalyzer():
    """ Analyze WhatsApp data and get statistics """
    def __init__(self, content=None, df=None):
        """
        Either content or dataframe is required
        """
        if df:
            self.df = df
        elif not content and not df:
            raise AssertionError("No Dataframe or content passed")
        else:
            self.df = self.parse_chat(content)

    def parse_chat(self, content) -> pd.DataFrame:
        """ Parses content and returns a Dataframe with contact, datetime object and message """
        lines = content.splitlines()
        if "end-to-end encryption" in lines[0]:
            lines.pop(0)  # Remove message about end-to-end encryption
        messages = []
        for line in lines:
            try:
                date_str = line.split(' - ')[0]
                contact = line.split(' - ')[1].split(':')[0]
                message = line.split(':')[2].lstrip(' ')
                date = datetime.strptime(date_str, "%d/%m/%Y, %I:%S %p")
            except:  # For multi-line messages
                prev_msg = messages[-1].get('message') + "\n"
                messages[-1]['message'] = prev_msg + message
            else:
                message_data = {
                    'contact': contact,
                    'date': date,
                    'message': message
                }
                messages.append(message_data)
        df = pd.DataFrame(messages)
        return df

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


if __name__ == "__main__":
    file = 'sample_chat/sample_chat.txt'  # Chat data exported from WhatsApp
    with open(file) as f:
        content = f.read()
    analyzer = WhatsAppAnalyzer(content)
