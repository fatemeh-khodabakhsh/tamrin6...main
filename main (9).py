def calculate_distance(word1,word2):
    diff = abs(len(word2) - len(word1))

    if len(word1) < len(word2):
        word1 += '_' * diff
    else:
        word2 += '_' * diff

    distance = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            distance += 1
    return distance


n = int(input())
sentence = input()
keyword = input()
sentence = sentence.replace(".", "").replace("،", "").replace(":", "")
for word in sentence.split():
    if calculate_distance(keyword, word) <= n:
        print(word)


