import requests, argparse #makes HTTP requests and parses CLI args
import concurrent.futures
from collections import OrderedDict
from colorama import init, Fore #for colored terminal output
import time, random

init()
WEBSITES = OrderedDict([
    ("Instagram", "https://www.instagram.com/{}"),
    ("Facebook", "https://www.facebook.com/{}"),
    ("Linkedin", "https://www.linkedin.com/{}"),
    ("YouTube", "https://www.youtube.com/user/{}"),
    ("TikTok", "https://www.tiktok.com/@{}")
    ])

REQUEST_DELAY = 2
MAX_RETRIES = 3
last_request_times = {}

def check_username(website, username):
    url = website.format(username)
    retries = 0 #init counter
    while retries < MAX_RETRIES:
        try:
            current_time = time.time()
            if website in last_request_times and current_time - last_request_times[website] < REQUEST_DELAY:
                delay = REQUEST_DELAY - (current_time - last_request_times[website])
                time.sleep(delay)

            response = requests.get(url)
            last_request_times[website] = time.time()
            if response.status_code == 200:
                return url
            else:
                return False
        except requests.exceptions.RequestException:
            retries += 1
            delay = random.uniform(1, 3)
            time.sleep(delay)

    return False

def main():
    parser = argparse.ArgumentParser(description="See if uname exists")
    parser.add_argument("username", help="The username to check")
    parser.add_argument("-o", "--output", help="Path to save results too")
    args = parser.parse_args()
    username = args.username
    output_file = args.output
    print(f"Checking for username>: {username}")
    results = OrderedDict()
    with concurrent.futures.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(check_username, website, username): website_name for website_name, website in WEBSITE.items()}
        for future in concurrent.futures.as_completed(futures):
            website_name = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                print(f"{website_name} generated an exception: {exc}")
                result = False
            finally:
                result[website_name] = result

    print("\nResults:")
    for website, result in results.items():
        if result:
            print(f"{Fore.GREEN}{website}: Found ({result})")
        else:
            print(f"{Fore.RED}{website}: Not Found")

    if output_file:
        with open(output_file, "w") as f:
            for website, result in results.item():
                if result:
                    f.write(f"{website}: Found ({result})\n")
                else:
                    f.write(f"{website}: Not Found\n")

        print(f"{Fore.GREEN}\nResutls saved to {output_file}")

main()

