""" Calculate student's grade by combining data from many sources.

Using pandas, this script combines from the:

_ roster
_Homework and Exam grades
_Quize grades

to calculating final score for students.
"""

import pandas as pd
from functools import reduce

roster = pd.read_csv("C:\\Users\\hamid\Desktop\\pandas first project\\data\\roster.csv")
roster["NetID"]=roster["NetID"].str.lower()
roster=roster.drop(["Section", "ID"], axis=1)
roster= roster.set_index("NetID")
roster= roster.sort_values("NetID")
#print(roster)





hw_exam_grades_Excel= pd.read_csv("C:\\Users\hamid\Desktop\\pandas first project\\data\\hw_exam_grades.csv")
hw_exam_grades_Excel["SID"] = hw_exam_grades_Excel["SID"].str.lower()
hw_exam_grades_Excel= hw_exam_grades_Excel.drop(columns=["Homework 1 - Submission Time", "Homework 2 - Submission Time","Homework 3 - Submission Time"
                                                 ,"Homework 4 - Submission Time", "Homework 5 - Submission Time", "Homework 6 - Submission Time",
                                                 "Homework 7 - Submission Time","Homework 8 - Submission Time","Homework 9 - Submission Time",
                                                 "Homework 10 - Submission Time"], axis=1)
hw_exam_grades_Excel= hw_exam_grades_Excel.set_index("SID")
hw_exam_grades_Excel= hw_exam_grades_Excel.sort_values("SID")
print(hw_exam_grades_Excel)


quiz_one_grade= pd.read_csv("C:\\Users\\hamid\Desktop\\pandas first project\data\\quiz_1_grades.csv")
quiz_one_grade["First Name"]= quiz_one_grade["First Name"].str.lower()
quiz_one_grade["Last Name"]= quiz_one_grade["Last Name"].str.lower()
quiz_one_grade= quiz_one_grade.sort_values("First Name")
quiz_one_grade= quiz_one_grade.set_index("First Name")
#print(quiz_one_grade)




quiz_two_grade= pd.read_csv("C:\\Users\\hamid\\Desktop\\pandas first project\\data\\quiz_2_grades.csv")
quiz_two_grade["First Name"]= quiz_two_grade["First Name"].str.lower()
quiz_two_grade["Last Name"]= quiz_two_grade["Last Name"].str.lower()
quiz_two_grade= quiz_two_grade.sort_values("First Name")
quiz_two_grade= quiz_two_grade.set_index("First Name")
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



merged_grades_datafram = pd.merge(quiz_one_grade,quiz_two_grade[['Grade']],on='First Name', how='left',suffixes=('_1','_2'))
merged_grades_datafram = pd.merge(merged_grades_datafram,quiz_three_grade[['Grade']],on='First Name', how='left',suffixes=('_2','_3'))
merged_grades_datafram = pd.merge(merged_grades_datafram,quiz_four_grade[['Grade']],on='First Name', how='left',suffixes=('_3','_4'))
merged_grades_datafram = pd.merge(merged_grades_datafram,quiz_five_grade[['Grade']],on='First Name', how='left',suffixes=('_4','_5'))
#print(merged_grades_datafram)


