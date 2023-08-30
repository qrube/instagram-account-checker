# Instagram Username Checker

This Python script checks the availability of Instagram usernames by examining profile pages. It sends requests to profile URLs and analyzes the response to determine if the username exists.

## Usage

1. **Install Dependencies:**
   Before using the script, make sure you have the required libraries installed. You can install them using the following command:

    pip install requests beautifulsoup4


2. **Create a Usernames File:**
Create a text file named `usernames.txt` in the same directory as the script. List the usernames you want to check, with one username per line.

3. **Run the Script:**
Open a terminal and navigate to the script's directory. Then run the script using the following command:

    python checker.py

Replace `checker.py` with the actual name of your Python script.

4. **View the Results:**
The script will display whether each username is taken or available. If a username is taken, it will show the profile URL. If a username is available, it will indicate that the username is available.

## Disclaimer

This script is intended for educational purposes and should be used responsibly. Be aware that using automated tools to check username availability on Instagram might violate their terms of service.

Feel free to contribute to this project and improve its functionality. If you find any issues or have suggestions, please create an issue or a pull request.
