# I will be using the lahman database as filler

  #import packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pylahman

  #if using a directory this shows all databases in it
print(dir(pylahman))

#create dataframe object
data = pylahman.Batting()
FILL_VALUE = "a stand in value"
df = pd.read_csv('FILE.csv') #pd.read_excel('FILE.xls')

#getting to know the data
data.head()
data.info()
data.isnull().sum()

#get the descriptives
data.describe() #this'n is the best. It's like the top dawg
data.mean(numeric_only=True)
data.std(numeric_only=True)
data.count()
data.nunique()
data.skew(numeric_only=True)
data.kurtosis(numeric_only=True)


#handling Null and empty spaces
dataExcludingNull = data.dropna() #if you want change the original dataframe just use (inplace= True)
dataDropNullIfCOLUMNhasNull.dropna(subset=['COLUMN_NAME'], inplace = True)

#filling NULLS
dataFilledNull = data.fillna(FILL_VALUE) #fills all empty cells
data.fillna({"COLUMN_NAME": FILL_VALUE}, inplace=True) #fills just a column

#gettin fancy with filling NULLS
x = data['COLUMN_NAME'].mean() #can use median, mode, and etc inplace of mean
data.fillna({'COLUMN_NAME': x},inplace=True)

#grouping stuff
data.groupby('COLUMN_NAME').describe() #can also use mean, median, std, and etc

#other operations
data["DATE_COLUMN"] = pd.to_datetime(data["DATE_COLUMN"],format="mixed") #change formate to date
data.duplicated().sum() #counts number of duplicate rows
data.drop_duplicates(inplace= True) #drop duplicates

#Exploration
data.corr() #corelation matrix simple

numpy.percentile('variable', 90) #change 90 to chage the percentile

#charting
data.plot(kind = 'scatter', x = 'X_VARIALBE', y = 'Y_VARIABLE')
data['COLUMN_NAME'].plot(kind='hist')

plt.show()



#matplot graphs

#general format
plt.scatter('X_VARIABLE', 'Y_VARIABLE', color="blue") #does not need quotes can also use df['column'] for x and y
plt.bar('X_VARIABLE', 'Y_VARIABLE')
plt.hist('X_VARIABLE')

plt.title("TITLE")
plt.xlabel('X_LABEL')
plt.ylabel('Y_LABEL')


plt.show()
