def myfunc():
  n = 400
  def myinnerfunc():
    print(n)
  myinnerfunc()

myfunc()