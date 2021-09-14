# Time complexity: O(1)
# Approach: Dictionary implementation

class Solution:
    def fractionToDecimal(self, num: int, den: int) -> str:
        neg = (num<0 and den>0) or (num>0 and den<0)
        num, den = abs(num), abs(den)
        dec = num//den
        if num%den==0:
            return str(dec) if not neg else str(-dec)
        left = (num%den)
        res = [str(dec), '.']
        mp, index = {}, 2
        while left:
            if left in mp:
                res = res[:mp[left]] + ['('] + res[mp[left]:] + [')']
                break
            else:
                mp[left] = index
            left *= 10
            res.append(str(left//den))
            left = left%den
            index += 1
        return ''.join(res) if not neg else '-'+''.join(res)
            