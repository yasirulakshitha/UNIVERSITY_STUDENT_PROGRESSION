
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: w2051737
# Date: 2023.12.10

from w2051737_part_3 import* #impot all things in myGraph for execute the chart

import os #this part connect with the operating sysytem for creat a text file.



#====================FUNCTIONS================================================================================================================================================================

# This function validates user input for a given credit type ('pass', 'defer', 'fail')

def validate_result(credit):  
   
    while True:  
        try:
            creadit_input = int(input(f"Enter your creadit at {credit}: "))
        except ValueError:  #if user enters an intereger, this part will catch the exception and prompt the user again
            print('integer required')
            continue

        if creadit_input in range(0,121,20): #if the entered value in the specified range,input is valid and return the value
            return creadit_input

        else:                                #otherwise it will display a error message for user
            print('out of range')    

            

# This function checks if the sum of pass, defer, and fail values is equal to 120

def calculate_total(pass_value,defer_value,fail_value):  
    if pass_value + defer_value + fail_value ==120: #if the total is correct equal to 120,it returns false to indicate the total is incorrect 
        return False                                # it will helps user to come out from the loop because loop will iterate while return true(means total not equal 120)
    else:
        print('total incorret') #if the total is incorrect it will gives user an error message and returning True 
        return True



# This function determines the progression outcome based on pass, defer, and fail values

def progression_outcome(pass_value,defer_value,fail_value): #In this function we are returning values for progression outcomes 
    if pass_value == 120:
        return 1
    elif pass_value == 100:
        return 2
    elif fail_value in range(80,121,20):
        return 3
    else:
        return 4



# This function prints the progression outcome based on the value provided

def print_progression(value):  #In this function,we assinging the name of progression outcome for the value that i return form progression_outcome function
    if value == 1:             # it is very manageable other than using a string 
        print("progress")      # it will very usefull when cretaing the list
    elif value == 2:           # if we call this function. it will prints the specific progression name
        print("progress(module trailer)")
    elif value == 3:
        print("exclude")
    elif value == 4:
        print("do not progress-module retriever")
    else:
        print("invalide value")



# This function appends the result details to the result_list

def creat_data_list(pass_value,defer_value,fail_value,progression_value):

  #parameters - pass_value ,defer_value,fail_value  (validate_creadits function)
  #           - progression _value = progression_outcome(pass_value,defer_value,fail_value) (this part also calling again in MAIN PROGRAM)

  #next appending those parameters to the resulit list


        result_list.append([pass_value,defer_value,fail_value,progression_value])

#list for enter output data
result_list = []


# This function displays the data stored in result_list

def display_data():
                                    #item[3] = 3 is the index value of the specific item. it represent 4th item
    for item in result_list:        #in the result list we append the progression_value at the 4th item (index value is 3).
                                    #and we returning values for the progression_value but in result_list we have to give that value the progression name because we have to print the list 
        if item[3] == 1:            #(we assigning value to the progression name in one time at the print_progression that is for just identify the outcome and print at that moment)
            result = "progress"
        elif item[3] == 2:
            result = "progress(module trailer)"
        elif item[3] == 3:
            result = "exclude"
        elif item[3] == 4:
            result = "do not progress-module retriever"
        else:
            result = "unknown"
        
                                                         
        print(f'{result}-{item[0]},{item[1]},{item[2]}')  #{result} from display_data
                                                         #{item[0]},{item[1]},{item[2]} from result_list
                                                         # usuing f string and {} for append data

               
# This function asks the user if they want to enter another set of data

def terminate_data():

    while True: # in this part user have to input simple y or q without any leading/trailing spaces in the input otherwise it will gives the user an error message 
        terminate_input = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quite and view results: ").lower().strip()

        if terminate_input == "y":
            return True
        elif terminate_input == "q":
            return False
        else:
            print("invalide input")


       
# This function reads the content of "text_output.txt" and appends the results from result_list

def read_write_files():

    if not os.path.exists('text_output.txt'): #this will helps to the code for creat a file for write data.
        f = open('text_output.txt', 'w')      
        f.close()


#open "text_output.txt" in read mode. we don't need to close it separately because we using with open methode. program will automatically closing it.
    with  open("text_output.txt","r") as file:  

# Read the existing content of the file into a list
        file1 = file.readlines()                
                                  
#iterating through items in result_list
    for item in result_list:
       
       # Match progression value and assign results
        match item[3]:
            case 1:
                result = "progress"
            case 2:
                result = "progress(module trailer)"
            case 3:
                result = "exclude"
            case 4:
                result = "do not progress-module retriever"
    
       # Format and append the result to the file content list
        file1.append(f'{result}-{item[0]},{item[1]},{item[2]}\n')

# Open "text_output.txt" in write mode
    with  open("text_output.txt","w") as file:

      # Write the updated content back in to the file
        file.writelines(file1)
         


# This function increments the count for each progression outcome

def add_count(value):

  # Iterate through the keys in the 'count' dictionary
    for item in count:

   # Check if the current key similar to the provided 'value'
        if item == value:

    # Increment the count for the specific progression value
            count[item] += 1
               
#EXTRA POINT - This function is designed to increment the count associated with a specific progression outcome.
# and it will be the inputs to the graph                

#dictionarie to add_count
count = {1:0,2:0,3:0,4:0}




#===========================MAIN=PROGRAM=================================================================================================================================================================



progress = 0
trailer = 0
retriever = 0
excluded = 0


# assign flag to True for entering the while loop
flag = True

# Loop until a valid input is provided for student or staff access
while flag:

    try:
        identification = int(input("STUDENT ACCESS - 1 OR STAFF ACCESS - 2 \nEnter the access number: "))

        #checking the entered value is number 1 or number 2
        if identification == 1 or identification == 2:
            flag = False #if the inputs are valide set the flag value False to exite the loop
        else:            #this part will handle the invalide integer error
            print("invalid input")


    except ValueError:  #This part will help to identify if user enter a string and display error message
        print("integer required")




#reset flage value for new loop
flag = True

#from this wile loop it will execute if user input valide data in the beginning (1 or 2)
while flag:
    

    if identification == 1: #student access

        print("")

        print("STUDENT ACCESS")

        print("")
        while flag: 
            """"from this while loop it will iterate data untill total value not equal to 120.if total equal to 120 then it will exit loop and print progression.
                that's happen because i assign flage value to true in loop. but in the function i return false for the total equal to 120. because when  
                       total equal to 120 we have to get to the next process """

            #assign values for pass_value,defer_value,fail_value through the validate_result function
            pass_value = validate_result('pass')                    
            defer_value =validate_result('defer')
            fail_value  = validate_result('fail') 

            print("")
            #calculate total creatits and check it they equal 120
            flag = calculate_total(pass_value,defer_value,fail_value)

        #processing the progression_value(that number we return) to assign progression name  
        progression_value = progression_outcome(pass_value,defer_value,fail_value)

        print("")
        # display the progression name for user
        print_progression(progression_value)
        # Exit the program after processing student data
        exit()

    elif identification == 2: #staff access

        print("")

        print("STAFF ACCESS")
        
        print("")

        while flag:                                                      
            """from this while loop it will iterate data untill total value not equal to 120.if total equal to 120 then it will exit loop and print progression.
                that's happen because i assign flage value to true in loop. but in the function i return false for the total equal to 120. because when  
                       total equal to 120 we have to get to the next process """
            #assign values for pass_value,defer_value,fail_value through the validate_result function
            pass_value = validate_result('pass')
            defer_value =validate_result('defer')
            fail_value  = validate_result('fail')  

            print("")
            #calculate total creatits and check it they equal 120
            flag = calculate_total(pass_value,defer_value,fail_value)  

        #processing the progression_value(that number we return) to assign progression name 
        progression_value = progression_outcome(pass_value,defer_value,fail_value)
    
        # display the progression name for user
        print_progression(progression_value)

        print("")
        #appending pass_value,defer_value,fail_value,progression_value to result_list
        creat_data_list(pass_value,defer_value,fail_value,progression_value)

        #counting specific progression_values
        add_count(progression_value)
   
        # Check if the user wants to terminate entering data   
        flag = terminate_data()
        print("")

# Display collected data form the user
display_data()
print("")

#read each progression outcomes and write it to a text file
read_write_files()
print("")

#printing the count of each progression outcome user input
print(list(count.values()))

#creat graph from the final outcomes that user input 
graph_connect(list(count.values()))

              


   






    


                
                


             
