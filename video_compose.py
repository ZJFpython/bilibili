from moviepy.editor import *
import os

L = []

for root, dirs, files in os.walk("E://video/新建文件夹"):
    files.sort()
    for file in files:
        if os.path.splitext(file)[1] == '.mp4':
            print(file)
            filePath = os.path.join(root, file)
            print(filePath)
            video = VideoFileClip(filePath)
            L.append(video)
final_clip = concatenate_videoclips(L)
final_clip.to_videofile("E://video/新建文件夹/target.mp4", fps=24, remove_temp=False)
