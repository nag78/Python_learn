#-------------------------------------------------------------------------------
# Name:        parrot
# Purpose:
#
# Author:      Nag
#
# Created:     26.10.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)