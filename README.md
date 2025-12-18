# Automated Cookie Clicker Bot

A high-speed automation script built with Python and Selenium that plays the classic [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/) game.

The bot automatically clicks the cookie and intelligently purchases the most expensive upgrades available every 5 seconds to maximize the "Cookies Per Second" (CPS) rate.

## Demo

![Cookie Clicker Demo](demo.gif)

## Key Features

-   **High-Frequency Clicking:** Clicks the main cookie continuously using a `while` loop.
-   **Smart Upgrades:** Every 5 seconds, the bot pauses briefly to analyze the store.
-   **Dynamic Pricing:** Scrapes the real-time cost of all upgrades (from Cursors to Time Machines) by parsing the HTML data.
-   **Greedy Algorithm:** Automatically prioritizes purchasing the most expensive affordable item to boost CPS as quickly as possible.
-   **Timed Execution:** Runs for a set duration (default: 5 minutes) and prints the final CPS score upon completion.

## Project Setup

This project uses Selenium Web Driver to control the Google Chrome browser.

### 1. Prerequisites

-   Python 3.x
-   Google Chrome Browser installed.
-   `pip` (Python package installer)

### 2. Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dheerajdhami2001-cyber/cookie-clicker-bot.git
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd cookie-clicker-bot
    ```

3.  **Install Selenium:**
    ```bash
    pip install selenium
    ```

### 3. Driver Setup

Newer versions of Selenium (4.6+) usually manage the browser driver automatically. However, if you encounter errors regarding `chromedriver`:
1.  Check your Chrome version (Settings -> About Chrome).
2.  Download the matching [ChromeDriver here](https://chromedriver.chromium.org/downloads).
3.  Ensure the driver is in your system PATH or the project folder.

## How to Run

1.  Run the script:
    ```bash
    python main.py
    ```
2.  **Watch it go:** A Chrome window will open. The bot will begin clicking immediately. You will see the cursor moving to the right panel to buy upgrades every 5 seconds.
3.  **Completion:** After 5 minutes, the bot will stop and print your final CPS (Cookies Per Second) to the console.

## Optimization & Future Improvements

This bot currently uses a "Greedy" strategy (buy the most expensive item possible). While effective, it can be further optimized for competitive scores:

-   **ROI Calculation:** Instead of buying the most expensive item, the logic could be updated to calculate the "Price vs. CPS" ratio to determine the most efficient upgrade.
-   **Multithreading:** Currently, the clicking stops for a fraction of a second while the bot checks prices. Using Python's `threading` module could allow the bot to click and check prices simultaneously.
-   **Element Selectors:** Transitioning from `XPath` to `CSS Selectors` could slightly improve the speed of locating elements on the page.

## Acknowledgments

This project was inspired by and completed with the guidance of the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)** by Dr. Angela Yu.

