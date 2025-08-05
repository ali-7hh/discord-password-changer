import tls_client
import concurrent.futures
from colorama import Fore
from threading import Lock
import json
def load_config():
    with open("config.json", "r") as f:
        return json.load(f)
def remove_from_file(filename: str, target_email: str):
    with Lock():
        with open(filename, 'r') as file:
            lines = file.readlines()
        lines = [line for line in lines if line.strip() != target_email.strip()]
        with open(filename, 'w') as file:
            file.writelines(lines)
def main(tokens):
    global succses, error

    password = tokens.split(':')[1]
    token = tokens.split(':')[2]
    email = tokens.split(':')[0]

    url = "https://discord.com/api/v9/users/@me"
    headers = {
            "accept": "*/*",
            "accept-language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
            "authorization": f"{token}",
            "content-type": "application/json",
            "priority": "u=1, i",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-discord-timezone": "Africa/Cairo",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImFyLUVHIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzOC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTM4LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tLz9kaXNjb3JkdG9rZW49TVRNM05EUTBOamN4TnpRMU16SXdPVGMwTUEuR0I5T0Z2LmVTYmVtU0JWbjA0azlSSnJ2RGdrM1ZOSUZpZDdjRGFOWFlzVWhrIiwicmVmZXJyaW5nX2RvbWFpbiI6ImRpc2NvcmQuY29tIiwicmVmZXJyZXJfY3VycmVudCI6Imh0dHBzOi8vZGlzY29yZC5jb20vP2Rpc2NvcmR0b2tlbj1NVE0zTkRRME5qY3hOelExTXpJd09UYzBNQS5HQjlPRnYuZVNiZW1TQlZuMDRrOVJKcnZEZ2szVk5JRmlkN2NEYU5YWXNVaGsiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJkaXNjb3JkLmNvbSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjQyNjAzMCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiY2xpZW50X2xhdW5jaF9pZCI6IjVmMGMwODE2LWMxYTMtNDkwMC1hYTY2LTMzZTgwNTgyZTgzYiIsImxhdW5jaF9zaWduYXR1cmUiOiJhYjA2NjI0MS0zMWM5LTQyOGItOTQxMC04NGI4ZWM5M2M1OWIiLCJjbGllbnRfaGVhcnRiZWF0X3Nlc3Npb25faWQiOiIzZGUzODI5OC0yNTE0LTQyMWUtYWI5YS0wZDY3YWMyNjBlM2UiLCJjbGllbnRfYXBwX3N0YXRlIjoiZm9jdXNlZCJ9"
        }
    data = {
        "password": password,
        "new_password": new_password
    }
    try:
        response = session.patch(url, headers=headers, json=data, proxy=proxy)
        if response.status_code == 200:
            succses += 1
            new_token = response.json().get("token")
            if new_token:
                with open("changedtoken.txt", "a") as file:
                    file.write(f"{email}:{new_password}:{new_token}\n")
                remove_from_file("tokens.txt", tokens)
                print(f"{Fore.GREEN}[{succses}] {email}:{new_password}:{new_token}")
        else:
            error += 1
            print(f"{Fore.RED}[{error}] Error for {token} → {response.text}")
    except Exception as e:
        print(f"Error for {email}: {e}")
logo = r"""
 __                          ________                   __          
|  \                        |        \                 |  \         
| ▓▓       ______  __     __ \▓▓▓▓▓▓▓▓ ______   ______ | ▓▓ _______ 
| ▓▓      /      \|  \   /  \  | ▓▓   /      \ /      \| ▓▓/       \
| ▓▓     |  ▓▓▓▓▓▓\\▓▓\ /  ▓▓  | ▓▓  |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓  ▓▓▓▓▓▓▓
| ▓▓     | ▓▓    ▓▓ \▓▓\  ▓▓   | ▓▓  | ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓\▓▓    \ 
| ▓▓_____| ▓▓▓▓▓▓▓▓  \▓▓ ▓▓    | ▓▓  | ▓▓__/ ▓▓ ▓▓__/ ▓▓ ▓▓_\▓▓▓▓▓▓\
| ▓▓     \\▓▓     \   \▓▓▓     | ▓▓   \▓▓    ▓▓\▓▓    ▓▓ ▓▓       ▓▓
 \▓▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓    \▓       \▓▓    \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓\▓▓▓▓▓▓▓ 
"""

credits = """
Created By ==> Rafa7awy ===> Discord user  ==> ii.y - levcqh
"""
if __name__ == "__main__":
    print(Fore.CYAN + logo)
    print(Fore.YELLOW + credits)

    config = load_config()
    proxy = {"https": config["proxy"], "http": config["proxy"]} if config["proxy"] else None
    Threads = config["Threads"]
    new_password = config["new_password"]

    session = tls_client.Session(client_identifier="chrome_138",random_tls_extension_order=True)
    succses = 0
    error = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=Threads) as executor:
        with open("tokens.txt", "r") as f:
            tokens = f.read().splitlines()
        futures = [executor.submit(main, tokens) for tokens in tokens]
        for future in concurrent.futures.as_completed(futures):
            future.result()
