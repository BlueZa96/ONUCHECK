import requests
from django.conf import settings

def onu_api_call_get(url):
    try:
        response = requests.get(
            url,
            headers={"Authorization": f"Bearer {settings.ONU_API_KEY}"}
        )
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        raise Exception(f"Error fetching ONU data: {e}")