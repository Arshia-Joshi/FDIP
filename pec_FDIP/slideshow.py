
import cv2
import os
import time


folder_path = 'images'           
display_time = 2                  
transition_frames = 30             
window_name = 'Mushroom Slideshow' 


image_files = sorted([
    os.path.join(folder_path, f)
    for f in os.listdir(folder_path)
    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
])

if len(image_files) < 2:
    print(" Need at least 2 images for a slideshow.")
    exit()


first_image = cv2.imread(image_files[0])
if first_image is None:
    print(" Failed to load images. Check file paths.")
    exit()

height, width = first_image.shape[:2]
size = (width, height)


def load_and_resize(path):
    img = cv2.imread(path)
    return cv2.resize(img, size)

images = [load_and_resize(p) for p in image_files]


cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 600)


while True:
    for i in range(len(images)):
        current_img = images[i]
        next_img = images[(i + 1) % len(images)]

       
        cv2.imshow(window_name, current_img)
        if cv2.waitKey(display_time * 1000) & 0xFF == 27:  
            break

       
        for alpha in range(transition_frames + 1):
            a = alpha / transition_frames
            blended = cv2.addWeighted(current_img, 1 - a, next_img, a, 0)
            cv2.imshow(window_name, blended)
            if cv2.waitKey(30) & 0xFF == 27:
                break

cv2.destroyAllWindows()
