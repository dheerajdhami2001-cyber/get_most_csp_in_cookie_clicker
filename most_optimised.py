import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Setup with high-speed options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get the cookie element once to save time
cookie = driver.find_element(By.ID, "cookie")

# 2. Timing logic
# We check the store every 1 second for maximum compounding interest
check_timeout = time.time() + 1
five_min_end = time.time() + 60 * 5

while time.time() < five_min_end:
    # Click as fast as the Python loop allows
    cookie.click()

    # Every 1 second, go on a shopping spree
    if time.time() > check_timeout:

        # Get all store items
        # We use CSS Selector to find all <b> tags inside the store
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # Convert price strings to integers
        for price in all_prices:
            text = price.text
            if text != "":
                # Using [-1] to grab the number regardless of word count (e.g., Alchemy Lab)
                cost = int(text.split("-")[-1].replace(",", "").strip())
                item_prices.append(cost)

        # Map prices to their parent div IDs so we can click them
        # The game has 8 standard upgrades in the classic version
        item_ids = [
            "buyCursor", "buyGrandma", "buyFactory", "buyMine",
            "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"
        ]

        upgrades = {}
        for n in range(len(item_prices)):
            upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        current_money = int(money_element.replace(",", ""))

        # STRATEGY: Buy the most expensive thing we can afford
        # Then immediately check if we can afford the next best thing with leftover cash
        affordable_upgrades = [cost for cost in item_prices if cost <= current_money]

        if affordable_upgrades:
            # Sort prices to find the biggest one
            highest_affordable_cost = max(affordable_upgrades)
            id_to_buy = upgrades[highest_affordable_cost]

            # Purchase the best item
            driver.find_element(By.ID, id_to_buy).click()

        # Reset the 1-second timer
        check_timeout = time.time() + 1

# 3. Game Over - Print Results
cps = driver.find_element(By.ID, "cps").text
print(f"--- 5 MINUTE CHALLENGE COMPLETE ---")
print(f"Final Score: {cps}")