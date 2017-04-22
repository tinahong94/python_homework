words = input("Print a series of string: ")

def reverse_order(n):
    new_words = n.split()
    new_words.reverse()
    new_words_string = ' '.join(new_words)
    return (new_words_string)

print(reverse_order(words))