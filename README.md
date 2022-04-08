# ce_interview_project_Kaelen_Baird

This program requires python3, pip, and fuzzywuzzy.
Debian should be shipped with python3, check the version using:

`$python --version`

To install pip use the following commands:

`$sudo apt update
$sudo apt install python-pip`

To install fuzzywuzzy use the folling command:

`$pip install fuzzywuzzy
$pip install python-Levenshtein`

To run the program navigate to the ce_interview_project_Kaelen_Baird directory and run:

`$python3 solution.py`

The terminal should then prompt the user for an input string to try to match to one of the lines
in the poem. Once the input is entered the program will return the best fit line in the poem
with the line number and levenshtein ratio of the two strings. The program will then continue
to prompt the user for more inputs. The program will end with exit is entered into the input.
