# The correlation function for two spins separated by r sites

You will be glad to know that we now have all the pieces we need to calculate the correlation function, which is given by the following expression:

![](https://render.githubusercontent.com/render/math?math=\delta(r)\frac{\frac{1}{N}\sum_{i=1}^N(s_i-\langle\s\rangle)(s_{i%2Br-\langle\s\rangle)}{\frac{1}{N}\sum_{i=1}^N(s_i-\langle\s\rangle)^2})

Notice that the numerator in this expression is the covariance between two spins separated by r sites that you calculated in the last exercise and that the denominator is the variance for a single spin, which you learned to calculate in the previous exercise.

With all of that in mind write a program called `correlation_function` that takes 2 argument

1. `spins` - a list of spin variables that gives the coordinates for a particular microstate.
2. `r` - the distance between the spins that you would like to calculate the correlation between.

Your function should then return the value of the correlation coefficient between two spins separated by `r` sites that you compute using the expression above.
