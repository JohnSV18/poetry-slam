#importing random module to use in random function later on 
import random

#variable that holds the text file
filename = "rupi.txt"

#variable that has the text file open to read
poem = open("rupi.txt", 'r')

#this function is to read the lines
def get_file_lines(filename):
    file_lines = poem.readlines()
    return file_lines
    
#variable lines_list holding the value you get when the function is called
lines_list = get_file_lines(filename)

#function that will print the lines backwards with the number of the line as well
def lines_printed_backwards(lines_list):
    #creating an empty list
    numbered_lines = []

    #for loop for every index in the length of the lines_list 
    #you will add to the empty list with a space and then the number of the index
    for i in range(len(lines_list)):
        numbered_lines.append(str(i) + ' ' + lines_list[i])
        #a variable that holds the list numbered_lines but in reverse
    reverse_list = numbered_lines.reverse()

    #for loop that prints out the lines of the numbered_lines list
    for line in numbered_lines:
        print(line.strip())

#calling the lines_printed_backwards function
lines_printed_backwards(lines_list)

 #function that prints the lines in a random order
def lines_printed_random(lines_list):
    #a variable that holds the length of lines_list
    list_len = len(lines_list)
    #for loop that for every item in the range of the list_len
    #you print lines_list at a random index
    for i in range(list_len):
        print(lines_list[random.randint(0,list_len-1)].strip())
        
    #calling the function to print the lines in a random order
lines_printed_random(lines_list)


#a custom function that prints the lines with a string right before
def lines_printed_custom(lines_list):
    for i in range(len(lines_list)):
        print("This line says: " + lines_list[i].strip())

lines_printed_custom(lines_list)
