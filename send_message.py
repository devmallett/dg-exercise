import requests
from secrets import GORGIAS_TICKET_ID 
from secrets import GORGIAS_CUSTOMER_ID 
from secrets import GORGIAS_API 
# from secrets import GORGIAS_ACCOUNT_EMAIL
        
def makeRequest(ticket_id ,user_id ,message_text ,password):
    url = f"https://dmalzzzstore.gorgias.com/api/tickets/{ticket_id}/messages"
    
    payload = {
            "receiver": {
                "email": "mallettdev@gmail.com",
                "id": user_id
            },
            "source": {
                "to": [
                    {
                        "address": "mallettdev@gmail.com",
                        "name": "Dmalzzzz"
                    }
                ],
                "from": {
                    "address": "v9417g10z2konr6m@emails.gorgias.com",
                    "name": "Devin's Help Desk"
                },
                "type": "email"
            },
            "body_text": message_text,
            "from_agent": True,
            "channel": "email",
            "via": "api"
        }
    headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Basic {password}"
        }
        
        
        
        
        
    response = requests.request("POST", url, json=payload, headers=headers)
    return (response.text)
    
        
        
    
    
print(makeRequest(GORGIAS_TICKET_ID ,GORGIAS_CUSTOMER_ID  ,"This is the newest test" , GORGIAS_API))
    
