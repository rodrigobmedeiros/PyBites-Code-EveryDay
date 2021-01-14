import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
tempfile = os.path.join('tmp')

urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    
    tree = ET.parse(tempfile)
    root = tree.getroot()
    channel = root[0]

    items = channel.findall('item')
    print(len(items))

    list_of_tags = []

    for item in items:

        categories = item.findall('category')

        for category in categories:

            list_of_tags.append(category.text.lower())

    
    cnt = Counter(list_of_tags, )
    return cnt.most_common(10)

print(get_pybites_top_tags(n=10))