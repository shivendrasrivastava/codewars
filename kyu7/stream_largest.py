__author__ = "Shiven"

def largest():
	largest = None
	smallest = None
	while True:
		num = raw_input("Enter a number: ")
		if num == "done":
			break
		try:
			num = float(num)
			if smallest is None:
				smallest = num
			if largest is None:
				largest = num
			if num < smallest:
				smallest = num
			elif num > largest:
				largest = num
		except:
			print "Please enter only numbers"

	print "The largest number is ", largest
	print "The smallest number is ", smallest

if __name__ == "__main__":
	largest()