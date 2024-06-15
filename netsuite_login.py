"""
netsuite_login.py

This module contains the function to automate downloading sales order data from NetSuite.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def download_reports(username, password, q1, a1, q2, a2, q3, a3, url1, url2, url3):
    """
    Automates the process of logging into NetSuite and downloading various reports.
    
    Parameters:
    username (str): NetSuite username.
    password (str): NetSuite password.
    q1 (str): First security question.
    a1 (str): Answer to the first security question.
    q2 (str): Second security question.
    a2 (str): Answer to the second security question.
    q3 (str): Third security question.
    a3 (str): Answer to the third security question.
    url1 (str): URL for the first report.
    url2 (str): URL for the second report.
    url3 (str): URL for the third report.
    """

    # Set up Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Navigate to the NetSuite login page
        driver.get(url1)

        # Log in to NetSuite
        username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "email")))
        username_input.send_keys(username)
        password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password")))
        password_input.send_keys(password)
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login_button.click()
        print("Logging in to NetSuite...")

        try:
            # Handle account selection if necessary
            choose_account_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//td[text()='PRODUCTION']/following-sibling::td/a"))
            )
            choose_account_link.click()
            print("Selecting account...")
        except:
            # Handle security questions
            secret_question = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[2]/div[2]/form/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]"))
            )
            if q1.lower() in secret_question.text.lower():
                answer_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "answer")))
                answer_input.send_keys(a1)
            elif q2.lower() in secret_question.text.lower():
                answer_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "answer")))
                answer_input.send_keys(a2)
            elif q3.lower() in secret_question.text.lower():
                answer_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "answer")))
                answer_input.send_keys(a3)
            login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "submitter")))
            login_button.click()
            print("Answered security questions.")

        # Download first report
        time.sleep(5)
        csv_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='Export - CSV']")))
        csv_button.click()
        print("Downloaded Report 1!")

        # Download second report
        time.sleep(3)
        print("Navigating to Report 2...")
        driver.get(url2)
        csv_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='Export - CSV']")))
        csv_button.click()
        print("Downloaded Report 2!")

        # Download third report
        time.sleep(3)
        print("Navigating to Report 3...")
        driver.get(url3)
        csv_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[title='Export - CSV']")))
        csv_button.click()
        print("Downloaded Report 3!")

        # Wait for the final download to complete
        time.sleep(5)

    except Exception as e:
        print(f"Download Failed! Error: {e}")

    finally:
        # Close the browser
        driver.quit()
