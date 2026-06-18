class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time = O(m*nlogn) , Space = O(m*n), m = len(strs) , n = longest word
        # anagrams = defaultdict(list)
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     anagrams[sorted_word].append(word)
        # return list(anagrams.values())


        # Time = O(m*n) , Space = O(m*n), m = len(strs) , n = longest word
        anagrams = defaultdict(list) 
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')] +=1
            
            anagrams[tuple(count)].append(word)
        
        return list(anagrams.values())

