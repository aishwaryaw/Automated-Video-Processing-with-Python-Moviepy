from moviepy.editor import *
from dir_structure import input_dir, output_dir
import os
from PIL import Image


input_video = os.path.join(input_dir, "sample.mp4")
thumbnails_dir = os.path.join(output_dir, "thumbnails")
thumbnails_dir_per_frame = os.path.join(output_dir, "thumbnails_per_frame")
thumbnails_dir_per_half_second = os.path.join(output_dir, "thumbnails_dir_per_half_second")

os.makedirs(thumbnails_dir, exist_ok=True)
os.makedirs(thumbnails_dir_per_frame, exist_ok=True)
os.makedirs(thumbnails_dir_per_half_second, exist_ok=True)


video_clip = VideoFileClip(input_video)
fps = video_clip.fps # frames per second - 30
duration = video_clip.duration # total video duration -  30.17s
frames = video_clip.reader.nframes # total frames in the video - 906 frames
#print(fps, duration, frames)
max_duration = int(duration) + 1


# 3 different methods --
#1.
for i in range(0, max_duration):
    #print(i) - prints seconds as 0 1 2 3 4....30
    frame = video_clip.get_frame(i) # numpy array of numbers which displays the pixel positions of the frame
    # [ 76 116 162]
    # [ 76 116 162]
    # [ 76 116 162]
    #print(frame)

    new_img_filepath = os.path.join(thumbnails_dir, f"{i}.jpg")
    new_img = Image.fromarray(frame) # takes numpy array and convert it into image
    new_img.save(new_img_filepath)


#2.
seconds = frames / (fps * 1.0)
for i, frame in enumerate(video_clip.iter_frames()):
    #print(frame) #906 frames

    if i % fps == 0: # here fps is 30
        current_ms = int((i / fps) * 1000) # converting second to millisecond , it will give the second for the frame
        # 0 , 1000, 2000, 3000....
        #print(current_ms)
        new_img_filepath = os.path.join(thumbnails_dir_per_frame, f"{current_ms}.jpg")
        new_img = Image.fromarray(frame) # takes numpy array and convert it into image
        new_img.save(new_img_filepath)
    

#3.
frames_per_half_second = int(fps / 2.0)
for i, frame in enumerate(video_clip.iter_frames()):

    if i % frames_per_half_second == 0:
        current_ms = int((i / fps) * 1000) # 0 , 500, 1000, 1500....
        #print(current_ms)
        new_img_filepath = os.path.join(thumbnails_dir_per_half_second, f"{current_ms}.jpg")
        new_img = Image.fromarray(frame) # takes numpy array and convert it into image
        new_img.save(new_img_filepath)









    














