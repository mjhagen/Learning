import unittest

class ByteConverter:
  def __init__(self):
    self.oneKiB=2**10
    self.prefixes=['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB']

  def toHumanReadable(self, numberOfBytes):
    # error checking:
    try:
      int(numberOfBytes)
    except ValueError:
      raise ValueError('Input must be a number')

    if numberOfBytes <= 0:
      raise ValueError('Input must be greater than 0')

    if numberOfBytes > 2**63-1:
      raise ValueError('Input must be no larger than 2^63-1')

    # the actual conversion:
    for prefix in self.prefixes:
      if numberOfBytes < self.oneKiB:
        return '%i %s' % (numberOfBytes, prefix)
      numberOfBytes /= self.oneKiB





# Unit Tests Below:
class Test_ByteConverter(unittest.TestCase):
  def setUp(self):
    self.byteConverter = ByteConverter()

  def test_one_byte(self):
    self.assertEqual(self.byteConverter.toHumanReadable(1), '1 B')
  def test_one_kibibyte(self):
    self.assertEqual(self.byteConverter.toHumanReadable(1024), '1 KiB')
  def test_one_mebibyte(self):
    self.assertEqual(self.byteConverter.toHumanReadable(1048576), '1 MiB')
  def test_another_mebibyte(self):
    self.assertEqual(self.byteConverter.toHumanReadable(1234567), '1 MiB')
  def test_nine_gibibytes(self):
    self.assertEqual(self.byteConverter.toHumanReadable(9999999999), '9 GiB')
  def test_cellar(self):
    self.assertRaisesRegex(ValueError, 'Input must be greater than 0', self.byteConverter.toHumanReadable, -5)
  def test_attic(self):
    self.assertRaisesRegex(ValueError, 'Input must be no larger than 2\^63-1', self.byteConverter.toHumanReadable, 2**63)
  def test_nan(self):
    self.assertRaisesRegex(ValueError, 'Input must be a number', self.byteConverter.toHumanReadable, 'I am not a number.')

if __name__ == '__main__':
    unittest.main()