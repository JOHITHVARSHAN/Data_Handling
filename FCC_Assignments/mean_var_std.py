import numpy as np

class Solution:
    
    def Calculate(self, ar):
        try:
            arr = np.array(ar)
            arr = arr.reshape(3,3)

        except:
            return ValueError("List must contain nine numbers.")
        
        result = {
            'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr).item()],
            'variance': [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr).item()],
            'standard deviation': [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr).item()],
            'max': [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr).item()],
            'min': [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr).item()],
            'sum': [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr).item()]
        }

        return result

c = Solution()
print(c.Calculate([0,1,2,3,4,5,6,7,8]))
