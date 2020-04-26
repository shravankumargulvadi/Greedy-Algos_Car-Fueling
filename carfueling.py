
# coding: utf-8

# In[1]:


# python3
import sys
no_stops=0
import numpy as np


def compute_min_refills(distance, tank, stops):
    global no_stops
    #print(distance)
    #print(stops)
    
    stops.append(distance)
    #print(stops)
    stops=np.sort(stops)
    current_stop=0
    i=0
    
    while current_stop<distance:
        
        if tank<(stops[i]-current_stop):
            if stops[i-1]==current_stop:
                no_stops=-1
                #print('tada')
                break
            elif stops[i-1]>current_stop:    
                current_stop=stops[i-1]
                i=i-1
                no_stops=no_stops+1
                #print(current_stop)
        if i==len(stops)-1 and tank>=(stops[i]-current_stop):
           
            current_stop=stops[i]
            #print('im here')
            break
        
        if i==len(stops)-1 and tank<(stops[i]-current_stop):
            no_stops=-1
            break
        
            
        #print(i)
        i=i+1
    
    #print(current_stop)
    return no_stops


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

