# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram():
    # [assignment] Add your code here
    word1= input("input first string :")
    word2 = input("input second string :")

    if(sorted(word1)== sorted(word2)):
      return True
    else:
        return False


find_anagram()



