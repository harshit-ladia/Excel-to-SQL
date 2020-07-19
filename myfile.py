import pandas as pd

my_data = pd.read_csv(r"file.csv")

table = input()

query=[]
# my file had id as a column
for j in range(my_data['Id'].count()):
    query.append("Insert into " + table + " values({},{});".format(my_data.iloc[j,0],my_data.iloc[j,1]))
    
with open("insert_query.sql","a") as sql:
    for i in query:
        sql.write(i+"\n")
