import json
import time
import gc
from machine import I2C,Pin
i2c=I2C(sda=Pin(02), scl=Pin(14), freq=1000000) #SDA D2 GPIO04; SCL D1 GPIO05
from ssd1306 import SSD1306_I2C#I2C的oled选该方法



oled = SSD1306_I2C(128, 64, i2c) #你的OLED分辨率，使用I2C




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

def showImage(li,oled,pix=1,step=1,fps=1):
    oled.fill(0)
    for i in li:
        if pix>1:
            oled.pixel(2*i[0],2*i[1],1)
            oled.pixel(2*i[0]+1,2*i[1],1)
            oled.pixel(2*i[0]+1,2*i[1]+1,1)
            oled.pixel(2*i[0],2*i[1]+1,1)
        else:
            oled.pixel(i[0],i[1],1)
    oled.vline(64,0,64,1)
    oled.text("Step:"+str(step),65,10,1)
    oled.text("Cell:"+str(len(li)),65,25,1)
    oled.text("FPS:"+str(1/fps),65,40,1)
    oled.show()

f=open("lo.json",'r')
d=json.loads(f.read())
f.close()
showImage(d,oled,2,0,1/10)
time.sleep(5)
for i in range(100):
    t=time.ticks_ms()
    d=lifegame(d,32,32)
    st=time.ticks_ms()-t
    me=gc.mem_free()
    gc.collect()
    showImage(d,oled,2,i,st/1000)
