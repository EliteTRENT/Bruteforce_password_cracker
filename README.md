# Bruteforce_password_cracker
This project is a simple brute force password cracker implemented in Python using the Tkinter library for the graphical user interface (GUI). The application attempts to find a user-specified password by first checking against a common passwords list and then using a brute force method.

Features
GUI for user interaction
Input validation for max length and target password
Checks for the password in a common passwords file (common.txt)
Brute force search with adjustable maximum length
User notifications for the password search process and results
Prerequisites
Python 3.x
Tkinter library (usually included with Python)
common.txt file (containing a list of common passwords, one per line)
Installation
Ensure you have Python installed. You can download it from python.org.

Clone or download this repository to your local machine.

Ensure the common.txt file is present in the same directory as the script. You can create a simple common.txt file if not already available.

Usage
Navigate to the project directory.

Run the script using Python:

bash
Copy code
python password_cracker.py
The application window will appear.

Enter the maximum length for the brute force password attempts.

Enter the target password you want to crack.

Click the "Crack!" button to start the process.

Code Overview
generate_characters()
Generates a list of characters to be used in the brute force attempts. This includes uppercase and lowercase letters, digits, and special characters.

search_file()
Checks if the target password exists in the common.txt file. If not found, initiates the brute force search.

brute_force(target_pass, max_length)
Attempts to brute force the target password by generating all possible combinations of characters up to the specified maximum length.

GUI Setup
Labels and Entries: For user inputs (max length and target password).
Button: To initiate the password cracking process.
Message Boxes: To provide feedback to the user about the progress and results.
Example common.txt
yaml
Copy code
123456
password
123456789
12345678
12345
1234567
1234
111111
123123
abc123
password1
qwerty
Contributing
Contributions are welcome! Please create a pull request or open an issue to discuss your ideas.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Disclaimer
This tool is intended for educational purposes only. Do not use it for any illegal activities. The author is not responsible for any misuse of this tool.

