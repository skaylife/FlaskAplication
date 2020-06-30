from flask import render_template
from app import app
import subprocess
import re
import win32api
import wmi
from ctypes import *


computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB


a = ('OS Name: {0}'.format(os_name))
b = ('OS Version: {0}'.format(os_version))
c = ('CPU: {0}'.format(proc_info.Name))
d = ('RAM: {0} GB'.format(system_ram))
e = ('Graphics Card: {0}'.format(gpu_info.Name))

# TwoMon = data[1]






@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu')
def menu():


    return render_template('menu.html')


@app.route('/about')
def about():


    return render_template('about.html')


@app.route('/test')
def test():


    return render_template('test.html')


@app.route('/page2')
def page2():
    proc = subprocess.Popen(['powershell', 'Get-WmiObject win32_desktopmonitor;'], stdout=subprocess.PIPE)
    res = proc.communicate()
    # monitors = re.findall('(?s)\r\nName\s+:\s(.*?)\r\n', res[0].decode("utf-8"))

    return render_template('page2.html')

    # return render_template('page2.html', monitors=monitors)

@app.route('/page3')
def page3():

    height = windll.user32.GetSystemMetrics(0)  # Высота монитора 1920 px
    width = windll.user32.GetSystemMetrics(1)  # Ширина монитора 1080 px


    # monitorss = win32api.EnumDisplayMonitors()
    # monitorsss = win32api.GetMonitorInfo(monitorss[0][0])
    #
    proc = subprocess.Popen(['powershell', 'Get-WmiObject win32_desktopmonitor;'], stdout=subprocess.PIPE)
    res = proc.communicate()
    monitors = re.findall('(?s)\r\nName\s+:\s(.*?)\r\n', res[0].decode(encoding='utf-8', errors='ignore'))

    # return render_template('page3.html', monitorsss=monitorsss, monitorss=monitorss, monitors=monitors)

    return render_template('page3.html', height=height, width=width, monitors=monitors, name=a, version=b, proc_info=c, system_ram=d, gpu=e)
    # return render_template('page3.html', height=height, width=width)


# return render_template('asset_information.html',
#                        username=user,
#                        password=password)

@app.route('/page4')
def page4():
    proc = subprocess.Popen(['powershell', 'Get-WmiObject win32_desktopmonitor;'], stdout=subprocess.PIPE)
    res = proc.communicate()
    # monitors = re.findall('(?s)\r\nName\s+:\s(.*?)\r\n', res[0].decode("utf-8"))

    return render_template('page4.html')

    # return render_template('page2.html', monitors=monitors)

@app.route('/page5')
def page5():


    return render_template('page5.html')



@app.route('/page6')
def page6():


    return render_template('page6.html')

@app.route('/page7')
def page7():


    return render_template('page7.html')


@app.route('/ColorBlack')
def ColorBlack():


    return render_template('ColorBlack.html')


@app.route('/ColorBlue')
def ColorBlue():


    return render_template('ColorBlue.html')


@app.route('/ColorGreen')
def ColorGreen():


    return render_template('ColorGreen.html')

@app.route('/ColorPurple')
def ColorPurple():


    return render_template('ColorPurple.html')

@app.route('/ColorRed')
def ColorRed():


    return render_template('ColorRed.html')


@app.route('/ColorWhite')
def ColorWhite():


    return render_template('ColorWhite.html')


