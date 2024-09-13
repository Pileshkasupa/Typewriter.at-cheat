from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui as autogui
import pyperclip

# Prompt for the IDs of the HTML elements you want to extract
element1_id = input("Enter the ID of the first HTML element: ")
element2_id = input("Enter the ID of the second HTML element: ")

# Set up Chrome options to connect to the existing session with remote debugging enabled
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # Connect to the existing Chrome session

# Initialize the Chrome WebDriver (connecting to the existing session)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def normalize_whitespace(text):
    # Dictionary mapping common white space characters to a normal space
    whitespace_mapping = {
        '\u200b': ' ', '\u00a0': ' ', '\u1680': ' ', '\u180e': ' ', '\u2000': ' ', '\u2001': ' ',
        '\u2002': ' ', '\u2003': ' ', '\u2004': ' ', '\u2005': ' ', '\u2006': ' ', '\u2007': ' ',
        '\u2008': ' ', '\u2009': ' ', '\u200a': ' ', '\u202f': ' ', '\u205f': ' ', '\u3000': ' ', '&nbsp;': ' '
    }
    
    # Replace each white space character with a normal space
    for char, replacement in whitespace_mapping.items():
        text = text.replace(char, replacement)
    
    return text

try:
    # Start an infinite loop to repeat the process
    while True:
        # Wait for the page to load completely
        time.sleep(0.2)

        # Try extracting the innerHTML of the two elements by their IDs
        try:
            # Locate the elements by their IDs
            element1 = driver.find_element(By.ID, element1_id)
            element2 = driver.find_element(By.ID, element2_id)

            # Get the innerHTML of the elements
            element1_text = element1.get_attribute('innerHTML') if element1 else 'Element 1 not found'
            element2_text = element2.get_attribute('innerHTML') if element2 else 'Element 2 not found'

            # Normalize white space characters
            element1_text = normalize_whitespace(element1_text)
            element2_text = normalize_whitespace(element2_text)

            # Combine the extracted text from both elements
            combined_text = f"{element1_text}{element2_text}"
            print(f"Extracted text:\n{combined_text}")

            # Copy the combined text to the clipboard
            pyperclip.copy(combined_text)

            # Simulate pressing F6 to switch to another element or task
            autogui.press('f6')
            print("Text copied to clipboard, F6 pressed")

        except Exception as e:
            print(f"Error extracting elements: {str(e)}")

        # Wait for a bit before repeating the loop (adjust the time as needed)
        time.sleep(0.3)

except KeyboardInterrupt:
    # Handle script stop (Ctrl + C)
    print("Script stopped by the user.")

finally:
    # Close the driver when the loop is stopped
    driver.quit()
