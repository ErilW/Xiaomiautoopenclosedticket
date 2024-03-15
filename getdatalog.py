import requests
import time

previous_data = None

url ='https://reqres.in/api/users'
data = \
{
    "name": "asd",
    "job": "asdasdas"
}

while True:
    getdata = requests.get('https://reqres.in/api/users?page=2',
    data={"key": "value"},
    headers={"Content-Type": "application/json"},
    )
    print(getdata.json())
    time.sleep(2)

    postdata = requests.post(url,json=data
    )
    # print(postdata.json())
    # time.sleep(2)
    current_data = getdata.json()

    if previous_data is not None and current_data != previous_data:
        print("mesin bermasalah ")
    else:
        print("mesin aman")
    
    previous_data = current_data
    







    