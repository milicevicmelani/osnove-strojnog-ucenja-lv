import numpy as np
import matplotlib . pyplot as plt

black=np.ones((50,50), dtype=np.uint8)
white=np.zeros((50,50), dtype=np.uint8)

bottom=np.hstack((white,black))
top=np.hstack((black,white))

blocks=np.vstack((bottom,top))
plt.imshow(blocks,cmap ="gray")
plt.show()