# import requests
# import pybase64
# import json
# from secrets import GORGIAS_TICKET_ID 
# from secrets import GORGIAS_CUSTOMER_ID 
# from secrets import GORGIAS_API
# from secrets import GORGIAS_STORE_NAME
# from secrets import GORGIAS_CUSTOMER_EMAIL



# # def pull_ticket_id():
# #pass through a first name 
# #if first name matches api call of first name
# #return that first name's id number 

# def pull_customer_id(customer_email):
#     url = f"https://{GORGIAS_STORE_NAME}.gorgias.com/api/tickets"

#     querystring = {"per_page":"30","page":"1"}

#     headers = {
#         "Accept": "application/json",
#         "Authorization": f"Basic {GORGIAS_API}"
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)
#     # print(response.text)

#     data = json.loads(response.text)
#     for id in data['data']:
#         if id['requester']['email'] == customer_email:
#             print(id['requester']['id'])

# pull_customer_id('dev@lifebydam.com')



def some_function():
    print("hello world")

def new_function():
    some_function()