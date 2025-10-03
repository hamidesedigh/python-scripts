# -*- coding: utf-8 -*-
"""
Dad Joke SMS Sender
-----------------------------------------------------------
This program fetches a random dad joke from the
icanhazdadjoke API and sends it to a given phone number
using the Kavenegar SMS API.

Author: hamid
Created on Sat Jul 12 12:43:14 2025
"""

import requests


def send_sms(number: str, text: str, api_key: str) -> bool:
    """
    Send an SMS using the Kavenegar API.

    Parameters:
        number (str): Recipient phone number.
        text (str): Message text.
        api_key (str): Kavenegar API key.

    Returns:
        bool: True if successful, False otherwise.
    """
    url = f"https://api.kavenegar.com/v1/{api_key}/sms/send.json"
    payload = {"receptor": number, "message": text, 'sender': "2000660110"}

    try:
        r = requests.post(url, data=payload)
        r.raise_for_status()
        result = r.json()
        print("Kavenegar response:", result)
        return r.ok
    except requests.RequestException as e:
        print("Failed to send SMS:", e)
        return False


def get_dad_joke() -> str:
    """Fetch a random dad joke from the icanhazdadjoke API."""
    url = "https://icanhazdadjoke.com/slack"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()["attachments"][0]["text"]
    except requests.RequestException as e:
        print("Error fetching dad joke:", e)
        return "Couldn't fetch a dad joke right now 😢"


def main():
    API_KEY = "4966414173324A506B303133536F4B74754A4E446956594B483268507A61424158693831704946714C464D3D" #your_api_key_here
    PHONE_NUMBER = "09111839543" #your_phone_number_here

    joke = get_dad_joke()
    print("Joke fetched:", joke)

    if not send_sms(PHONE_NUMBER, joke, API_KEY):
        print(f"Failed to send SMS to {PHONE_NUMBER}")


if __name__ == "__main__":
    main()
