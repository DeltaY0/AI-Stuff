visited = {}

class Trie:
    __init__(self, root):
        self.root = root # root = character
        self.children = {} # maps child char -> trie()
        self.final = False

    def list_words(self):

        words_list = []
        cnt = 0

        def dfs(node: Trie, word: str):
            if node.final == True:
                words_list.append(word)

            for child in node.children.values():
                current_word = word + child.root
                cnt += 1
                dfs(child, current_word)
            
            return

        dfs(self, "")
        print(f"number of nodes {cnt}")
        return words_list


def dfs(node):
    if node not in visited:
        return

    for child in node.children:

        # processing of current node

        dfs(child)


        


def dfs(u: Trie, s: str):
    if u in visited:
        return

    str.append(u.root)
    for root, child in enumerate(u.children):
        visited.append(child)
        dfs(child)


Trie t('a')
t.add("abc")
t.add("adbe")

t.dfs("")