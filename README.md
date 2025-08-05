# Discord Password Changer

A multithreaded Python script to change passwords for Discord accounts using user tokens.

> ⚠️ **Disclaimer**  
> This tool is for educational and research purposes only.  
> Misuse of this script for unauthorized access or malicious activity is strictly prohibited.

---

## 📁 Project Structure

| File               | Description                                  |
|--------------------|----------------------------------------------|
| `main.py`          | Main script to execute the password changer. |
| `tokens.txt`       | List of Discord user tokens.                 |
| `changedtoken.txt` | Stores tokens after a successful change.     |
| `config.json`      | Configuration file (proxy, threads, password). |
| `requirements.txt` | Python dependencies file.                    |

---

## ⚙️ Requirements

- Python 3.8+
- Internet connection

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/ali-7hh/discord-password-changer.git
cd discord-password-changer
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Fill in `config.json` with your settings.

> **Proxy (optional): use if needed, leave blank if not.**

4. Add your tokens to `tokens.txt` in the format:
```
email:old_password:token
```

---

## 🚀 Usage

Run the script:

```bash
python main.py
```

The script will process each token, attempt to change the password, and save successfully updated tokens to `changedtoken.txt`.

---

## 🙋 Author

Made by ali-7hh
