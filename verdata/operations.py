from symath import symbols

VER_ADD,VER_DELETE = symbols('VER_ADD VER_DELETE')

def op_add(obj, version):
  return (VER_ADD(version), obj)

def op_del(obj, version):
  return (VER_DELETE(version), obj)
