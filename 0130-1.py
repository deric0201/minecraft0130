from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

name = input("請問你叫什麼名字:")
long = int(input(name+"請問你要蓋多長的房子"))#高
width =int(input(name+"請問你要蓋多寬的房子")) #寬
length =int(input(name+"請問你要蓋高的房子")) #高
block = int(input(name+"請問要用什麼樣子的材料"))
air = 0

mc.setBlocks(x,y,z,x+long,y+length,z+width,block)

mc.setBlocks(x+1,y+1,z+1,x+long-1,y+length-1,z+width-1,air)

mc.setBlocks(x+1,y+length-1,z+1,x+long-1,y+length-1,z+width-112,169)

mc.postToChat(name+"你指定的建材"+str(block))
mc.postToChat("你的房子長:"+str(long)+"寬:"+str(width)+"高:"+str(length)+"的建築物已經建好了")