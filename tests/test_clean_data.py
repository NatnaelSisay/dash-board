import unittest
import clean_data
class TestCleanData(unittest.TestCase):

  def test_clean_tweet_has_2_columns(self):
    row, columns = clean_data.cleanTweet.shape
    self.assertTrue(columns,2)
