import Final_Project


# Fill in your Main Program Here following the instructions

# STEP1 : Create an instance of class PasswordManager with the name 'Student' and the master password 'FINAL'.
# Assign this to variable name user_1
# Add your code for STEP1 below this line
user_1 = Final_Project.PasswordManager('Student', 'FINAL')



# STEP2: Open ‘company.csv’ file in variable filename.
# Add your code for STEP2 below this line
with open('company-1.csv', 'r') as filename:


# STEP3: Read the data from the ‘company.csv’ file one company name at a time
# and process each company name to get rid of leading or trailing characters.
# Add your code for STEP3 below this line
    for line in filename:
        x=line.strip()
        


# STEP4: Add company login information for each company name from the ‘company.csv’ file
# To do this, you must use the add_data() method such as,
# You must pass each company name as the argument for the parameter comp_name.
# You must pass ‘user_1’ as the argument for the parameter username.
# You must‘FINAL’as the argument for the parameter master_pass.
# You should not pass any argument for the parameter criteria.
# Add your code for STEP4 below this line
        user_1.add_data(x, user_1, 'FINAL')
filename.close()

# STEP5: Change the password for the company name ‘Costco Wholesale Corporation’ to ‘costco_password’.
# You must use the change_password() method for this with appropriate arguments being passed.
# You must pass ‘FINAL’ as the argument for the parameter master_pass.
# Add your code for STEP5 below this line
user_1.change_password('Costco Wholesale Corporation', 'FINAL', 'costco_password')



# STEP6: Remove the first five items from the dictionary login
# You must use the remove_comp() method for this by passing appropriate arguments
# You must pass ‘FINAL’ as the argument for the parameter master_pass.
# Add your code for STEP6 below this line
z=0
for company in user_1.get_comp_list():
    user_1.remove_comp(company,'FINAL')
    z+=1
    if z == 5:
        break

# STEP7: Open a file named ‘password_file.csv’ in writing mode.
# Add your code for STEP7 below this line
with open('password_file.csv', 'w') as m:
    


# STEP8: Using the appropriate methods defined in class PasswordManager, write in file ‘password_file.csv’ such as
# each line corresponds to each item from the dictionary login as in the format as shown in the instructions
# You should first create a website for each company by getting rid of periods (‘.’), spaces (‘ ’), and adding ‘www.’ before ‘.com’ after the company name in lowercase.
# You must use get_comp_list() method to get a list of all the company names, to create the website (str) as shown for each company one at a time.
# You must use get_comp_info() to pull the username and password for each company name  to be written in ‘password_file.csv’.
# You must pass ‘FINAL’ as an argument for get_comp_info() along with other appropriate arguments.
# Add your code for STEP8 below this line
    for company in user_1.get_comp_list():
        m.write('www.' + str(company.replace(' ','').replace(',','').replace('.','').lower()) + '.com' +', ' +'user_1' + ', ' +user_1.get_comp_info(company,'FINAL')[1] + '\n')
        
        
m.close()
