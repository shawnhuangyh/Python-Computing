import time

if __name__ == '__main__':

    word_list = []
    # result = []

    start = time.time()

    with open("words.txt") as f:
        for line in f:
            word_list.append(line.strip('\n'))

    word_set = set(word_list)

    for word in word_list:
        reversed_word = word[::-1]
        if reversed_word != word and reversed_word in word_set:
            print(word + " " + reversed_word)
    # result.append((word, reversed_word))

    # for word in result:
    #     print(*word)

    end = time.time()

    print(str(end - start))
