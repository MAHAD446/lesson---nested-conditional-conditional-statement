# teke input for the student that he can attendend the exam or not 
medical_cause=input("did.you heve a medicel cause yes or no:")
# take input of the attendance 
atten = int(input("enter the attendence of the student:"))

# checking yhe user input predicting output acordingly

if medical_cause == 'y' : #checking yhe condition 1
    print ("you are allowed")
else:
    if atten>=75: #checking yhe condition2
        print("allowed")
    else:
       print("not allowed")
