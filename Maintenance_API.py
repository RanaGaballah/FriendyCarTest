import requests
import json
import time
import os 
email1 = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

def error_msg(exeption):
    errorMsg = str(exeption)
    error_lines = errorMsg.split('\n')
    for line in error_lines[:2]:
            return line

test_cases = [
    {
        'API' : "Maintenance",
        'Login_URL' : "https://nova.friendycar.com/api/login",
        'DashBoard_URL' : "https://nova.friendycar.com/maintenance-api/v1/dashboard",
        'Upcoming_URL' : "https://nova.friendycar.com/maintenance-api/v1/maintenances?status=Upcoming&page=1&per_page=10&date_filter_type",
        'History_URL' : "https://nova.friendycar.com/maintenance-api/v1/maintenances?status=History&page=1&per_page=10&date_filter_type",
        "email": email1,
        "password": password,
    },
    {
        'API' : "Maintenance STG",
        'Login_URL' : "https://beta.friendycar.com/api/login",
        'DashBoard_URL' : "https://beta.friendycar.com/maintenance-api/v1/dashboard",
        'Upcoming_URL' : "https://beta.friendycar.com/maintenance-api/v1/maintenances?status=Upcoming&page=1&per_page=10&date_filter_type",
        'History_URL' : "https://beta.friendycar.com/maintenance-api/v1/maintenances?status=History&page=1&per_page=10&date_filter_typee",
        "email": email1,
        "password": password,
    },
    {
        'API' : "Maintenance DEV",
        'Login_URL' : "https://nova.friendyboat.com/api/login",
        'DashBoard_URL' : "https://nova.friendyboat.com/maintenance-api/v1/dashboard",
        'Upcoming_URL' : "https://nova.friendyboat.com/maintenance-api/v1/maintenances?status=Upcoming&page=1&per_page=10&date_filter_type",
        'History_URL' : "https://nova.friendyboat.com/maintenance-api/v1/maintenances?status=History&page=1&per_page=10&date_filter_type",
        "email": email1,
        "password": password,
    },
]


def DashBoard_API(URL,access):
    access_token = access
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'maintenance',
        'Content-Type': 'application/json'

    }
    try:
        response = requests.get(URL,headers=vheaders).json()
        if 'message' in response:
            if response['message'] == "Dashboard Data":
                print("FriendyCar Maintenance : DashBoard API passed successfully.")
            else:
                print("---------------------------------------------------------------------")
                print("ERROR! FriendyCar Maintenance : DashBoard API faild, Please check your credentials.")
                print("---------------------------------------------------------------------")
        else:
            print("---------------------------------------------------------------------")
            print("ERROR! FriendyCar Corporate : Unexpected response from the Dashboard API.")
            print("---------------------------------------------------------------------")
            print(response)
    except Exception as e:
        print("---------------------------------------------------------------------")
        print("ERROR! ",error_msg(e))
        print("---------------------------------------------------------------------")

def History_API(URL,access):
    access_token = access
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'maintenance',
        'Content-Type': 'application/json'

    }
    try:
        response = requests.get(URL,headers=vheaders)
        if response.status_code == 200:
            print("FriendyCar Maintenance : History API passed successfully.")
        else:
            print("---------------------------------------------------------------------")
            print("ERROR! FriendyCar Maintenance : Unexpected response from the History API.")
            print("---------------------------------------------------------------------")
            print(response) 
    except Exception as e:
        print("---------------------------------------------------------------------")
        print("ERROR! ",error_msg(e))
        print("---------------------------------------------------------------------")

def Upcoming_API(URL,access):
    access_token = access
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'maintenance',
        'Content-Type': 'application/json'

    }
    try:
        response = requests.get(URL,headers=vheaders)
        if response.status_code == 200:
            print("FriendyCar Maintenance : Upcoming API passed successfully.")
        else:
            print("---------------------------------------------------------------------")
            print("ERROR! FriendyCar Maintenance : Unexpected response from the Upcoming API.")
            print(response)    
            print("---------------------------------------------------------------------")
    except Exception as e:
        print("---------------------------------------------------------------------")
        print("ERROR! ",error_msg(e))
        print("---------------------------------------------------------------------")
def Login_API(email,password,login_url,dashboard_url,upcoming_url,history_url):
    Login_Data = {
        "email": email,
        "password": password
    }

    vheaders = {
        'accept': 'application/json',
        'app-type': 'maintenance',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(login_url, json=Login_Data, headers=vheaders).json()
        if 'message' in response:
            if response['message'] == "Logged successfully!.":
                print("FriendyCar Maintenance : Login API Passed successfully.")
                access_token = response['data']['access_token']
                DashBoard_API(dashboard_url,access_token)
                Upcoming_API(upcoming_url,access_token)
                History_API(history_url,access_token)
            else:
                print("---------------------------------------------------------------------")
                print("ERROR! FriendyCar Maintenance : Login API failed. Please check your credentials.")
                print("---------------------------------------------------------------------")
        else:
            print("---------------------------------------------------------------------")
            print("ERROR! FriendyCar Maintenance: Unexpected response from the Login API.")
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
        print("ERROR! An unexpected error occurred.")
        print(e)      
        print("---------------------------------------------------------------------")


def loop():
    for test_case in test_cases:
        try:
            api_name = test_case['API']
            login_url = test_case['Login_URL']
            dashboard_url = test_case['DashBoard_URL']
            upcoming_url = test_case['Upcoming_URL']
            history_url = test_case['History_URL']
            email = test_case['email']
            password = test_case['password']
            print(f"Testing API : {api_name}")
            Login_API(email,password,login_url,dashboard_url,upcoming_url,history_url)
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







