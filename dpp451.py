from collections import OrderedDict
import numpy as np
class Solution:
    def frequencySort(self, s: str) -> str:
        dict={}
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        keys = list(dict.keys())
        values = list(dict.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
        s=""
        print(sorted_dict)
        for i in sorted_dict:
            s=i*sorted_dict[i]+s
        return s
