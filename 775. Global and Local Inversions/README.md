For each local, it must be a global pair.  So we just need to compare this(A[idx]) and min(A[idx + 2:]). If it exists, return False


Time Complexity O(N). Space Complexity O(1)