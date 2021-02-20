# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 10:00:43 2021

@author: User
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

a=int(input('enter your block:'))
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,a)


try:
    a=int(input('enter your block:'))
    mc.setBlock(x,y,z,a)
except:
    print('pls enter numbers')


name= (input('enter your name:'))
message= (input('enter your message:'))
mc.plstToChat("<"+name+">"+message)