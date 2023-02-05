def emojis():
    sentence=input(">")
    words=sentence.split(' ')
emojis={
    ":)":"😀",
    ":(":"😥",
    "<3":"❤️",

}
output=""
for word in emojis:
    output+=emojis.get(word, word) + " "
print(output)