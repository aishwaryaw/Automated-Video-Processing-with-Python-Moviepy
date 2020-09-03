from moviepy.editor import *
import os
from dir_structure import input_dir, output_dir
from moviepy.video.fx.all import crop


input_video = os.path.join(input_dir, "sample.mp4")
output_gif_dir = os.path.join(output_dir, "gifs")
os.makedirs(output_gif_dir, exist_ok=True)

output_gif1 = os.path.join(output_gif_dir, "sample1.gif")
output_gif2 = os.path.join(output_gif_dir, "sample2.gif")

# method 1
video_clip = VideoFileClip(input_video)
fps = video_clip.fps
gif_clip = video_clip.subclip(6,10)
gif_clip = video_clip.resize(width = 500)

gif_clip.write_gif(output_gif1, fps= fps, program='ffmpeg')


# method 2
w, h = video_clip.size
gif_clip2 = video_clip.subclip(10,20)
square_cropped_gif = crop(gif_clip2, width = 320 , height = 320, x_center = w/2 , y_center = h/2)
square_cropped_gif.write_gif(output_gif2 , fps=fps, program='ffmpeg')




