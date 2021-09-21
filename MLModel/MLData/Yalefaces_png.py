from PIL import Image
import os
from tqdm import tqdm

MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(MAIN_DIR,"yalefaces")
dest_root = os.path.join(MAIN_DIR,"yalefaces_png")
#
# if not os.path.isdir(dest_root):
#     os.mkdir(dest_root)

for image_name in tqdm(os.listdir(root_dir)):
    print("Processing\t{}".format(os.path.join(root_dir, image_name)))
    imagename = image_name.replace(".","_")
    imagename = imagename + ".png"
    img = Image.open(os.path.join(root_dir, image_name)).resize((512,512))
    img.save(os.path.join(dest_root, imagename))



