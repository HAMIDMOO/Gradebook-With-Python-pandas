""" Calculate student's grade by combining data from many sources.

Using pandas, this script combines from the:

_ roster
_Homework and Exam grades
_Quize grades

to calculating final score for students.
"""

import pandas as pd
from functools import reduce
import os

directory_of_saving_datas=os.path.dirname(os.path.abspath("C:\\Users\\hamid\\Desktop\\pandas first project\\data\\exp_final_project"))




def seperate_last_name(name):
    Name = ""
    Last_Name = ""
    for i in range(len(name)):
        if name[i] == ",":
            Name = name[:i]
            Last_Name = name[i+1:]
            Name=Name.lower()
            Last_Name=Last_Name.lower()
    return Name, Last_Name 

roster = pd.read_csv("C:\\Users\\hamid\Desktop\\pandas first project\\data\\roster.csv")
roster["NetID"]=roster["NetID"].str.lower()
roster=roster.drop(["Section", "ID"], axis=1)
roster= roster.set_index("NetID")
roster= roster.sort_values("NetID")



hw_exam_grades_Excel= pd.read_csv("C:\\Users\hamid\Desktop\\pandas first project\\data\\hw_exam_grades.csv")
hw_exam_grades_Excel= hw_exam_grades_Excel.rename(columns={"SID":"NetID"})
hw_exam_grades_Excel["NetID"] = hw_exam_grades_Excel["NetID"].str.lower()
hw_exam_grades_Excel= hw_exam_grades_Excel.drop(columns=["Homework 1 - Submission Time", "Homework 2 - Submission Time","Homework 3 - Submission Time"
                                                 ,"Homework 4 - Submission Time", "Homework 5 - Submission Time", "Homework 6 - Submission Time",
                                                 "Homework 7 - Submission Time","Homework 8 - Submission Time","Homework 9 - Submission Time",
                                                 "Homework 10 - Submission Time", "Exam 1 - Submission Time", "Exam 2 - Submission Time"
                                                 ,"Exam 3 - Submission Time"], axis=1)
hw_exam_grades_Excel= hw_exam_grades_Excel.set_index("NetID")
hw_exam_grades_Excel= hw_exam_grades_Excel.sort_values("NetID")
#print(hw_exam_grades_Excel)


quiz_one_grade= pd.read_csv("C:\\Users\\hamid\Desktop\\pandas first project\data\\quiz_1_grades.csv")
quiz_one_grade["First Name"]= quiz_one_grade["First Name"].str.lower()
quiz_one_grade["Last Name"]= quiz_one_grade["Last Name"].str.lower()
quiz_one_grade= quiz_one_grade.sort_values("First Name")
#quiz_one_grade= quiz_one_grade.set_index("First Name")
#print(quiz_one_grade)




quiz_two_grade= pd.read_csv("C:\\Users\\hamid\\Desktop\\pandas first project\\data\\quiz_2_grades.csv")
quiz_two_grade["First Name"]= quiz_two_grade["First Name"].str.lower()
quiz_two_grade["Last Name"]= quiz_two_grade["Last Name"].str.lower()
quiz_two_grade= quiz_two_grade.sort_values("First Name")
#quiz_two_grade= quiz_two_grade.set_index("First Name")
#print(quiz_two_grade)



quiz_three_grade= pd.read_csv("C:\\Users\\hamid\\Desktop\\pandas first project\\data\\quiz_3_grades.csv")
quiz_three_grade["First Name"]= quiz_three_grade["First Name"].str.lower()
quiz_three_grade["Last Name"]= quiz_three_grade["Last Name"].str.lower()
quiz_three_grade= quiz_three_grade.sort_values("First Name")
quiz_three_grade= quiz_three_grade.set_index("First Name")
#print(quiz_three_grade)


quiz_four_grade= pd.read_csv("C:\\Users\\hamid\\Desktop\\pandas first project\\data\\quiz_4_grades.csv")
quiz_four_grade["First Name"]= quiz_four_grade["First Name"].str.lower()
quiz_four_grade["Last Name"]= quiz_four_grade["Last Name"].str.lower()
quiz_four_grade= quiz_four_grade.sort_values("First Name")
quiz_four_grade= quiz_four_grade.set_index("First Name")
#print(quiz_four_grade)



quiz_five_grade= pd.read_csv("C:\\Users\\hamid\\Desktop\\pandas first project\\data\\quiz_5_grades.csv")
quiz_five_grade["First Name"]= quiz_five_grade["First Name"].str.lower()
quiz_five_grade["Last Name"]= quiz_five_grade["Last Name"].str.lower()
quiz_five_grade= quiz_five_grade.sort_values("First Name")
quiz_five_grade= quiz_five_grade.set_index("First Name")
#print(quiz_five_grade)

"""
Merging the all quizes frades
"""

merged_grades_dataframe = quiz_one_grade.merge(quiz_two_grade[['Email', 'Grade']], on="Email", suffixes=( '_1','_2') )
merged_grades_dataframe = merged_grades_dataframe.merge(quiz_three_grade[['Email', 'Grade']], on="Email", suffixes=('_2', '_3') )
merged_grades_dataframe = merged_grades_dataframe.merge(quiz_four_grade[['Email', 'Grade']], on="Email", suffixes=('_3', '_4') )
merged_grades_dataframe = merged_grades_dataframe.merge(quiz_five_grade[['Email', 'Grade']], on="Email", suffixes=('_4', '_5') )
#print(merged_grades_dataframe)
#merged_grades_dataframe.to_csv(os.path.join(directory_of_saving_datas, "Merged quizes grades.csv"))

"""
in this script i seperated name and last name from toghether from roster df and create a new column to add the last name in result dada frame

"""
result= pd.merge(roster,hw_exam_grades_Excel, how="left", on=["NetID"] )
result.insert(1, "Last_Name", "Nan", True)
for i in range(0, 150):
   result["Name"].values[i],result["Last_Name"].values[i] =seperate_last_name(roster["Name"].values[i])
   i+=1
result=result.rename(columns={'Email Address': 'Email'})


result.to_csv(os.path.join(directory_of_saving_datas, "result of Merging roster & hw.csv"))

ro_hw=pd.read_csv("C:\\Users\\hamid\Desktop\\pandas first project\\data\\result of Merging roster & hw.csv")
ro_hw['Email']=ro_hw['Email'].str.lower()
quizes_grades=pd.read_csv("C:\\Users\\hamid\Desktop\\pandas first project\\data\Merged quizes grades.csv")
quizes_grades['Email']=quizes_grades['Email'].str.lower()


final_merged_file=pd.merge(ro_hw,quizes_grades[['Email','Grade ','Grade_2','Grade_3','Grade_4','Grade_5']], on="Email", how='left')
final_merged_file['Homework 1'].fillna(70, inplace=True)
nan=pd.isnull(final_merged_file['Homework 1'])
#final_merged_file.to_csv(os.path.join(directory_of_saving_datas, "Final Merged File.csv"))
    
# for j , x , z in zip((6,27,2), (1,11), (38, 49)):
#     final_merged_file.insert(z+1, "home work {} score".format(x), True)
#     for i in range (0,150):
#         final_merged_file.at[i,"home work {} score".format(x)]= ((final_merged_file.iat[i,j] / final_merged_file.iat[i,j+1]) * 0.1)
# print(final_merged_file.iloc[:,-10:])        


final_merged_file.insert(37, "Exam 1 Score", True)
for i in range (0,150):

    final_merged_file.at[i,"Exam 1 Score"]= (final_merged_file.iat[i,26] / final_merged_file.iat[i,26+1]) 
    

final_merged_file.insert(38, "Exam 2 Score", True)
for i in range (0,150):

    final_merged_file.at[i,"Exam 2 Score"]= (final_merged_file.iat[i,28] / final_merged_file.iat[i,29]) 

final_merged_file.insert(39, "Exam 3 Score", True)
for i in range (0,150):

   final_merged_file.at[i,"Exam 3 Score"]= (final_merged_file.iat[i,30] / final_merged_file.iat[i,31])

"""
in this code we calculate the home work score by TOTAL SCORE
"""

final_merged_file.insert(40, "Total home work", True)

for i in range(0,150):
    sum=0
    tsum=0
    for j in range (6,26,2):
        sum+=final_merged_file.iat[i, j]
    for j in range (6,26,2):    
        tsum+=final_merged_file.iat[i, j+1]
    final_merged_file.at[i, "Total home work"]= sum/tsum
#print(final_merged_file[ "Total home work"])

final_merged_file.insert(41, "Average Home Work", True)

for i in range(0,150):
    for j in range (6,26,2):
        final_merged_file.at[i,"Average Home Work" ]=final_merged_file.iat[i, j]/final_merged_file.iat[i, j+1]
#print(final_merged_file["Average Home Work"])




"""
in this script we calculate the all quizes grade once with total grades and ones with average grade.
note that we will chose the bigger grade.
"""

quizes_max_grades= pd.Series(
    {"Grade ":11, "Grade 2": 15, "Grade 3": 17, "Grade 4": 14, "Grade 5": 12}
)


final_merged_file.insert(42, "Total Quizes", True)

for i in range(0,150):
    sum=0
    tsum=0
    for j in range (32,37):
        sum+=final_merged_file.iat[i, j]
    tsum=quizes_max_grades.sum()
    final_merged_file.at[i, "Total Quizes"]= sum/tsum
#print(final_merged_file["Total Quizes"])


final_merged_file.insert(43, "Average Total Quizes", True)

for i in range(0,150):
    for j in range (32,37):
        for z in range (0,4):
            final_merged_file.at[i,"Average Total Quizes" ]=final_merged_file.iat[i, j]/quizes_max_grades[z]
#print(final_merged_file["Average Total Quizes"])


final_merged_file.insert(44, "Final Quizes Grade", True)

for i in range(0, 150):
    final_merged_file.at[i,"Final Quizes Grade"]= max(final_merged_file.at[i,"Average Total Quizes"],final_merged_file.at[i,"Total Quizes"])



"""finding the max of home work grades"""

final_merged_file.insert(45, "Final Home Work", True)

for i in range(0, 150):
    final_merged_file.at[i,"Final Home Work"]= max(final_merged_file.at[i,"Total home work"],final_merged_file.at[i,"Total home work"])

print(final_merged_file["Final Home Work"])


Final_Grades_File= final_merged_file.filter(['NetID', 'Name', 'Last_Name','Email', "Exam 1 Score","Exam 2 Score", "Exam 3 Score", "Final Quizes Grade", "Final Home Work"], axis=1)
Final_Grades_File.to_csv("Final_Grades_File.csv")