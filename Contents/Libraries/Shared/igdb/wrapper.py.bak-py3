"""IGDB wrapper module for the api v4 with Apicalypse"""

from requests import post

API_URL = "https://api.igdb.com/v4/"

class IGDBWrapper:
    def __init__(self, client_id=None, auth_token=None):
        self.client_id = client_id
        self.auth_token = auth_token

    def api_request(self, endpoint=None, query=None):
        """
        Takes an endpoint and the Apicalypse query and returns the api response as a byte string.
        """
        url = IGDBWrapper._build_url(endpoint)
        params = self._compose_request(query)

        response = post(url, **params)
        response.raise_for_status()

        return response.content

    @staticmethod
    def _build_url(endpoint=''):
        return f'{API_URL}{endpoint}'

    def _compose_request(self, query=None):
        if not query:
            raise Exception('No query provided!\nEither provide an inline query following Apicalypse\'s syntax or an Apicalypse object')
       
        request_params = {
            'headers': {
                'Client-ID': self.client_id,
                'Authorization': f'Bearer {self.auth_token}',
            }
        }

        if isinstance(query, str):
            request_params['data'] = query
            return request_params

        raise TypeError('Incorrect type of argument \'query\', only Apicalypse-like strings or Apicalypse objects are allowed')
