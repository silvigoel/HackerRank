def find_sub_string(index, string):    
    for entry in range(index, len(string)):
        yield(string[index:entry+1])

def get_score(wordList, string):
    score = 0
    for entry in wordList:        
        score += string.count(entry)
        print("{0} : {1}".format(entry, string.count(entry)))
    print("{0} : {1}".format(wordList, score))
    return score
    
def minion_game(string):
    scores = {
        "Stuart" : 0,
        "Kevin" : 0 
    }
    
    choice = {
        "vowel" : ["Kevin"],
        "consonant" : ["Stuart"]
    }
    
    vowels = ['A','E','I','O','U']
    
    char_details = {}
    
    for char in string:
        if char not in char_details.keys():
            char_details[char] = string.index(char)
            
    for user in scores.keys():
        print("User {0} in progress...".format(user))
        wordsList = []
        
        if user in choice["vowel"]:
            choiceID = 'v'
        else:
            choiceID = 'c'
        
        if choiceID == 'v':
            for char,index in char_details.items():
                if char in vowels:
                    for entry in find_sub_string(index, string):
                        wordsList.append(entry)
        else:
            for char,index in char_details.items():
                if char not in vowels:
                    for entry in find_sub_string(index, string):
                        wordsList.append(entry)
                        
        scores[user] = get_score(wordsList, string)
        
        
        
        
