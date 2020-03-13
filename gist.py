import requests
import json
import base64
import argparse

debug = False
api_url = "https://api.github.com/gists"
token = ""
header = {"Authorization": "token " + token}


def create_gist(filename, content):
    global header, api_url
    d = {
        "description": "None",
        "public": True,
        "files": {filename: {"content": content,},},
    }
    r = requests.post(api_url, headers=header, data=json.dumps(d))
    data = json.loads(r.text)
    if debug:
        print(data)
        print(data["files"][filename]["raw_url"])
    return data


def update_gist(id, filename, content):
    global header, api_url
    url = api_url + "/" + id
    d = {
        "description": "None",
        "public": True,
        "files": {filename: {"content": content,},},
    }
    r = requests.post(url, headers=header, data=json.dumps(d))
    data = json.loads(r.text)
    if debug:
        print(data)
        print(data["files"][filename]["raw_url"])
    return data


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("filename", help="filename to upload")
    parse.add_argument("-n", help="specify the filename to use")
    parse.add_argument("-b", action="store_true", help="base64 encode")
    args = parse.parse_args()
    if debug:
        print(args)
    with open(args.filename, "rb") as f:
        byte = f.read()
    if args.b:
        content = base64.b64encode(byte)
    else:
        content = byte.decode()
    if args.n:
        filename = args.n
    else:
        filename = args.filename
    data = create_gist(filename, content)
    print(data["files"][filename]["raw_url"])


# update_gist("ba252326a093f63a328dda5e0621de1c", "test", "bbbbbbb")

