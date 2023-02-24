from backpack_tf2.app.classifieds import Account

from backpack_tf2.app.config import (
    BACKPACK_API_KEY,
    CLIENT_ID,
    CLIENT_SECRET
)

acc = Account(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, api_key=BACKPACK_API_KEY)


def main():
    first = acc.get_class_unusual_classifieds(page_size=30, class_="scout,soldier,pyro")
    second = acc.get_class_unusual_classifieds(page_size=30, class_="demoman,heavy,engineer")
    third = acc.get_class_unusual_classifieds(page_size=30, class_="medic,sniper,spy")
    print(first+second+third)


if __name__ == "__main__":
    main()
