import numpy as np
import scipy.integrate as sp

class Lorenz:
    def __init__(self,waarden,sigma=10,rho=28,beta=8/3):
        self.start = waarden
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        
    def fdot(self,vector,t):
        xdot = self.sigma*(vector[1] - vector[0])
        ydot = vector[0]*(self.rho - vector[2]) - vector[1]
        zdot = vector[0]*vector[1] - self.beta*vector[2]
        return [xdot, ydot, zdot]
        
    def solve(self,T,dt):
        y = sp.odeint(self.fdot,self.start,np.arange(0,T+dt,dt))
        return y