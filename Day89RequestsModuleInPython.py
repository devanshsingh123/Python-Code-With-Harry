# # The requests module in Python is one of the most popular libraries used to
# #  send HTTP requests easily and efficiently. It's a higher-level interface built
# #  on top of Python's built-in http.client module — designed to be more user-friendly,
# #  readable, and powerful.

# ✍️ Example: Simple GET Request

# import requests

# response = requests.get("https://api.github.com")

# print("Status Code:", response.status_code)
# print("Headers:", response.headers)
# print("JSON Response:", response.json())



# ✍️ Example: POST Request with JSON

# url = "https://httpbin.org/post"
# payload = {"name": "Alice", "age": 30}

# response = requests.post(url, json=payload)

# print("Response JSON:", response.json())


# 🛠️ Useful Features
# 🔸 Query Parameters

# params = {"search": "python", "limit": 5}
# requests.get("https://api.example.com/data", params=params)


# 🔸 Custom Headers

# headers = {"Authorization": "Bearer YOUR_TOKEN"}
# requests.get("https://api.example.com/data", headers=headers)


# 🔸 Handling Timeouts

# requests.get("https://api.example.com", timeout=5)


# 🔸 Upload Files

# files = {'file': open('myfile.txt', 'rb')}
# requests.post("https://httpbin.org/post", files=files)


# 📌 Response Object Attributes
# Attribute	Description
# .status_code	HTTP status code (e.g., 200, 404)
# .text	Response body as text
# .json()	Parses JSON response (if any)
# .headers	Dictionary of response headers
# .content	Raw binary content


#NEWSAPI Exercise

#APIKey:e8c34c7e51d6411b9ca1fa789ef51104

import requests

url = "https://newsapi.org/v2/top-headlines"

def get_topheadline(url,cn,apikey):

    param = {"country":cn,"apikey":apikey}

    response = requests.get(url,params= param)

    if response.status_code == 200:
        data = response.json()
        articles = data.articles
        print(articles)
    else:
        print("api call failed: ",response.status_code,response.text)




get_topheadline(url,'us','e8c34c7e51d6411b9ca1fa789ef51104')
