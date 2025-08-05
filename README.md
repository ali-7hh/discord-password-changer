# Discord Password Changer

This Python script automates the process of changing Discord account passwords using user tokens.

> ⚠️ **Disclaimer**  
> This tool is for educational and research purposes only.  
> Misuse of this script for unauthorized access or any malicious activity is strictly prohibited.

---

## 📁 Project Structure

| File               | Description                                  |
|--------------------|----------------------------------------------|
| `main.py`          | Main script to execute the password changer. |
| `tokens.txt`       | List of Discord user tokens.                 |
| `changedtoken.txt` | Stores tokens after a successful change.     |
| `config.json`      | Contains the old and new passwords.          |
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
3. Add your tokens to `tokens.txt` in the format:
        
```bash
email:old_password:token
```

## 🚀 Usage

4. Run the script:

```bash
python main.py
```

The script will process each token, attempt to change the password, and save successfully updated tokens to `changedtoken.txt`.

---

## 📄 License

This project is open-source and provided for educational purposes only.  
Using it on unauthorized accounts is strictly prohibited.
