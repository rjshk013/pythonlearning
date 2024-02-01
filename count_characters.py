def wordcounter(word):
    alpha_counter=0
    numeric_counter=0
    symbol_counter=0
    whitespace_counter=0
    
    for char in word:
        if char.isalpha():
            alpha_counter += 1
        elif char.isdigit():
            numeric_counter += 1
        elif char.isspace():
            whitespace_counter += 1
        else:
            symbol_counter += 1
            
    print("No of albhabets: {}".format(alpha_counter))
    print("No of digits: {}".format(numeric_counter))
    print("No of spaces: {}".format(whitespace_counter))
    print("No of symbols: {}".format(symbol_counter))

given_word = "python   %%%%%%^  2387559"
wordcounter(given_word)
