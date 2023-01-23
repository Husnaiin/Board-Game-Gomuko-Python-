import random  
import os
import sys

def init():
    b=[]
    dim=int(input("Dim:"))
    nop=int(input('No of players:'))
    w=int(input('Win Count:'))
    for r in range(0,dim+1):
        arow=[]
        for c in range(0,dim+1):
            arow.append('-')   
        b.append(arow)
    sym=[]
    pname=[]
    for i in range(0,nop):
        pname.append(input(f"Player {i+1},s Name: "))
        sym.append(input(f"Player {i+1},s Symbol: "))
        
    turn=random.randint(0,nop-1)
    
    return b,dim,nop,sym,pname,turn,w

def init2():
    b=[]
    dim=int(input("Dim:"))
  
    nop=2
    w=int(input('Win Count:'))
    for r in range(0,dim+1):
        arow=[]
        for c in range(0,dim+1):
            arow.append('-')   
        b.append(arow)
    sym=[]
    pname=[]
    
    pname.append("Computer")
    pname.append(input("Enter your name: "))
    sym.append('+')
    sym.append(input("Enter your symbol: "))

   
        
    turn=random.randint(0,nop-1)
    
    return b,dim,nop,sym,pname,turn,w

def printb(b,dim):
    
    for r in range (0,dim):
        for c in range (0,dim):
            print(b[r][c],end=" ")
        print()  
   
        
def turnmsg(n):
    print(f"{n}'s Turn: ")
    


def pm(b,pr,pc,s):
    b[pr][pc]=s
    
def tchange(turn,nop):
    turn=(turn+1)%nop
    return turn

def isvalid(b,pr,pc):
    if(b[pr][pc]=='-'):
        return True
    else:
        return False

def winh(b,dim,w,sym,ri,ci):
    for i in range(0,w):
        if(b[ri][ci+i]!=sym):
            return False
    return True        
    
def winv(b,dim,w,sym,ri,ci):
    for i in range(0,w):
        if(b[ri+i][ci]!=sym):
            return False
    return True 

def wind1(b,dim,w,sym,ri,ci):
    for i in range(0,w):
        if(b[ri+i][ci+i]!=sym):
            return False
    return True        

def wind2(b,dim,w,sym,ri,ci):
    for i in range(0,w):
        if(b[ri+i][ci-i]!=sym):
            return False
    return True 

def doiwin(b,dim,w,sym,ri,ci):
    if winh(b, dim, w, sym,ri,ci) or winv(b, dim, w, sym,ri,ci) or wind1(b, dim, w, sym,ri,ci) or wind2(b, dim, w, sym,ri,ci):
        return True
	
    return False


def iswinn( b,  dim, w,sym):
    for ri in range(0, dim):
        for ci in range(0, dim):
            if (doiwin(b, dim, w, sym,ri,ci)==True):
                return True
    return False      
	

		
def isdraw(b,dim):
    for ri in range(0, dim):
        for ci in range(0, dim):
            if (b[ri][ci]=='-'):
               
                return False
    return True  
		
				
def cmove(b,dim,sym,w):
    wc=w
    for wc in range(w,wc>1,-1):
        for ri in range(0,dim):
            for ci in range(0,dim):
                if (isvalid(b, ri, ci)):
                    b[ri][ci] = sym[1]
                    if(iswinn(b, dim, wc, sym[1])):
                        b[ri][ci] = '-'
                        pr= ri
                        pc= ci
                        return pr,pc
                    b[ri][ci] ='-'
                    
        for ri in range(0,dim):
            for ci in range(0,dim):
                if (isvalid(b, ri, ci)):
                    b[ri][ci] = sym[0]
                    if(iswinn(b, dim, wc, sym[0])):
                        b[ri][ci] = '-'
                        pr= ri
                        pc= ci
                        return pr,pc
                    b[ri][ci] ='-'    
		
                    
    pr=random.randint(0,dim-1)
    pc=random.randint(0,dim-1)
    while(isvalid(b,pr,pc)==False):
        pr=random.randint(0,dim-1)
        pc=random.randint(0,dim-1)
        
    return pr,pc		
def spos2(b,dim,t,sym,w):
    if(t==1):
        pr=int(input(f"Select Row (1-{dim}): "))
        pc=int(input(f"Select Col (1-{dim}): "))
        pr=pr-1
        pc=pc-1
    if(t==0):
        pr,pc=cmove(b,dim,sym,w)
        
def spos(dim):
    pr=int(input(f"Select Row (1-{dim}): "))
    pc=int(input(f"Select Col (1-{dim}): "))
    pr=pr-1
    pc=pc-1
    
    return pr,pc

       
   
    
    return pr,pc	

#main-------------------------------------------------------------------------

n=int(input("For H v H press 1, For C v H press 2: "))
if(n==2):
    b,dim,nop,sym,pname,turn,w=init2()
    printb(b,dim)
    
    while(True):
       
       
        turnmsg(pname[turn])
        
        pr,pc=spos2(b,dim,turn,sym,w)
        while(isvalid(b,pr,pc)==False):
            pr,pc=spos2(b,dim,turn,sym,w)
        
        
       
        pm(b,pr,pc,sym[turn])
       
        printb(b,dim)
       
        if(iswinn(b, dim, w, sym[turn])):
            print(f"{pname[turn]} is winner!")
            break
        if  isdraw(b,dim):
            print("Game Draw")
            break
            
        
        turn=tchange(turn,nop)
        
if(n==1):
    b,dim,nop,sym,pname,turn,w=init()
    printb(b,dim)

    while(True):
       
        turnmsg(pname[turn])
        
        pr,pc=spos(dim)
        while(isvalid(b,pr,pc)==False):
            pr,pc=spos(dim)
        
        
       
        pm(b,pr,pc,sym[turn])
     
        printb(b,dim)
        #iswinn(b,dim,w,sym[turn])
        if(iswinn(b, dim, w, sym[turn])):
            print(f"{pname[turn]} is winner!")
            break
        if  isdraw(b,dim):
            print("Game Draw")
            break
            
            
        
     
        turn=tchange(turn,nop)
        
        
        
        
        
