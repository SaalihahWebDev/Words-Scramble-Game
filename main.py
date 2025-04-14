import random
words=["rat","pat","pot","hen","sun"]
word=random.choice(words)
scrambled=''.join(random.sample(word, len(word)))
print("🧿🧿🧿🧿🧿Welcome to Word Scramble!")
print("Can you guess the word? Scrambled Word: {}".format(scrambled))
for attempt in range(3):
    guess=input(f"Attempt {attempt+1}: ").lower()
    if guess==word:
        print("🎉🎉🎉Correct,You guessed the word")
        break
    else:
        print("Try Again")
else:
    print(f"Out of trys,The answer is {word}")