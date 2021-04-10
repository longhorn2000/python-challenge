#import poll
import os
import csv
#working directory
csvpath=os.path.join('..','Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    #Declaring variables
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []