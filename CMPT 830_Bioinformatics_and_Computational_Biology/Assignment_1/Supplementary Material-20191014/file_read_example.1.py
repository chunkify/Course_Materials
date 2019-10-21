#!/usr/bin/env python3
# This script will open the file "Glycoprotein.fasta" and read, on one
# operation, the entire content of the file.  It then outputs the number
# of characters in the file.
file = open("Glycoprotein.fasta")

# The next operation will read the entire content of the file in one
# operation.  Line ends are 
content = file.read()
# A problem with the above operation is that the string in "f" contains
# characters such as newline characters.  

# Output the length of the string that was input.
print( "the file contains ", len(content), " characters")

# Close the opened file.  This step is actually optional if it occurs 
# at the end of the script.
file.close()

