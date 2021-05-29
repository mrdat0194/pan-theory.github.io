from PIL import Image
import os
from tqdm import tqdm
from MLModel import MAIN_DIR

root_dir = os.path.join(MAIN_DIR,"CASIA-FaceV5-Crop")
dest_root = os.path.join(MAIN_DIR,"test_face_v3")
if not os.path.isdir(dest_root):
    os.mkdir(dest_root)

for subfolder in tqdm(os.listdir(root_dir)):
    if not os.path.isdir(os.path.join(dest_root, subfolder)):
        os.mkdir(os.path.join(dest_root, subfolder))
    if subfolder != '.DS_Store':
        for image_name in os.listdir(os.path.join(root_dir, subfolder)):
            if image_name != "Thumbs.db":
                print("Processing\t{}".format(os.path.join(root_dir, subfolder, image_name)))
                imagename = image_name.replace(".bmp",".png")
                img = Image.open(os.path.join(root_dir, subfolder, image_name)).resize((512,512))
                img.save(os.path.join(dest_root, subfolder, imagename))
