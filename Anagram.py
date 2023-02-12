#------------------------------------------------------------------------------ 
#  Adam Wu
#  Anagram.py
#  A program to help me win when playing the game anagram (game pigeon)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# definitions of required functions (and other structures, if any)
#------------------------------------------------------------------------------

def norm(s):
   """
   Returns the norm of a string obtained by alphabetizing its characters.
   """
   return "".join(sorted(s))
# end norm()

def AnagramDictionary(f):
   """
   Returns a dictionary whose keys are the norms of the words in file f, and 
   whose values are lists of words with a given norm. Thus each list contains
   a group of words in f that are anagrams of each other.
   """
   d = dict()

   for line in f:
      word = line.strip()
      sorted_word = norm(word)
      if sorted_word not in d:
         d[sorted_word] = [word]
      else:
         d[sorted_word].append(word)
   return d
# end AnagramDictionary()

def printWordList(L):
   """Prints the words in L on a single line, separated by commas."""
   if L == None:
      print()
      return None
   else:
      for i in range(len(L)):
         if i == len(L)-1:
            print(L[i])
         else:
            print(L[i], end=", ")
# end printWordList()

#------------------------------------------------------------------------------
# definition of function main()
#------------------------------------------------------------------------------
def main():
   print()
   # open a word file, assemble the dictionary using words, close file
   fin = open("scrabble.txt")
   Assembly_dic = AnagramDictionary(fin)
   fin.close() # always close file once done with it, this is a good habit

   # repeatedly get input from user, and query the dictionary
   while True:
      # get a string from the user
      word = input("Enter a string (or nothing to quit): ")
      norm_word = norm(word)

      # look up string in the dictionary, print its anagrams if they exist
      if word == "":
         print("\nBye!\n")
         break
      elif Assembly_dic.get(norm_word) == None:
         print()
         print("The letters in '"+word+"' do not form a word in the dictionary")
         printWordList(Assembly_dic.get(norm_word))
      else:
         print("\nThe anagrams of", word, "are:")
         printWordList(Assembly_dic.get(norm_word))
         print()
   # end while
# end main()
# end

#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end

   