def double_letters():
    ''' prints all words that have 3 consectutive pairs of double letters
    '''
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                for i in range(len(word)-5):
                    if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
                        print(word)
                        
if __name__ == "__main__":
    double_letters()
    