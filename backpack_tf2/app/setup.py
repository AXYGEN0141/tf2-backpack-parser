import pymongo
from backpack_tf2.app.config import MONGODB_IP, MONGODB_PORT, MONGO_DB_NAME
from discord_webhook import DiscordWebhook

db_connect = pymongo.MongoClient(MONGODB_IP, MONGODB_PORT)

db = db_connect[MONGO_DB_NAME]

burning_flames_content = "New classified listing with Burning Flames Hat"
scorching_flames_content = "New classified listing with Scorching Flames Hat"
purple_energy_content = "New classified listing with Purple Energy Hat"
green_energy_content = "New classified listing with Green Energy Hat"
sunbeams_content = "New classified listing with Sunbeams Hat"
collector_content = "New classified listing with Collector's item"

burning_flames_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1080793973867679784/o4IpLdATMXIyOUSlSLcfho6_hJZyyeyJYkxkT7aGukEES8zAiYCBuqnmTLV_X9Oi8Unf", content=burning_flames_content)
scorching_flames_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1080794561141542932/7Ek7FbBFuaEhwxTNFkt7WH84Xk8s4vc9VCyu3F_h5ODpHA5c0PBsntgFd2Mzvi1NGJJ7", content=scorching_flames_content)
purple_energy_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1080794716465012836/dtqG9xik-szkjSkmMo1Ugidh1Xe9w-OdnDn95KrtLDHZnW84LRVCsn3n-ENlEe8qd5sk", content=purple_energy_content)
green_energy_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1080794899684786267/Vqj3D2XQcase1IJFWfhPBIgkbv3CGqv9PkwPaKPApXsPNsNCiR1hjEJ_NDxI9SBiyz8I", content=green_energy_content)
sunbeams_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1080794993712709682/CwGxjmZRfFD5jyVjDkoFT72e5GAaRfrrr-VaQJzetr2VQgQK2E8ppGP9ZANuNvWHxqMH", content=sunbeams_content)
collector_webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1080795383095103558/ExxvQ8cHUgZNJkZMqqfOZwXRbMGsKmR25FZlVoJ0Q6EOJ3bZyt7YCdonevoB9Mj91qD2", content=collector_content)
