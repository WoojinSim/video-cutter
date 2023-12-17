# Run.py

import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
import multiprocessing
import logging

inputVideosPath = "./input-videos"
outputVideosPath = "./output-videos"
logging.getLogger("moviepy").setLevel(logging.WARNING)

def makeClipVideo(args):
    path, save_path, start_t, end_t = args
    clip_video = VideoFileClip(path).subclip(start_t, end_t)
    clip_video.write_videofile(save_path)
    print(f" - 영상 '{save_path}' 의 작업이 완료됐습니다.")

if __name__ == "__main__":
    print("\ninput-videos 폴더에서 파일들을 읽어들입니다...")
    inputFileList = os.listdir(path = inputVideosPath)
    for index in inputFileList: 
        print(f" - {index}")
    print(f"총 {len(inputFileList)}개의 파일이 인식됐습니다.\n비디오 자르기 작업을 시작합니다.\n\n")

    procs = []
    for index in inputFileList:
        args = (f"{inputVideosPath}/{index}", f"{outputVideosPath}/{index}", 20, 200)
        p = multiprocessing.Process(target = makeClipVideo, args = (args, ))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()

    print("\n\n완료!")
