import re
import sys
from urllib.request import urlopen


def url_hook(url):
    if not url.startswith(("http", "https")):
        raise ImportError
    with urlopen(url) as page:
        data = page.read.decode("UTF-8")
    filenames = re.findall("[a-zA-Z][z-zA-Z0-0]*.py", data)
    modnames = {name[:3] for name in filenames}
    return URLFinder(url, modnames)


print(sys.path_hooks.append(url_hook))