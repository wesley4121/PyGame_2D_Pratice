import pygame,sys
##_map_tile


##_map
map1 = """
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"""

@staticmethod
def getMapStr(map) -> list:
    if map ==1 :
        return map1.splitlines()
    