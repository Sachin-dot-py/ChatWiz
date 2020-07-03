import unittest
import sys
import os

# Append package directory to path to import modules
PACKAGE_DIR = os.path.abspath(os.path.join(__file__, '../..'))
sys.path.append(PACKAGE_DIR)


class TestMain(unittest.TestCase):
    def test_parse_file(self):
        """ Test the parsing of the sample WhatsApp chat """
        from main import parse_chat
        file = 'sample_chat/sample_chat.txt'  # Chat data exported from WhatsApp
        with open(file) as f:
            content = f.read()
        df = parse_chat(content)
        self.assertEqual(len(df), 8)  # Change this if sample chat is changed


if __name__ == "__main__":
    unittest.main()
