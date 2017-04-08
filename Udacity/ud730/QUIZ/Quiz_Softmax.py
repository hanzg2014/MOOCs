# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

def softmax(x):
# """Compute softmax values for each sets of scores in x."""
#     pass  # TODO: Compute and return softmax(x)  
    return np.exp(x) / np.sum(np.exp(x), axis = 0)

if __name__ == '__main__':
    print(softmax(scores))
    
    x = np.arange(-2.0, 6.0, 0.1)
    scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])    #(v,h,d)
    lines = plt.plot(x, softmax(scores).T, linewidth=2)
    plt.title("Softmax([x,ones,ones])")
    plt.xlabel("x")
    plt.ylabel("Probability")
    plt.legend(lines,["x", "1.0", "0.2"], loc = 7)
    plt.show()