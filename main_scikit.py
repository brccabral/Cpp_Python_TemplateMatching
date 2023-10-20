# %%
import numpy as np
import skimage as ski
from skimage.feature import match_template
import cv2

# %%
farm_img = ski.io.imread("assets/farm.png")
needle_img = ski.io.imread("assets/needle.png")
farm_img = cv2.cvtColor(farm_img, cv2.COLOR_RGB2BGR)
needle_img = cv2.cvtColor(needle_img, cv2.COLOR_RGB2BGR)
yellow = (0, 255, 255)

# %%
# show farm
cv2.imshow("Farm", farm_img)
cv2.waitKey()
cv2.destroyAllWindows()

# %%
# show needle
cv2.imshow("Needle", needle_img)
cv2.waitKey()
cv2.destroyAllWindows()

# %%
result = match_template(farm_img, needle_img)

# %%
# show result
cv2.imshow("Result", result)
cv2.waitKey()
cv2.destroyAllWindows()

# %%
ij = np.unravel_index(np.argmax(result), result.shape)
c, x, y = ij[::-1]
x = int(x)
y = int(y)

# %%
h, w, c = needle_img.shape

# %%
cv2.rectangle(farm_img, (x, y), (x + w, y + h), yellow, 2)

# %%
# show farm
cv2.imshow("Farm", farm_img)
cv2.waitKey()
cv2.destroyAllWindows()

# %%
# reset farm
farm_img = ski.io.imread("assets/farm.png")
farm_img = cv2.cvtColor(farm_img, cv2.COLOR_RGB2BGR)

# %%
threshold = 0.9
yloc, xloc, cloc = np.where(result >= np.array(threshold))


# %%
len(xloc)

# %%
for x, y in zip(xloc, yloc):
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), yellow, 2)

# %%
# show farm
cv2.imshow("Farm", farm_img)
cv2.waitKey()
cv2.destroyAllWindows()

# %%
rectangles = []
for x, y in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    # force a duplication so cv2.groupRectangles don't remove
    # locations that have only one rectangle
    rectangles.append([int(x), int(y), int(w), int(h)])


# %%
rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
len(rectangles)

# %%
# reset farm
farm_img = ski.io.imread("assets/farm.png")
farm_img = cv2.cvtColor(farm_img, cv2.COLOR_RGB2BGR)

# %%
# loop the new rectangles
for x, y, w, h in rectangles:
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), yellow, 2)

# %%
# show farm
cv2.imshow("Farm", farm_img)
cv2.waitKey()
cv2.destroyAllWindows()
