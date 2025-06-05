import requests

domain = input("<DOMAIN>: ")
#File of most common subdomains from a github
file = open("subdomain.txt")
content = file.read()

#Split by new lines
subdomains = content.splitlines()

discovered_subdomains = []
for subdomain in subdomains:
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Discovered subdomain: ", url)
        discovered_subdomain.append(url)

with open("discovered_subdomains.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)

