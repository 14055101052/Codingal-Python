test_dic = {
    "Codingal" : 2,
    "is" : 2,
    "best" : 2,
    "for" : 2,
    "Coding" : 1
}
print("The orginal dictionary : " +str(test_dic))

K = 2
res = 0

for key in test_dic :
    if test_dic[key] == K :
        res = res + 1
print("The frequency of K : " +str(res))



country_code = {
    "India" : "0091",
    "Australia" : "0025",
    "Nepal" : "00977"
}

print("The country code of India : ")
print(country_code.get("India" , "Not Found"))

print("The country code of Japan : ")
print(country_code.get("Japan" , "Not Found"))