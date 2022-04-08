from fuzzywuzzy import fuzz
import os    

"""
@author Kaelen Baird

The goal of this program is to take a user input and find the refereced line
in the poem. For this I implemented the match function @param usr_input.
The function uses fuzzywuzzy's fuzz to measure the difference between
the input and the lines of the poem. The function will then keep track of
the closest matching string, it's line number, and the levenshtein ratio
of the strings return from fuzz.partail_ratio. The levenshtein ratio is
the sum of costs given by the formula (lev_sum - ldist) / lensum.
So the ratio gives us a better perception of the relation between the strings.
The levenshtein distance is calculated as a bottom-up dynammic algorithm 
which creates a 2d matrix that calculates the cost between the char of the string
arrays which is dependent on the deletions, insertions, and substitutions needed
for the strings to match. The partial_ratio() function allows the program to perform
substring matching. This works by taking the shortest string and matching it with
all substrings that are of same length. The function will then print out to the 
user the closest matching string with line number and the levenstein ratio.

"""

def match(usr_input):
    bMatch = [-1, -1, '']
    poem = open('lepanto.txt', 'r')
    lines = poem.readlines()
    num = 0
    for line in lines:
        lev_ratio = fuzz.partial_ratio(line, usr_input)
        if lev_ratio >= bMatch[0]:
            bMatch[0] = lev_ratio
            bMatch[1] = num
            bMatch[2] = line
        num += 1
    print('L:' +str(bMatch[1]) + " " + bMatch[2])
    print('L_Ratio: ' + str(bMatch[0]) + '\n')
    poem.close()


# #test cases
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
    print('\n')
    if input_str == 'exit':
        c = False
    else:
        match(input_str)

