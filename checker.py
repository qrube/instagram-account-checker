import requests
from bs4 import BeautifulSoup
import concurrent.futures

def check_instagram_username(username):
    base_url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        response = requests.get(base_url, headers=headers, timeout=10)

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
    except requests.RequestException:
        return None, None

def main():
    usernames_file = "usernames.txt"  # Replace with the actual name of your .txt file containing usernames

    with open(usernames_file, "r") as file:
        usernames = file.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(check_instagram_username, usernames))

    for username, (is_available, profile_url) in zip(usernames, results):
        if is_available:
            print(f"Username '{username}' is taken. Profile: {profile_url}")
        else:
            print(f"Username '{username}' is available.")

if __name__ == "__main__":
    main()
