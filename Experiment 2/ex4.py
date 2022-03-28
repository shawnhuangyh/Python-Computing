def get_reduced(word):
    reduced_set = set()
    for n in range(len(word)):
        reduced = word[:n] + word[n + 1:]
        if reduced in word_set and reduced not in failed_word:
            reduced_set.add(reduced)
    return reduced_set


def is_reducible(word):
    global max_len, max_len_word
    if len(word) > 1:
        for reduced in get_reduced(word):
            if reduced in succeed_word or is_reducible(reduced) is True:
                break
        else:
            failed_word.add(word)
            return False
    succeed_word.add(word)
    if len(word) > max_len:
        max_len = len(word)
        max_len_word = word
    return True


if __name__ == '__main__':
    word_set = {'i', 'a'}
    failed_word = set()
    succeed_word = set()
    max_len = 0
    max_len_word = str()

    with open("words.txt") as f:
        for line in f:
            word_set.add(line.strip('\n'))

    for i in word_set:
        is_reducible(i)

    print(succeed_word)
    print("Max length reducible word is " + max_len_word + ", its length is " + str(max_len))
