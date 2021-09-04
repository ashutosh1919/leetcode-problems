# Time complexity: O(len(words)*maxLen(words))
# Approach: Putting as many words as possible in line with single spaces and then calculate extra spaces using divmod and distributing from start to end

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur, curL, lines = [], 0, []
        for word in words:
            if curL + len(word) + len(cur) > maxWidth:
                nSpaces = maxWidth - curL
                if len(cur)==1:
                    lines.append(cur[0]+' '*nSpaces)
                else:
                    spaces, extra = divmod(nSpaces, len(cur)-1)
                    for i in range(extra):
                        cur[i] += ' '
                    lines.append((' '*spaces).join(cur))
                cur, curL = [word], len(word)
            else:
                curL += len(word)
                cur.append(word)
        lines.append(''.join([' '.join(cur), ' '*(maxWidth-curL-len(cur)+1)]))
        return lines