import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    # make the get request
    response = requests.get(url)

    # check if it is successful status_coe == 200
    if response.status_code == 200:
        data = response.json()  # convert text to dict
        print(f"Current User Id : {data['userId']}")
        print(f"Current user title: {data['title']}")
        print(f"Has Completed : {data['completed']}")
    else:
        print("Failed to get data")

# only catches connecion error
except requests.exceptions.RequestException:
    print("Internet connection failed!")

# catches other errors like code bugs
except Exception as e:
    print(f"An error occured in the logic {e}")
