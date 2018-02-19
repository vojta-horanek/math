#!/usr/bin/python

import os
import sys
import math

def main():
	start()
		
def start():
	menu = 0
	print ("Math 0.4")
	print ("Please select option:")
	print ("[1]Algebra\n[2]Geometry\n[3]Quit")
	try:
		global mode
		mode=int(input(""))
		if int(mode) == 1:
			algebra()
		elif int(mode) == 2:
			geometry()
		elif int(mode) == 3:
			print ("Quiting")
			sys.exit()
		else:
			print ("Please input valid number.\n")
	except ValueError:
		print ("Please input valid number.")
#inputs			
def algebra():
	print ("Please select option:")
	print ("[1]Addition\n[2]Subtraction\n[3]Division\n[4]Multiplication\n[5]Power\n[6]Root\n[7]Quit")
	try:
		global al_mode
		al_mode=int(input(""))
		if al_mode <= 8:
			algebra_functions()
		else:
			print ("Please input valid number.")
	except ValueError:
		print ("Please input valid number.")
def geometry():
	print ("Please select option:")
	print ("[1]Square content\n[2]Square circumference\n[3]Rectangle content\n[4]Rectangle circumference\n[5]Triangle content\n[6]Triangle circumference\n[7]Quit")
	try:
		global geo_mode
		geo_mode=int(input(""))
		if geo_mode <= 8:
			geometry_functions()
		else:
			print ("Please input valid number.")
	except ValueError:
		print ("Please input valid number.")
#functions selection	
def algebra_functions():
	if al_mode == 1:
		addition_func()
	elif al_mode == 2:
		subtraction_func()
	elif al_mode == 3:
		division_func()
	elif al_mode == 4:
		multiplication_func()
	elif al_mode == 5:
		power_func()
	elif al_mode == 6:
		root_func()
	elif al_mode == 7:
		print ("Quiting")
		sys.exit()
def geometry_functions():
	if geo_mode == 1:
		sqrco_func()
	elif geo_mode == 2:
		sqrci_func()
	elif geo_mode == 3:
		recco_func()
	elif geo_mode == 4:
		recci_func()
	elif geo_mode == 5:
		trico_func()
	elif geo_mode == 6:
		trici_func()
	elif geo_mode == 7:
		print ("Quiting")
		sys.exit()
#Algebra functions
def addition_func():
	try:
		num=float(input("With how much numbers do you want to count? "))
		if int(num) == 0 or int(num) == 1:
			print ("Please input valid number.")
		elif int(num) == 2:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			eq=a+b
			print (eq)
		elif int(num) == 3:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			eq=a+b+c
			print (eq)
		elif int(num) == 4:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			d=float(input("Fourth number:"))
			eq=a+b+c+d
			print (eq)
		elif int(num) == 5:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			d=float(input("Fourth number:"))
			e=float(input("Fifth number:"))
			eq=a+b+c+d+e
			print (eq)
		else:
			print ("Maximum limit reached.")
	except ValueError:
		print ("Please input valid number.")
def subtraction_func():
	try:
		num=float(input("With how much numbers do you want to count? "))
		if int(num) == 0 or int(num) == 1:
			print ("Please input valid number.")
		elif int(num) == 2:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			eq=a-b
			print (eq)
		elif int(num) == 3:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			eq=a-b-c
			print (eq)
		elif int(num) == 4:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			d=float(input("Fourth number:"))
			eq=a-b-c-d
			print (eq)
		elif int(num) == 5:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			d=float(input("Fourth number:"))
			e=float(input("Fifth number:"))
			eq=a-b-c-d-e
			print (eq)
		else:
			print ("Maximum limit reached.")
	except ValueError:
		print ("Please input valid number.")
def division_func():
	try:
		num=float(input("With how much numbers do you want to count? "))
		if int(num) == 0 or int(num) == 1:
			print ("Please input valid number.")
		elif int(num) == 2:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			eq=a/b
			print (eq)
		elif int(num) == 3:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			eq=a/b/c
			print (eq)
		elif int(num) == 4:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			d=float(input("Fourth number:"))
			eq=a/b/c/d
			print (eq)
		elif int(num) == 5:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			d=float(input("Fourth number:"))
			e=float(input("Fifth number:"))
			eq=a/b/c/d/e
			print (eq)
		else:
			print ("Maximum limit reached.")
	except ValueError:
		print ("Please input valid number.")
def multiplication_func():
	try:
		num=float(input("With how much numbers do you want to count? "))
		if int(num) == 0 or int(num) == 1:
			print ("Please input valid number.")
		elif int(num) == 2:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			eq=a*b
			print (eq)
		elif int(num) == 3:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			eq=a*b*c
			print (eq)
		elif int(num) == 4:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			d=float(input("Fourth number:"))
			eq=a*b*c*d
			print (eq)
		elif int(num) == 5:
			a=float(input("First number:"))
			b=float(input("Second number:"))
			c=float(input("Third number:"))
			d=float(input("Fourth number:"))
			e=float(input("Fifth number:"))
			eq=a*b*c*d*e
			print (eq)
		else:
			print ("Maximum limit reached.")
	except ValueError:
		print ("Please input valid number.")
def power_func():
	try:
		a=float(input("First number:"))
		b=float(input("Power by:"))
		eq=a**b
		print (eq)
	except ValueError:
		print ("Please input valid number.")
def root_func():
	try:
		a=float(input("First number:"))
		b=float(input("Root by:"))
		
		if b == 2:
			eq = math.sqrt(a)
			print (eq)
		elif b > 2:
			eq = a**(1/b)
			print (eq)
		else:
		  print ("Please input valid number.")
	except ValueError:
		print ("Please input valid number.") 
#Geometry functions
def sqrco_func():
	print ("Please select option:")
	print ("[1]I know side\n[2]I know diagonal")
	try:
		option=int(input(""))
		if option == 1:
			try:
				a=float(input("Please enter the size of one side(in cm):"))
				eq=a**2
				print ("%s cm2" % eq )
			except ValueError:
				print ("Please input valid number.")
		elif option == 2:
			try:
				u=float(input("Please enter the size of a diagonal(in cm):"))
				eq=(u**2)/2
				print ("%s cm2" % eq)
			except ValueError:
				print ("Please input valid number.")
		else:
			print ("Please input valid number.")
	except ValueError:
		print ("Please input valid number.")
def sqrci_func():
	try:
		a=int(input("Please enter the size of one side(in cm):"))
		eq=4*a
		print (eq)
	except ValueError:
		print ("Please input valid number.")	
def recco_func():
	try:
		a=float(input("Please enter the size of the first side(in cm):"))
		b=float(input("Please enter the size of the second side(in cm):"))
		eq=a*b
		print ("%s cm2" % eq)
	except ValueError:
		print ("Please input valid number.")	
def recci_func():
	try:
		a=float(input("Please enter the size of the first side(in cm):"))
		b=float(input("Please enter the size of the second side(in cm):"))
		eq=2*(a+b)
		print (eq)
	except ValueError:
		print ("Please input valid number.")	
def trico_func():
	print ("Please select option:")
	print ("[1]Scalene triangle\n[2]Equilateral triangle\n[3]Rectangular triangle\n[4]Isosceles triangle")
	try:
		option=int(input(""))
		if option == 1:
			try:
				a=float(input("Please enter the size of one side(in cm):"))
				b=float(input("Please enter altitude of that side(in cm):"))
				eq=(a*b)/2
				print ("%s cm2" % eq)
			except ValueError:
				print ("Please input valid number.")
		elif option == 2:
			try:
				a=float(input("Please enter the size of one side(in cm):"))
				b=float(input("Please enter altitude(in cm):"))
				eq=(a*b)/2
				print ("%s cm2" % eq)
			except ValueError:
				print ("Please input valid number.")
		elif option == 3:
			try:
				a=float(input("Please enter the size of the first side(in cm):"))
				b=float(input("Please enter the size of the second side(in cm):"))
				eq=(a*b)/2
				print ("%s cm2" % eq)
			except ValueError:
				print ("Please input valid number.")
		elif option == 4:
			try:
				a=float(input("Please enter the size the triangle base(in cm):"))
				b=float(input("Please enter altitude of the base(in cm):"))
				eq=(a*b)/2
				print ("%s cm2" % eq)
			except ValueError:
				print ("Please input valid number.")
		else:
			print ("Please input valid number.")
	except ValueError:
		print ("Please input valid number.")
def trici_func():
	print ("Please select option:")
	print ("[1]Scalene triangle\n[2]Equilateral triangle\n[3]Rectangular triangle\n[4]Isosceles triangle")
	try:
		option=int(input(""))
		if option == 1:
			try:
				a=float(input("Please enter the size of first side(in cm):"))
				b=float(input("Please enter the size of second side(in cm):"))
				b=float(input("Please enter the size of third side(in cm):"))
				eq=a+b+c
				print ("%s cm" % eq)
			except ValueError:
				print ("Please input valid number.")
		elif option == 2:
			try:
				a=float(input("Please enter the size of one side(in cm):"))
				eq=3*a
				print ("%s cm" % eq)
			except ValueError:
				print ("Please input valid number.")
		elif option == 3:
			try:
				a=float(input("Please enter the size of first side(in cm):"))
				b=float(input("Please enter the size of second side(in cm):"))
				b=float(input("Please enter the size of third side(in cm):"))
				eq=a+b+c
				print ("%s cm" % eq)
			except ValueError:
				print ("Please input valid number.")
		elif option == 4:
			try: 
				a=float(input("Please enter the size of first side(in cm):"))
				b=float(input("Please enter the size of the triangle base(in cm):"))
				eq=2*a+b
				print ("%s cm" % eq)
			except ValueError:
				print ("Please input valid number.")
		else:
			print ("Please input valid number.")
	except ValueError:
		print ("Please input valid number.")
#main
if __name__ == "__main__":
	main()
