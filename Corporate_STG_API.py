import requests
import json
import os 

Login_URL = "https://beta.friendycar.com/api/login"
email = os.environ.get('USERNAME1')
password = os.environ.get('PASSWORD1')


def DashBoard_API(URL):
    access_token = '716|A420x6yljFiqaMpeAxb4nKiazPgC1R5jmoslP5Cq'
    vheaders = {
        "Authorization": f"Bearer {access_token}",
        'accept': 'application/json',
        'app-type': 'corporate',
        'Content-Type': 'application/json'

    }
    response = requests.get(URL,headers=vheaders).json()
    if 'message' in response:
        if response['message'] == "Dashboard Data":
            print("FriendyCar Corporate : DashBoard API passed successfully.")
        else:
            print("FriendyCar Corporate : DashBoard API faild, Please check your credentials.")
    else:
        print("FriendyCar Corporate : Unexpected response from the Dashboard API.")
        print(response)

def Borrower_API(URL):
    access_token = '722|zeRTQWoD5E5gnFzgkfr6Kdc1IT2lHYhwZMWkrCyr'
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

def Login_API(URL):
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
        response = requests.post(URL, json=Login_Data, headers=vheaders).json()
        if 'message' in response:
            if response['message'] == "Logged successfully!.":
                print("FriendyCar Corporate STG : Login API Passed successfully.")
            else:
                print("FriendyCar Corporate STG : Login API failed. Please check your credentials.")
        else:
            print("FriendyCar Corporate STG: Unexpected response from the Login API.")
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
