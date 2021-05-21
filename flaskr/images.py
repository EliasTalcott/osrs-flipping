"""Get images URLS from the OSRS Wiki"""

import re
import hashlib

###
## Append _detail before .png for high quality image
###

def wiki_image_url(filename):
    """
    Get image URL from OSRS Wiki
    :param filename: Image filename found in mapping
    :return: Image URL
    """
    filename = re.sub(' ', '_', filename)
    md5hash = hashlib.md5(filename.encode()).hexdigest()
    filename = re.sub('\\(', '%28', filename)
    filename = re.sub('\\)', '%29', filename)
    return f'https://oldschool.runescape.wiki/images/{md5hash[0:1]}/{md5hash[0:2]}/{filename}?7263b'
