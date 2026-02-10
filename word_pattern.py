class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):
            ch = pattern[i]
            w = words[i]

            if ch in char_to_word:
                if char_to_word[ch] != w:
                    return False
            else:
                char_to_word[ch] = w

            if w in word_to_char:
                if word_to_char[w] != ch:
                    return False
            else:
                word_to_char[w] = ch

        return True
