import os

inputdir = '/Users/petern/Desktop/'
outdir = '/Users/petern/Desktop/'

for filename in os.listdir(inputdir):
    actual_filename = filename[:-4]
    if (filename.endswith(".mp4")):
        os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}/{}.wav'.format(filename, outdir, actual_filename))
    else :
        continue