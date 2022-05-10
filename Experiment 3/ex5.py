import re


def rotateword(strsrc, n):
    des = [chr((ord(i) + n - ord("a")) % 26 + ord("a")) if i.islower() else chr((ord(i) + n - ord("A")) % 26 + ord("A"))
           for i in strsrc]
    strdes = "".join(des)
    return strdes


def avoids(word, ban):
    word = word.lower()
    ban = ban.lower()
    regex = re.compile("[%s]" % ban)
    if regex.search(word):
        return True
    else:
        return False


def useonly(word, allow):
    word = word.lower()
    allow = allow.lower()
    regex = re.compile("[^%s]" % allow)
    if regex.search(word):
        return False
    else:
        return True


def useall(word, allow):
    word = word.lower()
    allow = allow.lower()
    regex = re.compile("[^%s]" % word)
    if regex.search(allow):
        return False
    else:
        return True


def hasnoe(word):
    word = word.lower()
    regex = re.compile("[e]")
    if regex.search(word):
        return False
    else:
        return True


def isabecedarian(word):
    word = word.lower()
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    else:
        return True


if __name__ == '__main__':
    # rotateword
    print("Rotate 'Test': {}".format(rotateword("Test", 10)))

    # avoids function
    print("=========================================================================================")
    print("Is 't' in 'Test': {}".format(avoids("Test", "t")))
    print("Is 'b' in 'Test': {}".format(avoids("Test", "b")))

    # useonly
    print("=========================================================================================")
    print("Is 'Test' only use 'tes': {}".format(useonly("Test", "tes")))
    print("Is 'Test' only use 'ts': {}".format(useonly("Test", "ts")))

    # useall
    print("=========================================================================================")
    print("Is 'Test' use all 'tes': {}".format(useall("Test", "tes")))
    print("Is 'Test' use all 'tsa': {}".format(useall("Test", "tsa")))
    print("All word use 'aeiou' in words.txt:")
    with open("words.txt") as f:
        text = f.read().split()
    for i in text:
        if useall(i, "aeiou"):
            print(i, end=" ")
    print()

    # hasnoe
    print("=========================================================================================")
    print("Does 'Test' have no 'e': {}".format(hasnoe("Test")))
    print("Does 'Might' have no 'e': {}".format(hasnoe("Might")))
    total = 0
    havee = 0
    for i in text:
        total += 1
        if hasnoe(i):
            havee += 1
    print("Percentage: {}".format(havee / total))

    # isabecedarian
    print("=========================================================================================")
    print("Is 'Test' abecedarian: {}".format(isabecedarian("Test")))
    print("Is 'Abcde' abecedarian: {}".format(isabecedarian("Abcde")))
    for i in text:
        if isabecedarian(i):
            print(i, end=" ")
    print()
