import keyboard
import turtle
tecnos=turtle.Turtle()
tecnos.speed(1)
tecnos.pensize(10)
tecnos.hideturtle()
while keyboard.is_pressed('q')==False:
    if keyboard.is_pressed('1')==True:
        tecnos.clear()
        tecnos.fd(1)
    if keyboard.is_pressed('2')==True:
        tecnos.clear()
        tecnos.fd(20)
    if keyboard.is_pressed('3')==True:
        tecnos.clear()
        tecnos.fd(30)
        tecnos.rt(90)
        tecnos.fd(40)
        tecnos.lt(217)
        tecnos.fd(50)

    if keyboard.is_pressed('4')==True:
        tecnos.clear()
    if keyboard.is_pressed('5')==True:
        tecnos.clear()
    if keyboard.is_pressed('6')==True:
        tecnos.clear()
    if keyboard.is_pressed('7')==True:
        tecnos.clear()
    if keyboard.is_pressed('8')==True:
        tecnos.clear()
    if keyboard.is_pressed('9')==True:
        tecnos.clear()
print("<==================================>")
print("Vége")