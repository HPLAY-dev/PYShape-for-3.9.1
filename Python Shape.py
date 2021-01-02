import turtle
turtle.title("PYShape - Input Datas")
sc = turtle.Screen()
sc.setup(960,720)
# Setup Windows(Turtle)
a = turtle.textinput ("Python Shape", "forward")
# VARIABLE
print(a)
# Print Var
b = turtle.textinput ("Python Shape", "turn")
# VARIABLE
print(b)
# Print Var
c = turtle.textinput ("Python Shape", "color")
# VARIABLE
print(c)
# Print Var
d = turtle.textinput ("Python Shape", "repeat time(s)")
# VARIABLE
print(d)
# Print VAriable
e = turtle.textinput ("Python Shape", "backgroundcolour?")
# VARIABLE
print(e)
# Print VAriable
f = turtle.textinput ("Python Shape", "drawspeed")
# VARIABLE
print(f)
# Print VAriable
turtle.title("PYShape - drawing")
turtle.bgcolor(e)
t = turtle
# Make it Easier
t.pencolor (c)
# Setup Color
turtle.speed(int(f))
for x in range(int(d)):
# Repeat
 t.forward (int(a))
#Forward
 t.left (int(b))
#Left
t.hideturtle()
t.done()
# End Codes
t.title("PYShape - Thanks for Using")
