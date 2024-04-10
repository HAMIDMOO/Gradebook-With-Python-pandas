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



merged_grades_dataframe = quiz_one_grade.merge(quiz_two_grade[['Email', 'Grade']], on="Email", suffixes=('_1', '_2') )
merged_grades_dataframe = merged_grades_dataframe.merge(quiz_three_grade[['Email', 'Grade']], on="Email", suffixes=('_2', '_3') )
merged_grades_dataframe = merged_grades_dataframe.merge(quiz_four_grade[['Email', 'Grade']], on="Email", suffixes=('_3', '_4') )
merged_grades_dataframe = merged_grades_dataframe.merge(quiz_five_grade[['Email', 'Grade']], on="Email", suffixes=('_4', '_5') )
merged_grades_dataframe.to_csv(os.path.join(directory_of_saving_datas, "Merged quizes grades.csv"))
"""
in this script i seperated name and last name from toghether from roster df and create a new column to add the last name in result dada frame

"""
result= pd.merge(roster,hw_exam_grades_Excel, how="left", on=["NetID"] )
result.insert(1, "Last_Name", "Nan", True)
for i in range(0, 150):
   result["Name"].values[i],result["Last_Name"].values[i] =seperate_last_name(roster["Name"].values[i])
   i+=1
#print(result)
