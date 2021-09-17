# Search Engine

text = input ('Enter your text:')
word = input ('Enter your word:')

def search (text, word):
    if word in text:
        print('Word found')
    else:
        print ('Word not found')

search (text, word)