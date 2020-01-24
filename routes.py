from flask import render_template
from app import app
import subprocess
import re
import win32api
from ctypes import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    proc = subprocess.Popen(['powershell', 'Get-WmiObject win32_desktopmonitor;'], stdout=subprocess.PIPE)
    res = proc.communicate()
    monitors = re.findall('(?s)\r\nName\s+:\s(.*?)\r\n', res[0].decode("utf-8"))

    return render_template('page2.html', monitors=monitors)

@app.route('/page3')
def page3():

    height = windll.user32.GetSystemMetrics(0)  # Высота монитора 1920 px
    width = windll.user32.GetSystemMetrics(1)  # Ширина монитора 1080 px
    # monitorss = win32api.EnumDisplayMonitors()
    # monitorsss = win32api.GetMonitorInfo(monitorss[0][0])
    #
    proc = subprocess.Popen(['powershell', 'Get-WmiObject win32_desktopmonitor;'], stdout=subprocess.PIPE)
    res = proc.communicate()
    monitors = re.findall('(?s)\r\nName\s+:\s(.*?)\r\n', res[0].decode("utf-8"))

    # return render_template('page3.html', monitorsss=monitorsss, monitorss=monitorss, monitors=monitors)
    return render_template('page3.html', height=height, width=width, monitors=monitors)


# return render_template('asset_information.html',
#                        username=user,
#                        password=password)
