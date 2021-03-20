# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:06:59 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
 
for i in range (100):
    mc.setBlock(x,y-1,z-i,1)
    
    
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
 
for i in range (100):
    mc.setBlocks(x+i,y-1,z+i,x+i,y-1,z+i+3,1)
    
    
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x+2,y+2,z+2,x+2,y-2,z+2)
     
     
     
    