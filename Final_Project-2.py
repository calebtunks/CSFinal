import string
import random
class PasswordManager:

    def __init__(self, name, master_pw):
        self.__name = #store name of the user
        self.__master_pw = #store master password
        self.__login = #store an empty dictionary
    
    #def checker(self):
        #return self.__passwords.copy()

    def validate(self, master_pass):
        # Checks whether mp is the same as the master password
        # Returns a boolean
        # DELETE PASS AND ADD YOUR CODE BELOW THIS LINE
        pass

    def get_name(self):
        # Return the name of the owner of the password manager
        # DELETE PASS AND ADD YOUR CODE BELOW THIS LINE
        pass

    def get_comp_list(self):
        # Return a list of all the company names (all the keys from dictionary login, not the values)
        # DELETE PASS AND ADD YOUR CODE BELOW THIS LINE
        pass

    def get_comp_info(self, comp_name, master_pass):
        # If master_password entered correctly
        # If company name is present in the dictionary login
        # Returns a tuple of username and password for the company name passed in as the argument
        # If master password is wrong, print the error message according to instructions and returns False
        # DELETE PASS AND ADD YOUR CODE BELOW THIS LINE
        pass

# ****** __generate_password begins. ******
    #__generate_password is correct.Do not change anything in it.

    def __generate_password(self, criteria = {'length':14, 'min_lower':0, 'min_upper':0, 'min_digits':0, 'min_special':0}):
        lower_letters = string.ascii_lowercase # a string of all alphabets in lowercase
        upper_letters = string.ascii_uppercase # a string of all alphabets in uppercase
        digits = string.digits # a string of all numbers
        special_chars = string.punctuation # a string of all punctuations
        length = criteria.get('length', 14) # refer to the dictionary 'criteria' and set default required length of the password to 14
        min_special = criteria.get('min_special', 0) # refer to the dictionary 'criteria' and set min num of speacial characters to 0
        min_digits = criteria.get('min_digits', 0) # refer to the dictionary 'criteria' and set min num of digits to 0
        min_upper = criteria.get('min_upper', 0) # refer to the dictionary 'criteria' and set min num of uppercase to 0
        min_lower = criteria.get('min_lower', 0) # refer to the dictionary 'criteria' and set min num of lowercase to 0

        # Ensure length requirements are met
        if length >= min_lower + min_upper + min_special + min_digits:
            # Generate password with required characters
            password = (random.choices(lower_letters, k=min_lower)) + (random.choices(upper_letters, k=min_upper)) + (
                random.choices(special_chars, k=min_special)) + (random.choices(digits, k=min_digits))
            # Fill the remaining length with random characters
            remaining_length = length - (min_lower + min_upper + min_special + min_digits)
            password += ''.join(
                random.choices(upper_letters + lower_letters + digits + special_chars, k=remaining_length))
            # Shuffle the password to ensure randomness
            password_list = list(password)
            random.shuffle(password_list)
            password = ''.join(password_list)
            return password

# ****** __generate_password ends. ******
    
    def add_data(self, comp_name, username, master_pass, criteria = {'length':14, 'min_lower':0, 'min_upper':0, 'min_digits':0, 'min_special':0}):
        # If master_password entered is correct
        # If company name not in dictionary login
        # generate a new password according to criteria by appropriately calling generate_password() method
        # add the company as key  and [username, password] as the value to the dictionary login
        # If __generate_password does not return a password, prints the error message according to instructions
        # If master password is wrong, print the error message according to instructions and return False
        # DELETE pass AND ADD YOUR CODE BELOW THIS LINE
        pass

    
    def change_password(self, comp_name, master_pass, new_pass = None, criteria = {'length':14, 'min_lower':0, 'min_upper':0, 'min_digits':0, 'min_special':0}):
        # If master_password entered correctly
        # If company name is present in the dictionary login
        # Updates the password to the company name
        # This will be new_pass if provided, otherwise, will generate a
        # New password using criteria by appropriately calling generate_password() method
        # If generte_password does not return a password, print the error message according to instructions
        # If site does not exist, print the error message according to instructions
        # If master password is wrong, print the error message according to instructions and returns False
        # DELETE pass AND ADD YOUR CODE BELOW THIS LINE
        pass
        

    def remove_comp(self, comp_name, master_pass):
        # If master_password entered correctly
        # If company name is present in the dictionary login
        # Delete the company name and the associated data (delete item from dictionary login based on key)
        # If master password is wrong, print the error message according to instructions and returns False
        # DELETE pass AND ADD YOUR CODE BELOW THIS LINE
        pass

    
    def __str__(self):
        # Return a string representation of ONLY the sites
        # Should look like this
        # Company names stored for NAME_OF_OWNER are as follows:
        # Google
        # Meta
        # Tesla
        # One company name per line with the header line
        # DELETE pass AND ADD YOUR CODE BELOW THIS LINE
        pass




