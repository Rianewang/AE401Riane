# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:07:22 2021

@author: User
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
width=10
height=6
lengh=5

mc.setBlocks(x,y,z, x+width, y+height, z+lengh,8)
mc.setBlocks(x+1,y+1,z+1, x+width-1, y+height-1, z+lengh-1,66)



