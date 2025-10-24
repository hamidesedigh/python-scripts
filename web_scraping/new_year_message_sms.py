# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 13:02:43 2025
@Author: Hamideh

Bulk SMS Sender
-----------------------------------------------------------
This program reads phone numbers from a text file and sends
a New Year greeting SMS to each one using the Kavenegar API.
"""

import requests


def read_phones(filename: str) -> list[str]:
    """Read phone numbers from a text file (ignoring empty lines)."""
    try:
        with open(filename, encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Error: file '{filename}' not found.")
        return []


def send_sms(number: str, text: str, api_key: str, sender: str = "2000660110") -> bool:
    """
    Send an SMS using the Kavenegar API.

    Parameters:
        number (str): Recipient phone number.
        text (str): Message text.
        api_key (str): Kavenegar API key.
        sender (str): Sender ID (optional, default = '2000660110').

    Returns:
        bool: True if successful, False otherwise.
    """
    url = f"https://api.kavenegar.com/v1/{api_key}/sms/send.json"
    payload = {"receptor": number, "message": text, "sender": sender}

    try:
        r = requests.post(url, data=payload, timeout=10)
        r.raise_for_status()
        result = r.json()
        if r.ok:
            print(f"✅ SMS sent to {number}")
            return True
        else:
            print(f"⚠️ Failed for {number}: {result}")
            return False
    except requests.RequestException as e:
        print(f"❌ Error sending SMS to {number}: {e}")
        return False


def main():
    API_KEY = "4966414173324A506B303133536F4B74754A4E446956594B483268507A61424158693831704946714C464D3D" #your_api_key_here
    FILENAME = "my_phone_numbers.txt"
    MESSAGE = "سال نو مبارک! 🎉"

    phones = read_phones(FILENAME)
    if not phones:
        return

    for phone in phones:
        success = send_sms(phone, MESSAGE, API_KEY)
        if not success:
            print(f"Retry later or check number: {phone}")


if __name__ == "__main__":
    main()
