#!/usr/bin/env python

import requests
import json
from .creds import pd_api_key, pd_from, pd_service_id

# Update to match your API key
API_KEY = pd_api_key
SERVICE_ID = pd_service_id
FROM = pd_from


def trigger_incident(pd_title, pd_details):
    """Triggers an incident via the V2 REST API using sample data."""

    url = "https://api.pagerduty.com/incidents"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.pagerduty+json;version=2",
        "Authorization": "Token token={token}".format(token=API_KEY),
        "From": FROM,
    }

    payload = {
        "incident": {
            "type": "incident",
            "title": pd_title,
            "service": {"id": SERVICE_ID, "type": "service_reference"},
            "incident_key": pd_title+pd_details,
            "body": {"type": "incident_body", "details": pd_details},
        }
    }

    r = requests.post(url, headers=headers, data=json.dumps(payload))

    print("Status Code: {code}".format(code=r.status_code))
    print(r.json())


if __name__ == "__main__":
    trigger_incident()
