#!/usr/bin/env python3
# This script will open the file "Glycoprotein.fasta" and read each line of the
# file within a for-loop.  That means that each iteration through the for-loop
# will be performed with a new (the next) line of the input file.  The
# number of characters in each line is printed.

# Open the file
#file = open("Glycoprotein.fasta")
flag = 0
total_sequence = 0
amino_acid = "";
amino_acid_count = 0
print("Enter the name of a FASTA file: ")
file_name = input()
file_name_list = file_name.split(".")
length_list = len(file_name_list)
if length_list == 2 and file_name_list[1] != "fasta":
  print("enter a valid FASTA file name with extension fasta ")
elif length_list == 1:
  fasta_file_name = file_name + ".fasta" # make the file name with extension "fasta"
  file = open(fasta_file_name, "r")
  flag = 1
else:
  file = open(file_name,"r")
  flag = 1
f= open("out.txt","w+")
# The next operation will repeatedly read the next line of the file and place
# it in the string "line".  The loop will then be performed for each
# value of "line".  Note that the terminating newline character
# (of the line that was read) will be included in the value of "line"
if flag:
  for line in file:
  #Print out the length of the line
    if line[0] == ">":
      header = line
      if amino_acid_count != 0:
        print("the first ten characters are: ",amino_acid[0:10]," and the total amino acid count is: ",amino_acid_count)
        amino_acid_count = 0
        amino_acid = ""
      print("the header is: ", line.rstrip())
      total_sequence += 1
      #f.write(line)
    else:
      line = line.rstrip()
      amino_acid += line
      amino_acid_count += len(line)
    #line = line.rstrip()
    #print( "the line contains ", len(line), " characters")
    #print("the string: ", line)

# Close the opened file.  This step is actually optional if it occurs
# at the end of the script.
#file.close()
if header[0] == ">":
  print("the first ten characters are: ", amino_acid[0:10], " and the total amino acid count is: ", amino_acid_count)
print("total sequence is: ", total_sequence)

