import requests
from flask import Flask

app = Flask(__name__)

TOKEN = '7761429377:AAF6Nw5Xlfb1EZMTYsmEZPGg0_s3mCM-az4'
CHAT_ID = '157853518'

@app.route('/')
def home():
    return "ربات آنلاین است!"

@app.route('/send_message')
def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    message = 'سلام از ربات تلگرام'
    payload = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(url, data=payload)
    return f"پیام ارسال شد: {response.json()}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)