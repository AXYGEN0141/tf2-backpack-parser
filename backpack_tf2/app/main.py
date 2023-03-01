from backpack_tf2.app.bp_acc import Account
from backpack_tf2.app.bp_api import Backpack
import time

from backpack_tf2.app.config import BACKPACK_API_KEY, CLIENT_ID, CLIENT_SECRET

acc = Account(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, api_key=BACKPACK_API_KEY
)
bp = Backpack(acc=acc)


def main():
    start_time = time.time()
    # bp.get_unusual_classifieds_by_effect(page_size=30, particle=13)
    bp.get_collectors_classifieds()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
