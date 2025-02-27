class Solution:
    def maximumNumberOfStringPairs(self, words):
        repeated = set()
        counter = 0
        for word in words:
            reversed_word = word[::-1]
            if reversed_word in repeated:
                counter += 1
            repeated.add(word)
        return counter