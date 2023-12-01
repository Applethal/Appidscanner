import os
import requests

folderpath = 'AppList'
url = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'

params = {}

for filename in os.listdir(folderpath):
    if filename == 'NoQuestion.bin':
        break
    file_path = os.path.join(folderpath, filename)

    with open(file_path, 'r') as file:
        file_content = file.read().strip()

    print(f"File: {filename}\nGameID: {file_content}\n")

    params['appids'] = file_content

    response = requests.get(url, params=params)
    results = response.json()

    if 'applist' in results and 'apps' in results['applist']:
        apps = results['applist']['apps']
        if apps:
            for app in apps:
                if app.get('appid') == int(file_content):
                    app_name = app.get('name', "No game title found")
                    print(f"Game ID: {file_content}, Game Title: {app_name}")
                    break  
            else:
                print("No matching app ID found.")
        else:
            print("No search results found.")
    else:
        print("Invalid response from Steam API.")
