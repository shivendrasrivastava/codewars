__author__ = "Shiven"

import re

def remove_vowels(str):
	return re.sub(r'[aeiouAEIOU]', "", str)