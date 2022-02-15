# Brute-Force
Brute Force partial Digest
Algorithm 1:
Write an algorithm that, given a set X, calculates the multiset ΔX of the complete digest and partial digest.
For example in partial digest, if X={0, 2, 4, 7, 10} then ΔX={2, 2, 3, 3, 4, 5, 6, 7, 8, 10}  containing 5(5-1)/2  = 10 integers which are the ten pairwise distances between these points. 

Algorithm 2:
Goal: Given all pairwise distances between points on a line, reconstruct the positions of those points
 Input: The multiset of pairwise distances L, containing n(n-1)/2 integers
 Output: A set X, of n integers, such that ∆ X = L
