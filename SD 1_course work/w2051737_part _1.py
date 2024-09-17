from w2051737_part_3 import * #import fully code for execute graph

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: w2051737
# Date: 2023.12.10


#===============FUNCTIONS====================================================================================================================================================================

#function for validate creadits
def validate(creadit):
   
    while True:
        try:
            user_credit = int(input(f"Enter your creadit at {creadit}: "))

             # Check if the entered credit is within the valid range.if it is not prompt the input again
            if user_credit not in [0,20,40,60,80,100,120]:
                print("out of range")
                continue
            
            # check if the entered creadit is a string
        except ValueError:
            print("integer required")
            continue

            #returning valid user creadits
        return user_credit




# Function to get user selection for entering more data or quitting
def user_selection():


    while True:
    # in this part user have to input simple y or q without any leading/trailing spaces in the input otherwise it will gives the user an error message 
        user_input = input("would you like to enter another set of data?\nEnter 'y' for yes or 'q' for quite and view results: ").lower()
        user_input = user_input.strip()
        match user_input:
            case 'y':
                return True
            case 'q':
                return False
            case _:
                print('wrong input')




#===================MAIN=PROGRAM============================================================================================================================================================================================================================================================================================================================


progress = 0
trailer = 0
retriever = 0
excluded = 0



flag = True #assign flag variable to false it will helps us to get out from the loop if we assign it again to false 
while flag:


#validate pass,defer,fail values thriugh validate function
    pass_value = validate('pass')
    defer_value = validate('defer')
    fail_value  = validate('fail')


#separate students from thier credit values
    
        #checking for progress
    if pass_value==120 and defer_value==0 and fail_value==0:
        print("Progress")
        progress = progress + 1


        #checking for module trailer
    elif pass_value==100 and defer_value==20 and fail_value==0 or pass_value==100 and defer_value==0 and fail_value==20:
        print("progress(module trailer)")
        trailer = trailer + 1

        #checking for exclude
    elif pass_value==40 and defer_value==0 and fail_value==80 or pass_value==20 and defer_value==20 and fail_value==80 or pass_value==20 and defer_value==0 and fail_value==100 or pass_value==0 and defer_value==40 and fail_value==80 and pass_value==0 and defer_value==20 and fail_value==100 or pass_value==0 and defer_value==0 and fail_value==120:
        print("Exclude")
        excluded = excluded + 1

        #checking for retriver
    elif pass_value==80 and (defer_value==40 or defer_value==20 or defer_value==0) and (fail_value ==0 or fail_value==20 or fail_value==40):
        print("Do not progress - module retriever")
        retriever = retriever + 1


    elif pass_value==60 and defer_value==60 and fail_value==0 or pass_value==60 and defer_value==0 and fail_value==60:
        print("Do not progress - module retriever")
        retriever = retriever + 1 


    elif pass_value==60 and ( defer_value==40 or defer_value==20 or defer_value==0) and (fail_value==0 or fail_value==20 or fail_value==40 ):
        print("Do not progress - module retriever")
        retriever = retriever + 1


    elif pass_value==40 and (defer_value==80 or defer_value==60 or defer_value==40 or defer_value==20) and (fail_value==0 or fail_value==20 or fail_value==40 or fail_value==60):
        print("Do not progress - module retriever")
        retriever = retriever + 1



    elif pass_value==20 and (defer_value==100 or defer_value==80 or defer_value==60 or defer_value==40) and (fail_value==0 or fail_value==20 or fail_value==40 or fail_value==60):
        print("Do not progress - module retriever")
        retriever = retriever + 1


    elif pass_value==0 and defer_value==[120 , 100 ,80 ,60] and fail_value== [0 ,20 ,40 , 60]:
        print("Do not progress - module retriever")
        retriever = retriever + 1


    else:
        print("total is incorrect")


#asking user for terminate data
    flag = user_selection()

# Prepare data for graph and call graph_connect (function not provided)
data_for_graph =[progress,trailer,retriever,excluded]

graph_connect(data_for_graph)   



