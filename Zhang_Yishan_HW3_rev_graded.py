#Stuart- Very nice output, good job. 

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:01:47 2016

@author: zyszys1992
"""

import pandas as pd#import pandas
df = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv')
df.hist()#draw histogram of data you use

import pandas as pd
df = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv')
df.boxplot()#draw boxplot 




#This is for diamond 
import matplotlib.pyplot as plt#import pandas and pyplot
import pandas as pd
df = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv')
df

df.columns = ['', 'carat', 'colour','clarity','certification','price']#name the 
#columns that show up in the data 
Df=df.describe()#describe the information of data

upper = (Df.ix[6,2]+(Df.ix[6,2]-Df.ix[4,2])*1.5)
#set upper limit for upper outlier
lower = (Df.ix[4,2]-(Df.ix[6,2]-Df.ix[4,2])*1.5)
#set upper limit for lower outlier
upperoutlier=0
loweroutlier=0
for i in range(0,308):
    #for loop to make comparision between upper limit and each data, lower 
#limit and each data 
    if df.ix[i,5]>upper:
       upperoutlier+=1
       #count the number of upper outlier 
    elif df.ix[i,5]<lower:
        loweroutlier+=1
        #count the number of lower outlier 
print(upperoutlier)
print(loweroutlier)


optimalbins=2*(Df.ix[6,2]-Df.ix[4,2])/(308**(1/3))
#use freedman diaconis formula to get the optimal bins size
binsnum=round((Df.ix[7,2]-Df.ix[3,2])/optimalbins)
#get the number of bins in graph by optimal bin size 
print(optimalbins)
plt.hist(df['price'], color='b',bins=binsnum, range=(638,16008))
#plot the diamond price graph and set the bins number and range 
plt.title("price" )
plt.xlabel("diamond price")
plt.ylabel("Frequency")
#to give the title and x label and y label for the graph


import matplotlib.pyplot as plt
import pandas as pd#import pandas and pyplot
df = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv')
plt.boxplot(df['price'])
#boxplot for the diamond price individually





#This is for diamond carat
import matplotlib.pyplot as plt
import pandas as pd#import pandas and pyplot
df = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv')
df.columns = ['', 'carat', 'colour','clarity','certification','price']
#name the 
#columns that show up in the data 
Df=df.describe()
#describe the information of data

upper = Df.ix[6,1]+(Df.ix[6,1]-Df.ix[4,1])*1.5
 #set upper limit for upper outlier
lower = Df.ix[4,1]-(Df.ix[6,1]-Df.ix[4,1])*1.5
#set upper limit for lower outlier
upperoutlier=[0]*309

loweroutlier=[0]*309

for i in range(0,308):
     #for loop to make comparision between upper limit and each data, lower 
#limit and each data
    if df.ix[i,1]>upper:
       upperoutlier+=1
   #count the number of upper outlier
    elif df.ix[i,1]<lower:
        loweroutlier+=1
     #count the number of lower outlier    

optimalbins=2*(Df.ix[6,1]-Df.ix[4,1])/(308**(1/3))
#use freedman diaconis formula to get the optimal bins size
binsnum=round((Df.ix[7,1]-Df.ix[3,1])/optimalbins)
#get the number of bins in graph by optimal bin size 
print(optimalbins)
plt.hist(df['carat'], color='b',bins=binsnum, range=(0.18,1.1))
#plot the diamond price graph and set the bins number and range 
plt.title("carat" )
plt.xlabel("diamond carat")
plt.ylabel("Frequency")
#to give the title and x label and y label for the graph


import matplotlib.pyplot as plt
import pandas as pd#import pandas and pyplot
df = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv')
plt.boxplot(df['carat'])
#boxplot for the diamond carat individually
 



import matplotlib.pyplot as plt
import pandas as pd#import pandas and pyplot
abalone=pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
#name the 
#columns that show up in the data 
abalone.columns=['sex','length','diameter','height','whole weight',
    'shucked weight','viscera weight','shell weight','rings']
abalone.hist(abalone.columns)
#give the histogram for each column

    
import pandas as pd#import pandas and pyplot
abalone=pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
#name the 
#columns that show up in the data 
abalone.columns=['sex','length','diameter','height','whole weight',
    'shucked weight','viscera weight','shell weight','rings']
abalone.boxplot()
#give the box plot for each column



import pandas as pd
import matplotlib.pyplot as plt
#import pandas and pyplot
abalone=pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
abalone.columns=['sex','length','diameter','height','whole weight',
    'shucked weight','viscera weight','shell weight','rings']
    #name the 
#columns that show up in the data 
abalone
Df=abalone.describe()
#describe the information of data
upper=[0]*8
lower=[0]*8
#give 8 spaces for upper and lower limits 
for i in range(0,8):
    #for loop to set the upper and lower limits for each column
    upper[i] = Df.ix[6,i]+(Df.ix[6,i]-Df.ix[4,i])*1.5
    lower[i] = Df.ix[4,i]-(Df.ix[6,i]-Df.ix[4,i])*1.5




upperoutlier=[0]*9
loweroutlier=[0]*9
#give 8 spaces for upperoutliers and loweroutlier

for j in range(1,9):
    for i in range(0,4176):
        #two for loops to make i go first which means calculate rows first 
    #once we finish row calculation, we move to next column to calculate the 
    #same thing 
        if abalone.ix[i,j]>upper[j-1]:
            #compare each number from the same column with coressponding 
        #upper limit
            upperoutlier[j]=upperoutlier[j]+1
            #count the number of upperoutlier 
        elif abalone.ix[i,j]<lower[j-1]:
             #compare each number from the same column with coressponding 
        #lower limit
            loweroutlier[j]=loweroutlier[j]+1
         #count the number of loweroutlier 
        
        
for i in range(0,8):       
    print(upperoutlier[i])
    print(loweroutlier[i])
#prin the upperoutliers and loweroutliers one by one correspondingly 

optimalbins=[0]*9
binsnum=[0]*9
#set the space size for optimal bins and coressponding number of bin
for i in range(0,8):
    #for loop makes i go from the first bin to tehe end
    optimalbins[i]=2*(Df.ix[6,i]-Df.ix[4,i])/(4176**(1/3))
    #get the corresponding optimal bins by using freedman diaconis formula 
    binsnum[i]=round((Df.ix[7,i]-Df.ix[3,i])/optimalbins[i])
    #get the number of bins corrsponing to its optimal bins 
    print(binsnum[i])

for i in range(1,9):
    abalone.hist(abalone.columns[i], bins=binsnum[i-1],range=(Df.ix[3,i-1],Df.ix[7,i-1]))
#plot the histogram for each modified abalone columns with coressponding bins 
#number and range.
#above part was done by yishan zhang
    
     
#KDD Data part 
#This part is from  my group member Yichen Zhang
#Her part is different from mine which includes the KDD data part but I can't only 
#extract that part because that will affect the other parts completion
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series
import numpy

def histogram_outlier(data,tit):
    '''
    the function, histogram_outlier() is to test for severe outliers that could 
    hide the true shape of the distribution, separate that part of the data, 
    and plot histograms for both segments of the distribution.
    
    Parameter:
    data: a series of data
    tit: the title of this data
    
    output:
    no return, but histograms of segments of data and one box plot of whole data
    '''
    # separate the outliers
    stati = data.describe()# obtain the simple location statistics
    upper = stati.ix[6,0]+(stati.ix[6,0]-stati.ix[4,0])*1.5#caculate outliers up threshold
    lower = stati.ix[4,0]-(stati.ix[6,0]-stati.ix[4,0])*1.5# caculate outliers down threshold
    outlierup=[] #initialize a list to store upper outliers 
    outlierdown=[] #initialize a list to store lower outliers 
    norm=[] #initialize a list to store main part of data 
    up=1
    low=1# initalize a key to determine if there is outliers
    for i in range(0,len(data)):
        if float(data[i])> upper:
            outlierup=outlierup+[float(data[i])] # if data are beyond the upper threshold, store them in outlierup      
        elif float(data[i])<lower:
            outlierdown=outlierdown+[float(data[i])]# if data are lower than the lower threshold, store them in outlierdown
        else:        
            norm=norm+[float(data[i])]# if data are between the two thresholds, store them in norm
    outlierup=Series(outlierup) 
    norm=Series(norm)
    outlierdown=Series(outlierdown)# transfer these three lists into pandas' series  
    if len(outlierup)==0:
        print('there is no up outliers for %s' %tit) # if outlierup is empty, there is no upper outliers and value up with 0
        up=0
    if len(outlierdown)==0:
        print('there is no down outliers for %s' %tit)# if outlierdown is empty, there is no lower outliers and value low with 0
        low=0
    
    # calculate the optimal bin width and draw historgram
    stat=norm.describe() # obtain the simple location statistics of main part data
    iqr=stat.ix[6,0]-stat.ix[4,0]# caculate the IQR
    h=2*iqr/(len(norm)**(1/3))#use freedom-diaconis rule to caculate the optimal bin width
    bin=round((max(norm)-min(norm))/h)# caculate the optimal bins number
    plt.figure()
    plt.hist(norm, bins=bin) #draw the histogram with optimal bins number
    plt.title("Main Part Histogram of %s" %tit)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()
   
    
    if up==1:# if there are upper outlier's data, draw upper outlier histogram
        statup=outlierup.describe()# obtain the simple location statistics of upper outliers
        iqr=statup.ix[6,0]-statup.ix[4,0] #caculate the IQR
        h=2*iqr/(len(outlierup)**(1/3))#use freedom-diaconis rule to caculate the optimal bin width
        bin=round((max(outlierup)-min(outlierup))/h)# caculate the optimal bins number
        plt.figure()
        plt.hist(outlierup, bins=bin)#draw the histogram with optimal bins numbe
        plt.title("Upper Outlier Histogram of %s" %tit)
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()
       
    if low==1: # if there are lower outlier's data, draw lower outlier histogram
        statdown=outlierdown.describe()# obtain the simple location statistics of lower outliers
        iqr=statdown.ix[6,0]-statdown.ix[4,0]#caculate the IQR
        h=2*iqr/(len(outlierdown)**(1/3))#use freedom-diaconis rule to caculate the optimal bin width
        bin=round((max(outlierdown)-min(outlierdown))/h)# caculate the optimal bins number
        plt.figure()
        plt.hist(outlierdown, bins=bin)#draw the histogram with optimal bins number
        plt.title("Lower Outlier Histogram of %s" %tit)
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.show()
      
    #draw box plot
    plt.figure()
    plt.boxplot(data)# draw the box plot of whole data
    plt.title("%s box plot" %tit)
    plt.show()
    
def main1():
    '''
    this main1() function is to read the diamond pricing dataset and then draw 
    histograms
    '''
    data_index='https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv'
    diamond=pd.read_csv(data_index)# read the data set from website
    title=diamond.head(0)# value the 'title' with the header of 'diamond' data set
    
    carat=diamond.ix[:,1] # value the 'carat' with diamond's carat data
    price=diamond.ix[:,5] # value the 'price' with diamond's price data
    
  
    histogram_outlier(carat,title.columns[1])#draw the histograms about carat data set
    histogram_outlier(price,title.columns[5])#draw the histograms about price data set
    
def main2():
    data_index='http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
    abalone=pd.read_csv(data_index,header=None,names=['sex','length','diameter','height','whole weight',\
    'shucked weight','viscera weight','shell weight','rings'])# read the Abalone dataset and then add the column names to them
    title=abalone.head(0)# value the 'title' with the header of 'abalone' data set
    
    for i in range(0,len(title.columns)): #read the abalone dataset column by column
        if type(abalone.ix[1,i])==numpy.float64:# if it is float number, draw the histograms of this series
            histogram_outlier(abalone.ix[:,i],title.columns[i])
        
def main3():
    kdd=pd.read_csv('/Users/zyszys1992/Downloads/census-income.data-')
    header=None,names=['AAGE','ACLSWKR','ADTIND','ADTOCC','AGI','AHGA','AHRSPAY','AHSCOL','AMARITL','AMJIND','AMJOCC','ARACE','AREORGN','ASEX',
                  'AUNMEM','AUNTYPE','AWKSTAT','CAPGAIN','CAPLOSS','DIVVAL','FEDTAX','FILESTAT','GRINREG','GRINST','HHDFMX','HHDREL','MARSUPWT',
                  'MIGMTR1','MIGMTR3','MIGMTR4','MIGSAME','MIGSUN','NOEMP','PARENT','PEARNVAL','PEFNTVTY','PEMNTVTY','PENATVTY','PRCITSHP','PTOTVAL',
                  'SEOTR','TAXINC']
    title=kdd.head(0)
    
    for i in range(0,len(title.columns)):
        if type(kdd.ix[1,i])==numpy.float64:
            histogram_outlier(kdd.ix[:,i],title.columns[i])   









