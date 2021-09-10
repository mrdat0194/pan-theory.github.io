import os

input = r'C:\\Hello\\AI\\'
outdir = r'C:\\Hello\\AI\\'

for filename in os.listdir(input):
    actual_filename = filename[:-4]
    if (filename.endswith(".avi")):
        os.system("ffmpeg -i {}/{} -c:v libx264 -crf 19 -preset slow -c:a aac -b:a 192k -ac 2 {}/{}.mp4".format(input ,filename , outdir, actual_filename))
    else :
        continue
