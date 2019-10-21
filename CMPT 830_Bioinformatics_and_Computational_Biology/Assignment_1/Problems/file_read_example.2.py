#!/usr/bin/env python3
# This script will open the file "Glycoprotein.fasta" and read each line of the 
# file within a for-loop.  That means that each iteration through the for-loop
# will be performed with a new (the next) line of the input file.  The
# number of characters in each line is printed.

# Open the file 
file = open("Glycoprotein.fasta")

# The next operation will repeatedly read the next line of the file and place 
# it in the string "line".  The loop will then be performed for each
# value of "line".  Note that the terminating newline character
# (of the line that was read) will be included in the value of "line"
for line in file:
  # Print out the length of the line
  print( "the line contains ", len(line), " characters")

# Close the opened file.  This step is actually optional if it occurs 
# at the end of the script.
file.close()

