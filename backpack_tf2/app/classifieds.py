from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import urllib.parse
import json
import requests


class Account:
    def __init__(self, client_id, client_secret, api_key):
        self.api_key = api_key
        self.client_id = client_id
        self.client_secret = client_secret

        # Gets The Token
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(
            token_url="https://backpack.tf/oauth/access_token",
            client_id=self.client_id,
            client_secret=self.client_secret,
        )

        self.token = token

    # This function searches for classified listings
    #
    # intent - either sell, buy, or both
    # page_size - the results / page 0 < page_size <= 30
    # page - the page number you want to view
    # fold - if set 0 disables listing folding
    # item_name - the name of the item you want to search for
    # steamid - the steam id of the user who you want to check their listings
    # tradable - 0/1
    # craftable - 0/1
    # australium - 0/1
    # wear_tier - 1-5 for tier of skin wear, in order - factory new, minimal wear, field-tested, well-worn, battle scared
    # texture_name - required to search by wear_tier, the name of the skin / texture to search by
    # quality - the integer of the quality to search by use MiscUtils.qualityStringToInt("unique") to get it
    # paint - the paint's ID to search by, TODO: add a function to find the paint ID
    # particle - particle ID effect, TODO: add a function to find the particle ID from string
    # killstreak_tier - 1-3, in order standard, specialized, professional
    # sheen - 0-7, in order team shine, deadly daffodil, manndarin, mean green, agonizing emerald, villainous violet, hot rod
    # killstreaker - the id of the killstreaker
    #
    def search_classifieds(
        self,
        intent="sell",
        page_size=30,
        fold=1,
        item_name="",
        steamid="",
        tradable="",
        craftable="",
        australium="",
        wear_tier="",
        quality="",
        paint="",
        particle="",
        killstreak_tier="",
        sheen="",
        killstreaker="",
        page=0,
        texture_name="",
        slot="",
    ):
        payload = {
            "key": self.api_key,
            "intent": intent,
            "texture_name": texture_name,
            "page": str(page),
            "page_size": str(page_size),
            "fold": str(fold),
            "item": item_name,
            "steamid": str(steamid),
            "tradable": str(tradable),
            "craftable": str(craftable),
            "australium": str(australium),
            "wear_tier": str(wear_tier),
            "quality": str(quality),
            "paint": str(paint),
            "particle": str(particle),
            "killstreak_tier": str(killstreak_tier),
            "sheen": str(sheen),
            "killstreaker": str(killstreaker),
            "slot": str(slot)
        }

        encoded = urllib.parse.urlencode(payload)

        r = requests.get("https://backpack.tf/api/classifieds/search/v1?" + encoded)
        jsondata = json.loads(r.text)

        return jsondata
