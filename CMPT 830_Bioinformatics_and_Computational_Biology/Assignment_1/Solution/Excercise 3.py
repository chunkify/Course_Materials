#!/usr/bin/env python3
# This script will open the file provided by the user and read each line of the
# file within a for-loop.  That means that each iteration through the for-loop
# will be performed with a new (the next) line of the input file.
# Open the file
#file = open("Glycoprotein.fasta")

# the first few lines are used for taking the input file name from the user
#if the input file does not contain FASTA extension then the program will print a message and stop the processing.
# if the user give only the file name then it will automatically embed the FASTA extension.
flag = 0
sequence = ""
search_string = "ATATGC"
print("Enter the name of a FASTA file: ")
file_name = input() # read the input file name
file_name_list = file_name.split(".") #split the file name for checking extension
length_list = len(file_name_list)
if length_list == 2 and file_name_list[1] != "fasta": # check if the file name has valid extension or not
  print("enter a valid FASTA file name with extension fasta ")
elif length_list == 1:
  fasta_file_name = file_name + ".fasta" # make the file name with extension "fasta" # embed FASTA extension with the input file name
  file = open(fasta_file_name, "r")
  flag = 1
else:
  file = open(file_name,"r") # user gives correct input file name with extension FASTA
  flag = 1
# The next operation will repeatedly read the next line of the file and place
# it in the string "sequence".  The loop will then be performed for each
# value of "line".  Note that the terminating newline character
# (of the line that was read) will be excluded in the value of "line" by using "line = line.rstrip()"

#test whether the file is properly read or not
if flag:
  for line in file:
    if line[0] != ">": #check whether the fist line is header or not. if header then ignore it.
      line = line.rstrip() # discard the whitespace or newline characters.
      sequence += line # make a string from each line of sequence


index = sequence.find(search_string) # find the index of first occurrence
if index < 0:
  print("No sequence found!") # if no sequence is found
else:
  total_occurence = sequence.count(search_string) # count the total number of occurrences.
  print("The starting position is: ", index + 1, " and the number of occurence is: ",total_occurence)

