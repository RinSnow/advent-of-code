import re
import sys
input = open(sys.argv[1]).read().strip()
inputArray = input.split('\n')
number_list = ("one","two","three","four","five","six","seven","eight","nine")
first_number = []
second_number = 0
for line in inputArray:
    first_number.clear()
    first_number=re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))', line)
    if len(first_number) > 0:
        for i in range(len(first_number)):
                try:
                    first_number[i]=str(number_list.index(first_number[i])+1)
                except ValueError:
                    next
        second_number+=int(first_number[0]+first_number[-1])
print(second_number)        
    



