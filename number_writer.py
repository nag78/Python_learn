#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nag
#
# Created:     29.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers,f_obj)