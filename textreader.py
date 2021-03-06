def read_file():
    with open("words.txt") as file:
        count = 0
        for line in file:
            for word in line.split():
                print(word)
    print(count)
    
def at_least():
    ''' prints all words that are at least 20 characters long
    '''
    with open("words.txt") as file:
        for line in file:
            if len(line) >= 20:
                print(line)
                
def has_no_e(word):
    ''' returns true if the word has no e in it and false otherwise
    '''
    if 'e' not in word.lower():
        return True
    return False

def no_e():
    ''' prints the percentage of words that don\'t have e
    '''
    with open("words.txt") as file:
        count = 0
        wcount = 0
        for line in file:
            wcount += 1
            if has_no_e(line):
                count += 1
    pct = count/wcount
    print(f"{pct*100:.3f}%")
    
def avoids(word,letters):
    ''' takes a word and a string of letters and returns true if the word avoids those letters
        returns false otherwise
    '''
    for letter in letters:
        if letter.lower() in word.lower():
            return False        
    return True

def counts_avoids():
    ''' counts the amount of words that avoid a given string of letters
    '''
    print("Enter the letters you want to avoid split by commas: ")
    letters = input('> ')
    llist = letters.split(',')
    with open("words.txt") as file:
        count = 0
        for line in file:
            if avoids(line,llist):
                count += 1
    print(count)
    
def uses_only(word,letters):
    ''' returns true if the word uses each given letter
    '''
    for letter in word.lower():
        if letter not in letters.lower():
            return False
    return True

def words_with_only(letters):
    ''' prints the words that use only the given letters
    '''
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if uses_only(word,letters):
                    print(word)
        
def uses_all(word,letters):
    ''' returns true if the word uses every given letter at least once
    '''
    count = 0
    req = len(letters)
    for letter in letters:
        if letter in word:
            count += 1
    if count == req:
        return True
    else:
        return False
    
def how_many_uses_all(letters):
    '''counts the amount of words that uses every given letter once
    '''
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if uses_all(word,letters):
                    count += 1
    print(count)

def is_abecedarian(word):
    ''' returns true if the word\'s letters are in alphabetical order and false otherwise
    '''
    if len(word) == 1:
        return True
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            return False
    return True

def count_abecedarian():
    ''' counts the amount of abecedarian words
    '''
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if is_abecedarian(word):
                    count += 1
    print(count)

if __name__ == "__main__":
    count_abecedarian()