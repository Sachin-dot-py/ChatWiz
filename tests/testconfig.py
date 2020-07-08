from datetime import datetime
import pandas as pd

tests = {
    'sample_chat/sample_chat.txt': {
        "TOTAL_MESSAGES": 128,
        "START_DATE": "29/09/2019, 12:56 pm",
        "END_DATE": "03/07/2020, 4:32 pm",
        "TOTAL_DAYS": 278,
        "TOTAL_WORDS": 735,
        "TOTAL_LETTERS": 3922,
        "TOTAL_MEDIA": 106,
        "CHAT_NAME" : 'WhatsApp Group',
        "MOST_ACTIVE_DATE" : ('December 11, 2019', 31),
        "MOST_ACTIVE_DAY" : 'Wednesday',
        "HIGHEST_MESSAGES" : 'Sachin',
        "HIGHEST_WORDS" : ('Sachin', 650),
        "TOTAL_DELETED" : 0,
        "AVERAGE_MESSAGES" : 0
    }
}

for test, test_dict in tests.items():  # Turning strings into Pandas Timestamp objects
    f_msg = test_dict['START_DATE']
    f_dt = datetime.strptime(f_msg, "%d/%m/%Y, %I:%M %p")
    f_ts = pd.Timestamp(f_dt)
    l_msg = test_dict['END_DATE']
    l_dt = datetime.strptime(l_msg, "%d/%m/%Y, %I:%M %p")
    l_ts = pd.Timestamp(l_dt)
    test_dict['START_DATE'] = f_ts
    test_dict['END_DATE'] = l_ts
