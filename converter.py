import os
import sys

bat_dir = os.path.abspath("mkv2mp4.bat")

try:
    import moviepy.editor as movpy
    import keyboard
except:
    if not 'moviepy' in sys.modules.keys():
        print(f'\nMissing moviepy module, installing now, please wait, thank you!')
        os.system('pip install moviepy -q -q -q')
        os.system('cls')
        os.system(f'call "{bat_dir}"')
    elif not 'keyboard' in sys.modules.keys():
        print(f'\nMissing keyboard module, installing now, please wait, thank you!')
        os.system('pip install keyboard -q -q -q')
        os.system('cls')
        os.system(f'call "{bat_dir}"')


mkv_dir = os.path.abspath("./files")
out_dir = os.path.abspath("./output")

def noAudio():
    for path, folder, files in os.walk(mkv_dir):
        if len(files) == 0:
                print('\nNo files found')
                print('\nPlease put some .mkv files in the files folder')
        else:
            pass
        for file in files:
            if file.endswith('.mkv'):
                mkv = file.split('.')
                fileName = mkv[0]
                print(f"\nFound file: {file}\n")
                clip = movpy.VideoFileClip(f'{mkv_dir}/{file}') #Reading .mkv file
                clip.write_videofile(f'{out_dir}/{fileName}.mp4', codec="libx264",audio=False) #Writing .mp4 file
                print(f"\nFinished converting {fileName}")
            else:
                pass


def withAudio():
    for path, folder, files in os.walk(mkv_dir):
        if len(files) == 0:
            print('\nNo files found')
            print('\nPlease put some .mkv files in the files folder')
        else:
            pass
        for file in files:
            if file.endswith('.mkv'):
                mkv = file.split('.')
                fileName = mkv[0]
                print(f"\nFound file: {file}\n")
                clip = movpy.VideoFileClip(f'{mkv_dir}/{file}') #Reading .mkv file
                clip.write_videofile(f'{out_dir}/{fileName}.mp4', codec="libx264",audio_codec="aac") #Writing .mp4 file
                print(f"\nFinished converting {fileName}")
            else:
                pass

while not keyboard.is_pressed('ctrl'):
    val = input('\nNeed audio in new mp4? (Y/N) ')
    if val.lower() == 'y':
        withAudio()

    elif val.lower() == 'n':
        noAudio()