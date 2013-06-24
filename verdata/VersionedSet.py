from operations import *
from symath import wilds,WildResults

class VersionedSet(object):

  def __init__(self):
    self._oplist = [] # reverse sorted list of operations
    self.version = 0

  def __contains__(self, item):

    w = wilds('w')

    for op,i in self._oplist:
      if i != item:
        continue

      if op.match(VER_DELETE(w)):
        return False
      elif op.match(VER_ADD(w)):
        return True
      else:
        raise Exception("INVALID OPERATION FOUND: %s" % (op))

  def add(self, item):
    if item in self:
      return

    self._oplist.insert(0, op_add(item, self.version))

  def remove(self, item):
    if item not in self:
      raise KeyError(item)

    self._oplist.insert(0, op_del(item, self.version))

  def get_version(self, version):

    w,v = wilds('w v')
    val = WildResults()

    new_oplist = filter(lambda x: x[0].match(w(v), val) and val.v.value() <= version, self._oplist)
    rv = VersionedSet()
    rv.version = version
    rv._oplist = new_oplist
    return rv
