import requests
import json
import time
import os 

email1 = os.environ.get('USERNAME1')
password1 = os.environ.get('PASSWORD1')
email2= os.environ.get('USERNAME2')
password2 = os.environ.get('PASSWORD2')

def error_msg(exeption):
    errorMsg = str(exeption)
    error_lines = errorMsg.split('\n')
    for line in error_lines[:2]:
            return line
test_cases = [
    {
        'API' : "Corporate",
        'Login_URL' : "https://nova.friendycar.com/api/login",
        'DashBoard_URL' : "https://nova.friendycar.com/borrower-api/v1/dashboard",
        'Borrower_URL' : "https://nova.friendycar.com/borrower-api/v1/contracts?page=1&per_page=10",
        "email": email1,
        "password": password1,
    },
    {
        'API' : "Corporate DEV",
        'Login_URL' : "https://nova.friendyboat.com/api/login",
        'DashBoard_URL' : "https://nova.friendyboat.com/borrower-api/v1/dashboard",
        'Borrower_URL' : "https://nova.friendyboat.com/borrower-api/v1/contracts?page=1&per_page=10",
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
    try:
        response = requests.get(URL,headers=vheaders).json()
        if 'message' in response:
            if response['message'] == "Dashboard Data":
                print("FriendyCar Corporate : DashBoard API passed successfully.")
            else:
                print("---------------------------------------------------------------------")
                print("ERROR! FriendyCar Corporate : DashBoard API faild, Please check your credentials.")
                print("---------------------------------------------------------------------")
        else:
            print("---------------------------------------------------------------------")
            print("ERROR! FriendyCar Corporate : Unexpected response from the Dashboard API.")
            print(response)
            print("---------------------------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------------------------")
        print("ERROR! ",error_msg(e))
        print("---------------------------------------------------------------------")

def Borrower_API(URL , access):
    access_token = access
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'corporate',
        'Content-Type': 'application/json'

    }
    try:
        response = requests.get(URL,headers=vheaders)
        if response.status_code == 200:
            print("FriendyCar Corporate : Borrower API passed successfully.")
        else:
            print("---------------------------------------------------------------------")
            print("ERROR! FriendyCar Corporate : Unexpected response from the Borrower API.")
            print(response)    
            print("---------------------------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------------------------")
        print("ERROR! ",error_msg(e))
        print("---------------------------------------------------------------------")

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
                access_token = response['data']['access_token']
                DashBoard_API(dashboard_url,access_token)
                Borrower_API(borrower_url,access_token)
            else:
                print("---------------------------------------------------------------------")
                print("ERROR! FriendyCar Corporate : Login API failed. Please check your credentials.")
                print("---------------------------------------------------------------------")
        else:
            print("---------------------------------------------------------------------")
            print("ERROR! FriendyCar Corporate : Unexpected response from the Login API.")
            print(response)
            print("---------------------------------------------------------------------")
    except requests.exceptions.ConnectionError as e:
        print("---------------------------------------------------------------------")
        print("ERROR! : Connection Error - Failed to connect to the server.")
        print("---------------------------------------------------------------------")
    except requests.exceptions.RequestException as e:
        print("---------------------------------------------------------------------")
        print("ERROR! : Request Exception - Something went wrong with the request.")
        print("---------------------------------------------------------------------")
    except json.JSONDecodeError as e:
        print("---------------------------------------------------------------------")
        print("ERROR! : JSON Decode Error - Failed to decode the response as JSON.")
        print("---------------------------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------------------------")
        print("ERROR! ",error_msg(e))
        print("---------------------------------------------------------------------")




def loop():
    for test_case in test_cases:
            try:
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
            except Exception as e:
                print("---------------------------------------------------------------------")
                print("ERROR! ",error_msg(e))
                print("---------------------------------------------------------------------")    
            
try:            
    start_time = time.time()            
    loop()  
    end_time = time.time() - start_time
    print(f"Test completed in {end_time:.2f} seconds")   
except Exception as e:
        print("---------------------------------------------------------------------")
        print("ERROR! ",error_msg(e))
        print("---------------------------------------------------------------------")       
  
