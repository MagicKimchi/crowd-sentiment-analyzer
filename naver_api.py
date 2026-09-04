import os
import requests
from dotenv import load_dotenv

load_dotenv()

def naverSearch(Filtered_data):

    keyword = Filtered_data[0]
    dateInfo = Filtered_data[1]

    url = "https://naverapihub.apigw.ntruss.com/search-trend/v1/search"

    headers = {
    "X-NCP-APIGW-API-KEY-ID": os.getenv('Client_ID'),
    "X-NCP-APIGW-API-KEY": os.getenv('Client_Secret'),
    "Content-Type": "application/json"
    }

    body = {
        "startDate": dateInfo[0],
        "endDate": dateInfo[2],
        "timeUnit": dateInfo[1],
        "keywordGroups": [
            {
                "groupName": "사용자 검색어",
                "keywords": [keyword]
            },
        ],
        "device": "pc",
    }

    r=requests.post(
        url,
        headers=headers,
        json=body
    )

    response=r.json()

    return response