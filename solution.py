from time import sleep
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os        
        
#function to take string input and compare to the lines of the poem
#this will output the string line which has the highest levenshtein ratio
def match(usr_input):
    bMatch = [-1, '']
    poem = open('lepanto.txt', 'r')
    lines = poem.readlines()
    for line in lines:
        lev_ratio = fuzz.partial_ratio(line, usr_input)
        if lev_ratio >= bMatch[0]:
            bMatch[0] = lev_ratio
            bMatch[1] = line
    for i in range(1,len(bMatch)):
        print('Matched string: ' + bMatch[i])
    print('Levenshtein ratio: ' + str(bMatch[0]) + '\n')
    poem.close()


# #run the test cases
# directory = 'test_cases'
# for file in os.listdir(directory):
#     print(file + '\n')
#     test = open(os.path.join(directory,file))
#     lines = test.readlines()
#     line = lines[0]
#     print('Input: ' + line + '\n')
#     match(line)
#     test.close()

#user input
print('Type exit to halt program')
c = True
while(c):
    print('Input: ')
    input_str = input()
    if input_str == 'exit':
        c = False
    else:
        match(input_str)

