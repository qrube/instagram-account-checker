import requests
from bs4 import BeautifulSoup

def check_instagram_username(username):
    base_url = f"https://www.instagram.com/{username}/"
    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title')

        if title_tag and "Page not found" in title_tag.get_text():
            return False, None
        else:
            return True, base_url
    elif response.status_code == 404:
        return False, None
    else:
        return None, None

def main():
    usernames_file = "usernames.txt"  # Replace with the actual name of your .txt file containing usernames

    with open(usernames_file, "r") as file:
        usernames = file.read().splitlines()

    for username in usernames:
        is_available, profile_url = check_instagram_username(username)
        if is_available:
            print(f"Username '{username}' is taken. Profile: {profile_url}")
        else:
            print(f"Username '{username}' is available.")

if __name__ == "__main__":
    main()
