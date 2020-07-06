import unittest
import sys
import os
from datetime import datetime
from testconfig import TOTAL_DAYS, TOTAL_MESSAGES, FIRST_MESSAGE_DATE, LAST_MESSAGE_DATE, TOTAL_LETTERS, TOTAL_WORDS, TOTAL_MEDIA

# Append package directory to path to import modules
PACKAGE_DIR = os.path.abspath(os.path.join(__file__, '../..'))
sys.path.append(PACKAGE_DIR)


class TestMain(unittest.TestCase):
    def test_statistics(self):
        """ Test the parsing of the sample WhatsApp chat """
        from analyzer import WhatsAppAnalyzer
        file = 'sample_chat/sample_chat.txt'  # Chat data exported from WhatsApp
        self.wa = WhatsAppAnalyzer(file)
        self.assertEqual(self.wa.total_messages, TOTAL_MESSAGES)
        self.assertEqual(
            self.wa.first_message_date,
            datetime.strptime(FIRST_MESSAGE_DATE, "%d/%m/%Y, %I:%S %p"))
        self.assertEqual(
            self.wa.last_message_date,
            datetime.strptime(LAST_MESSAGE_DATE, "%d/%m/%Y, %I:%S %p"))
        self.assertEqual(self.wa.total_days, TOTAL_DAYS)
        self.assertEqual(self.wa.total_words, TOTAL_WORDS)
        self.assertEqual(self.wa.total_letters, TOTAL_LETTERS)
        self.assertEqual(self.wa.total_media, TOTAL_MEDIA)


if __name__ == "__main__":
    unittest.main()
