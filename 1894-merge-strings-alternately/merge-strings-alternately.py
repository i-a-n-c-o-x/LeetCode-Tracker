class Solution(object):
    def mergeAlternately(self, word1, word2):
        string = ''
        if len(word1) == len(word2):
            for i in range(len(word1)):
                string += word1[i]
                string += word2[i]
        if len(word1) > len(word2):
            for i in range(len(word2)):
                string += word1[i]
                string += word2[i]
            string += word1[len(word2):]
        if len(word2) > len(word1):
            for i in range(len(word1)):
                string += word1[i]
                string += word2[i]
            string += word2[len(word1):]
        return string
        