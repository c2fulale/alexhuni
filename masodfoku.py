import unittest
import math
def masodfoku(a:int,b:int,c:int)->int:
    return -b +-math.sqrt((b*b)-4*a*c)/2*a

class teszkegyenletegesz(unittest.TestCase):
    def masodfoku_egyenlet_test(self):
        fgv=masodfoku(2,-2,-2,)
        self.assertEqual(fgv,10)


unittest.main()