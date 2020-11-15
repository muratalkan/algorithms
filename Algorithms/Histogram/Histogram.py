import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#get values from excel files and add column
grades259 = pd.read_excel('259_grades.xlsx')
grades264 = pd.read_excel('264_grades.xlsx')
grades259['Overall-259'] = (grades259['LQ1-259']*0.15) + (grades259['LQ2-259']*0.15) + (grades259['MIDTERM-259']*0.35) +(grades259['FINAL-259']*0.35)
grades264['Overall-264'] = (grades264['LABEXAM-264']*0.30) + (grades264['MIDTERM-264']*0.35) + (grades264['FINAL-264']*0.35) 

#259 LIST
print("259 Grades:")
print(grades259)
avg259 = grades259["Overall-259"].mean()
print("CTIS259 Course - overall grades average is", avg259)

#264 LIST
print("\n264 Grades:")
print(grades264)
avg264 = grades264["Overall-264"].mean()
print("CTIS264 Course - overall grades average is", avg264)


#HISTOGRAM
plt.figure(1) 
plt.clf()

plt.subplot(1,2,1)
plt.hist(grades259['Overall-259'], color = 'red',edgecolor='blue') 
plt.xlabel('259 Overall Scores')
plt.ylabel('Frequency')

plt.subplot(1,2,2)
plt.hist(grades264['Overall-264'], 5, color = 'green', edgecolor='red') 
plt.xlabel('264 Overall Scores')
plt.ylabel('Frequency')

plt.show()
