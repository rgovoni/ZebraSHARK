import hashlib
import urllib


def gravatar_url(email):
    size = 40

    url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    url += urllib.urlencode({'s': str(size)})
    return url
