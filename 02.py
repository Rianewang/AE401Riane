from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x=241
y=89
z=240


mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)

t=0
while True:
    t=t+1
    mc.postToChat(str(t) + 'times')
    
while True:
    x,y,z= mc.player.getTilePos()
    mc.postToChat(str(x)+" "+str(y) +" "+str(z))
    
