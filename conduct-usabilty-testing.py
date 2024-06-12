from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def verify_component_visibility(driver, component_locator):
    try:
        component = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, component_locator))
        )
        print("Component is visible on the dashboard.")
    except:
        print("Component is not visible on the dashboard.")


# Create a new instance of the WebDriver
driver = webdriver.Chrome()

# Navigate to the dashboard URL
dashboard_url = "http://127.0.0.1:2376"
driver.get(dashboard_url)

# Perform usability testing actions

# Example 1: Verify if a specific element is present
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "element_id"))
    )
    print("Element is present on the dashboard.")
except:
    print("Element is not present on the dashboard.")

# Example 2: Test navigation to a different page
try:
    # Click on a link or button to navigate to a different page
    driver.find_element(By.ID, "nav_link").click()

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(
        EC.url_contains("new_page")
    )
    print("Navigation to a different page is successful.")
except:
    print("Navigation to a different page failed.")

# Example 3: Verify the visibility of a specific component using daisyui.css
component_locator = "daisyui.css:.component"
verify_component_visibility(driver, component_locator)

# Close the WebDriver
driver.quit()