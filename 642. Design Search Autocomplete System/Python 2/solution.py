class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.d = collections.defaultdict(int)
        self.partial = ''
        self.matches = []
        for s,t in zip(sentences,times):
            self.d[s]=t

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':            
            self.d[self.partial] += 1
            self.partial = '' # reset self.partial and self.matches and return []
            self.matches = []
            return []
        
        if self.partial == '':
            self.matches = [(-count,s) for s,count in self.d.items() if s[0]==c]
            self.matches.sort()#sort self.matches by count
            self.matches = [s for _,s in self.matches]#remove count
        else:
            i = len(self.partial)
            self.matches = [s for s in self.matches if len(s)>i and s[i]==c]
            
        self.partial += c
        return self.matches[:3]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)