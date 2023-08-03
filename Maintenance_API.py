import requests
import json
import time
import os 
email1 = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')


test_cases = [
    {
        'API' : "Maintenance",
        'Login_URL' : "https://nova.friendycar.com/api/login",
        'DashBoard_URL' : "https://nova.friendycar.com/maintenance-api/v1/dashboard",
        'Upcoming_URL' : "https://nova.frievndycar.com/maintenance-api/v1/maintenances?status=Upcoming&page=1&per_page=10&date_filter_type",
        'History_URL' : "https://nova.friendycar.com/maintenance-api/v1/maintenances?status=History&page=1&per_page=10&date_filter_type",
        'dashboard_access' : '799|1ETWkHmr8EVOALNsfgWSTSizOptKrc4NLNHLm7o7',
        'history_access' : '799|1ETWkHmr8EVOALNsfgWSTSizOptKrc4NLNHLm7o7',
        'upcoming_access' : '799|1ETWkHmr8EVOALNsfgWSTSizOptKrc4NLNHLm7o7',
        "email": email1,
        "password": password,
    },
    {
        'API' : "Maintenance STG",
        'Login_URL' : "https://beta.friendycar.com/api/login",
        'DashBoard_URL' : "https://beta.friendycar.com/maintenance-api/v1/dashboard",
        'Upcoming_URL' : "https://beta.friendycar.com/maintenance-api/v1/maintenances?status=Upcoming&page=1&per_page=10&date_filter_type",
        'History_URL' : "https://beta.friendycar.com/maintenance-api/v1/maintenances?status=History&page=1&per_page=10&date_filter_typee",
        'dashboard_access' : '51|sUA935JiWC0hKaoHWc0upN7h6QRf43GGVoVA4xMV',
        'history_access' : '51|sUA935JiWC0hKaoHWc0upN7h6QRf43GGVoVA4xMV',
        'upcoming_access' : '51|sUA935JiWC0hKaoHWc0upN7h6QRf43GGVoVA4xMV',
        "email": email1,
        "password": password,
    },
    {
        'API' : "Maintenance DEV",
        'Login_URL' : "https://nova.friendyboat.com/api/login",
        'DashBoard_URL' : "https://nova.friendyboat.com/maintenance-api/v1/dashboard",
        'Upcoming_URL' : "https://nova.friendyboat.com/maintenance-api/v1/maintenances?status=Upcoming&page=1&per_page=10&date_filter_type",
        'History_URL' : "https://nova.friendyboat.com/maintenance-api/v1/maintenances?status=History&page=1&per_page=10&date_filter_type",
        'dashboard_access' : '1182|ceG5cLWG5IlJCVP9iTRzbuG0SUB09EE9VLOozxyv',
        'history_access' : '1182|ceG5cLWG5IlJCVP9iTRzbuG0SUB09EE9VLOozxyv',
        'upcoming_access' : '1182|ceG5cLWG5IlJCVP9iTRzbuG0SUB09EE9VLOozxyv',
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
    response = requests.get(URL,headers=vheaders).json()
    if 'message' in response:
        if response['message'] == "Dashboard Data":
            print("FriendyCar Maintenance : DashBoard API passed successfully.")
        else:
            print("FriendyCar Maintenance : DashBoard API faild, Please check your credentials.")
    else:
        print("FriendyCar Corporate : Unexpected response from the Dashboard API.")
        print(response)


def History_API(URL,access):
    access_token = access
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'maintenance',
        'Content-Type': 'application/json'

    }
    response = requests.get(URL,headers=vheaders)
    if response.status_code == 200:
        print("FriendyCar Maintenance : History API passed successfully.")
    else:
        print("FriendyCar Maintenance : Unexpected response from the History API.")
        print(response)      

def Upcoming_API(URL,access):
    access_token = access
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'maintenance',
        'Content-Type': 'application/json'

    }
    response = requests.get(URL,headers=vheaders)
    if response.status_code == 200:
        print("FriendyCar Maintenance : Upcoming API passed successfully.")
    else:
        print("FriendyCar Maintenance : Unexpected response from the Upcoming API.")
        print(response)    

def Login_API(email,password,login_url,dashboard_url,upcoming_url,dashboard_access,history_url,history_access,upcoming_access):
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
                DashBoard_API(dashboard_url,dashboard_access)
                Upcoming_API(upcoming_url,upcoming_access)
                History_API(history_url,history_access)
            else:
                print("FriendyCar Maintenance : Login API failed. Please check your credentials.")
        else:
            print("FriendyCar Maintenance: Unexpected response from the Login API.")
            print(response)
    except requests.exceptions.ConnectionError as e:
        print("Error: Connection Error - Failed to connect to the server.")
    except requests.exceptions.RequestException as e:
        print("Error: Request Exception - Something went wrong with the request.")
    except json.JSONDecodeError as e:
        print("Error: JSON Decode Error - Failed to decode the response as JSON.")
    except Exception as e:
        print("An unexpected error occurred.")
        print(e)        


def loop():
    for test_case in test_cases:
            api_name = test_case['API']
            login_url = test_case['Login_URL']
            dashboard_url = test_case['DashBoard_URL']
            upcoming_url = test_case['Upcoming_URL']
            history_url = test_case['History_URL']
            dashboard_access = test_case['dashboard_access']
            history_access = test_case['history_access']
            upcoming_access = test_case['upcoming_access']
            email = test_case['email']
            password = test_case['password']
            print(f"Testing API : {api_name}")
            Login_API(email,password,login_url,dashboard_url,upcoming_url,dashboard_access,history_url,history_access,upcoming_access)
            
start_time = time.time()            
loop()  
end_time = time.time() - start_time
print(f"Test completed in {end_time:.2f} seconds")    







