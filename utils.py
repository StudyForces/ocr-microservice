import requests


def download_image(session: requests.Session, url: str, path: str) -> bool:
    r = session.get(url, stream=True)
    if r.status_code == 200:
        with open(path, "wb") as f:
            f.write(r.content)
        return True
    return False
