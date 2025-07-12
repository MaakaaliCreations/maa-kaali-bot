import requests

icons = {
    "instagram": "ff0069",
    "youtube": "ff0000",
    "facebook": "1877f2",
    "x": "1da1f2",
    "pinterest": "e60023",
    "threads": "000000"
}

for name, color in icons.items():
    url = f"https://cdn.simpleicons.org/{name}/{color}/png"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{name}.png", "wb") as f:
            f.write(response.content)
        print(f"Downloaded {name}.png")
    else:
        print(f"Failed to download {name}") 