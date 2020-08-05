class WordDictionary(object):

    def __init__(self):
        self.t = {}
        

    def addWord(self, word):
        curr = self.t
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['#'] = {} # the end

    def search(self, word):
        if not word: return True
        stack = [(0, self.t)]
        while(stack):
            curr, trie = stack.pop()
            if curr == len(word): # check if it is the end
                if '#' in trie:
                    return True
                else: # cannot return False due to the '.' case
                    continue
                    
            if word[curr] == '.': # search all children if the curr is '.'
                for child in trie:
                    stack.append((curr + 1, trie[child]))
            else:
                if word[curr] in trie: # otherwise search the corresponding children
                    stack.append((curr + 1, trie[word[curr]]))
        return False