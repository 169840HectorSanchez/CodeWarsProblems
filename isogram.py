def is_isogram(string):
    myString = list(string.lower()) #first lower all to make it easier
    if len(myString) != len(set(myString)): #compare set to original
        return False #diferent then false
    else: 
        return True #same then true
    