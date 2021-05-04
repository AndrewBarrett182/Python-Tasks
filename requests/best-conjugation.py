import requests

response = requests.get('http://www-personal.umich.edu/~jlawler/wordlist')
wordlist = (response.text).split()

word = input("Please enter a word: ")
letters = list(word)
foundwords = []
while len(letters) != 0:
    temp = []
    for i in range(len(letters)):
        temp.append(letters[i])
        string = ''.join(temp)
        if (string in wordlist) and (string not in foundwords):
            foundwords.append(string)
    letters.pop(0)
count = len(foundwords)
print(f"{count} subwords found: {', '.join(foundwords)}")