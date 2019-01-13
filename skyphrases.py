from collections import Counter


def skyphrase_is_valid(skyphrase):
    counter = Counter(skyphrase.split())
    most_common = counter.most_common()[0][1]
    if most_common > 1:
        return False
    return True


def main():
    skyphrase_list = open('skychallenge_skyphrase_input.txt', 'r')
    valid_phrases_list = [line.rstrip() for line in skyphrase_list if skyphrase_is_valid(line.rstrip())]
    return "There are " + str(len(valid_phrases_list)) + " valid skyphrases"


print(main())
