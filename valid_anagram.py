class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if 1 <= len(s) <= 5 * (10 ** 4) and 1 <= len(t) <= 5 * (10 ** 4):
            s = s.lower()
            t = t.lower()

            if len(s) != len(t):
                return False

            # hashmaps
            countS, countT = {}, {}

            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
            for c in countS:
                if countS[c] != countT.get(c, 0):
                    return False
            return True