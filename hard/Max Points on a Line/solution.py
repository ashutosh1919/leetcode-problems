# Time complexity: O(n*n)
# Approach: Define slope by tuple of numerator and denomenator and then store count by slope in dictionary.

class Solution:
    def count_lines(self, i):
        lines, h_lines, ct, dups = {}, 1, 1, 0
        
        def get_slope(x1, x2, y1, y2):
            dx, dy = x1-x2, y1-y2
            if dx==0:
                return (0, 0)
            elif dy==0:
                return (sys.maxsize, sys.maxsize)
            elif dx<0:
                dx, dy = -dx, -dy
            g = math.gcd(dx, dy)
            return (dx/g, dy/g)
        
        def add_line(i, j, ct, dups):
            x1, y1, x2, y2 = self.points[i][0], self.points[i][1], self.points[j][0], self.points[j][1]
            if x1==x2 and y1==y2:
                dups += 1
            elif y1==y2:
                nonlocal h_lines
                h_lines+=1
                ct = max(ct, h_lines)
            else:
                slope = get_slope(x1, x2, y1, y2)
                if slope in lines:
                    lines[slope] = lines[slope]+1
                else:
                    lines[slope] = 2
                ct = max(ct, lines[slope])
            return ct, dups
        for j in range(i+1, len(self.points)):
            ct, dups = add_line(i, j, ct, dups)
        return ct+dups
    
    def maxPoints(self, points: List[List[int]]) -> int:
        self.points = points
        n = len(points)
        if n<3:
            return n
        max_pts = 0
        for i in range(n-1):
            max_pts = max(max_pts, self.count_lines(i))
        return max_pts