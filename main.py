# config

web_url = "url"

# import

import httpx 

# code

def start_pinging(web):
    try:
        httpx.get(web)
        return True
    except:
        return False

while True:
        req = start_pinging(web_url)
        if req == True:
            print("[+] up\n\n")
        else:
            print("[-] down\n\n")


# @ spencexd7
