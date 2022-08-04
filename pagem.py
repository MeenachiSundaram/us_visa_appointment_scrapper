import requests
from creds import pagem_api_key, pagem_app_id


def send_page(page_text):
    url = "https://www.pagem.com/api/v2/page/send"
    payload=f"id={pagem_app_id}&message={page_text}"
    headers = {
    'authentication': pagem_api_key,
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
