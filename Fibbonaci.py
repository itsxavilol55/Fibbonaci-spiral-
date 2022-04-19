from turtle import *
import colorsys
bgcolor("black")
num1=0 
num2=1
num3=1
h =0
speed(0.1)
for i in range(20):
	color(colorsys.hsv_to_rgb(h,0.7,1))
	h+=1/20
	for j in range(4):
		forward(num3*10)
		left(90)
	circle(num3*10,90)
	num3 = num1+num2
	num1 = num2
	num2 = num3
done()