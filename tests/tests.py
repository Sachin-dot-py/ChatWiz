import unittest
import sys
import os
from datetime import datetime

# Append package directory to path to import modules
PACKAGE_DIR = os.path.abspath(os.path.join(__file__, '../..'))
sys.path.append(PACKAGE_DIR)


class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from testconfig import tests
        from analyzer import WhatsAppAnalyzer
        cls.tests = {
            WhatsAppAnalyzer(file): expected_results
            for file, expected_results in tests.items()
        }

    def test_statistics(self):
        """ Test the parsing of the sample WhatsApp chat """
        for wa, expected_results in self.tests.items():
            with self.subTest(chat=wa.file):
                results = {
                    "TOTAL_MESSAGES": wa.total_messages,
                    "START_DATE": wa.first_message_date,
                    "END_DATE": wa.last_message_date,
                    "TOTAL_DAYS": wa.total_days,
                    "TOTAL_WORDS": wa.total_words,
                    "TOTAL_LETTERS": wa.total_letters,
                    "TOTAL_MEDIA": wa.total_media,
                    "CHAT_NAME" : wa.name,
                    "MOST_ACTIVE_DATE" : wa.most_active_date,
                    "MOST_ACTIVE_DAY" : wa.most_active_day,
                    "HIGHEST_MESSAGES" : wa.highest_messages,
                    "HIGHEST_WORDS" : wa.highest_words,
                    "TOTAL_DELETED" : wa.total_deleted,
                    "AVERAGE_MESSAGES" : wa.average_messages
                }
                self.assertEqual(expected_results, results)


if __name__ == "__main__":
    unittest.main()
