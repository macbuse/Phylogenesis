
import numpy as np

def sv_main(vts0=[[]],vts1=[[]]):

    in_sockets = [
        ['s', 'verts seed',    vts0],
        ['s', 'verts delaunay',vts1]
    ]
    
    vts0 = [np.array(x[:])for x in vts0[0] ] 
    vts1 = [np.array(x[:])for x in vts1[0] ]
    
    data = []
    
    #for each pt make a list of indices
    #of the nearest points in the original distribution
    for pt in vts1:

        xx = [ ( np.linalg.norm(y - pt), i) 
                                     for i,y  in enumerate(vts0)]      
                                             
        xx.sort(key= lambda x : x[0])
        
        #this is a hack - I suppose that vts0 are in general position
        #so I only have to take the first 3
        min_dist = xx[0][0]
        data.append([ index for dist,index in xx[:3] 
                            if dist - min_dist < .0001] )
        
    #each pt in the original distribution is a face
    polys = [[] for x in vts0]
    for i,x in enumerate(data):
        for k in x:
            polys[k].append(i)
            
    #kill_list = [ j for j,x in enumerate(vts1) 
                   if np.linalg.norm(x) > 1.2] 
            
    #order vertices anti-clocwise       
    for k, ff in enumerate(polys):
        pp = [ (vts1[i]  - vts0[k], i) for i in ff]
        pp.sort(key=lambda x : np.arctan2(x[0][0],x[0][1]) )
        polys[k] = [ i for tt,i in pp]
        

    out_sockets = [
        ['s', 'Polys', [polys]]
    ]

    return in_sockets, out_sockets
