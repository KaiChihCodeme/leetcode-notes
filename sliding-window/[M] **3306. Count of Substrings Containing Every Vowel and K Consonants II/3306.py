class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def countAtLeastMConsonants(m):
            l, r, ans = 0, 0, 0
            vowels = ('a', 'e', 'i', 'o', 'u')
            vowels_map = defaultdict(int)
            n_consonants = 0

            while l < len(word) or r < len(word):
                # process if match condition with at least m of consonants
                if len(vowels_map) == 5 and n_consonants >= m:
                    # calculate ans by this rule:
                    # https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/solutions/5846076/python3-o-n-sliding-window-simple-explanation/comments/2656104/?parent=2651029
                    ans += len(word) - r + 1
                    # move left due to match
                    # if l is in vowels, means we need to remove it from map
                    if word[l] in vowels:
                        vowels_map[word[l]] -= 1
                        # delete key if value is 0
                        if vowels_map[word[l]] == 0:
                            del vowels_map[word[l]]
                    else:
                        # if l not in vowels, minus n_consoants
                        n_consonants -= 1
                    l += 1
                else:
                    # process not match rule scenario, extend right to find matches
                    # if r is in the end and not match the rule, then break the loop
                    if r == len(word):
                        break
                    # if not in vowels, add n_consonants
                    if word[r] not in vowels:
                        n_consonants += 1
                    else:
                        # else, add map
                        vowels_map[word[r]] += 1
                    r += 1
            return ans 

        return countAtLeastMConsonants(k) - countAtLeastMConsonants(k+1)
        # due to we want to get exactly k, and we can use (>= k) - (>= k+1) to get k
                
# time complexity: O(n), where n is the length of the word
# space complexity: O(1), since vowels_map will never contain more than 5 entries (a, e, i, o, u)