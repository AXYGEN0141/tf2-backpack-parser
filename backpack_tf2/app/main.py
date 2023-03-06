from backpack_tf2.app.bp_acc import Account
from backpack_tf2.app.bp_api import Backpack
from backpack_tf2.app.setup import (burning_flames_webhook,
                                    scorching_flames_webhook,
                                    purple_energy_webhook,
                                    green_energy_webhook,
                                    sunbeams_webhook,
                                    collector_webhook)
import time

from backpack_tf2.app.config import BACKPACK_API_KEY, CLIENT_ID, CLIENT_SECRET

acc = Account(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, api_key=BACKPACK_API_KEY
)
bp = Backpack(acc=acc)


def main():
    bp.get_collectors_classifieds(page_size=30)  # Getting all collector weapons
    bp.get_unusual_classifieds_by_effect(page_size=30, particle="13")  # Getting all unusuals with Burning Flames
    bp.get_unusual_classifieds_by_effect(page_size=30, particle="14")  # Getting all unusuals with Scorching Flames
    bp.get_unusual_classifieds_by_effect(page_size=30, particle="10")  # Getting all unusuals with Purple Energy
    bp.get_unusual_classifieds_by_effect(page_size=30, particle="9")  # Getting all unusuals with Green Energy
    bp.get_unusual_classifieds_by_effect(page_size=30, particle="17")  # Getting all unusuals with Sunbeams

    bp.get_collectors_classifieds(discord_webhook=collector_webhook, page_size=30)
    print("FINISH COLLECTORS")
    bp.get_unusual_classifieds_by_effect(discord_webhook=burning_flames_webhook, page_size=30, particle="13")
    print("FINISH BURNING")
    bp.get_unusual_classifieds_by_effect(discord_webhook=scorching_flames_webhook, page_size=30, particle="14")
    print("FINISH SCORCHING")
    bp.get_unusual_classifieds_by_effect(discord_webhook=purple_energy_webhook, page_size=30, particle="10")
    print("FINISH PURPLE")
    bp.get_unusual_classifieds_by_effect(discord_webhook=green_energy_webhook, page_size=30, particle="9")
    print("FINISH GREEN")
    bp.get_unusual_classifieds_by_effect(discord_webhook=sunbeams_webhook, page_size=30, particle="17")
    print("FINISH SUNBEAMS")


if __name__ == "__main__":
    main()
