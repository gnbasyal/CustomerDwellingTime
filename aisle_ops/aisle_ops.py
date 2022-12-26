'''
Chef        : gnbasyal
Chef-Id     : pvr2114
Dish        : aisle_ops
Created on  : Thursday, 23rd September 2021 4:25:31 pm
'''
import cv2
import json 

def create_aisle_layout(width, height):
    '''
    Creates the layout of aisles according to 8 partitions
    '''
    aisles = {
    'A1':(0, 0, width//4, height//2),
    'A2':(width//4, 0, width//2, height//2),
    'A3':(width//2, 0, 3*width//4, height//2),
    'A4':(3*width//4, 0, width, height//2),

    'A5':(0, height//2, width//4, height),
    'A6':(width//4, height//2, width//2, height),
    'A7':(width//2, height//2, 3*width//4, height),
    'A8':(3*width//4, height//2, width, height),
        }
    # with open(r"aisle_ops\aisle_layout.json", "w") as aisle_file:
    #     json.dump(aisles, aisle_file,indent=4)
    
    return aisles


def get_aisle_from_centre(centre, aisles):
    xc,yc = centre
    for aisle in aisles:
        xt,yt,xb,yb = aisles[aisle]
        if xt<=xc and xc<=xb and yt<=yc and yc<=yb:
            return aisle
    return ''


def draw_aisle_rects(img, aisles):
    for aisle in aisles:
        xt,yt = aisles[aisle][0],aisles[aisle][1]
        xb,yb = aisles[aisle][2],aisles[aisle][3]
        cv2.rectangle(img, (xt,yt), (xb,yb), (255,0,0), thickness=2)
        cv2.putText(img, aisle, (xt+5, yt+20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0,0),thickness=2)
    return img

# if __name__=='__main__':
    # print(aisles)