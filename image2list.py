import json
from PIL import Image
from pathlib import Path

def pl(img,x=128,y=64,fr=False):
    e=[]
    fe=[]
    c=Path(img)
    if c.is_file():
        d=Image.open(img)
        q=d.convert("1")
        q2=q.resize((x,y))
        q2.show()
        q3=q2.load()
        for i in range(x):
            for j in range(y):
                if q3[i,j]>150:
                    e.append([i,j])
                else:
                    fe.append([i,j])
    f=open(c.stem+".json","w")
    if fr:
        f.write(json.dumps(fe))
        f.close()
        return fe
    else:
        f.write(json.dumps(e))
        f.close()
        return e

q=pl("lo.png",32,32,True)
print(len(q))
