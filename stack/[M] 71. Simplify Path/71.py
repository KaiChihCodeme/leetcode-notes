class Solution:
    def simplifyPath(self, path: str) -> str:
        content = path.split('/')
        tmp = []
        
        while content:
            cur = content.pop()
            if cur == '' or cur == '.':
                continue
            
            if cur == '..':
                cnt = 1
                while content and content[-1] == '..':
                    content.pop()
                    cnt += 1
                while cnt > 0 and content:
                    c = content.pop()
                    if c == '.' or c == '':
                        continue
                    if c == "..":
                        cnt += 2
                    cnt -= 1
            else:
                tmp.append(cur)

        # structure
        ans = ""
        if not tmp:
            return "/"
        for i in range(len(tmp)-1, -1, -1):
            ans += f'/{str(tmp[i])}'
        return ans


# time complexity: O(n)
# space complexity: O(n) 