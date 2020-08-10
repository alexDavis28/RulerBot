import json
with open("config.json") as file:
    data = json.load(file)

token = data["BOT_TOKEN"]
prefix = data["BOT_PREFIX"]
activity = data["DEFAULT_ACTIVITY_MESSAGE"]
