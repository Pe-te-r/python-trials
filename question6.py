#Write a program that counts the number of vowels in a sentence.

def check_vowel(sentence):
    vowels=['a','e','i','o','u']

    sentence=sentence.lower()

    counter=0

    for char in sentence:
        if char in vowels:
            counter += 1
    
    return counter


print("Enter the sentense to count the number of vowels from\n")
sentense=input('>> ')
print(f'Total vowels: {check_vowel(sentense)}')
print()