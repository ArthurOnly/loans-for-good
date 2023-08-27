import requests


class CreditApiFacade:
    url = "https://loan-processor.digitalsys.com.br/api/v1/loan/"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    def __init__(self, url=None):
        if url:
            self.url = url

    def verify_credit(self, data):
        response = requests.post(self.url, data=self._parse_data(data), headers=self.headers)
        approved = response.json().get("approved", False) == True
        return approved
    
    def _parse_data(self, data):
        try:
            return {
                "name": data["name"],
                "document": data["document"],
            }
        except KeyError:
            raise ValueError("Missing required fields (name or document)")