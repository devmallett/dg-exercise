import requests
import pybase64
import json
from secrets import GORGIAS_TICKET_ID 
from secrets import GORGIAS_CUSTOMER_ID 
from secrets import GORGIAS_API
from secrets import GORGIAS_STORE_NAME
from secrets import GORGIAS_CUSTOMER_EMAIL


class SendMessage:
    def __init__(self ,ticket_id ,customer_id ,customer_name ,api_key,store_name ,customer_email ,ticket_message): 
        self.ticket_id = ticket_id
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.api_key = api_key
        self.store_name = store_name
        self.ticket_message = ticket_message
        self.header = {}
        
        
    def pull_customer_id(self):
        url = f"https://{GORGIAS_STORE_NAME}.gorgias.com/api/tickets"

        querystring = {"per_page":"30","page":"1"}

        headers = {
            "Accept": "application/json",
            "Authorization": f"Basic {GORGIAS_API}"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        # print(response.text)

        data = json.loads(response.text)
        for id in data['data']:
            if id['requester']['email'] == self.customer_email:
                print(id['requester']['id'])
    
    
    def make_request(self):
        
        url = f"https://{self.store_name}.gorgias.com/api/tickets/{self.ticket_id}/messages"
        
        payload = {
            "receiver": {
                "email": self.customer_email,
                "id": self.customer_id
            },
            "source": {
                "to": [
                    {
                        "address": self.customer_email,
                        "name": self.customer_name
                    }
                ],
                "from": {
                    "address": "v9417g10z2konr6m@emails.gorgias.com",
                    "name": "Devin's Help Desk"
                },
                "type": "email"
            },
            "body_text": self.ticket_message,
            "from_agent": True,
            "channel": "email",
            "via": "api"
        }
        
        self.header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_key}"
        }
        response = requests.request("POST", url, json=payload, headers=self.header)
        # print(url)
        # print(payload)
        # print(response.text)
        # return (response.text)
        print(response.text)
        # print(self.ticket_message)


new_message = SendMessage(GORGIAS_TICKET_ID ,GORGIAS_CUSTOMER_ID , "Dmalzzzz" ,GORGIAS_API ,GORGIAS_STORE_NAME ,GORGIAS_CUSTOMER_EMAIL ,'This is with encoded api call')
# new_message.make_request()
new_message.pull_customer_id()
        
        