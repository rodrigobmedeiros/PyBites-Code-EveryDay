import os
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)

def get_harry_most_common_word():
    
    with open(harry_text, 'r', encoding='utf8') as harry_file:

        harry_text_to_use = harry_file.read()

    with open(stopwords_file, 'r', encoding='utf8') as stopwords_file_to_read:

        stop_words_text = stopwords_file_to_read.readlines()

    stop_words_text = [word.strip().strip('\n') for word in stop_words_text]

    for word in stop_words_text:

        harry_text_to_use = harry_text_to_use.replace(word.strip('\n'), ' ')

    non_alpha_numerical = '!@#&()."–[{]}:;,?/*`~$^+=<>\'-“”—’'

    for char in non_alpha_numerical:

        harry_text_to_use = harry_text_to_use.replace(char, ' ')

    harry_text_to_use = harry_text_to_use.split()
    harry_text_to_use = [word.strip('\n').strip() for word in harry_text_to_use]
    harry_text_to_use = [word for word in harry_text_to_use if word not in ['', 't', 's', 'd', 'w', 'n', 'ng', 'r', 'h', 'th', 'nd', 'l', 'll', 've', 'He']]
    harry_text_to_use = [word.lower() for word in harry_text_to_use if word not in 'abcdefghijklmnopqrstuvxyw']

    cnt = Counter(harry_text_to_use)

    return cnt.most_common(1)[0]


text = get_harry_most_common_word()
print(text)