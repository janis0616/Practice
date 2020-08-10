#!/usr/bin/env python
# coding: utf-8

# In[29]:


#define the function to extract prophage sequences from a genome, based on the start and stop coordinates
def getprophages(host_genome, prophage_coordinates):
    #open the prophage coordinates file
    Positions = open(prophage_coordinates)
    #read each line of the prophage coordinates file into a list
    Positions_list = Positions.readlines()
    #start a for loop with the positions list to extract each prophage based on its coordinates
    for position in Positions_list:
        #open the output file [append]
        Output = open("output.txt", "a")
        #strip the newline from the end of each line of the positions list
        strip_positions = position.rstrip("\n")
        #split each line of the positions list based on the comma 
        split_positions = strip_positions.split(",")
        #define the start and stop coordinates as the [integer] first and second values in each line of the positions list
        start = int(split_positions[0])
        stop = int(split_positions[1])
        #open and read the genome fasta
        DNA = open(host_genome)
        DNA_read = DNA.read()
        #define each prophage as the start minus one to the stop positions, read from the genome file
        prophage = DNA_read[(start - 1):stop]
        #append each prophage to the output file, with a newline at the beginning and end of each prophage
        Output.write("\n" + prophage + "\n")
        #close all the files
        Output.close()
        DNA.close()
    Positions.close()
#call the function, using genome.fasta as the host genome file and prophages.txt as the prophage coordinates file
getprophages("genome.fasta","prophages.txt")


# In[ ]:




