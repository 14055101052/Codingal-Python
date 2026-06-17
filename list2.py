def match_words(words):
    count = 0
    lst = []
    for word in words :
        reverse = word[::-1]
        if word == reverse :
            count = count + 1
            lst.append(word)
    print("List of words with first and last letter same\n", lst)

count = match_words(["abc","cfc","xyz","1221"])


print("Words having first and last lettr same : ", count)
