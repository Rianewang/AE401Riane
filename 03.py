# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 09:56:38 2021

@author: User
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

time.sleep(5)

x,y,z = mc.player.getTilePos()

mc.setBlocks( x+25,y,z+25,x-25,y,z-25,46)


mc.setBlock( x+1,y,z,46)
mc.setBlock( x-1,y,z,46)
mc.setBlock( x,y,z+1,46)
mc.setBlock( x,y,z-1,46)
mc.setBlock( x-1,y,z-1,46)
mc.setBlock( x+1,y,z+1,46)
mc.setBlock( x-1,y,z+1,46)
mc.setBlock( x+1,y,z-1,46)


mc.setBlock(x,y,z,46)
mc.setBlock(x,y+1,z,46)
mc.setBlock(x,y+2,z,46)
mc.setBlock(x,y+3,z,46)
mc.setBlock(x,y+4,z,46)
mc.setBlock(x,y+5,z,46)
mc.setBlock(x,y+6,z,46)
mc.setBlock(x,y+7,z,46)
mc.setBlock(x,y+8,z,46)
mc.setBlock(x,y+9,z,46)


