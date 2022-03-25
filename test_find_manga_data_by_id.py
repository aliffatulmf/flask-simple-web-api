import unittest
import data
from multiprocessing import Process, Manager
from time import sleep


class TestFindMangaDataById(unittest.TestCase):

    def setUp(self):
        self.data = data.MANGA_LIST
        self.assertEqual(type(self.data), list)

    def multiprocess(self, id, iter, ns):
        self.assertIs(type(id), int)
        if iter["id"] == id:
            ns.match = iter

    def test_find_by_id(self):
        manager = Manager()
        ns = manager.Namespace()
        jobs = []

        id = 2
        for x in self.data:
            p = Process(target=self.multiprocess, args=(id, x, ns))
            p.daemon = True
            jobs.append(p)

        for x in jobs:
            x.run()

        self.assertIs(type(ns.match), dict)


if __name__ == "__main__":
    unittest.main()
