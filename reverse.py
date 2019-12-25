text = str(input ("Введіть текст"))
sentence = text [::-1]
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print (sentence_rev)
