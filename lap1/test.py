from vowelnum import vowelnum
from index import index
from multipli import multipli
from dictions import dictions
import unittest



class TestAssignmentOne(unittest.TestCase):

    def test_vowelnum(self):
        self.assertEqual(vowelnum('mobile'), 'mbl')
        self.assertEqual(vowelnum('MOBILE'), 'MBL')
        self.assertEqual(vowelnum('MobIlE'), 'Mbl')


    def test_index(self):
        self.assertEqual(index('This is javaScript','i'), [2,5,15])
    
    def test_multipli(self):
        self.assertEqual(multipli(3), [[1],[2,4],[3,6,9]])



    
    def test_dictions(self):
        l1 = ["ahmed", "fatma", "ibrahim"]
        d1 = {'a':['ahmed'], 'f':['fatma'],'i':['ibrahim']}
        self.assertEqual(dictions(l1),d1)

if __name__ == '__main__':
    unittest.main()