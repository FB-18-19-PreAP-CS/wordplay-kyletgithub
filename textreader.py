def read_file():
    with open("words.txt") as file:
        count = 0
        for line in file:
            for word in line.split():
                print(word)
    print(count)
    
def at_least():
    with open("words.txt") as file:
        for line in file:
            if len(line) >= 20:
                print(line)
                
def has_no_e(word):
    if 'e' not in word.lower():
        return True
    return False

def no_e():
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
    for letter in letters:
        if letter.lower() in word.lower():
            return False        
    return True

def counts_avoids():
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
    for letter in word.lower():
        if letter not in letters.lower():
            return False
    return True

def words_with_only(letters):
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if uses_only(word,letters):
                    print(word)
        
def uses_all(word,letters):
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
    count = 0
    with open("words.txt") as file:
        for line in file:
            for word in line.split():
                if uses_all(word,letters):
                    count += 1
    print(count)


        

if __name__ == "__main__":
    how_many_uses_all('aeiou')