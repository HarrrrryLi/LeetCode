Count frequency of all ages

First consider ageA == ageB, if the frequency is larger than 1 and the ages is greater than 14(this makes sure ageB > ageA * 0.5 + 7), result add C(freq, 2).

Secondly, consider all unique ages, if ageA and ageB meet those condition, skip,  else, add freq[ageA] * freq[ageB]


Time Complexity O(N ^ 2). Space Complexity O(N)