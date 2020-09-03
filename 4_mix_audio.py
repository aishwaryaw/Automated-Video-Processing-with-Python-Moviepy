from moviepy.editor import *
from moviepy.audio.fx.all import volumex
import os
from dir_structure import input_dir, output_dir

input_audio = os.path.join(input_dir, "audio.mp3")
input_video = os.path.join(input_dir, "sample.mp4")

mix_audio_dir = os.path.join(output_dir, "mixed_audio")
os.makedirs(mix_audio_dir,exist_ok=True)
output_original_audio = os.path.join(mix_audio_dir, "original_audio.mp3")
output_final_audio = os.path.join(mix_audio_dir, "final_audio.mp3")
final_video = os.path.join(mix_audio_dir, "final_video_with_mixed_audio.mp4")


# getting audio from the original video file
video_clip = VideoFileClip(input_video)
original_audio = video_clip.audio
original_audio.write_audiofile(output_original_audio)


# getting audio of the input audio file
audio_clip = AudioFileClip(input_audio)
bg_music = audio_clip.subclip(0, video_clip.duration)

# decreasing the volume of the audio
bg_music = bg_music.volumex(0.10)

final_audio = CompositeAudioClip([original_audio, bg_music])
final_audio.write_audiofile(output_final_audio, fps=original_audio.fps)


# here we are converting final audio file into audio clip and then setting the audio to video
# new_audio = AudioFileClip(output_final_audio)
# final_clip = video_clip.set_audio(new_audio)

# or we can use below code for directly setting the audio to video
final_video_clip = video_clip.set_audio(final_audio)
final_video_clip.write_videofile(final_video, codec = 'libx264', audio_codec = 'aac')








