# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 08:58:47 2025
@Author: Hamideh

Bitcoin Price Alert with SMS Notification
-----------------------------------------------------------
This program checks the current Bitcoin price (in USD) using
the Coinbase API. If the price drops below a target threshold,
an SMS notification is sent via the Kavenegar API.

Requirements:
- requests library
- Valid Kavenegar API key and phone number

"""

import requests


def send_sms(message: str, receptor: str, api_key: str) -> None:
    """
    Send an SMS message using the Kavenegar API.

    Parameters:
        message (str): The message text to send.
        receptor (str): The recipient phone number.
        api_key (str): The Kavenegar API key.
    """
    url = f'https://api.kavenegar.com/v1/{api_key}/sms/send.json'
    payload = {"receptor": receptor, "message": message, 'sender': "2000660110"}
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("SMS sent successfully:", response.json())
    except requests.RequestException as e:
        print("Failed to send SMS:", e)


def get_bitcoin_price(proxy: dict | None = None) -> float:
    """
    Get the current Bitcoin price in USD from Coinbase API.

    Parameters:
        proxy (dict, optional): Proxy settings if required.

    Returns:
        float: Current BTC price in USD.
    """
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
    response = requests.get(url, proxies=proxy)
    response.raise_for_status()
    return float(response.json()["data"]["amount"])


def main():
    # --- Config ---
    API_KEY = "4966414173324A506B303133536F4B74754A4E446956594B483268507A61424158693831704946714C464D3D"  # your_api_key_here
    PHONE_NUMBER = "09111839543"  # your_phone_number_here
    TARGET_PRICE = 150_000  # in USD
    PROXIES = {"https": "socks5://127.0.0.1:10808"}  # set None if not needed

    try:
        price = get_bitcoin_price(PROXIES)
        print(f"Current Bitcoin price: ${price:,.2f}")

        if price < TARGET_PRICE:
            send_sms(
                message=f"Alert! Bitcoin price dropped to ${price:,.2f}",
                receptor=PHONE_NUMBER,
                api_key=API_KEY
            )
    except requests.RequestException as e:
        print("Error fetching Bitcoin price:", e)


if __name__ == "__main__":
    main()
