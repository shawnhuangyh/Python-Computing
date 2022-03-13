import string
from collections import Counter

if __name__ == '__main__':
    print("(1)")
    word_list = []
    with open("timemachine.txt") as f:
        text = f.read().split()

    for word in text:
        word_list.append(word.strip(string.punctuation).lower())
    counter_words = Counter(word_list)

    for word in word_list:
        print(word + " : " + str(counter_words[word]))

    print("\n\n\n(2)")

    with open("keyword.txt") as fb:
        keyword = fb.read().split()

    for word in keyword:
        print(word + " : " +str(counter_words[word]))
