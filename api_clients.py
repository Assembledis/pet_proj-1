import requests


class APIClient:
    def __init__(self,base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0'})

    def get(self,path, **kwargs):
        return self.session.get(f"{self.base_url}{path}", **kwargs)
    def post(self,path, **kwargs):
        return self.session.post(f"{self.base_url}{path}", **kwargs)
    def put(self,path, **kwargs):
        return self.session.put(f"{self.base_url}{path}", **kwargs)
    def delete(self,path, **kwargs):
        return self.session.delete(f"{self.base_url}{path}", **kwargs)
    def patch(self,path, **kwargs):
        return self.session.patch(f"{self.base_url}{path}", **kwargs)


