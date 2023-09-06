phrase = "There's no dark side in the moon really. Matter of fact, it's all dark..."
phrase = phrase.lower()
howManyAs = phrase.count('a')
firstA = phrase.find('a')
lastA = phrase.rfind('a')

print("How many 'a': {}".format(howManyAs))
print("First 'a' in: {}".format(firstA + 1))
print("Last 'a' in: {}".format(lastA + 1))