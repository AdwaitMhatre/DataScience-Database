#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import plotly as plt
import plotly.offline as po
import cufflinks as cf


# In[ ]:


po.init_notebook_mode(connected='True')
cf.go_offline()


# In[ ]:


def dataframe_func(var):
    if data == 1:
        df = pd.DataFrame(np.random.rand(100,5), columns=["A","B","C","D","E"])
    elif data == 2:
        c1 = [0,0,0,0,0]
        r1 = [0,0,0,0,0]
        r2 = [0,0,0,0,0]
        r3 = [0,0,0,0,0]
        r4 = [0,0,0,0,0]
        
        print("Enter the names for 5 columns")
        j=0
        for i in c1:
            c1[j]=input()
            j=j+1
        print("Enter the values for first row")
        j=0
        for i in r1:
            r1[j]=input()
            j=j+1
        print("Enter the values for second row")    
        j=0
        for i in r2:
            r2[j]=input()
            j=j+1
        print("Enter the values for third row") 
        j=0
        for i in r3:
            r3[j]=input()
            j=j+1
        print("Enter the values for fourth row") 
        j=0
        for i in r1:
            r3[j]=input()
            j=j+1
        df = pd.DataFrame([r1,r2,r3,r4], columns=c1)
        
    elif data == 3:
        abcd = input("Enter your file name along with extension")
        dcba = pd.read_csv(abcd)
        df = pd.DataFrame(dcba)
    else:
        print("Your input is incorrect. Try again")
    return df


# In[ ]:


def plotter1():
    print("Enter the corresponding number of the type of plot you want")
    print("1. Line Plot")
    print("2. Scatter Plot")
    print("3. Bar Plot")
    print("4. Box Plot")
    print("5. Histogram")
    print("6. 3-D Surface Plot")
    ace = int(input())
    if ace == 1:
        finalplot = df1.iplot(kind='scatter')
    elif ace == 2:
        finalplot = df1.iplot(kind='scatter',mode='markers',size=7)
    elif ace == 3:
        finalplot = df1.iplot(kind='bar')
    elif ace == 4:
        finalplot = df1.iplot(kind='box')
    elif ace == 5:
        finalplot = df1.iplot(kind='hist')
    elif ace == 6:
        finalplot = df1.iplot(kind='surface',theme='solar')
    else:
        ace = input("Your input is incorrect. Please enter again: ")
    return finalplot    


# In[ ]:


def plotter2():
    print("Preselect and enter the corresponding number of the type of plot you want")
    print("1. Line Plot")
    print("2. Scatter Plot")
    print("3. Bar Plot")
    print("4. Box Plot")
    print("5. Histogram")
    print("6. 3-D Surface Plot")
    print("7. Bubble Plot")
    ace1 = int(input())
    cha = int(input("Enter the number of columns you want to plot(1,2,3)"))
    if cha == 1:
        colm = input("Enter the exact column name you want to plot: ")
        if ace1 == 1:
            finalplot = df1[colm].iplot(kind='scatter')
        elif ace1 == 2:
            finalplot = df1[colm].iplot(kind='scatter',mode='markers',size=7)
        elif ace1 == 3:
            finalplot = df1[colm].iplot(kind='bar')
        elif ace1 == 4:
            finalplot = df1[colm].iplot(kind='box')
        elif ace1 == 5:
            finalplot = df1[colm].iplot(kind='hist')
        elif ace1 == 6 or ace1 == 7:
            finalplot = print("This plot is not possible with just one column")
        else:
            ace1 = input("Your input is incorrect. Please enter again: ")
    elif cha == 2:
        col1 = input("Enter the exact first column name you want to plot: ")
        col2 = input("Enter the exact second column name you want to plot: ")
        if ace == 1:
            finalplot = df1[[col1,col2]].iplot(kind='scatter')
        elif ace1 == 2:
            finalplot = df1[[col1,col2]].iplot(kind='scatter',mode='markers',size=7)
        elif ace1 == 3:
            finalplot = df1[[col1,col2]].iplot(kind='bar')
        elif ace1 == 4:
            finalplot = df1[[col1,col2]].iplot(kind='box')
        elif ace1 == 5:
            finalplot = df1[[col1,col2]].iplot(kind='hist')
        elif ace1 == 6: 
            finalplot = df1[[col1,col2]].iplot(kind='surface',theme='solar')
        elif ace1 == 7:
            size = input("Enter the column name presenting size")
            finalplot = df1[[col1,col2]].iplot(kind='bubble',x=col1,y=col2,size=size)
        else:
            ace1 = input("Your input is incorrect. Please enter again: ")
    elif cha == 3:
        col1 = input("Enter the exact first column name you want to plot: ")
        col2 = input("Enter the exact second column name you want to plot: ")
        col3 = input("Enter the exact third column name you want to plot: ")
        if ace1 == 1:
            finalplot = df1[[col1,col2,col3]].iplot(kind='scatter')
        elif ace1 == 2:
            finalplot = df1[[col1,col2,col3]].iplot(kind='scatter',mode='markers',size=7)
        elif ace1 == 3:
            finalplot = df1[[col1,col2,col3]].iplot(kind='bar')
        elif ace1 == 4:
            finalplot = df1[[col1,col2,col3]].iplot(kind='box')
        elif ace1 == 5:
            finalplot = df1[[col1,col2,col3]].iplot(kind='hist')
        elif ace1 == 6: 
            finalplot = df1[[col1,col2,col3]].iplot(kind='surface',theme='solar')
        elif ace1 == 7:
            size = input("Enter the column name presenting size")
            finalplot = df1[[col1,col2,col3]].iplot(kind='bubble',x=col1,y=col2,z=col3,size=size)
        else:
            ace1 = input("Your input is incorrect. Please enter again: ")
        
    return finalplot


# In[ ]:


def main(something):
    if something == 1:
        plotter1()
    elif something == 2:
        plotter2()


# In[ ]:


print("Select in what way you want top plot data")
print("Enter 1 to create a random dataframe of 100 rows and 5 cloumns")
print("Enter 2 to customize your own dataframe of 5 rows and 5 cloumns")
print("Enter 3 to upload a csv/json/txt file to plot its data")
data = int(input("Your Entry: "))
df1 = dataframe_func(data)


# In[ ]:


print("Excerpt of you dataframe:")
df1.head()


# In[ ]:


category=int(input("Enter 1 to plot the entire dataframe or Enter 2 to plot only certain columns"))


# In[ ]:


main(category)


# In[ ]:





# In[ ]:





# In[ ]:




