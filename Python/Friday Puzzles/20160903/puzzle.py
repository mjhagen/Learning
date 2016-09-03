import unittest

# Main function:
class ByteConverter:
  def __init__(self):
    self.oneKiB=2**10
    self.prefixes=['','Ki','Mi','Gi','Ti','Pi','Ei']

  def toHumanReadable(self,numberOfBytes):
    if numberOfBytes <= 0:
      raise ValueError('Input must be > 0')

    if numberOfBytes > 2**63-1:
      raise ValueError('Input must be < 2^63')

    for prefix in self.prefixes:
      if numberOfBytes < self.oneKiB:
        return '%i %sB' % (numberOfBytes,prefix)
      numberOfBytes /= self.oneKiB

# Unit Tests Below:
class Test_ByteConverter(unittest.TestCase):
  def setUp(self):
    self.byteConverter = ByteConverter()

  def test_one_byte(self):
    self.assertEqual(self.byteConverter.toHumanReadable(1),'1 B')
  def test_one_kibibyte(self):
    self.assertEqual(self.byteConverter.toHumanReadable(1024),'1 KiB')
  def test_one_mebibyte(self):
    self.assertEqual(self.byteConverter.toHumanReadable(1048576),'1 MiB')
  def test_another_mebibyte(self):
    self.assertEqual(self.byteConverter.toHumanReadable(1234567),'1 MiB')
  def test_nine_gibibytes(self):
    self.assertEqual(self.byteConverter.toHumanReadable(9999999999),'9 GiB')
  def test_cellar(self):
    self.assertRaises(ValueError,self.byteConverter.toHumanReadable,-5)
  def test_attic(self):
    self.assertRaises(ValueError,self.byteConverter.toHumanReadable,2**63)

if __name__ == '__main__':
    unittest.main()