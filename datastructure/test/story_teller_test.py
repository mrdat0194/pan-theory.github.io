from datastructure.story_teller import story_teller

import unittest

class TestStory(unittest.TestCase):

    def test_story_teller(self):
        arr = [4,3,1,2]
        res = story_teller.minimumSwaps(arr)
        self.assertEqual(res, 3)

        arr = [5,1,2,3,4]
        res = story_teller.minimumBribes(arr)
        self.assertEqual(res, 4)

        # freqQuery: 1 is insert, 2 is delete, 3 is query, which has n frequency
        arr = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
        res = story_teller.freqQuery(arr)
        self.assertEqual(res, [0, 1])



if __name__ == '__main__':

    unittest.main()
