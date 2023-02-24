from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from typing import Optional
import urllib.parse
import json
import requests


class Account:
    """
    Account class is responsible for initiating OAuth2 connection and implementing operations related to classifieds.
    """
    def __init__(self, client_id, client_secret, api_key):
        self.api_key = api_key
        self.client_id = client_id
        self.client_secret = client_secret

        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(
            token_url="https://backpack.tf/oauth/access_token",
            client_id=self.client_id,
            client_secret=self.client_secret,
        )
        self.token = token

    def search_unusual_classifieds(self,
                                   intent: Optional[str] = "dual",
                                   page_size: Optional[int] = 10,
                                   fold: Optional[int] = 0,
                                   quality: Optional[int] = 5,
                                   particle: Optional[int] = 13,
                                   page: Optional[int] = 1,
                                   slot: Optional[str] = "misc",
                                   class_: Optional[str] = ""
                                   ):
        """
        :param intent: Filter listings by intent. Default: dual. Valid options: sell, buy, dual. Takes str as input
        :param page_size: Modify the page size used to paginate. Must be >= 1 and <= 30.
        Use the "page" parameter to paginate. Default: 10. Takes int as input
        :param fold: If set to 0, disables listing folding. Takes int as input
        :param quality: Filters listings by quality of item. Takes int as input
        (e.g. unusual quality converts to value of 5).
        :param particle: Filter listings by particle ID. Takes int as input.
        (e.g. burning flames particle converts to value of 13). Read more --> https://backpack.tf/developer/particles.
        :param page: The page number you want to view. Takes int as input
        :param slot: Filter listings by slot (e.g.: misc, )
        :param class_: Filter listings by TF2 classes (e.g.: scout,soldier,pyro etc). P.S. Write without spaces
        :return: dict of filtered classifieds
        """
        payload = {"key": self.api_key,
                   "intent": intent,
                   "page": page,
                   "page_size": page_size,
                   "fold": fold,
                   "quality": quality,
                   "particle": particle,
                   "slot": slot,
                   "class": class_
                   }

        encoded = urllib.parse.urlencode(payload)

        r = requests.get("https://backpack.tf/api/classifieds/search/v1?" + encoded)
        jsondata = json.loads(r.text)

        return jsondata

    def get_class_unusual_classifieds(self, page_size: Optional[int] = 10, class_: str = ""):
        page_to_parse = 1
        classifieds_res = self.search_unusual_classifieds(page=page_to_parse, page_size=page_size, class_=class_)
        repeat = classifieds_res["sell"]["total"]
        count_page = 1
        while repeat > 0:
            classifieds_res = self.search_unusual_classifieds(page=page_to_parse, page_size=page_size, class_=class_)
            for listing in classifieds_res["sell"]["listings"]:
                repeat -= 1
                print(listing)
            page_to_parse += 1
            print(count_page)
            count_page += 1
        return count_page
