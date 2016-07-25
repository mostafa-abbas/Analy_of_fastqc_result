import random
import os
import linecache
import sys
import errno
import re
#read files from the specific path
def list_files(path):
    # returns a list of names (with extension, without full path) of all directories
    # in folder path
    files = []
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            files.append(name)
    return files
if __name__ == "__main__":
    path = "fastqc_results"
    files = list_files(path)
    No_reads ={}
    GC = {}
    print files
    for x in files:
        f= open(path+"\\"+x+"\\"+x+"_fastqc\\fastqc_data.txt",'r')
        for line in f:
            s=line.strip()
            if(s.find("Total Sequences")>-1):
                s_ = s.split()
                No_reads[x]=int(s_[2])

            elif(s.find("%GC")>-1):
                s_ = s.split()
                GC[x]=float(s_[1])
                       
            
        f.close()
    print len(No_reads)
    print len(GC)
    print len(files)
    f = open("summary_of_samples.xls",'w')
    f.write("SampleName\tNo_reads\tGC%\n")
    for x in files:
        f.write(x+"\t"+str(No_reads[x])+"\t"+str(GC[x])+"\n")
    f.close()
    
                               
                               
                               
    
