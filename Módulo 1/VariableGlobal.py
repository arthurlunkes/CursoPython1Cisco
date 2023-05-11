x = "awesome"

def myfunc1():
  global x
  x = "fantastic"

def myfunc2():
  y = "fantastic"

myfunc1()
print("Python is " + x)

# Dá erro pois a variável y só está criada no escopo da função myfunc2()
#myfunc2()
#print("Python is " + y)