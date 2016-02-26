#!/usr/bin/python

import os
import sys
import math

def main():
	start()
		
def start():
	menu = 0
	print "Math 0.1"
	print "Please select option:"
	print "[1]Addition\n[2]Subtraction\n[3]Division\n[4]Multiplication\n[5]Power\n[6]Root\n[7]Quit"
	try:
		global mode
		mode=int(raw_input(""))
		if int(mode) <= 7:
			functions()
		else:
			print "Please input valid number."
	except ValueError:
		print "Please input valid number."
				
def functions():
	if mode == 1:
		addition_func()
	elif mode == 2:
		subtraction_func()
	elif mode == 3:
		division_func()
	elif mode == 4:
		multiplication_func()
	elif mode == 5:
		power_func()
	elif mode == 6:
		root_func()
	elif mode == 7:
		print "Quiting"
		sys.exit()

def addition_func():
	try:
		num=float(raw_input("With how much numbers do you want to count? "))
		if int(num) == 0 or int(num) == 1:
			print "Please input valid number."
		elif int(num) == 2:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			eq=a+b
			print eq
		elif int(num) == 3:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			eq=a+b+c
			print eq
		elif int(num) == 4:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			d=float(raw_input("Fourth number:"))
			eq=a+b+c+d
			print eq
		elif int(num) == 5:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			d=float(raw_input("Fourth number:"))
			e=float(raw_input("Fifth number:"))
			eq=a+b+c+d+e
			print eq
		else:
			print "Maximum limit reached."
	except ValueError:
		print "Please input valid number."
def subtraction_func():
	try:
		num=float(raw_input("With how much numbers do you want to count? "))
		if int(num) == 0 or int(num) == 1:
			print "Please input valid number."
		elif int(num) == 2:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			eq=a-b
			print eq
		elif int(num) == 3:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			eq=a-b-c
			print eq
		elif int(num) == 4:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			d=float(raw_input("Fourth number:"))
			eq=a-b-c-d
			print eq
		elif int(num) == 5:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			d=float(raw_input("Fourth number:"))
			e=float(raw_input("Fifth number:"))
			eq=a-b-c-d-e
			print eq
		else:
			print "Maximum limit reached."
	except ValueError:
		print "Please input valid number."
def division_func():
	try:
		num=float(raw_input("With how much numbers do you want to count? "))
		if int(num) == 0 or int(num) == 1:
			print "Please input valid number."
		elif int(num) == 2:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			eq=a/b
			print eq
		elif int(num) == 3:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			eq=a/b/c
			print eq
		elif int(num) == 4:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			d=float(raw_input("Fourth number:"))
			eq=a/b/c/d
			print eq
		elif int(num) == 5:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			d=float(raw_input("Fourth number:"))
			e=float(raw_input("Fifth number:"))
			eq=a/b/c/d/e
			print eq
		else:
			print "Maximum limit reached."
	except ValueError:
		print "Please input valid number."
def multiplication_func():
	try:
		num=float(raw_input("With how much numbers do you want to count? "))
		if int(num) == 0 or int(num) == 1:
			print "Please input valid number."
		elif int(num) == 2:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			eq=a*b
			print eq
		elif int(num) == 3:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			eq=a*b*c
			print eq
		elif int(num) == 4:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			d=float(raw_input("Fourth number:"))
			eq=a*b*c*d
			print eq
		elif int(num) == 5:
			a=float(raw_input("First number:"))
			b=float(raw_input("Second number:"))
			c=float(raw_input("Third number:"))
			d=float(raw_input("Fourth number:"))
			e=float(raw_input("Fifth number:"))
			eq=a*b*c*d*e
			print eq
		else:
			print "Maximum limit reached."
	except ValueError:
		print "Please input valid number."
def power_func():
	try:
		a=float(raw_input("First number:"))
		b=float(raw_input("Power by:"))
		eq=a**b
		print eq
	except ValueError:
		print "Please input valid number."
def root_func():
	try:
		a=float(raw_input("First number:"))
		b=float(raw_input("Root by:"))
		
		if b == 2:
			eq = math.sqrt(a)
			print eq
		elif b > 2:
			eq = a**(1/b)
			print eq
		else:
			print "Please input valid number." 
		
	except ValueError:
		print "Please input valid number."

	
				

if __name__ == "__main__":
	main()
