# Utils/Config.py
import json
import os

CONFIG_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config.json"
)


def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)


def get_allowed_channels(guild_id):
    config = load_config()
    return config.get("allowed_channels", {}).get(str(guild_id), [])


def add_allowed_channel(guild_id, channel_id):
    config = load_config()
    if "allowed_channels" not in config:
        config["allowed_channels"] = {}
    gid = str(guild_id)
    if gid not in config["allowed_channels"]:
        config["allowed_channels"][gid] = []
    if channel_id not in config["allowed_channels"][gid]:
        config["allowed_channels"][gid].append(channel_id)
    save_config(config)


def remove_allowed_channel(guild_id, channel_id):
    config = load_config()
    gid = str(guild_id)
    if gid in config.get("allowed_channels", {}):
        if channel_id in config["allowed_channels"][gid]:
            config["allowed_channels"][gid].remove(channel_id)
    save_config(config)
