letter_counts = {}
for letter in "Mississippim":
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

print(letter_counts)

letter_items = list(letter_counts.items())
letter_items.sort()
print(letter_items)
