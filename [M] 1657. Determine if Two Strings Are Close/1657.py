class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        counter_map = {}
        counter_map2 = {}
        for i in word1:
            if i not in counter_map:
                counter_map[i] = 1
            else:
                counter_map[i] += 1

        for j in word2:
            if j not in counter_map2:
                counter_map2[j] = 1
            else:
                counter_map2[j] += 1

        # validate keys
        if counter_map.keys() != counter_map2.keys():
            return False

        # validate # val
        j_list = list(counter_map2.values())
        for i in counter_map.values():
            if i in j_list:
                j_list.remove(i)
        
        return len(j_list)==0
