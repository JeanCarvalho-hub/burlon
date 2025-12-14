# Rat Brute

> ⚠️ **For educational purposes only**

**Rat Brute** is a Python-based script designed to perform **brute force testing on Instagram via a web browser**, using a **custom wordlist**.  
The script relies on browser automation with **Selenium** and works **only with Google Chrome or Mozilla Firefox**.

---

## 📌 Features

- Brute force testing via real browser automation
- Custom wordlist support
- Simple and interactive CLI
- Compatible with Chrome and Firefox
- Built-in delay between password attempts to reduce detection

---

## 📦 Requirements

- Python 3.x
- Google Chrome or Mozilla Firefox
- Selenium library

Install Selenium using pip:

```bash
pip install selenium
```

> Make sure you have the appropriate **WebDriver** installed and accessible in your system PATH (ChromeDriver or GeckoDriver).

---

## 🚀 Usage

1. Ensure that your **wordlist**:
   - Is located in the **same directory** as `ratbrute.py`
   - Has the **exact filename expected by the script**

2. Run the script from the terminal:

```bash
python ratbrute.py
```

3. When prompted:
   - Enter the **Instagram username or email**
   - Press **Enter** to start

4. The brute force process will begin automatically.
   
   > ⏱️ After each password attempt, the script pauses for **1 minute** to help avoid IP blacklisting and reduce the chance of detection by **IDS/WAF systems**.

---

## ⚠️ Disclaimer

This project was created **strictly for educational and learning purposes**, such as:

- Understanding rate limiting and delay strategies
- Studying how IDS/WAF systems detect automated behavior

- Studying browser automation with Selenium
- Understanding authentication mechanisms
- Practicing cybersecurity concepts in controlled environments

Any misuse of this script may violate **laws and platform terms of service**.  
The author **assumes no responsibility** for improper or illegal usage.

---

## 🛠️ Technologies Used

- Python
- Selenium
- Chrome / Firefox WebDriver

---

## 📄 License

This project is provided for educational use only. Use responsibly.

