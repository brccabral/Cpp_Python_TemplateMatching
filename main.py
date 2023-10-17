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
