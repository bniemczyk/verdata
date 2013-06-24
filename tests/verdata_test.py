import unittest
from verdata import *
from verdata.operations import *

class TestProblemSet1(unittest.TestCase):

  def setUp(self):
    pass

  def test_operations(self):
    thing = 'some thing'
    oadd = op_add(thing, 1)
    odel = op_del(thing, 2)

    self.assertEqual(oadd, (VER_ADD(1), 'some thing'))
    self.assertEqual(odel, (VER_DELETE(2), 'some thing'))

  def test_versionedset(self):
    vs = VersionedSet()
    vs.version = 1
    vs.add('one')
    vs.version = 2
    vs.add('two')
    vs.version = 3
    vs.add('three')
    vs.remove('one')

    self.assertFalse('one' in vs)
    self.assertTrue('two' in vs)
    self.assertTrue('three' in vs)

    vs = vs.get_version(2)
    self.assertFalse('three' in vs)
    self.assertTrue('one' in vs)
    self.assertTrue('two' in vs)
