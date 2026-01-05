class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        c1 = Counter(word1)
        c2 = Counter(word2)

        # Operation 2 implies both strings must contain the exact same set of characters
        if set(c1.keys()) != set(c2.keys()):
            return False

        # Operation 1 lets you permute letters, and operation 2 lets you swap frequencies between existing letters
        return sorted(c1.values()) == sorted(c2.values())
