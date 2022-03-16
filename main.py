import turtle,time,os
a = 1
b = 0


turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.begin_fill()
turtle.color('#3333ff')
turtle.circle(50)
turtle.color('#3333ff')
turtle.end_fill()
turtle.color('#666666')
turtle.penup()
turtle.goto(0,-100)
turtle.shape("circle")

while True:
    turtle.color('#666666')
    turtle.circle(100)
    turtle.penup()
    astr = str(a)
    a += 1
    os.system('cls')
    print(astr +" Day Has Passed")

      
    if a == 29:
      print("")
      b += 1
      a = 0
      if b >= 2:
        print(str(b) + " Months have past")
        
      else:
          print(str(b) + " Month has past")
      
      
    elif a >= 2:
      os.system('cls')
      print(astr +" Days Has Passed")
      if b == 0:
        pass
      else:
        print(str(b) + " Months have past")
      
