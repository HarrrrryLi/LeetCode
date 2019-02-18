Greedy.

Use a list as stack. if k and stack and the last number is larger then the number,keep popping, else push the number.

If k is not zero, get list[:-k] else get list. Then join the lsit and lstrip('0').  if the string is empty return '0'