import os
import urllib.request

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

        stop_words_text = stopwords_file_to_read.read()

    for word in stop_words_text:

        harry_text_to_use.replace(word, '')

    non_alpha_numerical = '!@#&()."–[{]}:;,?/*`~$^+=<>\''

    for char in non_alpha_numerical:

        print(char)
        harry_text_to_use.replace(char, ' ')

    return harry_text_to_use


text = get_harry_most_common_word()
print(text)