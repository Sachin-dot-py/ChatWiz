import pandas as pd
from datetime import datetime


def parseChat(content: str) -> pd.DataFrame:
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


if __name__ == "__main__":
    file = 'wac.txt'  # Chat data exported from WhatsApp
    with open(file) as f:
        content = f.read()
    df = parseChat(content)
    df.to_csv(file.replace('.txt', '.csv'))
    print(df)
