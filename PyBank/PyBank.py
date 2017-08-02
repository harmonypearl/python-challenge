#dependencies
import os
import csv
import pandas as pd
import numpy as np

#create a path to current working directory
resourcePath = os.getcwd()

#create a list and add all .csv files from current directory to it using a for loop
filepaths = []
for file in os.listdir(resourcePath):
    if file.endswith(".csv"):
        filepaths.append(os.path.join(resourcePath, file))

        #read the .csv files as a dataframe
        dataFileDf = pd.read_csv(file)

        #find total rows
        totalMonths = len(dataFileDf.iloc[:,0])

        #create a list of column 1
        revList = dataFileDf.iloc[:, 1].tolist()

        #calculate average change of rows in column 1
        aveChange = (revList[-1] - revList[0])/(totalMonths - 1)

        #create a list for the difference between each row in column 1
        deltaElement = [y - x for x, y in zip(revList, revList[1:])]

        #turn that list into a dataframe and title the column
        deltaDf = pd.DataFrame(deltaElement)
        deltaDf.columns=["Delta"]

        #create a 1x1 dataframe with value 0 and append onto previous dataframe
        zeroRowDf = pd.DataFrame([0])
        zeroRowDf.columns=["Delta"]
        deltaDf2 = zeroRowDf.append(deltaDf, ignore_index=True)

        #merge created dataframe with original file dataframe
        mergeTable = pd.merge(dataFileDf, deltaDf2, right_index=True, left_index=True)
      
        #index the total dataframe by the new column
        newIndex = mergeTable.set_index("Delta")
       
        #find max and min of new column, 
        #and set variables equal to the coresponding Date column
        x=max(deltaElement)
        maxDate=newIndex.loc[x].Date
        y=min(deltaElement)
        minDate=newIndex.loc[y].Date

        #print results for each .csv file in cwd
        print (f"Financial Analysis\n"
                "------------------\n"
                f"Total Months: {totalMonths}\n"
                f"Total Revenue: ${np.sum(revList)}\n"
                f"Average Revenue Change: ${round(aveChange,2)}\n"
                f"Greatest Increase in Revenue:  {maxDate} ${max(deltaElement)}\n"
                f"Greatest Decrease in Revenue:  {minDate} ${min(deltaElement)}\n")

        #create a .txt file that will add results for each .csv file in cwd
        f = open("BankResults.txt", "a")
        f.write(f"Financial Analysis\n"
                "------------------\n"
                f"Total Months: {totalMonths}\n"
                f"Total Revenue: ${np.sum(revList)}\n"
                f"Average Revenue Change: ${round(aveChange,2)}\n"
                f"Greatest Increase in Revenue:  {maxDate} ${max(deltaElement)}\n"
                f"Greatest Decrease in Revenue:  {minDate} ${min(deltaElement)}\n")
        f.close()