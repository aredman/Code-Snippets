# Python script for processing baby names
# Data must be pulled from http://www.ssa.gov/oact/babynames/names.zip 
# Script is unoptimized and will take 2 minutes to run on a laptop due to large array operations

import re
import argparse
import csv
import time
import sys
import urllib.request
import zipfile
from os import walk
from os.path import splitext

remote_names_url = 'http://www.ssa.gov/oact/babynames/names.zip' 
local_file = 'Names.zip'
names_folder = "Records"
script_names_folder = [f".\\{names_folder}\\"]

class NameParser:
    def __init__(self):
        print("Initializing Parser")
        self.male = dict()
        self.female = dict()
        self.neutral = dict()
        self.get_year = re.compile('[1-2][0-9]{3}')
        self.yearlist = []

    def add_file(self,filename):
        print("ADDING FILE:\t"  + str(filename) + "\t",end='')
        file_extension = splitext(filename)[-1]
        if(file_extension!='.txt'):
            print(f"REJECTED: Bad filename")
            return

        # Parse year
        year = self.get_year.search(filename)[0]
        self.yearlist.append(year)

        # Open file for reading
        fid = open(filename,'r')

        # For each line, split and check sex
        # Check if name exists in database, 
        # if it does add the current year
        for line in fid:
            self.parse_line(line,year)

        print("DONE")

    def parse_line(self,line,year):
        array = line.split(',')
        name = array[0]
        sex = array[1]
        count = int(array[2])

        if(sex == 'M'):
            if(name not in self.male):
                self.male[name] = {}
                self.male[name]["Name"] = name
            self.male[name][year] = count

        elif(sex == 'F'):
            if(name not in self.female):
                self.female[name] = {}
                self.female[name]["Name"] = name
            self.female[name][year] = count

        else:
            print("Parsing error at sex")
            return -1

    def pad_dictionary(self):
        print("Padding dictionary for data from missing years")
        nyears = len(self.yearlist)
        print("Padding male list")
        for entry in self.male:
            if(not len(self.male[entry]) == nyears):
                for y in self.yearlist:
                    if(y not in self.male[entry]):
                        self.male[entry][y] = 0

        print("Padding female list")
        for entry in self.female:
            if(not len(self.female[entry]) == nyears):
                for y in self.yearlist:
                    if(y not in self.female[entry]):
                        self.female[entry][y] = 0

    def pad_entry(self,entry):
        for y in self.yearlist:
            if(y not in entry):
                for y in self.yearlist:
                    if(y not in self.female[entry]):
                        self.female[entry][y] = "0"

    def output_csv(self):
        print("Outputting names lists to csv")

        fname = "male.csv"
        fid = open(fname,'w')
        fieldnames = ["Name"] + self.yearlist
        writer = csv.DictWriter(fid, delimiter=',',fieldnames=fieldnames)
        writer.writeheader()
        
        for entry in self.male:
            writer.writerow(self.male[entry])
        fid.close()

        fname = "female.csv"
        fid = open(fname,'w')
        fieldnames = ["Name"] + self.yearlist
        writer = csv.DictWriter(fid, delimiter=',',fieldnames=fieldnames)
        writer.writeheader()
        
        for entry in self.female:
            writer.writerow(self.female[entry])

# Option to look for overlap and output neutral names that are on both M/F lists
#        fname = "neutral.csv"
#        fid = open(fname,'w')
#        fieldnames = ["Name"] + self.yearlist
#        writer = csv.DictWriter(fid, delimiter=',',fieldnames=fieldnames)
#        writer.writeheader()
#        
#        for entry in self.neutral:
#            writer.writerow(self.neutral[entry])
#        fid.close()

    def neutral_search(self):
        for key in self.male:
            try:
                year_compare = '2001'
                pop_thresh = 300
                if(key in self.female and year_compare in self.female[key]):
                    m_count = self.male[key][year_compare]
                    f_count = self.female[key][year_compare]
            
                    #if (m_count > pop_thresh and f_count > pop_thresh):
                    ratio = m_count / f_count
                    rat_set = 1.2
                    if( ratio >=1/rat_set and ratio <= rat_set):
                        print(key + "\tM: " + str(m_count) + " F: " + str(f_count) + " R: " + str(round(ratio,2)))
            except:
                continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Social Security baby name lists")
    parser.add_argument('-d','--download', action='store_true',help="Download records as zip from SSA.gov website and unarchive")
    parser.add_argument('-p','--process', action='store_true',help="Process records after download")
    parser.add_argument('-f','--folder',required=False,metavar='Folder location', nargs='+',help="Input folder which directly contains record files")
    my_args = parser.parse_args()

    if(my_args.download):
        print(f"Downloading records from {remote_names_url}")
        urllib.request.urlretrieve(remote_names_url, local_file)
        print(f"Download succeeded. Records placed in {local_file}")
        print(f"Attempting to extract {local_file} to ./{names_folder}")
        with zipfile.ZipFile(local_file, 'r') as zip_ref:
            zip_ref.extractall(names_folder)
        print("Success")

    if(my_args.process):
        my_args.folder = script_names_folder
        print(f"Attempting to process records stored in {my_args.folder}")

    if(my_args.folder == None):
        print("No input folder to process... Quitting")
        sys.exit()

    my_names = NameParser()

    print(f"Records folder: {my_args.folder}")
    for fo in my_args.folder:
        for (dir_path,_,filenames) in walk(fo):
            for f in filenames:
                my_names.add_file(f"{dir_path}{f}")

    #my_names.neutral_search()
    my_names.pad_dictionary()
    my_names.output_csv();
