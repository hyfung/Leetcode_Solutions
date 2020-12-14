"""
Generalized Solution:
(N) = 10: [0,1,2,3,4,5,6,7,8,9]
(B)lacklist: [1,3,5,7,11,12]
(V)alid Blacklist: [1,3,5,7]
(C)hoices: [0,2,4,6,8,9]

Actual number of choices = len(N) - len(V) = 10 - 4 = 6, which is length of C
Solution is to random the x-th element from C

First we random a choice 'i' which which we should return C[i]
Since C is not available, we have to derive C by iterating through x in range(N)
If x in V then we it is a valid skip
Else we increment counter


"""
