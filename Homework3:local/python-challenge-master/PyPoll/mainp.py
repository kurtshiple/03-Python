#dependencies
import os
import csv
#this is the most effective way of reading in a csv file
csvpath = os.path.join('..','PyPoll','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    
    #This shows you how your data is going to be formatted
    #print(f"CSV_Header = {csv_header}")

    total_votes = 0

    candidate_names_list = []
    #This for loop does two things. It counts the total number of rows to represent
    #Thw total number of votes. It also makes a list of the votes represented by the 
    #candidates names only
    for rows in csvreader:
        total_votes = total_votes + 1
        candidate_names = rows[2]
        candidate_names_list.append(candidate_names)
    #print(total_votes) would show how many votes there were total
    unique_names_list = list(set(candidate_names_list))
    #print(unique_names_list) would show that when you take a list and turn it into a set,
    #you get no duplicate elements in return. This allows us to see four unique strings that
    #That are present in our longer list. The idea is to then create a unique for loop
    #with nested if statements to iterate across the longer list and see what indices
    #match with one of our four unique strings and tally the results according to name.
    Li = 0
    Khan = 0
    OTooley = 0
    Correy = 0
    
    for name in candidate_names_list:
        if name == "Li":
            Li = Li + 1
        elif name == "Khan":
            Khan = Khan + 1
        elif name == "O'Tooley":
            OTooley = OTooley + 1
        elif name == "Correy":
            Correy = Correy + 1
           
    name_count_list= [Li,Khan,OTooley,Correy]

    #print(name_count_list) would show a list of four integers each corresponding to a name.
    #This for loop takes the raw totals we received in our name_count_list and divide by 
    #Total votes in order to turn the name_count_list  into percentages.
    name_percentage_list = []
    for x in name_count_list:
        name_percentage_list.append((x/total_votes)*100)

    #print(name_percentage_list)

    with open('mainp.txt','w') as f:
        print("Election Results")
        f.write("Election Results")
        f.write("\n")
        print("-----------------------")
        f.write("-----------------------")
        f.write("\n")
        print(f"Total Votes:  {total_votes}")
        f.write(f"Total Votes:  {total_votes}")
        f.write("\n")
        print("-----------------------")
        f.write("-----------------------")
        f.write("\n")
        print(f"Khan:  {round(name_percentage_list[1],3)} %  ({name_count_list[1]})")
        f.write(f"Khan:  {round(name_percentage_list[1],3)} %  ({name_count_list[1]})")
        f.write("\n")
        print(f"Correy:  {round(name_percentage_list[3],3)} %  ({name_count_list[3]})")
        f.write(f"Correy:  {round(name_percentage_list[3],3)} %  ({name_count_list[3]})")
        f.write("\n")
        print(f"Li:  {round(name_percentage_list[0],3)} %  ({name_count_list[0]})")
        f.write(f"Li:  {round(name_percentage_list[0],3)} %  ({name_count_list[0]})")
        f.write("\n")
        print(f"O'Tooley:  {round(name_percentage_list[2],3)} %  ({name_count_list[2]})")
        f.write(f"O'Tooley:  {round(name_percentage_list[2],3)} %  ({name_count_list[2]})")