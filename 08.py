# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 09:59:47 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
x,y,z = mc.player.getTilePos()
for i in range(5):
    for j in range(5):
        plantTree(x+i*5,y+j*4,z)
    for k in range (5):
        plantTree(z+k*4)
    for i in range(10):
        for j in range(10):
            plantTree (x+i*5,y + i*j,z)
        
    
