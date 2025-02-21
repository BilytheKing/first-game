words = ['Sky',
'Tree',
'Moon',
'Book',
'Light',
'River',
'Magic',
'Smile',
'Ocean',
'Peace']

import random

word = random.choice(words)
n_word = '_ ' * len(word)

guess = input("Bir harf tahmin edin: ").upper()
while len(guess) != 1 or not guess.isalpha():
    guess = input("Lütfen tek bir harf girin: ").upper()

print(n_word)