import unittest

def osszead(a:int, b: int) -> int:
    return a+b


szamok=[1,2,3]


class TesztOsszeadas(unittest.TestCase):

    def tearDown(self):
        szamok.clear()
        print(szamok)


    def test_two_positive(self):
        fgv=osszead(1,-2)
        self.assertGreater(fgv,0 )



    def test_two_zero(self):
        fgv=osszead(0,0)
        self.assertEqual(fgv,0)


unittest.main()
"""
print(osszead(1,2))
print(osszead(0,0))
print(osszead(-2,5))
print(osszead(-2,-3))
"""