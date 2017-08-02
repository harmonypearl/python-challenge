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
        totalVotes = len(dataFileDf.iloc[:,0])

        #find unique names in Candidate column,
        #and tally how many times each name appears
        results = dataFileDf["Candidate"].value_counts()

        #create a dataframe from the value counts,
        #and title the new column
        resultsDf = pd.DataFrame(results)
        resultsDf.columns=["Votes"]

        #create a list from column zero of the dataframe
        votesList = resultsDf.iloc[:, 0].tolist()
        
        #divide each list element by total num of rows,
        #and mult by 100 and round to 1 decimal place

        #create lists from the columns in the dataframe
        candidateList = resultsDf.index.tolist()
        votesList = resultsDf.iloc[:, 0].tolist()

        #divide each list element by total num of rows,
        #and mult by 100 and round to 1 decimal place,
        #and create a new list with a % sign after each element
        votePercentList = np.multiply(np.divide(votesList, totalVotes),100).round(1)
        votePercent = list(map("{}%".format, votePercentList))

        #create a dataframe with all three lists
        resultsDf = pd.DataFrame({
            "Candidate": candidateList,
            "Number of Votes": votesList,
            "Percentage": votePercent
            })

        #create a new index for Number of Votes
        newIndex = resultsDf.set_index("Number of Votes")
        
        #find max of new index, 
        #and set a new variable equal to the coresponding Candidate column
        x=max(votesList)
        maxVotes=newIndex.loc[x].Candidate

        #print results for each .csv file in cwd
        print(f"Election Results\n"
                "----------------\n"
                f"Total Votes: {totalVotes}\n"
                "----------------\n"
                f"{resultsDf.to_string(index=False)}\n"
                "----------------\n"
                f"Winner: {maxVotes}\n")

        #create a .txt file that will add results for each .csv file in cwd
        f = open("ElectionResults.txt", "a")
        f.write(f"Election Results\n"
                "----------------\n"
                f"Total Votes: {totalVotes}\n"
                "----------------\n"
                f"{resultsDf.to_string(index=False)}\n"
                "----------------\n"
                f"Winner: {maxVotes}\n")
        f.close()

