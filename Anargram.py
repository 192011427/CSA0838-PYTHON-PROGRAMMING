class Solve():
   def Anagrams( self, li ):
       '''
       Function to Group Anagrams
       :param li: list of words
       :return: list of grouped anagrams
       '''
       dictionary = {}
       for word in li:
           sortedWord = ''.join(sorted(word))
           # If word is not in dictionary
           if sortedWord not in dictionary:
               dictionary[sortedWord] = [word]
           # If previously it is present that means its anagram
           # was previously present
           else:
               dictionary[sortedWord] += [word]
       return [dictionary[i] for i in dictionary]

if __name__ == '__main__':
   li = ["eat","tea","tan","ate","nat","bat"]
   # Call to function to Solve and group Anagrams
   print(Solve().Anagrams(li))
 
