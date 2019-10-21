#!/usr/bin/env python3
# This script will open the file provided by the user and read each line of the
# file within a for-loop.  That means that each iteration through the for-loop
# will be performed with a new (the next) line of the input file.
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
  fasta_file_name = file_name + ".fasta" # make the file name with extension "fasta"
  file = open(fasta_file_name, "r")
  flag = 1
else:
  file = open(file_name,"r") # user gives correct input file name with extension FASTA
  flag = 1
# The next operation will repeatedly read the next line of the file and place
# it in the string "sequence".  The loop will then be performed for each
# value of "line".  Note that the terminating newline character
# (of the line that was read) will be excluded in the value of "line" by using "line = line.rstrip()"


if flag: #test whether the file is properly read or not
  for line in file:
    if line[0] != ">": #check whether the fist line is header or not. if header then ignore it.
      line = line.rstrip() # discard the whitespace or newline characters.
      sequence += line # make a string from each line of sequence


# this is a simple way to count the total number of occurrences of a
# particular sequence pattern in a long sequence
index = sequence.find(search_string) # find the index of first occurrence
if index < 0:
  print("No sequence found!") # if no sequence is found
else:
  total_occurrence = sequence.count(search_string) # count the total number of occurrences.
  print("The starting position of first occurrence is: ", index + 1, " and the number of occurrences is: ",total_occurrence)


# here is another way to calculate total number of occurrences and the position of first occurrence

search_str_seq_length = len(search_string)
temp = 1
sequence_count = 0
iteration = len(sequence) - search_str_seq_length
i = 0
while i <= iteration:
  if sequence[i : i + search_str_seq_length] == search_string: # match the pattern
    if(temp):
      idx = i # save the index of first occurrence of search string
      temp = 0
      sequence_count += 1 #increase the sequence count
    else:
      sequence_count += 1  # increase the sequence count
  i += 1 #increment the loop
if temp:
  print("No sequence found!") # if no sequence is found
else:
  print("The starting position of first occurrence is: ", idx + 1, " and the number of occurrences is: ",sequence_count)


