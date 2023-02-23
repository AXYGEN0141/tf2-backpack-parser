from backpack_tf2.app.classifieds import Account

from backpack_tf2.app.config import (
    BACKPACK_API_KEY,
    CLIENT_ID,
    CLIENT_SECRET
)

acc = Account(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, api_key=BACKPACK_API_KEY)


def main():
    classifieds_result = acc.search_classifieds(intent="sell", quality=5, particle=13, page_size=30, page=1, slot="misc")


if __name__ == "__main__":
    main()
