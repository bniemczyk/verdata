from operations import *
from symath import wilds,WildResults

class VersionedSet(object):
  '''
  versioned set container

  this allows you to keep 'versions' of a set easily and rollback (using get_version)
  one thing to note is __contains__ runs in LINEAR time, unlike the python set(), same for len(vs)
  '''

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

  def _get_set(self):
    
    v = wilds('v')

    removed = set([])
    values = set([])

    for op,i in self._oplist:

      if op.match(VER_ADD(v)) and i not in removed:
        values.add(i)

      elif op.match(VER_DELETE(v)):
        removed.add(i)

    return values

  def __iter__(self):
    return self._get_set().__iter__()

  def __len__(self):
    return self._get_set().__len__()
