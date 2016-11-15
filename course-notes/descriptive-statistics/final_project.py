import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')


deck = []
suits = ['spade', 'heart', 'club', 'diamond']
faces = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


for s in suits:
    i = 0
    while i < len(faces):
        d = {}
        d['Suit'] = s
        d['Face'] = faces[i]
        d['Value'] = values[i]
        deck.append(d)
        i += 1

df = pd.DataFrame(deck)
print(len(df))


df.plot.hist(alpha=0.5)
plt.title("Card Values", fontsize=14)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Count", fontsize=12)
# plt.show()
plt.savefig('original52.png', bbox_inches='tight')

pick = df.sample(n=3)
print(pick)
print(pick.sum(0))

def sample(sample_size):
    sample = []
    i = 0
    while i < sample_size:
        pick3 = df.sample(n=3)
        sample.append(pick3.sum(0))
        i += 1
    return pd.DataFrame(sample)

sample500 = sample(500)
sample30 = sample(30)

print(sample500.head())
print(sample500.describe())
print(sample500.mode())
print(sample500.sem())
print(sample500.var())
print(sample500.mad())

sample500.plot.hist(alpha=0.5)
plt.title("500 Samples of Sum of 3 Randomly Drawn Cards", fontsize=14)
plt.xlabel("Sum Value", fontsize=12)
plt.ylabel("Count", fontsize=12)
# plt.show()
plt.savefig('sample500.png', bbox_inches='tight')

print('\n\n')
print(sample30.tail())
print(sample30.describe())
print(sample30.mode())
print(sample30.sem())
print(sample30.var())
print(sample30.mad())

sample30.plot.hist(alpha=0.5)
plt.title("30 Samples of Sum of 3 Randomly Drawn Cards", fontsize=14)
plt.xlabel("Sum Value", fontsize=12)
plt.ylabel("Count", fontsize=12)
# plt.show()
plt.savefig('sample30.png', bbox_inches='tight')
