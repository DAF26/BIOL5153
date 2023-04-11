#! /derekdean/bin/env python3

import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="The script parses a GFF file")

# add positional (required) arguments
parser.add_argument("gff", help= "The Name of the GFF file to parse", type=str)
parser.add_argument("fasta", help="Name of the FASTA file to parse", type=str)

# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args()

# open the GFF file
with open(args.gff) as x:
    # loop over the lines in the file
    for line in x:
        line = line.strip() # Remove the newline character
        columns = line.split("\t") # Split the line into individual columns
        feature_type = columns[2] # Extract the feature type from the third column
        feature_len = int(columns[4]) - int(columns[3]) + 1 # Calculate the feature length
        print(f"{feature_type}\t{feature_len}") # Print the feature type and its length, separated by a tab character

		
