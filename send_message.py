import requests
from secrets import GORGIAS_URL 
from secrets import GORGIAS_USER_ID 
from secrets import GORGIAS_PASSWORD 
        
def makeRequest(ticket_id ,user_id ,text ,password):
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
            "body_text": text,
            "from_agent": True,
            "channel": "email",
            "via": "api"
        }
    headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": password
        }
        
        
        
        
        
    response = requests.request("POST", url, json=payload, headers=headers)
    return (response.text)
    
        
        
    
    
print(makeRequest(GORGIAS_URL ,GORGIAS_USER_ID  ,"This is some rad stuff if it works" , GORGIAS_PASSWORD))
    
