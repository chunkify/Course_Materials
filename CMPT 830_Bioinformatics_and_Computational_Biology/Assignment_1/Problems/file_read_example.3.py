#!/usr/bin/env python3
# This script is the same functionality as file_read_example.2.py, except
# that any terminating whitespace characters, especially newline characters,
# are removed from the end of each line read, should that character be 
# present.  This latter operation is performed with the rstrip() method.

# Open the file 
file = open("Glycoprotein.fasta")

# The next operation will repeatedly read the next line of the file and place 
# it in the string "line".  The loop will then be performed for each
# value of "line".  Note that the terminating newline will be included
# in the value of "line"
for line in file:
  # Remove any trailing whitespace characters from the string in the
  # variable "line", including any newline characters
  line=line.rstrip()
  # Print out the length of the trimmed line
  print( "the line contains ", len(line), " characters")

# Close the opened file.  This step is actually optional if it occurs 
# at the end of the script.
file.close()
