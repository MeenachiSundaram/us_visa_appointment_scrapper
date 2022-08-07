# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from re import sub
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from creds import (
    sendgrid_api,
    sendgrid_to_emails,
    sendgrid_from_email,
    sendgrid_subject,
)

os.environ["SENDGRID_API_KEY"] = sendgrid_api


def send_email(sendgrid_email_content):
    message = Mail(
        from_email=sendgrid_from_email,
        to_emails=sendgrid_to_emails,
        subject=sendgrid_subject,
        # html_content=sendgrid_html_content,
        plain_text_content=sendgrid_email_content,
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
        return response
    except Exception as e:
        return e.message


if __name__ == "__main__":
    # Testing
    print('Sending a test message.')
    response = send_email('This is a Test')
    print(response.status_code)
    print(response.body)
    print(response.headers)
