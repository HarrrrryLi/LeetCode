Because the number will in range(1, 10 ^ 18)


We call an arbitary number in range(L, R + 1) as P, P = Q * Q

So go through number in range(10^5) regard it as the half of a palindrome which will be Q. For example, if the number is 1234, we can get two palindrome numbers 12344321 and 1234321. So Q will be always palindrome. Then we can calculate P. We only need to judge whether P is palindrome. 


Time Complexity O(10 ^ (l // 4 + 1) * l) where l is the max length of L and R 