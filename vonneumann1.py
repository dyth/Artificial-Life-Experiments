#!/usr/bin/env python

'''
Program self-replicates when run
'''

import os

old_program = "vonneumann1.py"
input_string, output_string = open(old_program_name).read().split("\n"), ""

for i in range(len(input_string)):
    if (input_string[i] == 'old_program_name = "vonneumann0.py"'):
        input_string[i] = 'old_program_name = "vonneumann1.py"'
        new_program = "vonneumann1.py"
    elif (input_string[i] == 'old_program_name = "vonneumann1.py"'):
        input_string[i] = 'old_program_name = "vonneumann0.py"'
        new_program = "vonneumann0.py"
    output_string += input_string[i] + '\n'

open(new_program_name, "w").write(output_string)
os.system("python " + new_program_name)















































































































































































































































































































































































































































































































































































































































































































































































