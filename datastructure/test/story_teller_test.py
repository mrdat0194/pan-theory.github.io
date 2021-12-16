from datastructure.story_teller import story_teller

import unittest

class TestStory(unittest.TestCase):

    def test_story_teller(self):
        # arr = [4,3,1,2]
        # res = story_teller.minimumSwaps(arr)
        # self.assertEqual(res, 3)

        arr = [5,1,2,3,4]
        res = story_teller.minimumBribes(arr)
        self.assertEqual(res, 4)


if __name__ == '__main__':

    unittest.main()
