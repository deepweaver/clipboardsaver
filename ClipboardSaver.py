#encoding=utf-8
import sys, os 
if sys.version_info < (3,0):
    reload(sys); 
    sys.setdefaultencoding( "utf-8" )
    input = raw_input

from tkinter import Tk; tk = Tk()
import time 
import argparse
parser = argparse.ArgumentParser(description='Save your clipboard, save your time!')
parser.add_argument('--path','-p', action='store', default='./', help='The history files will be stored here. e.g. --path /home/desktop/')
parser.add_argument('--sizelimit','-s', type=int, default='1024', help='The entire directory will be subject to this size limit(MB), if exceeded, the oldest file will be deleted.')
parser.add_argument('--timelimit', '-t', type=int, default='365', help='If you do not want a limit, 36500 will do :D')
parser.add_argument('--zip', '-z', action='store_true', default=False, help='compress old files')
# TODO: convert txt to zip to save storage
parser.add_argument('--zipasswd', '--zp', action='store', default=None, help='in case you want to send file to github and do not want people to see')
# parser.add_argument('--pack')
# if history file size <= 3MB or file reach one month limit
args = parser.parse_args() 
if not os.path.isdir(args.path):
    print("Invalid root path, your clipboard files will be stored in running directory!\n\
        Do you want to proceed? Y/N")
    ipt = input()
    ipt = 'y' if ipt == '' or ipt.lower() == 'y' else 'n'
    if ipt == 'n':
        sys.exit(0)
    else:
        args.path = os.path.abspath('.')
args.targetdir = os.path.join(args.path, 'cliphistory')
print(args.targetdir)
if not os.path.isdir(args.targetdir):
    os.makedirs(args.targetdir) 
print("History file will be in {}".format(args.targetdir))

x = None
oldday = None
while True:
    t = tk.selection_get(selection="CLIPBOARD")
    if x != t:
        x = t 
        thismonthfilename = args.targetdir + os.sep + time.strftime("%Y_%m") + ".txt"
        with open(thismonthfilename, 'a') as f:
            timestamp = time.strftime("Day%d %H:%M:%S", time.localtime()) 
            newday, daytime = timestamp.split(' ') 
            if newday != oldday:
                # print()
                f.write('_'*10 + newday + '_'*10 + '\n') 
                oldday = newday 
            f.write(daytime + '\n' + x + '\n\n')

    time.sleep(3)
# os.mkdirs




def checksize(): # remove zip files until args.targetdir size < args.sizelimit
    # os.path.getsize(args.path)
    # dirsize = getDirSize(args.targetdir)
    # if dirsize > args.sizelimit:
    dirfiles = os.listdir(args.targetdir)
    dirfiles.sort(reverse=True)
    for file in dirfiles:
        dirsize = getDirSize(args.targetdir)
        if dirsize < args.sizelimit:
            break
        else:
            if file.split('.')[-1] == 'zip':
                try:
                    os.remove(file)
                except Exception as err:
                    print(err)
    if dirsize >= args.sizelimit: # still!?
        print("Something's wrong...")
    # print(convert_bytes(dirsize))


def checktime():
    os.path.getsize(file)


def getDirSize(path):
    dirsize = 0
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            dirsize += getDocSize(os.path.join(root, name))
    dirsize /= (2**20) # bytes to mb
    return dirsize # as MB

def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return size
    except Exception as err:
        print(err)
        







