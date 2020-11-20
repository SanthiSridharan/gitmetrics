import requests
import json
import time




headers = {
    'Authorization': "Bearer 2f1ba89577f0a05cf5fd2a21b3f5f9604c688c9ac",
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }
rooturl = "https://api.github.com/repos/twitter/twemoji/pulls?state='closed'&page="
page = 1

while True:

    url = rooturl + str(page)
    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200 :

        final_dictionary = json.loads(response.text)
        #print(final_dictionary[0].keys())
        if len(final_dictionary) == 0  :
            print(len(final_dictionary))
            break;
        else:
            print("I am not breaking")
            print(len(final_dictionary))

            # 'created_at', 'updated_at', 'closed_at', 'merged_at'
            prnumber = [ i['number'] for i in final_dictionary]
            createdat = [ i['created_at'] for i in final_dictionary]
            mergedat = [ i['merged_at'] for i in final_dictionary]
            prstate = [ i['state'] for i in final_dictionary]
            closedat = [ i['closed_at'] for i in final_dictionary]
            print(createdat)
            print(prnumber)
            print(prstate)
            print(mergedat)

            page = page + 1
    if response.status_code == 401 :
            time.sleep(20)
