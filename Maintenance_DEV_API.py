import requests
import json
import os


Login_URL = "https://nova.friendyboat.com/api/login"
Dashboard_URL = "https://nova.friendyboat.com/maintenance-api/v1/dashboard"
Upcoming_URL = "https://nova.friendyboat.com/maintenance-api/v1/maintenances?status=Upcoming&page=1&per_page=10&date_filter_type"
History_URL = "https://nova.friendyboat.com/maintenance-api/v1/maintenances?status=History&page=1&per_page=10&date_filter_type"
email1 = os.environ.get('USERNAME')
password1 = os.environ.get('PASSWORD')
def DashBoard_API(URL):
    access_token = '1182|ceG5cLWG5IlJCVP9iTRzbuG0SUB09EE9VLOozxyv'
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'maintenance',
        'Content-Type': 'application/json'

    }
    response = requests.get(URL,headers=vheaders).json()
    if 'message' in response:
        if response['message'] == "Dashboard Data":
            print("FriendyCar Maintenance DEV : DashBoard API passed successfully.")
        else:
            print("FriendyCar Maintenance DEV : DashBoard API faild, Please check your credentials.")
    else:
        print("FriendyCar Maintenance DEV : Unexpected response from the Dashboard API.")
        print(response)


def History_API(URL):
    access_token = '1182|ceG5cLWG5IlJCVP9iTRzbuG0SUB09EE9VLOozxyv'
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'maintenance',
        'Content-Type': 'application/json'

    }
    response = requests.get(URL,headers=vheaders)
    if response.status_code == 200:
        print("FriendyCar Maintenance DEV : History API passed successfully.")
    else:
        print("FriendyCar Maintenance DEV : Unexpected response from the History API.")
        print(response)      

def Upcoming_API(URL):
    access_token = '1182|ceG5cLWG5IlJCVP9iTRzbuG0SUB09EE9VLOozxyv'
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'maintenance',
        'Content-Type': 'application/json'

    }
    response = requests.get(URL,headers=vheaders)
    if response.status_code == 200:
        print("FriendyCar Maintenance DEV : Upcoming API passed successfully.")
    else:
        print("FriendyCar Maintenance DEV : Unexpected response from the Upcoming API.")
        print(response)    

def Login_API(URL):
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
        response = requests.post(URL, json=Login_Data, headers=vheaders).json()
        if 'message' in response:
            if response['message'] == "Logged successfully!.":
                print("FriendyCar Maintenance DEV : Login API Passed successfully.")
                DashBoard_API(Dashboard_URL)
                Upcoming_API(Upcoming_URL)
                History_API(History_URL)
            else:
                print("FriendyCar Maintenance DEV : Login API failed. Please check your credentials.")
        else:
            print("FriendyCar Maintenance DEV : Unexpected response from the Login API.")
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


Login_API(Login_URL)
