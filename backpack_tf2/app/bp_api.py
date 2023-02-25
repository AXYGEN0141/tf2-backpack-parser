from backpack_tf2.app.bp_acc import Account
from backpack_tf2.app.entities import ListingObject
from backpack_tf2.app.helpers import del_multiple_keys, pop_multiple_keys
from backpack_tf2.app.listings_repo import ListingsRepository
from backpack_tf2.app import misc
from typing import Optional
import urllib.parse
import json
import requests
import hashlib
import time


class Backpack:
    """Backpack class is responsible for interaction with Backpack.tf API."""

    def __init__(self, acc: Account, result: dict):
        self.acc = acc
        self.result = result

    def search_classifieds(self,
                           intent: Optional[str] = "dual",
                           page_size: Optional[int] = 10,
                           fold: Optional[int] = 0,
                           quality: Optional[int] = 5,
                           particle: Optional[str] = 13,
                           page: Optional[int] = 1,
                           slot: Optional[str] = "misc",
                           class_: Optional[str] = "",
                           item: Optional[str] = "",
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
        :param item: Filter listings by item name.
        :return: dict of filtered classifieds
        """
        payload = {"key": self.acc.api_key,
                   "intent": intent,
                   "page": page,
                   "page_size": page_size,
                   "fold": fold,
                   "quality": quality,
                   "particle": particle,
                   "slot": slot,
                   "class": class_,
                   "item": item,
                   }

        encoded = urllib.parse.urlencode(payload)

        r = requests.get("https://backpack.tf/api/classifieds/search/v1?" + encoded)
        jsondata = json.loads(r.text)

        return jsondata

    def get_all_classifieds(self, page_size: Optional[int] = 10,
                            class_: str = "", item: Optional[str] = "", particle: Optional[int] = 13):
        unusual_repo = ListingsRepository()
        page_to_parse = 1
        classifieds = self.search_classifieds(page=page_to_parse, page_size=page_size,
                                              class_=class_, item=item, particle=particle)
        repeat = classifieds["sell"]["total"]
        while repeat > 0:
            classifieds = self.search_classifieds(page=page_to_parse, page_size=page_size,
                                                  class_=class_, item=item, particle=particle)
            for listing in classifieds["sell"]["listings"]:
                pop_multiple_keys(listing, ["automatic", "promoted"])
                del_multiple_keys(listing, ["appid", "offers", "buyout", "created", "bump", "intent"])
                listing_id = listing.pop('id', None)
                md5_hash = hashlib.md5(json.dumps(listing, sort_keys=True).encode('utf-8')).hexdigest()
                listing_instance = ListingObject(
                    listing_id=listing_id,
                    data_md5=md5_hash,
                    data=listing
                )

                db_record = unusual_repo.get_by_filter({"data_md5": listing_instance.data_md5})
                if db_record is not None:
                    pass
                else:
                    unusual_repo.create(listing_instance)
                repeat -= 1
            page_to_parse += 1

    def get_unusual_classifieds_by_effect(self, page_size: Optional[int] = 10, particle: int = 13):
        self.get_all_classifieds(page_size=page_size, class_="scout,soldier,pyro", particle=particle)
        self.get_all_classifieds(page_size=page_size, class_="demoman,heavy,engineer", particle=particle)
        self.get_all_classifieds(page_size=page_size, class_="medic,sniper,spy", particle=particle)
        for item in misc.all_class_hats:
            self.get_all_classifieds(page_size=30, item=item, particle=particle)
            time.sleep(1)
