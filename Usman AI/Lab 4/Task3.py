def sort_words_alphabetically(words):
   
    for i in range(len(words)):
        for j in range(0, len(words) - i - 1):
            if words[j] > words[j + 1]:
                
                words[j], words[j + 1] = words[j + 1], words[j]
    return words


text = input("Enter words separated by spaces: ")
words_list = text.split()
sorted_words = sort_words_alphabetically(words_list)
print("Sorted words:", ' '.join(sorted_words))
