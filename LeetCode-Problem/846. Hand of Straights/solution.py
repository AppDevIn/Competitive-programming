class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        def deleteMap(key):
            value = hashMap[key]
            if value - 1 == 0:
                hashMap.pop(key)
            else:
                hashMap[key] = value - 1
        if len(hand) % groupSize != 0:
            return False

        hashMap = {}

        for h in hand:
            if h not in hashMap:
                hashMap[h] = 1
            else:
                hashMap[h] = hashMap[h] + 1

        keys = sorted(list(hashMap.keys()))
        
        while keys:
            key = keys[0]
            
            for i in range(groupSize-1):
            
                if key+1 in hashMap:
                    deleteMap(key)
                    key = key + 1
                else:
                    return False
            deleteMap(key)
            keys = sorted(list(hashMap.keys()))


        return True
        
