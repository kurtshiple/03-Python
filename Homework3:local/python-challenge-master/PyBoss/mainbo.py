#dependencies

import os
import csv
#this is the most effective way of reading in a csv file
csvpath = os.path.join('..','PyBoss','employee_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    #This shows us what type of data we are dealing with.
    #We have Emp ID, Name, DOB, SSN, State
    #To tackle the problems in this assignment. My strategy is
    #to get all of these columns as individual lists, edit them,
    #and then put them back together as sublists in a greater list.

    #print(f"CSV_Header = {csv_header}")
    
    listofempdata = [] 
    
    for rows in csvreader:
        listofempdata.append(rows)

    print(listofempdata) 
    
    listofnames = [] 
    listofids = []
    listofdobs = []
    listofssns = []
    listofstates = []
    
    for rows in listofempdata:
        listofnames.append(rows[1])
        listofids.append(rows[0])
        listofdobs.append(rows[2])
        listofssns.append(rows[3])
        listofstates.append(rows[4])
    #----------------------------------------------------------------
    #First, we are going to split the name column into first and last
    
    listoffirstnames = []
    
    for i in listofnames:
        listoffirstnames.append(i.split(" ")[0])

    #print(listoffirstnames) #would show a list of first names
    #print(len(listoffirstnames)) #would show the length. We want to make
    #sure we dont have any missing data.

    listoflastnames = []
    for i in listofnames:
        listoflastnames.append(i.split(" ")[1])

    #print(listoflastnames) #would show a list of first names
    #print(len(listoflastnames)) #would show the length. We want to make
    #sure we dont have any missing data.
    
    #--------------------------------------------------------------
    
    #Next, we take our list of ssns and turn every item into
    #a sublist within the greater list. Then, within each sublist 
    #the string inside gets seperated iterably.
    
    seperatedlistofssns = [list(i) for i in listofssns]
    
    # print(seperatedlistofssns)
    
    #Next, within each sublist, the first 6 indices are replaced
    #and thus obscured by a "***-**" string.
    
    for sublist in seperatedlistofssns:
        sublist[0:6] = "***-**"

    obscuredlistofssns = seperatedlistofssns
    
    #print(obscuredlistofssns)
    
    # Next, the sublists (that seperate the strings by chracter)
    # are reconcatinated so that the format goes from 
    # [['*','-','3'],['*','-','6']] to ['*-3','*-6','*-7']
    
    finalobscuredlistofssns = []
    for sublist in obscuredlistofssns:
        finalobscuredlistofssns.append(''.join(sublist))

    #print(finalobscuredlistofssns)

    #--------------------------------------------------------------------

    #Next, our strategy is to manipulate the format of the date strings
    #in a similar manner to how we obscured the ssns. We are going take each
    #item in our listofdobs, turn that item into a sublist, and then within
    # that sublist, make each character iterable. After each character is
    #made iterable, we slice portions of these sublists and assign them
    #to variables like day,month,year so we can hope to rearrange the order
    #of these variables and add them to other chracters like forward
    #slashes. This way, we will have our desired date format.

    yearlist = []
    daylist = []
    monthlist = []

    seperatedlistofdobs = [list(i) for i in listofdobs]
    for item in seperatedlistofdobs:
        year = item[0:4]
        month = item[5:7]
        day = item[8:]
        yearlist.append(year)
        daylist.append(day)
        monthlist.append(month)

    #print(yearlist)
    #print(daylist)
    #print(monthlist)
    #We just sliced and assigned parts of our sublists but we need to
    #reconcatinate these variables into acceptable format.
    newyearlist = []
    for sublist in yearlist:
        newyearlist.append(''.join(sublist))
    #print(newyearlist)
    newdaylist = []
    for sublist in daylist:
        newdaylist.append(''.join(sublist))
    #print(newdaylist)
    newmonthlist = []
    for sublist in monthlist:
        newmonthlist.append(''.join(sublist))
    #print(newmonthlist)
    #print(len(newmonthlist))
    dashlist = []
    for x in range(651):
        dash = '/'
        dashlist.append(dash)

    #print(dashlist)

    formatteddoblist = [a+b+c+d+e for a,b,c,d,e in zip(newmonthlist, dashlist, newdaylist, dashlist, newyearlist)]
    #print(formatteddoblist)
    #print(len(formatteddoblist))

    #-------------------------------------------------------------

    #Next, we need to convert the states into a different format.
    # We will use this dictionary to simplify that process.
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
        }
    
    #Quite simply, we will use a for loop where we take each item
    #in our listofstates, use that item as an index (key) within
    #our dictionary, and append that returned item to a new list.

    formattedstatelist = []
    for item in listofstates:
        formattedstatelist.append(us_state_abbrev[item])

    #print(formattedstatelist)
    spacecommalist = []
    for x in range(651):
        spacecommalist.append(', ')
    #print(spacecommalist)
    formattedlistofempdata = [a+b+c+d+e+f+g+h+i+j+k for a,b,c,d,e,f,g,h,i,j,k 
    in zip(listofids, spacecommalist, listoffirstnames, spacecommalist,
     listoflastnames, spacecommalist,
    formatteddoblist , spacecommalist,
     finalobscuredlistofssns, spacecommalist, formattedstatelist)]
    print(formattedlistofempdata)
    finalproduct = [[i] for i in formattedlistofempdata]
    #print(finalproduct)
    #with open('mainbo.txt','w') as f:
    #    for 