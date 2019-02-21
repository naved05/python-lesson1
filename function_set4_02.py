"""

Brilliant School sets an exam wherein, 
                English exam is for 80 marks, 
                Science for 90 marks and 
                Mathematics for 100 marks. 
            Ask the student to enter the marks scored in each of these exams. 
            Calculate the total percentage marks and rank the student as below :
               - First Class if score is more than or equal to 90 %
               - Second Class if score is more than or equal to 75%
               - Average if student has not failed
               - Failed if score is less than or equal to 35 %

            Make sure your code uses the same principles 
                 as in the template codes of earlier exercises

                 """
def rank(percentage):

    if (percentage >=90):
        print("student got first class")
    elif(percentage >=75 or percentage <90):
        print("student has got second class")
    elif(percentage >=35 or percentage < 75):
        print("student has got average class")
    else:
        print("student got failed")

def calculate_percentage(total_student_marks,max_marks):

    percentage=((total_student_marks/max_marks)*100)

    return percentage

def student_marks():

    eng_marks=int(input("enter the english marks:"))
    science_marks=int(input("enter the science marks:"))
    maths_marks=int(input("enter the maths marks:"))

    total=eng_marks+science_marks+maths_marks

    return total
                                    
                  
   # science_marks=int(input("enter the science marks:")
                      
    #maths_marks=int(input("enter the maths marks:")

    #total=eng_marks+science_marks+maths_marks

    #return eng_marks

total_student_marks=student_marks()
english_max_marks=80
science_max_marks=90
maths_max_marks=100

max_marks=english_max_marks+science_max_marks+maths_max_marks

percentage=calculate_percentage(total_student_marks,max_marks)

rank(percentage)
