from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad_q = deque()
        dir_q = deque()

        n = len(senate)

        for ind, i in enumerate(senate):
            if i == 'R':
                rad_q.append(ind)
            else:
                dir_q.append(ind)

        while rad_q and dir_q:
            cur_rad = rad_q.popleft()
            cur_dir = dir_q.popleft()

            if cur_rad < cur_dir:
                rad_q.append(n)
            else:
                dir_q.append(n)
            n += 1

        return 'Dire' if not rad_q else 'Radiant'
