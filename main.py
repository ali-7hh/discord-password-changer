import tls_client
import concurrent.futures
from colorama import Fore
from threading import Lock
import json
def load_config():
    with open("config.json", "r") as f:
        return json.load(f)
def remove_email_from_file(filename: str, target_email: str):
    with Lock():
        with open(filename, 'r') as file:
            lines = file.readlines()
        lines = [line for line in lines if line.strip() != target_email.strip()]
        with open(filename, 'w') as file:
            file.writelines(lines)
def main(token):
    global succses, error

    password = token.split(':')[1]
    tok = token.split(':')[2]
    email = token.split(':')[0]

    url = "https://discord.com/api/v9/users/@me"
    headers = {
        "accept": "*/*",
        "authorization": tok,
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
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
                remove_email_from_file("tokens.txt", token)
                print(f"{Fore.GREEN}[{succses}] {email}:{new_password}:{new_token}")
        else:
            error += 1
            print(f"{Fore.RED}[{error}] Error for {tok} → {response.text}")
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
Created By ==> Rafa7awy |  Edited By ==> levcqh
Discord    ==> ii.y - levcqh
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
        futures = [executor.submit(main, token) for token in tokens]
        for future in concurrent.futures.as_completed(futures):
            future.result()
