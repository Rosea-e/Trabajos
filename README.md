# 🛡️ Keylogger (Educational & Authorized Use Only)

This project is a Python-based keylogger designed for **educational**, **testing**, and **authorized monitoring** purposes only. It captures keyboard input, logs active window titles, and sends the data via email and webhook for analysis.

> ⚠️ **Important Notice**  
> This tool must only be used on systems you own or have explicit permission to monitor. Unauthorized use of keyloggers is illegal and unethical. The author is not responsible for any misuse.

## 📦 Features

- Captures keystrokes in real time
- Logs active window titles
- Sends logs via:
  - Email (SMTP)
  - Webhook (HTTP POST)
- Filters out special keys
- Clears buffer after threshold (e.g., 5 Enter presses)

## 🔧 Requirements

- Python 3.x
- `keyboard`
- `requests`
- `smtplib` (built-in)
- `pygetwindow`

Install dependencies:

```bash
pip install keyboard requests pygetwindow
```

## ✉️ Email Setup

To enable email sending, configure these variables in the script:

```python
EMAIL_ORIGEN = "your_email@gmail.com"
EMAIL_DESTINO = "destination_email@gmail.com"
EMAIL_PASS = "your_app_password"
```

> 💡 Use an [App Password](https://support.google.com/accounts/answer/185833?hl=en) if you're using Gmail with 2FA.

## 🚀 Usage

Run the script:

```bash
python keylogger.py
```

It will begin logging keystrokes and sending data after every 5 Enter presses.

## 🧠 Legal & Ethical Use

This tool is intended for:

- Personal system monitoring
- Educational cybersecurity labs
- Authorized penetration testing

Do **not** use this software to monitor others without consent. Always comply with local laws and regulations.

## 📄 License

This project is released under the MIT License. See `LICENSE` for details.
