import unittest

from ant import Ant

class TestImages (unittest.TestCase) :

  def testAntHasImage (self) :
    a = Ant()
    self.assertNotEqual(a.image, None, "Ant has no image")
    self.assertNotEqual(a.rect, None, "Ant has no rect")

if __name__ == "__main__" :
  unittest.main()
