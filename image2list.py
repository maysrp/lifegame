# from machine import I2C,Pin
# from ssd1306 import SSD1306_I2C#I2C的oled选该方法
# i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000) 
# oled = SSD1306_I2C(128, 64, i2c) #你的OLED分辨率，使用I2C
# import ujson as json
# oled.fill(1) #清空屏幕
# oled.show()
# oled.fill(0)
# oled.show()

import json
import time
import gc

def lifegame(past,xa=128,ya=64):
    now=[]
    decell={}
    for i in past:
        j=[]
        j.append([i[0]-1,i[1]-1])
        j.append([i[0],i[1]-1])
        j.append([i[0]+1,i[1]-1])
        j.append([i[0]-1,i[1]])
        j.append([i[0]+1,i[1]])
        j.append([i[0]-1,i[1]+1])
        j.append([i[0],i[1]+1])
        j.append([i[0]+1,i[1]+1])
        jsj=0
        for x in j:
            if x in past:
                jsj+=1
            else:
                if x[0] in range(xa) and x[1] in range(ya):
                    xxx=json.dumps(x)
                    if xxx in decell:
                        decell[xxx]+=1
                    else:
                        decell[xxx]=1
        if jsj in [2,3]:
            now.append(i)
    for dec in decell:
        if decell[dec]==3:
            now.append(json.loads(dec))
    del past
    del decell
    gc.collect()
    return now

def showImage(li,oled):
    oled.fill(0)
    for i in li:
        oled.pixel(i[0],i[1],1)
    oled.show()

f=open("lo.json",'r')
d=json.loads(f.read())
f.close()
for i in range(100):
    t=time.time()
    d=lifegame(d)
    print(i,":",len(d),":",time.time()-t,gc.mem_free())
    showImage(d,oled)
    gc.collect()
