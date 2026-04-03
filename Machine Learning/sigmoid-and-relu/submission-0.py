import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        res=[]
        for i in z:
            x=1/(1+np.exp(-i))
            res.append(np.round(x,5))
        return res

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        res=[]
        for i in z:
            x=np.maximum(0,i)
            res.append(x)
        return res
