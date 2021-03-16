import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_win_fel(self):
        self.assertEqual([1, 1, 1, 1], list(main.win_fil([1, 1, 1, 1, 1], 5, 0, 2)))


    def test_append_buffer(self):
        self.assertEqual([1, 2, 3, 4], main.append_buffer(4, [1, 2, 3]))


    def test_aver(self):
        self.assertEqual([1], main.fill_buffer(list([1,1,1]),list([]), main.aver))



if __name__ == '__main__':
    unittest.main()
