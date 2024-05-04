from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()

# Open the website
driver.get("https://www.bestbuy.com/")

time.sleep(5)  # wait for button to appear on slow websites

print("opening chat")

# Find and click the button to open the chat window
open_chat_button = driver.find_element(
    By.CLASS_NAME, "blue-assist-minimized-beacon-container"
)
open_chat_button.click()

time.sleep(2)

print("writing message")

# Find the text area to write our message into
text_area = driver.find_element(By.ID, "chatMessage")

# Write a message into the text area
text_area.send_keys("Hello, this is a test message")

time.sleep(2)

print("sending message.")

# Find the button to send the message
send_button = driver.find_element(By.CLASS_NAME, "sendIconButton")

# Click the send button
send_button.click()

# Wait for a response (if applicable)
time.sleep(600)  # Adjust the sleep time as needed for the response

# Close the browser
driver.quit()
