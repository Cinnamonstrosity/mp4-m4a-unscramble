import os
import glob
from mutagen.id3 import ID3, TIT2
from mutagen.mp4 import MP4Tags, MP4
import shutil


forbidden = "\/:*?<>|"
dest1 = 'E:/Music'


def foldermagic():
    for mp3files in glob.glob('E:/Music/*/*.mp3', recursive=True):#renames all files in a directory with their actual name
        try:
            rawstring = ID3(mp3files)['TIT2']
        except KeyError:
            print("Caught a KeyError!")
            rawstring = ID3(mp3files)['TPE1']
        for k in forbidden:
            rawstring = str(rawstring).replace(k, '')
        print("Rawstring =", rawstring)
        try:
            os.rename(mp3files, u'E:/Music\%s.mp3' % rawstring)
            print("-----------------------------------------------------")
            #print("File", mp3files["TIT2"], "was processed successfully.")
            print("-----------------------------------------------------")
            input()
        except:
            print("Failed to rename file")
            print("This file is called %s" % mp3files)
            print("-----------------------------------------------------")


def m4a_move(): #tidies up leftover m4a files into a folder "m4a_folder"
    for m4a_files in glob.glob('E:/Music/*/*.m4a'):
        m4a_file_name = str(MP4(m4a_files)['\xa9nam'])[2:-2]
        for l in forbidden:
            m4a_file_name = str(m4a_file_name).replace(l, '')
        shutil.move(m4a_files, r'E:/Music/m4a_folder/%s.m4a' % m4a_file_name)
        print("File %s moved successfully!" % m4a_file_name)


def tidyup():
    pass


def menu(): #our starting menu
    print("-----------------------------------------------------")
    print("Enter 'r' for rename")
    print("Enter 'm4a' for moving m4a files")
    choice = input("What do you want to do? > ")
    if choice == "r":
        foldermagic()
    elif choice == "m4a":
        m4a_move()
    elif choice == "tidyup":
        tidyup()
    else:
        print("You entered something wrong, go again.")
        menu()

menu()
