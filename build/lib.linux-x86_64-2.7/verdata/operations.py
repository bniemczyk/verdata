from symath import symbols

VER_ADD,VER_DELETE = symbols('VER_ADD VER_DELETE')

def op_add(obj):
  return (VER_ADD, obj)

def op_del(obj):
  return (VER_DELETE, obj)
