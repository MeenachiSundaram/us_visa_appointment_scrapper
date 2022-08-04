import requests
from creds import token, chat_id


def send_message(text, chat_id=chat_id, notification=False):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    parameters = {
        'chat_id': chat_id,
        'text': text, 
        'disable_notification': notification
    }
    return requests.post(url, parameters)


def send_photo(photo_file,chat_id=chat_id, notification=False):
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    parameters = {
        'chat_id': chat_id,
        'disable_notification': notification
    }
    return requests.post(url, parameters, files={'photo': photo_file})


if __name__ == "__main__":
    # Testing
    import json
    import pprint as pp

    # print('Sending a test message.')
    # response = send_message('Testing')
    # response_json = json.loads(response.text)
    # assert response_json['ok']
    # print('Results:')
    # pp.pprint(response_json)

    with open('archive/test.jpg', 'rb') as f:
        response = json.loads(send_photo(f).text)
    assert response['ok']
    pp.pprint(response)