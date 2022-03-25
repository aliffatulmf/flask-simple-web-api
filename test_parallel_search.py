import unittest
import data
import lib.parallel as parallel


class TestParallelFind(unittest.TestCase):

    def setUp(self):
        self.data = data.MANGA_LIST
        self.assertEqual(type(self.data), list)

    def test_parallel(self):
        id = 2
        n = parallel.parallel_search(self.data, id)

        self.assertIs(type(n[0]), dict)
        self.assertEqual(n[0]["id"], id)


if __name__ == "__main__":
    unittest.main()
