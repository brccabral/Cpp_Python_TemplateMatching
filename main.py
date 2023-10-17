# %%
import cv2
import numpy as np

# %%
farm_img = cv2.imread("assets/farm.png", cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread("assets/needle.png", cv2.IMREAD_UNCHANGED)

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
result = cv2.matchTemplate(farm_img, needle_img, cv2.TM_CCOEFF_NORMED)

# %%
# show result
cv2.imshow("Result", result)
cv2.waitKey()
cv2.destroyAllWindows()

# %%
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# %%
h, w, c = needle_img.shape

# %%
# adds a yellow rectangle at the best needle result position
# changes farm_img
cv2.rectangle(farm_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 255), 2)

# %%
# show farm
cv2.imshow("Farm", farm_img)
cv2.waitKey()
cv2.destroyAllWindows()

# %%
# reset farm
farm_img = cv2.imread("assets/farm.png", cv2.IMREAD_UNCHANGED)

# %%
threshold = 0.60
yloc, xloc = np.where(result >= np.array(threshold))

# %%
len(xloc)

# %%
for x, y in zip(xloc, yloc):
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), (0, 255, 255), 2)

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
farm_img = cv2.imread("assets/farm.png", cv2.IMREAD_UNCHANGED)

# %%
# loop the new rectangles
for x, y, w, h in rectangles:
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), (0, 255, 255), 2)

# %%
# show farm
cv2.imshow("Farm", farm_img)
cv2.waitKey()
cv2.destroyAllWindows()

# %%
