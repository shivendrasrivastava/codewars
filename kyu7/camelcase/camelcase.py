__author__ = "Shiven"

import re

def countcase():
    s = input().strip()
    s_split = re.sub('(?!^)([A-Z][a-z]+)', r' \1', s).split()
    print(len(s_split))
