import requests
import json
import time
import os 
from colorama import Fore, Style, init

init()

def print_error(message):
    print(Fore.RED + message + Style.RESET_ALL)

def print_success(message):
    print(Fore.GREEN + message + Style.RESET_ALL)


email1 = os.environ.get('USERNAME1')
password1 = os.environ.get('PASSWORD1')
email2= os.environ.get('USERNAME2')
password2 = os.environ.get('PASSWORD2')
test_cases = [
    {
        'API' : "Corporate",
        'Login_URL' : "https://nova.friendycar.com/api/login",
        'DashBoard_URL' : "https://nova.friendycar.com/borrower-api/v1/dashboard",
        'Borrower_URL' : "https://nova.friendycar.com/borrower-api/v1/contracts?page=1&per_page=10",
        'dashboard_access' : '716|A420x6yljFiqaMpeAxb4nKiazPgC1R5jmoslP5Cq',
        'borrower_access' : '722|zeRTQWoD5E5gnFzgkfr6Kdc1IT2lHYhwZMWkrCyr',
        "email": email1,
        "password": password1,
    },
    {
        'API' : "Corporate STG",
        'Login_URL' : "https://beta.friendycar.com/api/login",
        'DashBoard_URL' : "https://nova.friendycar.com/borrower-api/v1/dashboard",
        'Borrower_URL' : "https://nova.friendycar.com/borrower-api/v1/contracts?page=1&per_page=10",
        'dashboard_access' : '716|A420x6yljFiqaMpeAxb4nKiazPgC1R5jmoslP5Cq',
        'borrower_access' : '722|zeRTQWoD5E5gnFzgkfr6Kdc1IT2lHYhwZMWkrCyr',
        "email" : email2,
        "password": password2,
    },
    {
        'API' : "Corporate DEV",
        'Login_URL' : "https://nova.friendyboat.com/api/login",
        'DashBoard_URL' : "https://nova.friendyboat.com/borrower-api/v1/dashboard",
        'Borrower_URL' : "https://nova.friendyboat.com/borrower-api/v1/contracts?page=1&per_page=10",
        'dashboard_access' : '1176|bfrbPhzEFy6FmZ1Hh7X8Sd1Lh6QfVjIhDKrKD2Eg',
        'borrower_access' : '1176|bfrbPhzEFy6FmZ1Hh7X8Sd1Lh6QfVjIhDKrKD2Eg',
        "email" : email2,
        "password": password2,
    },
]



def DashBoard_API(URL,access):
    access_token = access
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'corporate',
        'Content-Type': 'application/json'

    }
    response = requests.get(URL,headers=vheaders).json()
    if 'message' in response:
        if response['message'] == "Dashboard Data":
            print_success("FriendyCar Corporate : DashBoard API passed successfully.")
            #print("FriendyCar Corporate : DashBoard API passed successfully.")
        else:
            print_error("FriendyCar Corporate : DashBoard API faild, Please check your credentials.")
           # print("FriendyCar Corporate : DashBoard API faild, Please check your credentials.")
    else:
        print_error("FriendyCar Corporate : Unexpected response from the Dashboard API.")
        #print("FriendyCar Corporate : Unexpected response from the Dashboard API.")
        print(response)

def Borrower_API(URL , access):
    access_token = access
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'corporate',
        'Content-Type': 'application/json'

    }
    response = requests.get(URL,headers=vheaders)
    if response.status_code == 200:
        print("FriendyCar Corporate : Borrower API passed successfully.")
    else:
        print("FriendyCar Corporate : Unexpected response from the Borrower API.")
        print(response)    
def Login_API(email,password,login_url,dashboard_url,borrower_url,dashboard_access,borrower_access):
    Login_Data = {
        "email": email,
        "password": password
    }

    vheaders = {
        'accept': 'application/json',
        'app-type': 'corporate',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(login_url, json=Login_Data, headers=vheaders).json()
        if 'message' in response:
            if response['message'] == "Logged successfully!.":
                print("FriendyCar Corporate : Login API Passed successfully.")
                DashBoard_API(dashboard_url,dashboard_access)
                Borrower_API(borrower_url,borrower_access)
            else:
                print("FriendyCar Corporate : Login API failed. Please check your credentials.")
        else:
            print("FriendyCar Corporate : Unexpected response from the Login API.")
            print(response)
    
    except Exception as e:
        print("An unexpected error occurred.")
        print(e)        




def loop():
    for test_case in test_cases:
            api_name = test_case['API']
            login_url = test_case['Login_URL']
            dashboard_url = test_case['DashBoard_URL']
            borrower_url = test_case['Borrower_URL']
            dashboard_access = test_case['dashboard_access']
            borrower_access = test_case['borrower_access']
            email = test_case['email']
            password = test_case['password']
            print(f"Testing API : {api_name}")
            Login_API(email,password,login_url,dashboard_url,borrower_url,dashboard_access,borrower_access)
            
            
start_time = time.time()            
loop()  
end_time = time.time() - start_time
print(f"Test completed in {end_time:.2f} seconds")          
