class Solution(object):
    def openLock(self, deadends, target):

      queue = [('0000', 0)]
      seen = {'0000'}

      def children(curr):
        for index in range(4):
          x = int(curr[index])
          for d in (-1, 1):
            y = (x + d) % 10
            yield curr[:index] + str(y) + curr[index+1:]

      while queue:
        curr, depth = queue.pop(0)
        if curr == target: return depth
        if curr in deadends: continue 
        for child in children(curr):
          if child not in seen:
            seen.add(child)
            queue.append((child, depth + 1))
      return -1
        

  
