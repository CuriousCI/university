# -*- coding: utf-8 -*-

import images 
def generate_snake(start_img: str, position: list[int, int],
                   commands: str, out_img: str) -> int:
    x=position[0]
    y=position[1]
    count=-1
    pos=[(x,y)]
    out=images.load(start_img)
    out[y][x]=(0,255,0)
    com=commands.split()
    ln=len(out)
    lg=len(out[0])
    mov={'N':(0,-1),'S':(0,1),'E':(1,0),'W':(-1,0),'NE':(1,-1),'NW':(-1,-1),'SE':(1,1),'SW':(-1,1)}
    for c in com:        
        m_x,m_y=mov[c]
        if  out[(y+m_y)%ln][x]==(0,255,0) and out[y][(x+m_x)%lg]==(0,255,0):
            break        
        else:               
            x=(x+m_x)%lg
            y=(y+m_y)%ln            
        if out[y][x]==(0,255,0) or out[y][x]==(255,0,0):
            break
        pos.append((x,y))        
        if out[y][x]==(255,128,0):      
            count-=1
            out[y][x]=(0,255,0)
        else:
            out[pos[count-1][1]][pos[count-1][0]]=(128,128,128)
            out[y][x]=(0,255,0)
    images.save(out,out_img)
    return -count
