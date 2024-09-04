# site_connectivity_checker.py

import http.client

def check_website_connectivity(url):
    try:
        connection = http.client.HTTPConnection(url, port=80, timeout=10)
        connection.request("HEAD", "/")
        response = connection.getresponse()
        if response.status == 200:
            print(f"{url} is online.")
        else:
            print(f"{url} returned status code {response.status}.")
    except Exception as e:
        print(f"Error checking {url}: {e}")

if __name__ == "__main__":
    target_url = input("Enter a website URL: ")
    check_website_connectivity(target_url)
