# Bruteforce_password_cracker
This project is a simple brute force password cracker implemented in Python using the Tkinter library for the graphical user interface (GUI). The application attempts to find a user-specified password by first checking against a common passwords list and then using a brute force method.

# Features
* GUI for user interaction
* Input validation for max length and target password
* Checks for the password in a common passwords file. (Ensure that the file is present in the same directory as the script)
* Brute force search with adjustable maximum length
* User notifications for the password search process and results

# Usage
Navigate to the project directory.
You can create a simple common.txt file if not already available.
Run the code:

Enter the maximum length for the brute force password attempts.

Enter the target password you want to crack.

Click the "Crack!" button to start the process.

# Code Overview
generate_characters()
Generates a list of characters to be used in the brute force attempts. This includes uppercase and lowercase letters, digits, and special characters.

search_file()
Checks if the target password exists in the common.txt file. If not found, initiates the brute force search.

brute_force(target_pass, max_length)
Attempts to brute force the target password by generating all possible combinations of characters up to the specified maximum length.

# Cons
Time taken to crack the password increases drastically after the max length exceeds 4

License
This project is licensed under the MIT License. See the LICENSE file for details.




