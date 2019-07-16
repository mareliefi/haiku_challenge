import unittest
from haiku_exercise import haiku_checker

class testHaiku(unittest.TestCase):

  def testCorrectHaikuReturnSuccess(self):
    '''Tests that haiku_checker returns true'''
    line_1 = ("I am a baboon").split(" ")
    line_2 = ("I walk with hat and balloon").split(" ")
    line_3 = ("I am a bafoon").split(" ")
    self.assertEqual(haiku_checker(line_1,line_2,line_3),True)

  def testCorrectHaikuReturnFail(self):
    '''Tests that haiku_checker returns fail'''
    line_1 = ("I am not a baboon").split(" ")
    line_2 = ("I walk with hat, cane and spoon").split(" ")
    line_3 = ("I am a tutored loon").split(" ")
    self.assertEqual(haiku_checker(line_1,line_2,line_3),False)

'''
TestSuite.addTest(testHaiku("testCorrectHaikuReturnSuccess"))
TestSuite.addTest(testHaiku("testCorrectHaikuReturnFail"))
runner = unittest.TextTestRunner()
runner.run(TestSuite)
'''


