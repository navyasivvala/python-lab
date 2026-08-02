#navya

import keyword
print("soft keywords:")
print(keyword.softkwlist)
print("\nHard keywords:")
hard_keywords =[kw for kw in keyword.kwlist if kw not in keyword.softkwlist]
print(hard_keywords)