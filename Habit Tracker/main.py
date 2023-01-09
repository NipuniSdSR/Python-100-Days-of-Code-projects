import requests

USERNAME = "nipuni"
TOKEN = "qwert4878673ncvbsd"
# Todo: Step1-Creating a user account in pixela
# Need to run only once
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json= user_params)
# # since we donot expect any output,checking only the post has successful
# print(response.text)

# Todo: Step 2- Create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"
graph_config = {
    "id": graph_id,
    "name": "Coding Time graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",
}

# without token the POST command not working. to give the token as hidden input use headers.
# headers will not appear in the http address
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Todo: Step 3- Get the graph
"""
browse : https://pixe.la/v1/users/nipuni/graphs/graph1.html
"""

# Todo:  step 4- Post value to the graph,pixel data
graph_pixel_endpoint = f"{graph_endpoint}/{graph_id}"
import datetime as dt

date = dt.date.today().strftime("%Y%m%d")
hr = 5
pixel_data = {
    "date": date,
    "quantity": f"{hr * 60}"
}
# response = requests.post(url=graph_pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# ----------adding data to next step---------------#
# code_hours = [6, 4, 8, 1, 0.5, 4]
# for i, hr in enumerate(code_hours):
#     date = (dt.date.today() - dt.timedelta(days=i+1)).strftime("%Y%m%d")
#
#     print(date)
#     pixel_data = {
#         "date": date,
#         "quantity":f"{hr*60}"
#     }
#     response = requests.post(url=graph_pixel_endpoint, json=pixel_data, headers=headers)
#     print(response.text)


# Todo:  step 5- update/delete a pixel
"""
put: update 
delete: delete
"""
# Todo: update
pixel_update = {
    "quantity": "120",
}

update_date = (dt.date.today() - dt.timedelta(days=3)).strftime("%Y%m%d")
pixel_update_endpoint = f"{graph_pixel_endpoint}/{update_date}"
# response = requests.put(url=pixel_update_endpoint, json=pixel_update, headers=headers)
# print(response.text)

# todo: delete
pixel_delete_endpoint = pixel_update_endpoint
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)