import re

def striping(string):
    spRegex = re.compile(r'(^\s)' or '(\s$)', string)
    