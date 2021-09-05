# Time complexity: O(len(path))
# Approach: Using stack to push element when there is legal dir and pop when .. is found.

class Solution:
    def simplifyPath(self, path: str) -> str:
        sp = path.split('/')
        st = []
        for s in sp:
            if s not in ['..', '.', '']:
                st.append(s)
            elif s in ['..']:
                if len(st)>0:
                    st.pop()
        return '/'+'/'.join(st)