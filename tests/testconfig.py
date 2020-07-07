from datetime import datetime

tests = {
    'sample_chat/sample_chat.txt': {
        "TOTAL_MESSAGES": 128,
        "START_DATE": "29/09/2019, 12:56 pm",
        "END_DATE": "03/07/2020, 4:32 pm",
        "TOTAL_DAYS": 278,
        "TOTAL_WORDS": 693,
        "TOTAL_LETTERS": 3589,
        "TOTAL_MEDIA": 106
    }
}

for test, test_dict in tests.items():  # Turning strings into datetime objects
    f_msg = test_dict['START_DATE']
    l_msg = test_dict['END_DATE']
    test_dict['START_DATE'] = datetime.strptime(f_msg, "%d/%m/%Y, %I:%S %p")
    test_dict['END_DATE'] = datetime.strptime(l_msg, "%d/%m/%Y, %I:%S %p")
