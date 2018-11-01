def read_file():
    with open("words.txt") as file:
        count = 0
        for line in file:
            count += 1
    print(count)
    
def at_least():
    with open("words.txt") as file:
        for line in file:
            if len(line) >= 20:
                print(line)
                
def has_no_e(word):
    if 'e' not in word:
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
    print(count/wcount * 100)
    
def avoids(word,letters):
    for letter in letters:
        if letter in word:
            return False        
    return True

def counts_avoids():
    print("Enter the letters you want to avoid: ")
    letters = input('> ')
    list = letters.split(',')
    with open("words.txt") as file:
        count = 0
        for line in file:
            if avoids(line,list):
                count += 1
    print(count)


        

if __name__ == "__main__":
    pass