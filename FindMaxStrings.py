class Solution:
    def maximumNumberOfStringPairs(self, words):
        repeated_pair = set()
        counter = 0
        for word in words:
            reversed_word = word[::-1]
            if reversed_word in repeated_pair:
                counter += 1
            repeated_pair.add(word)
        return counter