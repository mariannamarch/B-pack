def read_file(filename):
    with open(filename, encoding='UTF-8') as f:
        script = f.readlines()
    return script

def lines_to_words(script):
    words = []
    for line in script:
        if ':' in line:
            name, phrase = line.split(':', maxsplit= 1)
            words.extend(phrase.split()) 
    return words
    
def main():
    script = read_file('episode1.txt')
    words = lines_to_words(script)
    print(words)

if __name__ == '__main__':
    main()
    
