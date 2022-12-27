class Solution:
    def sortSentence(self, s: str) -> str:
        sentenceDec = {}
        indexHolder = 0
        list1 = []
        ans= []
        for i in range(len(s)):
            if (s[i].isnumeric()):
                print(s[i])
                sentenceDec[int(s[i])] = s[indexHolder:i]
                indexHolder = i + 2
        for k in sentenceDec.keys():
            list1.append((k,sentenceDec[k]))
        list1.sort()
        for i in range(len(list1)):
            ans.append(list1[i][1])
        
        return ' '.join(ans)

