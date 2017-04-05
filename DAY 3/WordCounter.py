
def word_counter():
    sentence = str(input('Please enter sentence : '))
    word_list = sentence.split()
    words = {}
    for word in word_list:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    for key, value in sorted(words.items()):
        print(key, value)

