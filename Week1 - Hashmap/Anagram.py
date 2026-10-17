class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sSorted = sorted(s)
        tSorted = sorted(t)

        print("sSorted:", sSorted)
        print("tSorted:", tSorted)

        if sSorted != tSorted:
            return True
        return False



sol = Solution()
sol.isAnagram("anagram", "nagaram")