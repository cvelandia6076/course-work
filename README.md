Final Project Description

The Password Strength Analyzer is a simple Python tool that helps users check the strength and security of their passwords. It analyzes passwords against common weaknesses such as short length, lack of variety in characters, and predictable patterns. The program also provides feedback and suggestions to help users create stronger passwords that are harder for attackers to guess. This project supports cybersecurity awareness by automating password evaluation, typically done manually.
How the Program Works
1.	The user enters a password into the program.
2.	The program checks the password for:
•	Length (must be at least 8 characters)
•	Use of lowercase and uppercase letters
•	Numbers and special symbols
•	Common passwords (like "password" or "123456")
•	Repeating or sequential patterns (like "aaa" or "123")
3.	The password is scored on a scale from 0 to 5, and the strength is rated as Weak, Moderate, or Strong.
4.	The program then prints personalized suggestions for improving the password.
Example Output
Enter a password to analyze (or type 'exit' to quit): Hello123
Password Analysis:
Strength: Moderate
Score: 3 / 5
Suggestions to improve your password:
- Add special characters (like !, @, #, $).
How to Run the Program
1.	Open the file password_strength_analyzer.py in VS Code or any Python editor.
2.	Run the program by pressing Run.
3.	Type in any password you want to test.
4.	Type exit when you want to quit.

