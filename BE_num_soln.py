# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

L  = 2*np.pi;
N_x = 30;
dx = L/(N_x-1);
x = np.linspace(0,L,N_x);

T = 1;
N_T = 5;
dt = T/N_T;

nu = 0.3;

u = np.zeros((N_x,N_T))
x = np.linspace(0,L,N_x);

u[:,0] = np.sin(x);


for j in range(0,N_T-1):
    for i in range(0,N_x):
        
        print(i,j)
        
        if i == 0:
            
            A = (u[i+1,j] - 2*u[i,j] + u[-2,j])/dx**2;
            B = u[i,j]*(u[i+1,j] - u[-2,j])/(2*dx);
            
        elif i == N_x -1:
                
            A = (u[1,j] - 2*u[i,j] + u[i-1,j])/dx**2;
            B = u[i,j]*(u[1,j] - u[i-1,j])/(2*dx);
                
        else:
        
            A = (u[i+1,j] - 2*u[i,j] + u[i-1,j])/dx**2;
            B = u[i,j]*(u[i+1,j] - u[i-1,j])/(2*dx);
            
            
        u[i,j+1] = u[i,j] + dt*nu*A - dt*B;
        

plt.plot(x,u[:,0],'r-o',x,u[:,1],'b-o',x,u[:,2],'g-o',x,u[:,3],'c-o',x,u[:,4],'y-o')
plt.ylabel('u')
plt.xlabel('x')
plt.show()





