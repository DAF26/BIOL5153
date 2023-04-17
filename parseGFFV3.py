#! /derekdean/bin/env python3

import argparse
import csv
from Bio import SeqIO

# create an ArgumentParser object
parser = argparse.ArgumentParser(description="The script parses a GFF file")

# add positional (required) arguments
parser.add_argument("gff", help= "The Name of the GFF file to parse", type=str)
parser.add_argument("fasta", help="Name of the FASTA file to parse", type=str)

# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args()

# read in the FASTA file 
genome = SeqIO.read(args.fasta, "fasta")
print(genome.description)

# open the GFF file
with open(args.gff) as gff_file:
	
	 # create a csv reader object 
    reader = csv.reader(gff_file, delimiter='\t')
    
    for line in reader:  # loop over the lines in the file
        
        if not line:  # skip blank lines
            continue
            
        #columns = line.split("\t")  # Split the line into individual columns
        
        # creating variable names for the columns 
        organism = line[0]
        source = line[1]
        feature_type = line[2] 
        start = int(line[3])
        end = int(line[4])
        length = line[5]
        strand = line[6]
        attributes = line[8]
        
        line[5] = str(end - start + 1)  # Calculate the feature length
        
        # extract the feature
        feature_seq = genome.seq[start-1:end]
        
        #print(len(feature_seq) - ((end-start)+1))
        
        #print fasta output for this feature
        print(">" + organism, feature_type, attributes)
        print(feature_seq)
        
        new_line = "\t"
       # print(new_line)  # Print the feature type and its length, separated by a tab character.
    
    
    
    
    