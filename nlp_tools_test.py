"""
Ethan Price
Section AC
Runs unit tests on functions from
nlp_tools
"""


import unittest
import nlp_tools as nlp


class ToolsTest(unittest.TestCase):
    """
    Tests functions from the nlp_tools module
    """
    def test_get_sentiment(self):
        """
        Tests get_sentiment function from nlp_tools
        """
        self.assertEqual(-1.0,
                         nlp.get_sentiment("horrible terrible worst thing"))
        self.assertEqual(1.0, nlp.get_sentiment("wonderful best thing ever"))
        self.assertEqual(0.0, nlp.get_sentiment("wonderful horrible"))

        # Expected polarity given from TextBlob documentation
        self.assertEqual(0.39166666666666666,
                         nlp.get_sentiment("Textblob is"
                                           "amazingly simple to use."
                                           "What great fun!"))


if __name__ == '__main__':
    unittest.main()