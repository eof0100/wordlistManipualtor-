#!/usr/bin/env python3

'''
Wordlist Manipulator 

Author: eof0100
Contact: eof0100@hackersareus.com


My first official python project. Sometimes wordlists 
need some fine tuning or a manipulation of some kind
to get the most of your wordlists with the highest 
possible success of cracking your hash(es).

This tool will alter your existing wordlists, some examples
include changing uppercase to lowercase, capitalizing first 
letter, nad case mixing.

I realize there are better tools out there
such as wlm, crunch, or one of my favorites 
rsmangler. Reinventing the wheel so to speak 
is frowned upon by some but sometimes you 
have to in order to learn. Personally, the
best way I learn is by doing. 


"I hear and I forget,
   I see and I remember,
     I do and I understand."
         - confucius 



Version 1.0 - initial release 


'''


import re
from argparse import ArgumentParser, SUPPRESS 


__prog__ = 'wordlistManipulator'
__version__ = 1.0


# Main Banner
banner = '''

                     __        __            _ _ _     _   
                     \ \      / /__  _ __ __| | (_)___| |_ 
                      \ \ /\ / / _ \| '__/ _` | | / __| __|
                       \ V  V / (_) | | | (_| | | \__ \ |_ 
                        \_/\_/ \___/|_|  \__,_|_|_|___/\__|
                                                           
             __  __             _             _       _             
            |  \/  | __ _ _ __ (_)_ __  _   _| | __ _| |_ ___  _ __ 
            | |\/| |/ _` | '_ \| | '_ \| | | | |/ _` | __/ _ \| '__|
            | |  | | (_| | | | | | |_) | |_| | | (_| | || (_) | |   
            |_|  |_|\__,_|_| |_|_| .__/ \__,_|_|\__,_|\__\___/|_|   
                                 |_|                                
                     => Wordlist Manipulator v{0} 
                       => eof0100@HackersAreUs.com 
                         => https://www.hackersareus.com


'''.format(__version__)




def ShowVersion():
    print("Wordlist Manipulator v{0}".format(__version__))


# Wordlist Manipulation Functions 

def CapFirstLetter(wordlistRead, wordlistWrite):
    '''Read existing wordlist, capitalize each word per line, write to new wordlist'''
    try:
        fd = open(wordlistWrite, 'w')
        with open(wordlistRead, 'r') as f:
            for eachWord in f:
                cap=eachWord.title()
                fd.write(cap)
            fd.close()
    except FileNotFoundError as e:
        print("File not found. Make sure file exists and check file name is correct.\n")
    except PermissionError as e:
        print("Reading/Writing Permission Denied.\n")
    except:
        print("Unknown Error has Occurred.") 

 

def CapAllLetters(wordlistRead, wordlistWrite):
    '''Read from an existing wordlist, capitalizing all letters, write to new wordlist'''
    try:
        fd = open(wordlistWrite, 'w') 
        with open(wordlistRead, 'r') as f:
            for eachWord in f:
                cap = eachWord.upper()
                fd.write(cap)
            fd.close()
    except FileNotFoundError as e:
        print("File not found. Make sure file exists and check file name is correct.\n")
    except PermissionError as e:
        print("Reading/Writing Permission Denied.\n")
    except:
        print("Unknown Error has Occurred.") 


def LowercaseAllLetters(wordlistRead, wordlistWrite):
    '''Read from existing wordlist, lowercase each letter, write to new file '''
    try:
        fd = open(wordlistWrite, 'w')
        with open(wordlistRead, 'r') as f:
            for eachWord in f:
                lowercase = eachWord.lower()
                fd.write(lowercase)
            fd.close() 
    except FileNotFoundError as e:
        print("File not found. Make sure file exists and check file name is correct.\n")
    except PermissionError as e:
        print("Reading/Writing Permission Denied.\n")
    except:
        print("Unknown Error has Occurred.") 




def WPA(wordlistRead, wordlistWrite):
    '''Make a WPA/WPA2 wordlist from an existing wordlist 8 <= x <= 64'''
    try:
        fd = open(wordlistWrite, 'w')
        with open(wordlistRead, 'r') as f:
            for eachLine in f:
                # only write words that are between 8 and 63 characters
                # note using 9 and 64 b/c \n is counted as a character
                if len(eachLine) >= 9 and len(eachLine) <= 64:
                    fd.write(eachLine) 
                else:
                    pass 
            fd.close()
    except FileNotFoundError as e:
        print("File not found. Make sure file exists and check file name is correct.\n")
    except PermissionError as e:
        print("Reading/Writing Permission Denied.\n")
    except:
        print("Unknown Error has Occurred.") 



def MixCaseUpperToLower(wordlistRead, wordlistWrite):
    '''From existing wordlist will convert each words case starting from Uppercase to lower and repeat'''
    try:
        fd = open(wordlistWrite, 'w')
        mix_case = ''
        with open(wordlistRead, 'r') as f:
            for word in f:
             i = True # capitalize
             for letter in word:
                    if i:
                        mix_case += letter.upper()
                    else:
                        mix_case += letter.lower()
                    if letter != ' ':
                        # if not whitespace inverse bool value of i
                        i = not i
            fd.write(mix_case)
            fd.close() 
    except FileNotFoundError as e:
        print("File not found. Make sure file exists and check file name is correct.\n")
    except PermissionError as e:
        print("Reading/Writing Permission Denied.\n")
    except:
        print("Unknown Error has Occurred.") 


            


def MixCaseLowerToUpper(wordlistRead, wordlistWrite):
    '''From existing wordlist will convert each words case starting from Uppercase to lower and repeat'''
    try:
        fd = open(wordlistWrite, 'w')
        mix_case = ''
        with open(wordlistRead, 'r') as f:
            for word in f:
                i = False # begin with lowercase
                for letter in word:
                    if i:
                         mix_case += letter.upper()
                    else:
                        mix_case += letter.lower()
                    if letter != ' ':
                        # if not whitespace inverse bool value of i
                        i = not i
            fd.write(mix_case)
            fd.close()
    except FileNotFoundError as e:
        print("File not found. Make sure file exists and check file name is correct.\n")
    except PermissionError as e:
        print("Reading/Writing Permission Denied.\n")
    except:
        print("Unknown Error has Occurred.") 




def Suffix(wordlistRead, wordlistWrite, suffix_word):
    '''Function will read an existing wordlist and suffix user specified text
       and then write the contents to a newly created wordlist with a name of users choice'''
    try:
        new_word = ''
        new_line = '\n'
        fd_write = open(wordlistWrite, 'w')
        with open(wordlistRead, 'r') as f:
            for word in f:
                # Remove \n from each word since we are adding a text after if I didn't
                # remove newline the newly added suffix  would be on the next line
                strip_word = word.strip() 
                new_word = new_word+strip_word+suffix_word+new_line
        fd_write.write(new_word)
        fd_write.close() 
    except FileNotFoundError as e:
        print("File not found. Make sure file exists and check file name is correct.\n")
    except PermissionError as e:
        print("Reading/Writing Permission Denied.\n")
    except:
        print("Unknown Error has Occurred.") 

    



def Prefix(wordlistRead, wordlistWrite, prefix_word):
    '''Function will read an existing wordlist and prefix user specified text 
       and then write the contents to a newly created wordlist with a name of users choice'''
    try:
        new_word = ''
        fd_write = open(wordlistWrite, 'w')
        with open(wordlistRead, 'r') as f:
            for word in f:
                new_word = new_word+prefix_word+word
        fd_write.write(new_word) 
        fd_write.close()
    except FileNotFoundError as e:
        print("File not found. Make sure file exists and check file name is correct.\n")
    except PermissionError as e:
        print("Reading/Writing Permission Denied.\n")
    except:
        print("Unknown Error has Occurred.") 
        

'''
# Idea: Create different leet speak options such as 
# 1. Minor  leetspeak l=1 e=3
# 2. Minor  leetspeak l=1 e=3 o=0
# 3. Minor  leetspeak l=1 e=3 o=0 a=4 
# 4. Minor  leetspeak l=1 e=3 o=0 a=4 b=8 
# 5. Minor  leetspeak l=1 e=3 o=0 a=4 b=8 z=2 
# 6. Major which includes combination of these
    A: 4, /-\, /_\, @, /\, Д
    B: 8,|3, 13, |}, |:, |8, 18, 6, |B, |8, lo, |o, j3, ß,
    C: <, {, [, (, ©, ¢,
    D: |), |}, |], |>,
    E: 3, £, ₤, €
    F: |=, ph, |#, |", ƒ
    G: [, -, [+, 6, C-,
    H: #, 4, |-|, [-], {-}, }-{, }{, |=|, [=], {=}, /-/, (-), )-(, :-:, I+I,
    I: 1, |, !, 9
    J: _|, _/, _7, _), _], _}
    K: |<, 1<, l<, |{, l{
    L: |_, |, 1, ][
    M: 44, |\/|, ^^, /\/\, /X\, []\/][, []V[], ][\\//][, (V),//., .\\, N\,
    N: |\|, /\/, /V, ][\\][, И
    O: 0, (), [], {}, <>, Ø, oh,
    P: |o, |O, |>, |*, |°, |D, /o, []D, |7
    Q: O_, 9, (,), 0,kw,
    R: |2, 12, .-, |^, l2, Я, ®
    S: 5, $, §,
    T: 7, +, 7`, '|' , `|` , ~|~ , -|-, '][',
    U: |_|, \_\, /_/, \_/, (_), [_], {_}
    V: \/
    W: \/\/, (/\), \^/, |/\|, \X/, \\', '//, VV, \_|_/, \\//\\//, Ш, 2u, \V/,
    X: %, *, ><, }{, )(, Ж,
    Y: `/, ¥, \|/, Ч,
    Z: 2, 5, 7_, >_,(/),

mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

'''

def leetSpeak(wordlistRead, wordlistWrite):
    ''' Convert each word to leet speak. Only includes e=3 l=1 a=4 b=8 o=0 s=5'''
    try:
        leetWord = ''
        fd = open(wordlistWrite, 'w')
        with open(wordlistRead, 'r') as f:
            for eachWord in f:
                for eachLetter in eachWord:
                    if eachLetter == 'e' or eachLetter == 'E':
                        eachLetter = '3'
                        leetWord += eachLetter
                    elif eachLetter == 'l' or eachLetter == 'L':
                        eachLetter = '1'
                        leetWord += eachLetter
                    elif eachLetter == 'a' or eachLetter == 'A':
                        eachLetter = '4'
                        leetWord += eachLetter
                    elif eachLetter == 'b' or eachLetter == 'B':
                        eachLetter = '8'
                        leetWord += eachLetter
                    elif eachLetter == 'o' or eachLetter == 'O':
                        eachLetter = '0'
                        leetWord += eachLetter
                    elif eachLetter == 's' or eachLetter == 'S':
                        eachLetter = '5'
                        leetWord += eachLetter
                    else:
                        leetWord += eachLetter
            fd.write(leetWord)
            fd.close()
    except FileNotFoundError as e:
        print("Wordlist selected is not found.")
    except PermissionError as e:
        print("Reading/Writing Error: Permission Denied")
    except:
        print("Unknown Error Occurred.")




# -- End Wordlist Functions ---



# Disable default help
parser = ArgumentParser(add_help=False, usage=banner)
required = parser.add_argument_group('Required Arguments')
optional = parser.add_argument_group('Optional Arguments') 
# Add back help
optional.add_argument('-h', '--help', action='help', default=SUPPRESS, help='Show this help message and exit') 

# Required Arguments
required.add_argument('-w', '--wordlist', required=True, help='Existing wordlist to manipulate')
required.add_argument('-o', '--output', required=True, help='Output filename')


# Optional Arguments
optional.add_argument('-c', '--capitalize', action='store_true', help='Capitalize first letter of each word per line')
optional.add_argument('-a', '--allcaps', action='store_true', help='Capitalize all letters of each word per line')
optional.add_argument('-l', '--lowercase', action='store_true', help='Lowercase all letters of each word per line')
optional.add_argument('-f', '--wpa', action='store_true', help='Make WPA ready wordlist. Only keeps words between  8 <= x <= 63 characters')
optional.add_argument('-u', '--mixupper', action='store_true', help='Mixcase starting from Uppercase to lowercase and repeat')
optional.add_argument('-m', '--mixlower', action='store_true', help='Mixcase starting from lowercase to Uppercase and repeat')
optional.add_argument('-s', '--suffix', help='Suffix user specified string to end of each word per line')
optional.add_argument('-p', '--prefix', help='Prefix user specified string to beginning of each word per line')
optional.add_argument('-v', '--version', action='version', version='Wordlist Manipulator v{0}'.format(__version__)  ,help='Output version information and exit') 
optional.add_argument('-e', '--elasob', action='store_true', help='Minor leetspeak.Only includes e=3, l=1 a=4, s=8, o=0, b=8') 

# Access arguments via argparser.argument
argparser = parser.parse_args()


if argparser.capitalize:
    CapFirstLetter(argparser.wordlist, argparser.output) 

if argparser.allcaps:
    CapAllLetters(argparser.wordlist, argparser.output) 

if argparser.lowercase:
    LowercaseAllLetters(argparser.wordlist, argparser.output)
    
if argparser.wpa:
    WPA(argparser.wordlist, argparser.output)

if argparser.mixupper:
    MixCaseUpperToLower(argparser.wordlist, argparser.output)
if argparser.mixlower:
    MixCaseLowerToUpper(argparser.wordlist, argparser.output)

if argparser.suffix:
    Suffix(argparser.wordlist, argparser.output, argparser.suffix) 

if argparser.prefix:
    Prefix(argparser.wordlist, argparser.output, argparser.prefix) 

if argparser.elasob:
    leetSpeak(argparser.wordlist, argparser.output)
    
