class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if not s:
            return False

        stack = []
        for symbol in s:
            if symbol in "({[":
                stack.append(symbol)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if not self.matches(top, symbol):
                    return False

        return len(stack) == 0

    def matches(self, open, close):
        openings = "({["
        closings = ")}]"
        return openings.index(open) == closings.index(close)
