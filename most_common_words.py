def answer(paragraph, k):
    word_map = {}
    final = []

    words = paragraph.split(" ")
    for i in range(len(words)):
        if words[i] not in word_map:
            word_map[words[i]] = 1
        else:
            word_map[words[i]] += 1

    while k > 0:
        if len(word_map) < 1:
            return final

        greatest = None
        number = 0

        for key, value in word_map.iteritems():
            if greatest is None or number < value:
                greatest = key
                number = value

        del word_map[greatest]
        final.append(greatest)
        k -= 1

    return final

print(str(answer("I am a dog a dog dog", 5)))