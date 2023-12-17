import random
import string

def generate_password(min_length, nums = True, special_chars = True):
    #initializing letters, digits, and special chars
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    chars = letters #creates a string containing all the different chars we could be selecting from
    
    #if the varible is true for including numbers then we are taking all the digits and adding them to the letter string
    if nums:
        chars += digits
    #if we have special characters we'll add them to chars which will allow us to select from those when generating the password
    if special_chars:
        chars += special
    
    #password is empty and no criteria is met yet   
    pwd = "" #storing password
    meets_criteria = False
    has_num = False
    has_special = False
    
    #while the length of the password does not meet the criteria or min pwd length we will continue to add chars to the password
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(chars) #generate new random chars from the chars string ( this is why we add the numbers or special chars in lines 13-17)
        pwd += new_char #adding them to the password
        
        #determine if the new char was a number or special char and return true if so
        if new_char in digits: #if this char exists inside the digits adjust
            has_num = True
        elif new_char in special: #if this char exists inside the special chars adjust
            has_special = True
            
        #meets_criteria can be true for now and we will change it to false if needed when the criteria is checked
        meets_criteria = True
        
        #if we should include numbers or special characters 
        if nums: #meets_critera will change to the status of has_num 
            meets_criteria = has_num
        if special_chars:
            meets_criteria = meets_criteria and has_special #meets_criteria will only return true if both meets_criteria and has_special are true
            
    return pwd

#user inputs
min_length = int(input("Enter the minimum length: "))
has_num = input("Do you want to have numbers?(y/n) ").lower() == "y"
has_special = input("Do you want to have special characters?(y/n) ").lower == "y"
pwd = generate_password(min_length, has_num, has_special)
print("The generated password is:", pwd)