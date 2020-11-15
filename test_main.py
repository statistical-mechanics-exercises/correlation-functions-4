import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_correlation(self) : 
        for i in range(6,9) :
            for j in range(2^i) :
                num, spins = j, i*[0]
                for k in range(i) :
                    spins[k] = np.floor( num / 2**(4-k) )
                    num = num - spins[k]*2**(4-k)
                    if spins[k]==0 : spins[k] = -1
                average = sum(spins) / len(spins)
                for r in range(1,3) :
                    var, av2 = 0, 0 
                    for k in range(i) : 
                        av2 = av2 + (spins[k] - average)*(spins[(k+r)%len(spins)] - average )
                        var = var + (spins[k] - average)*(spins[k] - average)
    
                    if( var>0 ) : self.assertTrue( np.abs(av2/var - correlation_function(spins,r))<1e-7, "The correlation function you have computed is incorrect" )
