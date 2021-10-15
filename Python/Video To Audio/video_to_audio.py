# Import moviepy
import moviepy.editor

# Defining the Video Clip
videoClip = moviepy.editor.VideoFileClip("./video.mp4")

# Extracting the Audio
audioClip = videoClip.audio.write_audiofile("./audio.mp3")
