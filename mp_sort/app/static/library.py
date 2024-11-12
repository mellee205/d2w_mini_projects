from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	random.seed(seed)
	random_no=[]
	for i in range(number):
		random_no.append(random.randint(0,number))
	return random_no

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	pass

	array = gen_random_int(number,seed)
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	pass

	array_str = ""
	for num in array:
		array_str+=str(num)
		array_str+=","
	array_str=array_str[:-1]+'.'
	
	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str

def insertion_sort2(array:list[int|float])->list[int|float]:
    length=len(array)
    for outer in range(1,length):
        target=array[outer]
        target_idx=outer
        for inner in range(outer,0,-1):
            if array[inner-1]>target:
                target_idx-=1
        array.pop(outer)
        array.insert(target_idx,target)

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	unsorted_str=document.getElementById("generate").innerHTML
	unsorted_str=unsorted_str[0:-1]
	unsorted_list=unsorted_str.split(',')

	int_list=[int(item)for item in unsorted_list]

	insertion_sort2(int_list)

	array_str = ""
	for num in int_list:
		array_str+=str(num)
		array_str+=","
	array_str=array_str[:-1]+'.'
	
	pass
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	accepted_characters=[',','.','1','2','3','4','5','6','7','8','9','0','-']
	for character in value:
		if character not in accepted_characters:
			window.alert("You have entered an invalid number")
			return
	# Your code should start from here
	# store the final string to the variable array_str
	unsorted_list=value.split(',')

	def count(number,symbol):
		symbol_count=0
		for ch in number:
			if ch==symbol:
				symbol_count+=1
		return symbol_count

	int_list=[]
	skipped=[]

	for number in unsorted_list:
		if "." in number or '-' in number:
			valid=True
			if count(number,'.')>1:
				valid=False
			elif '-' in number and (count(number,'-')>1 or number[0]!='-'):
				valid=False
			
			if valid:
				int_list.append(float(number))
			else:
				skipped.append(number)

		elif number!="":
			int_list.append(float(number))

	insertion_sort2(int_list)

	array_str = ""
	for num in int_list:
		array_str+=str(num)
		array_str+=","
	array_str=array_str[:-1]+'.'

	pass

	document.getElementById("sorted").innerHTML = array_str
	if skipped!=[]:
		window.alert(f"Code skipped {skipped}.")



