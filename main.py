def correlation_function( spins, r ) :
  # Your code goes here
  av2, var, average = 0, 0, sum(spins) / len(spins) 
  for i in range(len(spins)) : 
    av2 = av2 + (spins[i] - average)*(spins[(i+r)%len(spins)] - average )
    var = var + (spins[i] - average)*(spins[i] - average) 
  return av2/var

spins1 = [1,-1,1,1,-1,1,1,1,-1,-1]
print( correlation_function( spins1, 1 ), correlation_function( spins1, 2 ), correlation_function( spins1, 3 ) )
spins2 = [-1,1,1,1,-1,-1,1,1,1,-1]
print( correlation_function( spins2, 2 ), correlation_function( spins2, 2 ), correlation_function( spins2, 3 ) )
