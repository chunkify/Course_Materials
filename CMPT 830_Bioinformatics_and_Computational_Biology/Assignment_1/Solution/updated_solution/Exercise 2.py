#!/usr/bin/env python3
# This script will open the file provided by the user and read each line of the
# file within a for-loop.  That means that each iteration through the for-loop
# will be performed with a new (the next) line of the input file.
# the first few lines are used for taking the input file name from the user
#if the input file does not contain FASTA extension then the program will print a message and stop the processing.
# if the user give only the file name then it will automatically embed the FASTA extension.

flag = 0
total_sequence = 0
amino_acid = "";
amino_acid_count = 0
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
    if line[0] == ">": #check for header
      header = line
      if amino_acid_count != 0:
        print("the first ten characters are: ",amino_acid[0:10]," and the total amino acid count is: ",amino_acid_count)
        amino_acid_count = 0
        amino_acid = ""
      print("the header is: ", line.rstrip())
      total_sequence += 1
      #f.write(line)
    else:
      line = line.rstrip() # discard the whitespace or newline characters.
      amino_acid += line # make the total sequence from line
      amino_acid_count += len(line) #count total characters
    #line = line.rstrip()
    #print( "the line contains ", len(line), " characters")
    #print("the string: ", line)

# Close the opened file.  This step is actually optional if it occurs
# at the end of the script.
#file.close()
if header[0] == ">":
  print("the first ten characters are: ", amino_acid[0:10], " and the total amino acid count is: ", amino_acid_count)
print("total sequence is: ", total_sequence) #print total number of sequences

