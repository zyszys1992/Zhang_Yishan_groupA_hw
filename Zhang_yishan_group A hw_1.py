# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


'''question 1 ''''
#define a function parlindrome with a parameter: something
#anytime you type parlindrome(something), this function will let you enter a
#text so that you can test whether it is parlindrome or not.
def parlindrome(something):
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~ '''# Define what punctions constain
    no_punct=""# define nonpunctions as no_punct with initial value 

     #delete all punctutaions and connect them
    for char in something:
        if char not in punctuations:
            no_punct = no_punct + char#delete all punctutaions and connect them
       

    def reverse(no_punct):#define a function to reverse the order of word or line
        return no_punct[::-1]

    def is_palindrome(no_punct):#define a function to distinguish parlindrome
        return no_punct.lower() == reverse(no_punct.lower())#

    if is_palindrome(no_punct):#output the word if is parlindrome
        print("Yes, it is a palindrome")
        print(something)
    else:
        print("No, it is not a palindrome")





'''question 2 '''
#define a function semordnilap
#parameter file is outside file from your computer as txt format
#anytime you wanna run semordnilap, if your txt is semordnilap, it will show 
#"Yes, it is a semordnilap", and you appended words
#otherwise nothing
def semordnilap(file):
    #define semordnilap functions
    filepath = open(file).read()
    #open a file
    words = filepath.split()
    #split the words in file
    results = []
    # set results initial value
    for word_1 in words:
        for word_2 in words:
            if word_1 == word_2[::-1]:
            #distinguish if word1=word2
                results.append(word_1)
   
    print("Yes, it is a semordnilap")#print the final result
    return results 
          
            
         

    
    
'''question 3'''
#define a function to look for the frequency of letter
#parameter is filepath is from your computer as txt format 
#anytime you run function, it gives the frequency of each letter shoing up in your file         
def char_freq_table(filepath):
    
    def displaycft(cft):
    #define a function to displace the frequency and corresponding letter
        for a, b in sorted(cft.items()):
    # a as the letter and b as the letter's frequency 
            print(a, b) 
        #print the letter and frequency pair  
    file = open(filepath).read()
    #open a file as only read file
    return displaycft({letter:file.count(letter) for letter in file})
    #count the letters' frequency in file and write them as letter and corresponding frequency
    #put the "letter" into function displaycft
    #Now, letter and corresponding frequency is set up and next is to sort them from a to z
    return print(char_freq_table(filepath))#print the output




'''question 4'''

import os, time #import os and time
#define a function to speak from modern English to ancient language 
#parameter is string as a text accepted from what you enter
#any time you type speak_icao(anything),it will let you enter text to speak
def speak_icao(string):

    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~ '''#set punctions 
    
    d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
	 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 
	 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 
	 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
	 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 
	 'z':'zulu'}
  #set ancient list containing original letter and corresponding pronounciation
    words = string.split()
    #split the words in the str to save into "words"
    for word in words:
        for char in word:
            if char not in punctuations:
            #skip the punctions by determining if it is punctuations
               os.system('say ' + d[char.lower()])
               #transfer every letter into lowercased
               #pronounce the corresponding letter
               time.sleep(0.01)#set the time interval between each letter 
               time.sleep(0.1)#set the time interval between each word

    







'''question 5'''
#Construct a dictionary that saves each word of text as its keys, and the counts of the words as its values.
#Construct a list that returns a word which occurs only once, named hapax
#parameter is file_name accepted from your computer.Anytime you a file name in 
#hapax function, it will give you a result.
def hapax(file_name):
    
    
    count_dict = {}
    hapax_list = []
    
    f = open(file_name,'r')#open a file as read file
    text = f.read()#give the file as read to text    
    
    # Each word in the text is splitted by blank space
    for word in text.split(' '):#split the words from text
       
        word = word.lower() # make all words lowercased
       
        if word in count_dict:# Check the occurance of each word
           count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1
     
    
    for word,count in count_dict.items():
        if count == 1:
            hapax_list.append(word)
     # 'word' as dictionary keys and 'count' as dictionary values
    return hapax_list
        





'''question 6'''
#define a function 
def text_lines(fileinput, fileoutput):
#define a function to number the line in file
    in_file = open(fileinput,'r')
    #read fileinput to save as in_file
    out_file = open(fileoutput,'w')#write fileoutput to save as out_file
    line_number = 1 #set intial value for line_number
    for line in in_file:
    #write in_file where line number goes first and line goes second
        out_file.write('{}: {}'.format(line_number, line))
        line_number += 1#increase linenumber by 1 each time
    return line_number






'''question 7'''

# Define what punctuaions constain

def ave_word_len(filepath):
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~ '''
#define a function for average length of word in a text
    file=open(filepath).read()#open a file as read
    no_punct=""
    print(str(file))#transfer file to a string and present it 
    words=file.split()#transfer file to a splitted format as a list
    for char in str(file):
        if char not in punctuations:
            no_punct = no_punct + char
            #get a string without any punctuations
    print(len(words))   
    print(len(no_punct))    
    print(len(no_punct)/len(words))  
    #get the total length of total words divided by the number of word in text.      
  



'''question 8 Write a program able to play the "Guess the number"-game, where
the number to be guessed is randomly chosen between 1 and 20.
'''
 

# define a function as funcguess which can let you guess a number several times 
#parameter: real which is an integer 
#when use this function, just type in funcguess(anynumer)
def funcguess(real):
    
    name = input('Hello! What is your name?')
# tell user what to do
    print('Well,',name,' I am thinking of a number between 1 and 20.')
# real number
    
    real=18
#Stuart- This should be a random number. Look at the random library.

# give the time user guessed an initial value
    time = 1
# use while loop to let user have a guess
    while True:
    # input user's guess
        guess = int(input('Take a guess,'))
    # if the guess number is high, give a clue
        if guess > real:
            print('Your guess is too high.')
        # guess time increase
            time+=1
    # if the guess number is low, give a clue
        elif guess < real:
            print('Your guess is too low.')
        # guess time increase
            time+=1
        else:
        # if the guess is correct, print the guess times
            print('Good job, ',name,'! You guessed my number in',time,'guesses!')
            break





'''question 9'''  
#define a function as funcshuffle which can shuffle the letters of words by
#permutation without changing the number of letters of words 
#parameter:x which is given as shuffled word by changing the order of combination
#of letters of word
def funcshuffle(x):
    import random
    import itertools
#import random and itertools
    words ={"red","black","brown","white","yellow","blue","green"}
#give the words range like some colors
    word=random.sample(words,1)[0]
#randomly pick some color words and take the first one out of them
    x=list(itertools.permutations(word))

#rearrange the letters of the word picked fromm words
    str1=''.join(x[1])
#use join to connect the all letters from list which contains one word without space or other things
    print(str1)
#print the rearranged the word

    print("Colour word anagram:  ")
    
    wordinput=input("Enter a color word you guess: ")
    
    while wordinput!=word:
        print("your guess is incorrect")
        
        wordinput=input("Enter a color word you guess: ")
 #use while loop to distinguish if the wordinput equals the picked word before it is rearranged 
 #keep inputing the word you guess until your answer is the picked word
    print("your guess is correct")





'''question 10'''
#define a function as wordguess which determine whether the owrd you guess is 
#correct or not 
#parameter:guess which is initially valued as null
def wordguess(guess):
    word = list("tiger")
#give a list of words
    print("import lingo")
    guess = []
 #meet the first requirement that correct letters placed in correct positions
#by using bracket to present the clue

    while True:#while loop to judge if the word guess is correct
        guess = list(input("Please enter your guess: "))#make the inputed word into a list
        if guess == word:#determine if the guessed word is equal to the existing word
            print("You guessed the right word!")
            break
        else:
            cluelst = guess# give the guss value to clu1st
            for i in range(0, len(word)):
        #for loop to make i go from 0 to the length of word 
                if guess[i] == word[i]:
            #determine if the ith letter you typed is equal the ith letter in existing word
            
                    cluelst[i] = "[" + guess[i] + "]" 
                #if so, put the guessed letter in the ith position of existing word
            for i in range(0, len(word)):
            #for loop again 
                for j in range(0, len(word)):
                # for loop makes j go from 0 to length of the word
                    if guess[i] == word[j]:
                    #judge if guessed ith letter is equal to jth letter of word
                        cluelst[i] = "(" + guess[i] + ")"
                    # give "(" + guess[i] + ")" to ith cluelst
                        clue = "".join(cluelst)#connect the letters from cluelst
                        print("Clue: " + clue)



'''question 11'''

import re

def sentence_splitter(file_name):
#define a function with one parameter 
#parameter is a filepath that you wanna run on python
    with open(file_name, 'r') as f:
    #open file as read and give the value of f to file_content
        file_content = f.read()

	# remove '\n' and use space instead in file_content as read
    sentences = re.sub(r'\n', '', file_content)

	#remove (?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1' from sentences as read
     #add a newline after period when that period is not followed
	# by 'Mr', 'Mrs' or 'Dr' and is followed by a space and an
	# uppercase letter
    sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)
    

 	#remove '!\s',add new line after ! from sentences as read
    sentences = re.sub(r'!\s', '!\n', sentences)

 	# remove ''\?\s', add newline after ? from sentences as read 
    sentences = re.sub(r'\?\s', '?\n', sentences)

    print(sentences)

#test
sentence_splitter('untitled4.txt')






'''question 12'''
def  anagram(filepath):#define a function anagram
#parameter is a filepath that you wanna test on python
#everytime you type in anagram with a filepath, it show you the test result on 
#on console
     filepath= open ('untitled2.txt').read()#open a file as read
     words=filepath.split()#split the word from file
     for word_similar in words:
         for word in words:
             if set(word)==set(word_similar):
             #distinguish if all letters in word are in word_similar
             #No considering the order of the letters
                 if len(word)==len(word_similar):
                 #distinguish if they have the same number of letter
                     print (word, word_similar)
                     #print outcomes
      
 
    
    
    

'''question 13'''


def brackets(n):#define a function with one parameter 
#parameter n works as length of what needs to be tested 
    i, result, brackets = 0, '', '[]'
    from random import randrange# import randrange
    import re
    #give values to i, result, brackets

	# add the value of brackets start from 0 to length of brackets to result
    while i < n*2:
        result += brackets[randrange(len(brackets))]
        i+=1

	# gieve the result' value to bracket_string
    bracket_string = result

	# Remove all found pairs of brackets using regex
    while len(re.findall(r'\[\]', result)) > 0:
        result = re.sub(r'\[\]', '', result)

	# If after removing all  brackets,  the string is not 0 
    if len(result) > 0:
        print(bracket_string, 'NOT OK')
    else:
        print(bracket_string, 'OK')
    

    def brackets(number):
        if number==1:
            print('[] OK')
            print('[[ Not OK')
            print('][ OK')
            print(']] Not OK')
        elif number==2:
            print('[[]] OK')
            print('[]]] Not OK')
            print('][]] Not OK')
            print('[[[] Not OK')
            print('[[[[ Not OK')
            print('[][] OK')
            print(']]]] Not OK')
            print('][][ Not OK')
            print('][[] Not OK')
        else:
            print('[[[]]] OK')
            print('[[]]]] Not OK')
            print('[[[[]] Not OK')
            print('[][[[[ Not OK')
            print(']][[[[ Not OK')
            print(']]][[[ OK')
            print('[][][] OK')
            print('][[[[[ Not OK')
            print('][[[[] Not OK')
            print('][][][ OK')
    print(brackets(int(input('Enter a number between 1 and 3: '))))



'''question 13 pokeman'''


def poke_names(file):
    #define a function that can list all possible outcomes
#parameter is a file accepetd from your computer 
    import re #import regular expression 
	# save all the names from the file as read
    with open(file, 'r') as f:
        names = re.findall(r'\w+', f.read())

	# set two variable as empty to start 
    longest_series, current_series = [], []

	# return to the next word with last letter as initial 
	# of the previous word
    def name_starts_with(lastletter, names):
        for index, name in enumerate(names):
            if name.startswith(lastletter):
                return index
        return False

	
	# for loop to add current to current series 
    for name in names:
        current_name = name
        current_series.append(current_name) # Add the first name to the series

        namelist = names[:] # save all names in namelist
        namelist.pop(namelist.index(current_name)) # Remove the 1st name 

        index = name_starts_with(current_name[-1], namelist)
        # get the last element of current_name

		#determine there is the next word with last letter as initial 
	# of the previous word
        while index is not False:
            current_name = namelist[index] # Get this name
            current_series.append(current_name) # Add it to the series
            namelist.pop(index) # Remove it from the list
            index = name_starts_with(current_name[-1], namelist) 
            # Get the index of the next name

		# determine the length of current series and longest series 
            if len(current_series) > len(longest_series):
                longest_series = current_series

		# make current series empty
                current_series = []
            else:
                break
	# Print the longest series
        print(longest_series)


#test
poke_names('untitled6.txt')


'''question 14'''
def wordfunc(file):
    #define a function that can combine two words 
    #parameter is a file which be found in your computer.

    for line in file:
        line = line.strip()#remove all all whitespace at the start and end.
        length = len(line)#get length of line
        wordfirst = ""
        wordsecond= ""#set these two variables empty
        for i in range(0, length,2):#for loop to add line[i] to wordfirst one by one
            wordfirst += line[i]
            try:
                wordsecond += line[i+1]#add the next line[i+1 to wordsecon]
            except:
                pass
            word1 = wordfirst.strip()#strip the whitespace off wordfirst
            word2 = wordsecond.strip()#strip the whitespace off wordsecond
            print(word1+" and "+word2)


#citation 
#yishan zhang did question1,2,3,4,7,9,12
#I put some annotation for each line 
#I did try to understand other codes to describe and annotate them
#group members tries their best to finish their pars where everyone was given 
#3 questions to solve and if anyone could understand other questions, they would 
#did more than 3. But if they cannot, they get code from memebers to make their 
#own correct and list the annotation
#change something in each code from group members
#question 5,6,8,10,11,13,14 code are changed from group members
#5,6 from vivi, 8 from Youjin, 10 from Ke, 11,13,14 from Kristen
