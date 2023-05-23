def find_longest_word(sentence: str) -> str:
    longest_word = ''
    for word in sentence.split(' '):
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


if __name__ == '__main__':
    n = int(input())
    sentence = input()
    word = find_longest_word(sentence)
    print(word)
    print(len(word))
