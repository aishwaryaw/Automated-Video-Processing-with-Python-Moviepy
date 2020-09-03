from dir_structure import input_dir, output_dir
import os
from moviepy.editor import *
from PIL import Image


output_video = os.path.join(output_dir, "video_from_dir.mp4")
thumbnail_dir = os.path.join(output_dir,"thumbnails")
thumbnails_dir_per_frame = os.path.join(output_dir, "thumbnails_per_frame")
thumbnails_dir_per_half_second = os.path.join(output_dir, "thumbnails_dir_per_half_second")


# this_dir = os.listdir(thumbnail_dir)
# #filepaths = [os.path.join(thumbnail_dir,fname) for fname in this_dir if fname.endswith(".jpg")]
# # or 
# filepaths = []
# for fname in this_dir:
#     if fname.endswith(".jpg"):
#         filepath = os.path.join(thumbnail_dir, fname)
#         filepaths.append(filepath)
    
#print(filepaths)

# clip = ImageSequenceClip(filepaths, fps=1)
# clip.write_videofile(output_video) 
# above method does not arrange the images in correct sequence 
# so we are using below methods for sorting the images.

directory = {}

for root, dirs, files in os.walk(thumbnails_dir_per_half_second):
    for fname in files :
        fpath = os.path.join(root, fname) # fname is name of image file like 1000.jpg
        try:
            key = float(fname.replace(".jpg", ""))

        except:
            key = None

        if key != None:
            directory[key] = fpath

new_paths = []


for key in sorted(directory.keys()):
    #print(directory[key])
    new_paths.append(directory[key]) # list of image file paths

# clip = ImageSequenceClip(new_paths, fps=10)
# clip.write_videofile(output_video)
# we can directly use above 2 lines code for creating video using image file paths or can use below method of using frames

new_clips = []
for path in list(new_paths):
    frame = ImageClip(path)
    #print(frame.img) # numpy array
    new_clips.append(frame.img)


video_clip = ImageSequenceClip(new_clips, fps = 5)
video_clip.write_videofile(output_video)





    







