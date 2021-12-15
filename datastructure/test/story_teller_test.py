from datastructure.story_teller import story_teller

import unittest

class TestStory(unittest.TestCase):

    def test_story_teller(self):
        arr = [4,3,1,2]
        res = story_teller.minimumSwaps(arr)
        self.assertEqual(res, 3)


if __name__ == '__main__':

    unittest.main()
