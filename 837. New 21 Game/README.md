The final number will be in the range of [K, K + W). So if N >= K + W, prob will be 1, if N < K, prob will be 0.

Then this problem can convert suppose we have number [K, K + W), each time we minus [1, W]. what's P(0)

Suppose every num in range [K, N] have probility 1. The reason we can make this assumption is K + W - 1 can not get from K + W - 2, because it will stop when it reaches K + W - 2. So numbers in range[K, K + W) won't influence each other

For each number P(num) = 1 / W * (P(num + 1) + ... + P(num + W))

Time Complexity O(K + W), Space Complexity O(K + W)
