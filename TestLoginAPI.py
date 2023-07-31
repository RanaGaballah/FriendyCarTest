
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, WebDriverException, UnexpectedAlertPresentException
import time
import os

Borrower_PATH = "//h1[contains(text(), 'Borrower')]"
Borrower_PATH_2 = '//a[@href="/borrower" and contains(@class, "menu-link")]'
Dashboard_PATH = '//a[@href="/"]'
Dashboard_PATH_2 = '//a[@href="/" and contains(@class, "menu-link")]'
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
actions = ActionChains(driver)
test_cases = [
    {
        'url': 'https://corporate.friendycar.com/',
        'email': 'mostafa.makram@hassanallam.com',
        'password': '#aJ&54c7'
    },
    {
        'url': 'https://staging.corporate.friendycar.com/',
        'email': 'corporate.portal@friendycar.com',
        'password': 'test1234'
    },
    {
        'url': 'https://dev.corporate.friendycar.com',
        'email': 'corporate.portal@friendycar.com',
        'password': 'test1234'
    },

]

def test_cases_from_list(test_cases):
    for test_case in test_cases:
        url = test_case['url']
        email = test_case['email']
        password = test_case['password']
        print(f"Testing URL: {url}, Email: {email}, Password: {password}")
        open_url(url)
        start_time = time.time()
        driver.maximize_window()
        SignIn(email, password)
        end_time = time.time() - start_time
        clear_old_values()
        print(f"Test completed in {end_time:.2f} seconds")
        print()
        
        



def error_msg(exeption):
    errorMsg = str(exeption)
    error_lines = errorMsg.split('\n')
    for line in error_lines[:2]:
            return line




def signOut():
    try:
        sign_out_element = driver.find_element(
            By.XPATH, "//div[@class='user-avatar-content']")
        sign_out_element.click()
        sign_out_buttom = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(), 'Sign Out')]")))
        sign_out_buttom.click()
        driver.implicitly_wait(2)
        print("sign out successfully!")
    except Exception as a:
        print("sign out faild", error_msg(a))
        

# automating URL
def open_url(url):
    try:
        driver.get(url)
        print(f"URL opened successfully!")
    except TimeoutException:
        print(f"Timeout: Failed to open URL {url} within the specified time.")
    except WebDriverException as e:
        print(f"WebDriverException: Failed to open URL {url}. Error: {error_msg(e)}")


def successfull_seq():
    open_hover_menu()
    click_menu_elements(Borrower_PATH, Borrower_PATH_2,
                        "clicked borrower successful!", "clicked borrower faild")
    time.sleep(2)
    click_select()
    time.sleep(2)
    loop_over_borrowers()
    open_hover_menu()
    click_menu_elements(Dashboard_PATH, Dashboard_PATH_2,
                        "clicked Dashboard successful!", "clicked Dashboard faild")
    time.sleep(2)
    signOut()

# automating sign in process
def SignIn(email, password):
    driver.find_element(By.NAME, "email").clear()  # Clear old email value
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.ID, "passwordInput").clear()
    driver.find_element(By.ID, "passwordInput").send_keys(password)
    remember_me_checkbox = driver.find_element(By.XPATH, "//label[@for='remember']")
    remember_me_checkbox.click()
    driver.find_element(By.TAG_NAME, "button").click()
    try:
        # Check if sign-in is successful (Dashboard page is loaded)
        successful_signin_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h1[contains(text(), 'Dashboard')]"))
        )
        print("Sign in successful!")
        successfull_seq()
        
    except Exception as e:
        # Check different error scenarios
        if "Invalid credentials" in driver.page_source:
            print("Sign in failed: Invalid credentials")
        elif "Email is required" in driver.page_source:
            print("Sign in failed: Email is required")
        elif "Password is required" in driver.page_source:
            print("Sign in failed: Password is required")
        else:
            print("Sign in failed: Unexpected error -",error_msg(e))

#clear old values after each test case in sign in 
def clear_old_values():
    driver.delete_all_cookies()
    print("Cleared old values.")

#click select in borrower page to show all borrowers and check if this process done or not
def click_select():
    try:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        another_element = wait.until(
            EC.element_to_be_clickable((By.TAG_NAME, "select")))
        actions.move_to_element(another_element).perform()
        select = Select(another_element)
        select.select_by_value("100")
        print("Clicked select Successfully and chosed greatest value")
    except Exception as a:
        print("Clicked select faild", error_msg(a))

#click on each borrower row
def loop_over_borrowers():
    rows = driver.find_elements("xpath", "//tbody/tr")
    print("number of borrowers :", len(rows))
    if (len(rows) > 0):
        for i in range(3):
            try:
                rows = driver.find_elements(By.XPATH, "//tbody/tr")
                rows[i].click()
                driver.switch_to.window(driver.window_handles[-1])
                print(f"Borrower Number {i+1} URL :", driver.current_url)
                time.sleep(5)
                switching(i)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except Exception as StaleElementReferenceException:
                continue
    else:
        print("no borrowers")

#check if each borrower page opened successfully or not 
def switching(i):
    try:
        successful_switch_borrower_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h3[contains(text(), 'Contract Details')]"))
        )
        print(f"switching to borrower {i+1} successfully")
    except Exception as c:
        print(f"switching to borrower {i+1} faild",error_msg(c))

#open hover menu to click on borrower or dashboard and check if this process done or not 
def open_hover_menu():
    # open hover section
    try:
        hover_element = wait.until(
            EC.visibility_of_element_located((By.ID, "kt_aside")))
        actions.move_to_element(hover_element).perform()
        print("Open Hover Menu successful!")
    except Exception as a:
        print("Open Hover Menu Faild", error_msg(a))

#pass (borrower or dashboard) path to click on it and check if this process done or not
def click_menu_elements(element_path, element_path_2, successMsg, faildMsg):
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, element_path_2)))
    element.click()
    try:
        successful_borrower_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, element_path))
        )
        print(successMsg)
        time.sleep(2)
    except Exception as b:
        print(faildMsg, error_msg(b))




#body
#test_cases_from_list(test_cases)
email = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
open_url("https://corporate.friendycar.com/")
start_time = time.time()
driver.maximize_window()
SignIn(email, password)
end_time = time.time() - start_time
clear_old_values()
print(f"Test completed in {end_time:.2f} seconds")

