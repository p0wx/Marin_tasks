def tokenize(text, sentence=False):
    if sentence:
        tokens = set(text.split('.'))
    else:
        tokens = set(text.split(' '))

    return tokens


def main():
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
              Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
              Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    
    print('split as sentence')
    tokens = tokenize(text, sentence=True)
    print(tokens)

    print('split as words')
    tokens = tokenize(text)
    print(tokens)
    

if __name__ == "__main__":
    main()
