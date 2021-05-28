from aiohttp import ClientSession
from re import findall
from json import load, dump

def is_url(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = findall(regex, string)
    if url: return True
    else: return False

async def get_json(link, headers=None, json=True):
    async with ClientSession() as s:
        async with s.get(link, headers=headers) as resp:
            return await resp.json() if json else await resp.text()