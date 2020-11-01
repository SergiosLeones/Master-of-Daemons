#!/usr/bin/python3
# coding:utf-8
# Master of Daemons (MoD)
# Written by Sergio_Leone
# rev: 2020.10.x

import os
import re
import time
import os.path
from sys import argv
from datetime import datetime

#import sys                      ############################################
#from subprocess import *        # Отключение вывода трассировки при Ctrl+C #
#sys.tracebacklimit = 0          ############################################

def colored(color, mess):
        if color == 'inv':
                color = "\033[7m\033[1m"
        elif color == 'blue':
                color = "\033[36m\033[1m"
        elif color == 'green':
                color = "\033[32m\033[1m"
        elif color == 'yellow':
                color = "\033[33m\033[1m"
        elif color == 'red':
                color = "\033[31m\033[1m"
        else:
                color = "\033[37m\033[1m"

        colorMess = color+mess+"\033[0m"
        return colorMess

def clearLine(sec):
        time.sleep(sec)
        print ('')

def bye():
        clearLine(0.05)
        print (' > BYE!')
        clearLine(0.05)
        exit(0)

class List():
        def run(self):
                check = list.checkList()
                if check == True:
                        print (' > LIST FILE FOUND')
                else:
                        print (' > FILE DOES '+colored('red','NOT EXIST!'))
                        list.createList()
                        check = list.checkList()
                        if check == True:
                                print (' > LIST FILE '+colored('green','CREATED'))
                        else:
                                print (' > FILE CREATION '+colored('red','ERROR!'))
                                bye()

        def autorun(self):
                clearLine(1)
                print (' > CHECKING AUTORUN...')
                clearLine(0.05)
                count = sum(1 for line in open('MoD.list', 'r'))
                f = open('MoD.list')
                line = f.readlines()
                while count > 2:
                        count = count - 1
                        pid, path = line[count].split()
                        status = process.status(pid)
                        if status == True:
                                time.sleep(0.05)
                                print (' > DAEMON '+colored('blue',path)+' IS '+colored('green','RUNNING'))
                        else:
                                clearLine(1)
                                print (' > DAEMON '+colored('blue',path)+' WITH PID '+colored('yellow',pid)+' IS '+colored('red','NOT RUNNING!'))
                                time.sleep(0.05)
                                print (' > STARTING DAEMON '+colored('blue',path)) 
                                newpid = process.create(path)
                                if newpid != False:
                                        list.delList(pid)
                                        list.putList(path, newpid)
                f.close()
                clearLine(1)
                print (' > CHECKING DONE!')

        def checkList(self):
                clearLine(1)
                print (' > CHECKING THE LIST OF DAEMONS...')
                time.sleep(0.05)
                listState = os.path.isfile("MoD.list")
                return listState

        def createList(self):
                time.sleep(0.05)
                print (' > FILE CREATION...')
                time.sleep(0.05)
                nowT = datetime.now()
                timeNow = nowT.strftime("%d.%m.%Y %H:%M")
                f = open('MoD.list', 'w+')
                f.write(">>> LIST OF DAEMONS [created: "+timeNow+"]\n")
                f.write("-----------------------------------------------\n")
                f.close()

        def putList(self, path, pid):
                #list.run()
                clearLine(1)
                print (' > MAKE A NEW RECORD...')
                f = open('MoD.list', 'a')
                f.write(pid+' '+path+"\n")
                f.close()
                return 'true'

        def delList(self, pid):
                #list.run()
                clearLine(1)
                print (' > DELETE RECORD...')
                os.popen("sed -i '/^"+pid+"/d' MoD.list").read()
                return True

class Show():
        def hello(self):
                clearLine(0.05)
                print (' +----------------------------------------------------------------+')
                time.sleep(0.05)
                print (' |            '+colored('green','___________              __')+'                         |')
                time.sleep(0.05)
                print (' |           '+colored('green','/  __   __  \  ______    / /\______    ______')+'        |')
                time.sleep(0.05)
                print (' |          '+colored('green','/  / /  / /  /\/  __  \  / / /  __  \  /  __  \\')+'       |')
                time.sleep(0.05)
                print (' |         '+colored('green','/  / /  / /  / /  _____/\/ / /  /_/  /\/  / /  /\\')+'      |')
                time.sleep(0.05)
                print (' |        '+colored('green','/__/ /__/ /__/ /\______/ /_/ /\______/ /__/ /__/ /')+'      |')
                time.sleep(0.05)
                print (' |        '+colored('green','\__\/\__\/\__\/  \_____\/\_\/  \_____\/\__\/\__\/')+'       |')
                time.sleep(0.05)
                print (' |       '+colored('red','____________')+'                                             |')
                time.sleep(0.05)
                print (' |      '+colored('red','/____   ____/\______    ________  ___________')+'             |')
                time.sleep(0.05)
                print (' |      '+colored('red','\___/  /\___\/  __  \  /  __   /\/  __   __  \\')+'            |')
                time.sleep(0.05)
                print (' |         '+colored('red','/  / /   /  _____/\/  __   / /  / /  / /  /\\')+'           |')
                time.sleep(0.05)
                print (' |        '+colored('red','/__/ /    \______/ /__/ /__/ /__/ /__/ /__/ /')+'           |')
                time.sleep(0.05)
                print (' |        '+colored('red','\__\/      \_____\/\__\/\__\/\__\/\__\/\__\/')+'            |')
                time.sleep(0.05)
                print (' |                                                                |')
                time.sleep(0.05)
                print (' |                                                                |')
                time.sleep(0.05)
                print (' |      Welcome to MASTER OF DAEMONS [MoD]                        |')
                time.sleep(0.05)
                print (' |                                                                |')
                time.sleep(0.05)
                print (' |      Tested on DEBIAN 8 releases                               |')
                time.sleep(0.05)
                print (' |                                                                |')
                time.sleep(0.05)
                print (' |      Written by Sergio_Leone                                   |')
                time.sleep(0.05)
                print (' |                                                                |')
                time.sleep(0.05)
                print (' |      rev: 2020.10.27                                           |')
                time.sleep(0.05)
                print (' |                                                                |')
                time.sleep(0.05)
                print (' +----------------------------------------------------------------+')

        def help(self):
                clearLine(0.05)
                print (' +----------------------------------------------------------------+')
                time.sleep(0.05)
                print (' |      ABOUT THE FUNCTIONALITY OF THE PROGRAM:                   |')
                time.sleep(0.05)
                print (' +----------------------------------------------------------------+')
                show.back()

        def menu(self):
                clearLine(1)
                print (" > "+colored('inv',"[MoD]")+" MENU")
                clearLine(0.05)
                print (' 1 - SHOW daemons')
                time.sleep(0.05)
                print (' 2 - CREATE daemon')
                time.sleep(0.05)
                print (' 3 - KILL the daemon')
                time.sleep(0.05)
                print (' 0 - READ me')
                print (' (press ENTER to EXIT)')

        def enter(self):
                clearLine(0.05)
                enter = input(' Enter > ')
                return enter

        def list(self):
                time.sleep(1)
                with open("MoD.list") as file:
                        fileData = file.read()
                        time.sleep(0.05)
                        print ("\n"+colored('',fileData))
                show.back()

        def back(self):
                clearLine(0.05)
                back = input(' Press ENTER to return > ')
                show.menu()
                inp.menu()

        def backErr(self):
                clearLine(0.05)
                print (' > OPERATION '+colored('red','CANCELED!')+' RETURN BACK...')
                show.menu()
                inp.menu()

class Inp():
        def menu(self):
                enter = show.enter()
                if enter == '1':
                        list.run()
                        show.list()
                elif enter == '2':
                        inp.create()
                elif enter == '3':
                        inp.kill()
                elif enter == '0':
                        show.help()
                else:
                        bye()
                        #clearLine(0.05)
                        #print (' > SELECTION '+red('ERROR!')+' TRY AGAIN...')
                        #show.menu()
                        #inp.menu()

        def create(self):
                clearLine(1)
                print (' > Enter the '+colored('blue','PATH')+' to the script:')
                enter = show.enter()
                if enter == '':
                        show.backErr()
                pid = process.create(enter)
                time.sleep(0.05)
                status = list.putList(enter, pid)
                if status == 'true':
                        print (' > RECORDING COMPLETED')
                else:
                        print (' > WRITE '+colored('red','ERROR!'))
                show.list()

        def kill(self):
                clearLine(1)
                print (' > Enter the daemon '+colored('yellow','PID')+':')
                enter = show.enter()
                if enter == '':
                        show.backErr()
                process.kill(enter)
                show.list() 

class Process():
        def status(self, pid):
                command = 'ps -p '+pid
                stat = os.popen(command).read()
                count = stat.count('\n')
                if not stat.endswith('\n'):
                        count += 1
                if count == 2:
                        return True
                else:
                        return False

        def create(self, script):
                command = 'nohup /usr/bin/php /home/sergio/test.php > /dev/null 2>&1 & echo $!'
                clearLine(1) 
                pid = os.popen(command).read()
                pid = re.sub("^\s+|\n|\r|\s+$", '', pid) # Удаляем перенос строки
                status = process.status(pid)
                if status == True:
                        print (' > DAEMON IS '+colored('green','RUNNING!'))
                        time.sleep(0.05)
                        print (' > DAEMON PATH: '+colored('blue',script))
                        time.sleep(0.05)
                        print (' > DAEMON ASSIGNED PID: '+colored('yellow',pid))
                        return pid
                else:
                        print (' > DAEMON IS '+colored('red','NOT RUNNING!'))
                        return False

        def kill(self, enter):
                command = 'kill '+enter
                clearLine(1) 
                status = process.status(enter)
                if status != True:
                        print (' > DAEMON WITH PID '+colored('yellow',enter)+' DOES '+colored('red','NOT EXIST!'))
                else:
                        print (' > DAEMON WITH PID '+colored('yellow',enter)+' FOUND')
                        time.sleep(0.05)
                        os.popen(command).read()
                        status = process.status(enter)
                        if status == True:
                                print (' > '+colored('red','ERROR!')+' DAEMON IS NOT KILLED!')
                        else:
                                print (' > DAEMON '+colored('red','KILLED'))
                                status = list.delList(enter)
                                if status == True:
                                        print (' > RECORD DELETED')
                                else:
                                        print (' > '+colored('red','ERROR!')+' RECORD IS NOT DELETED!')

# START

show = Show()
list = List()
process = Process()
inp = Inp()

mode = argv     # Принимаем аргумент

try:
        mode[1]
except IndexError:
        mode = None

if mode == None:        # Если аргумента НЕТ
        show.hello()
        list.run()
        list.autorun()
        show.menu()
        inp.menu()
else:                   # Если аргумент ЕСТЬ
        list.run()
        list.autorun()
        bye()
