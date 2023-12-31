
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



options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=options)
email = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

test_cases = [
    {
        'url': 'https://staging.maintenance-centers.friendycar.com',
        'email' : email,
        'password': password
    },
    {
        'url': 'https://develop.maintenance-centers.friendycar.com',
        'email' : email,
        'password': password
    },
    {
        'url': 'https://maintenance-centers.friendycar.com',
        'email' : email,
        'password': password
    },
]




Maintenance_PATH = "//h1[contains(text(), 'Maintenance')]"
Maintenance_PATH_2 = '//a[@href="/maintenances" and contains(@class, "menu-link")]'
Dashboard_PATH = '//a[@href="/"]'
Dashboard_PATH_2 = '//a[@href="/" and contains(@class, "menu-link")]'
wait = WebDriverWait(driver, 30)
actions = ActionChains(driver)

def test_cases_from_list(test_cases):
    for test_case in test_cases:
        try:
            url = test_case['url']
            email = test_case['email']
            password = test_case['password']
            print(f"Testing URL: {url}, Email: {email}")
            open_url(url)
            start_time = time.time()
            driver.maximize_window()
            SignIn(email, password)
            end_time = time.time() - start_time
            clear_old_values()
            print(f"Test completed in {end_time:.2f} seconds")
            print()
        except Exception as e:
            print("---------------------------------------------------------------------")
            print("ERROR! An error occurred:", error_msg(e))
            print("---------------------------------------------------------------------")





def error_msg(exeption):
    errorMsg = str(exeption)
    error_lines = errorMsg.split('\n')
    for line in error_lines[:2]:
            return line





# automating URL
def open_url(url):
    try:
        driver.get(url)
        time.sleep(3)
        print(f"URL opened successfully!")
        try:
            bad_gateway_element = driver.find_element(By.XPATH, "//center/h1[contains(text(), '502 Bad Gateway')]")
            print("---------------------------------------------------------------------")
            print("ERROR! Encountered a 502 Bad Gateway error.")
            print("---------------------------------------------------------------------")
        except:
            pass
    except TimeoutException:
        print("---------------------------------------------------------------------")
        print(f"ERROR! Timeout: Failed to open URL {url} within the specified time.")
        print("---------------------------------------------------------------------")
    except WebDriverException as e:
        print("---------------------------------------------------------------------")
        print(f"ERROR! WebDriverException: Failed to open URL {url}. Error: {error_msg(e)}")  
        print("---------------------------------------------------------------------")
    except  Exception as e:
        print("---------------------------------------------------------------------")
        print("ERROR! An error occurred:", error_msg(e))
        print("---------------------------------------------------------------------")


def successfull_seq():
    try:
        open_hover_menu()
        click_menu_elements(Maintenance_PATH, Maintenance_PATH_2,
                            "clicked on Upcoming Maintenance successful!", "ERROR! clicked on Upcoming Maintenance faild")
        time.sleep(2)
        click_select()
        time.sleep(2)
        loop_over_borrowers()
        open_hover_menu()
        click_menu_elements(Dashboard_PATH, Dashboard_PATH_2,
                            "clicked Dashboard successful!", "ERROR! clicked Dashboard faild")
    except Exception as e:
        print("---------------------------------------------------------------------")
        print("ERROR! An error occurred:", error_msg(e))
        print("---------------------------------------------------------------------")
    
    

# automating sign in process
def SignIn(email, password):
    try:
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
            print("---------------------------------------------------------------------")
            print("ERROR! Sign in failed: Unexpected error -",error_msg(e))
            print("---------------------------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------------------------")
        print("ERROR! Sign in failed: Unexpected error -",error_msg(e))
        print("---------------------------------------------------------------------")

#clear old values after each test case in sign in 
def clear_old_values():
    driver.delete_all_cookies()
    print("Cleared old values.")

#click select in borrower page to show all borrowers and check if this process done or not
def click_select():
    try:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "form-select"))) 
        actions.move_to_element(select_element).perform()
        select = Select(select_element)
        desired_option_value = "100"
        desired_option_locator = (By.XPATH, f"//option[@value='{desired_option_value}']")
        desired_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(desired_option_locator))
        desired_option.click()
        print("Clicked select Successfully and chosed greatest value")
    except Exception as a:
        print("---------------------------------------------------------------------")
        print("ERROR! Clicked select faild", error_msg(a))
        print("---------------------------------------------------------------------")

#click on each borrower row
def loop_over_borrowers():
    rows = driver.find_elements("xpath", "//tbody/tr")
    print("Number of Up Coming Maintenance :", len(rows))
    if (len(rows) > 0):
        for i in range(1):
            try:
                rows = driver.find_elements(By.XPATH, "//tbody/tr")
                rows[i].click()
                driver.switch_to.window(driver.window_handles[-1])
                print(f"Up Coming Maintenance Number {i+1} URL :", driver.current_url)
                time.sleep(5)
                switching(i)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except Exception as StaleElementReferenceException:
                continue
    else:
        print("No Up Coming Maintenance")

#check if each borrower page opened successfully or not 
def switching(i):
    try:
        successful_switch_borrower_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h3[contains(text(), 'Maintenance Details')]"))
        )
        print(f"switching to Up Coming Maintenance {i+1} successfully")
    except Exception as c:
        print("---------------------------------------------------------------------")
        print(f"ERROR! switching to Up Coming Maintenance {i+1} faild",error_msg(c))
        print("---------------------------------------------------------------------")
#open hover menu to click on borrower or dashboard and check if this process done or not 
def open_hover_menu():
    # open hover section
    try:
        hover_element = wait.until(
            EC.visibility_of_element_located((By.ID, "kt_aside")))
        actions.move_to_element(hover_element).perform()
        print("Open Hover Menu successful!")
    except Exception as a:
        print("---------------------------------------------------------------------")
        print("ERROR! Open Hover Menu Faild", error_msg(a))
        print("---------------------------------------------------------------------")

#pass (borrower or dashboard) path to click on it and check if this process done or not
def click_menu_elements(element_path, element_path_2, successMsg, faildMsg):
    try:
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
            print("---------------------------------------------------------------------")
            print(faildMsg, error_msg(b))
            print("---------------------------------------------------------------------")
    except Exception as b:
        print("---------------------------------------------------------------------")
        print(faildMsg, error_msg(b))
        print("---------------------------------------------------------------------")


test_cases_from_list(test_cases)







