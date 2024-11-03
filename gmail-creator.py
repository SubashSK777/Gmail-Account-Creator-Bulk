import os
import requests
import traceback
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Function to generate a random string
def random_string(length=8):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Fetch user agents from URL
def get_user_agents(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"Error fetching user agents: {e}")
        return []

# Gmail Account Creation Function
def gmail_account(driver, user_agent):
    options = Options()
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--start-maximized")
    driver.options = options

    try:
        driver.get("https://www.gmail.com")
        wait = WebDriverWait(driver, 50)

        # Click 'Create account' and wait
        create_account_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Create account']")))
        create_account_button.click()
        time.sleep(5)

        # Fill account details
        first_name, last_name = random_string(8), random_string(10)
        username, password = random_string(10) + "12345", random_string(12) + "123"

        wait.until(EC.element_to_be_clickable((By.ID, "firstName"))).send_keys(first_name)
        driver.find_element(By.ID, "lastName").send_keys(last_name)
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.NAME, "Passwd").send_keys(password)
        driver.find_element(By.NAME, "ConfirmPasswd").send_keys(password)
        driver.find_element(By.XPATH, "//div[@id='accountDetailsNext']/div/button").click()

        # Write credentials to file
        with open("created.txt", "a") as file:
            file.write(f"Username: {username}\nPassword: {password}\n\n")

    except TimeoutException as e:
        log_error("Timeout", driver, str(e))
    except Exception as e:
        log_error("General", driver, str(e))

# Error Logging Function
def log_error(error_type, driver, error_msg):
    driver.save_screenshot(f"{error_type}_error.png")
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{error_type} Exception: {error_msg}\n")

# Main Execution
user_agents_url = "https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt"
user_agents = get_user_agents(user_agents_url)

if user_agents:
    # Set up Chrome driver
    driver = webdriver.Chrome()
    for _ in range(5):  # Number of accounts to create
        gmail_account(driver, random.choice(user_agents))
    driver.quit()
else:
    print("No user agents fetched.")
