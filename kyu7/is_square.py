__author__ = "Shiven"

import math

def check_square(n):
	if n > 0:
		if (math.sqrt(n)).is_integer():
			return True
	return False