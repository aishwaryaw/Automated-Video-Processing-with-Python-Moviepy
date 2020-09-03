from dir_structure import input_dir, output_dir
import os
from moviepy.editor import *
from moviepy.audio.fx.all import volumex
from PIL import Image


source_video_path = os.path.join(input_dir, "sample.mp4")
source_audio_path = os.path.join(input_dir , "audio.mp3")

overlay_dir = os.path.join(output_dir, "overlay_text")
os.makedirs(overlay_dir,exist_ok=True)
output_audio = os.path.join(overlay_dir, "original_audio.mp3")
final_video = os.path.join(overlay_dir, "final_video.mp4")


video_clip = VideoFileClip(source_video_path)
original_audio_clip = video_clip.audio
original_audio_clip.write_audiofile(output_audio)


background_audio_clip = AudioFileClip(source_audio_path)

w,h = video_clip.size
fps = video_clip.fps

intro_time = 5
intro_text_clip = TextClip("hello world",fontsize=70, color='white', size = video_clip.size)
intro_text_clip = intro_text_clip.set_fps(fps)
intro_text_clip = intro_text_clip.set_duration(intro_time)
intro_text_clip = intro_text_clip.set_pos("center")

intro_music = background_audio_clip.subclip(0, intro_time)
intro_text_clip = intro_text_clip.set_audio(intro_music)


watermark_size = 60
watermark_text_clip = TextClip("Aishwarya", fontsize = watermark_size,color='white',size=(w,watermark_size), align='East')
# size is the size of outer box for the text clip, align = east or west for left or right on the original video screen 
watermark_text_clip = watermark_text_clip.set_fps(fps)
watermark_text_clip = watermark_text_clip.set_pos("bottom")
watermark_text_clip = watermark_text_clip.set_duration(video_clip.duration)


overlay_clip = CompositeVideoClip([video_clip, watermark_text_clip], size = video_clip.size)
overlay_clip = overlay_clip.set_duration(video_clip.duration)
overlay_clip = overlay_clip.set_fps(fps)
overlay_clip = overlay_clip.set_audio(original_audio_clip)


final_clip = concatenate_videoclips([intro_text_clip, overlay_clip])
final_clip.write_videofile(final_video, codec= 'libx264', audio_codec = 'aac')


# final_clip = concatenate_videoclips([intro_text_clip, video_clip])
# overlay_clip = CompositeVideoClip([final_clip, watermark_text_clip] , size = video_clip.size)
# overlay_clip = overlay_clip.set_duration(final_clip.duration)
# overlay_clip = overlay_clip.set_fps(fps)
# # overlay_clip = overlay_clip.set_audio(original_audio_clip)
# overlay_clip.write_videofile(final_video, codec= 'libx264', audio_codec = 'aac')









