# Live Currency Converter App


**Version:** 3.0  

## Overview
A simple currency converter app built using **PyQt6** for the graphical user interface (GUI) and **BeautifulSoup** for fetching live exchange rates. The app allows users to convert an amount from one currency to another based on real-time exchange rates.

## Features
- **Currency Selection**: Choose the input and output currencies from a dropdown list (USD, EUR, INR, CAD, GBP, AUD, JPY, CNY).
- **Amount Input**: Enter the amount you want to convert.
- **Conversion Button**: Click "Convert" to perform the currency conversion using live exchange rates.

## How It Works
The app fetches the live exchange rate for the selected currencies from [x-rates.com](https://www.x-rates.com) using **web scraping** with **BeautifulSoup**. It then performs the conversion and displays the result.

## Code Overview

### Web Scraping for Exchange Rate
The exchange rate is fetched using **BeautifulSoup** by parsing the HTML of the page.

## PyQt6 User Interface
The user interface is created using PyQt6 and contains:

Dropdown menus for currency selection (One for the current currency and the other for the target currency).
A text input for the amount.
A button to perform the conversion and display the result.

## Version History
- **Version 2.0**: 
  - Added dropdown menus to select input and output currencies dynamically.
  - No longer hardcoded to specific currencies; users can select any supported currency.
  - Cleaned up UI to make the app more user-friendly.
  
- **Version 1.0**: 
  - Hardcoded currencies (only CAD to USD conversion).
  - User input was limited to one fixed currency (USD) and conversion was fixed to EUR.

- **Version 3.0: (Latest)**
  - Introduced an advanced layout using nested horizontal and vertical layouts for a cleaner, more modular, and scalable design.
