class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set({0})
        
        [keys.add(x) for x in rooms[0]]
        
        # We keep adding keys until we
        # 1. Found all the keys -> True
        # 2. Can no longer find new key -> False
        while True:
            old_key = len(keys)
            
            for key in list(keys):
                [keys.add(x) for x in rooms[key]]
                if len(keys) == len(rooms):
                    print(keys)
                    return True
            
            if old_key == len(keys):
                return False
            else:
                old_key = len(keys)
        
