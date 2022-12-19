import os

with open('input_1.txt', 'r') as input_file:
   with open('output.txt', 'w') as output_file:
       for line in reversed(input_file.readlines()):
           output_file.write(line)


input_file.close()
output_file.close()