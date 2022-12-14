"""
Written by Benjamin Jack Cullen aka Holographic_Sol

Mechanized application template. Creates a grid of objects, creates modules containing functions pertaining to the objects and plugs the objects
into the modules created.

No need to move objects around tweaking geometries etc. No need to plug them in. Better workflow.
Object workflow: show/hide/repurpose/etc.
Blow it up, then go inside and grill some food.

1. Dial in Configuration 1 & 2 values according to desired specs.
2. Run. (objects will be automatically created in a grid and automatically plugged into automatically created modules).
3. Turn off auto_setup to ensure any changes made to the automatically created modules will not be overwritten.
4. Click something, it's all plugged in and ready.
5. Go ahead and start writing code straight into the mechanically created modules:
    auto_gen_btnx_function.py
    auto_gen_btnx_double_function.py
    auto_gen_btnx_title_toolbar_functions.py
    auto_gen_qle_returnpressed_connect_function.py
    auto_gen_qle_double_returnpressed_connect_function.py
    auto_gen_tbx_update_function.py

WARNING! SETTING auto_setup TRUE WILL WIPE ANY POTENTIAL PROGRESS MADE TO THE MECHANIZED MODULES CREATED. IF CHANGES
HAVE BEEN MADE TO AUTOGEN MODULES, BACK UP APERTAINING AUTOGEN MODULES BEFORE SETTING auto_setup TRUE.

"""

import os
from superglobals import *
# import sol_module as sol
import sys
import time
import datetime
import subprocess
import win32com.client
from importlib import reload
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QCursor, QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QDesktopWidget
from PyQt5.QtCore import Qt, QThread, QSize, QPoint, QCoreApplication, QTimer
from PyQt5.QtMultimedia import *
# import auto_gen_tbx_update_function
import defcon_scraper_module
import nasa_climate
import module_help

thread_nuclear_strike_imminent = []
defcon_update_time = 180
prev_defcon_level = []
i = 0
while i < 9:
    prev_defcon_level.append(None)
    i += 1
nasa_update_time = 3600

# Initialize Notification Player_default In Memory
player_url_default = QUrl.fromLocalFile("./resources/audio/nuke_siren_0.mp3")
player_content_default = QMediaContent(player_url_default)
player_default = QMediaPlayer()
player_default.setMedia(player_content_default)
player_default.setVolume(100)
mute_default_player = False

# Initialize Notification Player 0
player_url_0 = QUrl.fromLocalFile("./resources/audio/hud_7.mp3")
player_content_0 = QMediaContent(player_url_0)
player_0 = QMediaPlayer()
player_0.setMedia(player_content_0)
player_0.setVolume(100)

# CONFIGURATION 1 - SETUP APPLICATION TEMPLATE BOOLEAN
auto_setup = False  # WARNING (SET FALSE IF AFTER SETUP IS COMPLETE OR MODULES WILL BE OVERWRITTEN).
auto_generate = True  # creates objects automatically using values below.
auto_generate_btn = True  # enables automatic button creation. plugged in automatically to automatically created module.
auto_generate_btn_double = True
auto_generate_lbl = True
auto_generate_qle = True
auto_generate_qle_double = True
auto_generate_tb = True
enable_title_bar_toolbar = True  # enables toolbar creation.
debug_verbosity_bool = False  # enables verbose output
debug_enable_bool = True
pin_to_taskbar = False
configuration_override_size = False  # enables app_width_static and app_height_static to be set manually.
reserve_btnx_bool = False
reserve_btnx_double_bool = False
bool_switch_run_at_startup = False

# CONFIGURATION 2 - SETUP APPLICATION TEMPLATE GEOMETRY
app_width_static, app_height_static = 400, 200  # application window size
main_border_height = 2
titlebar_height = 28
btn_size_titlebar = 24
btnx_position_initialize_x, btnx_position_initialize_y = 0, 0  # offset button position
btnx_size = 100  # set button size
btnx_size_Y = btnx_size
btnx_sp_size = 4  # set button spacing
btnx_sp_size_Y = btnx_sp_size
turn_page_reserved = [0]
btnx_gen_max = 48  # maximum number of buttons to create (ensure btnx_gen_max is equally divisible by btnx_row_idx_max)
btnx_row_idx_max = 6  # maximum number of buttons in a row
reserve_btnx_double = []

top_row = []
def formula_top_row_dbl():
    i = 0
    i_2 = 0
    while i < btnx_row_idx_max:
        if i_2 == 0:
            top_row.append(i)
            reserve_btnx_double.append(i)
            i_2 = 1
        elif i_2 == 1:
            i_2 = 0
        i += 1
    print('top_row:', top_row)
formula_top_row_dbl()

lower_row = []
def formula_lower_row_dbl():
    i = btnx_gen_max - btnx_row_idx_max
    i_2 = 0
    while i < btnx_gen_max:
        if i_2 == 0:
            lower_row.append(i)
            reserve_btnx_double.append(i)
            i_2 = 1
        elif i_2 == 1:
            i_2 = 0
        i += 1
    print('lower_row:', lower_row)
formula_lower_row_dbl()

left_column = [0]
def formula_left_column_dbl():
    i = 0
    i_2 = 1
    while i < btnx_gen_max:
        if i == (btnx_row_idx_max * i_2):
            left_column.append(i)
            reserve_btnx_double.append(i)
            i_2 += 1
        i += 1
    print('left_column:', left_column)
formula_left_column_dbl()

right_column = []
def formula_right_column_dbl():
    i = 0
    i_2 = 1
    while i < btnx_gen_max:
        if i == ((btnx_row_idx_max * i_2) - 2):
            right_column.append(i)
            reserve_btnx_double.append(i)
            i_2 += 1
        i += 1
    print('right_column:', right_column)
formula_right_column_dbl()

non_reserve_non_overlap_group_0 = []
def formula_non_reserve_non_overlap_group_0():
    i = 0
    i_2 = 1
    while i < btnx_gen_max:
        if i == ((btnx_row_idx_max * i_2) - 2):
            i_2 += 1
        elif i not in reserve_btnx_double:
            valid = True
            for _ in reserve_btnx_double:
                if i == (_ + 1):
                    valid = False
                if (i + 1) in right_column:
                    valid = False
            if valid is True:
                non_reserve_non_overlap_group_0.append(i)
        i += 1
    print('non_reserve_non_overlap_group_0:', non_reserve_non_overlap_group_0)
formula_non_reserve_non_overlap_group_0()

reserve_lblx = []
reserve_qlex = []
reserve_qlex_double = []
reserve_tbx = []
title_bar_toolbar_w = 56
title_bar_toolbar_h = 24
title_bar_toolbar_sp = 4

btnx_master = []
btnx_master.append([btnx_gen_max, btnx_row_idx_max, btnx_position_initialize_x, btnx_position_initialize_y, btnx_size, btnx_size_Y, btnx_sp_size, btnx_sp_size_Y])

# amend stylesheet according to above specifications.

if os.path.exists('./sol_style.py'):
    style_line = []
    write_new_stylesheet = True

    # read stylesheet file
    with open('./sol_style.py', 'r') as fo:
        for line in fo:
            line = line.strip()

            # append any lines to list that are not main_border_height line.
            if not line.startswith('main_border_height = '):
                style_line.append(line)
            else:
                # append main_border_height line to list conditionally.
                if not line == 'main_border_height = ' + str(main_border_height):
                    style_line.append(str('main_border_height = ') + str(main_border_height))
                # if main_border_height in file equal to main_border_height above then do not ammend stylesheet.
                elif line == 'main_border_height = ' + str(main_border_height):
                    write_new_stylesheet = False
    fo.close()

    # amend stylesheet if main_border_height has changed.
    if write_new_stylesheet is True:
        open('./sol_style.py.tmp', 'w').close()
        with open('./sol_style.py.tmp', 'a') as fo:
            for _ in style_line:
                fo.write(_ + '\n')
        fo.close()

        # replace stylesheet with temp.
        os.replace('./sol_style.py.tmp', './sol_style.py')
    del style_line

# reload stylesheet module
import sol_style
reload(sol_style)

# initiation
tb_message = []
event_filter_self = []
shell = win32com.client.Dispatch("WScript.Shell")
pid_main = os.getpid()
print(str('[' + str(datetime.datetime.now()) + '] [pid_main]' + str(pid_main)))
print(str('[' + str(datetime.datetime.now()) + '] initializing application'))
program_fname = os.path.basename(__file__)
program_fname_no_suffix = program_fname.replace('.py', '')
print(str('[' + str(datetime.datetime.now()) + '] [program_fname] ' + str(program_fname)))
cwd = os.getcwd() + '\\'

# subprocess arguments
info = subprocess.STARTUPINFO()  # Subprocess Control
info.dwFlags = 1
info.wShowWindow = 0

# use high dpi scaling and high dpi pixel maps if available
if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    print(str('[' + str(datetime.datetime.now()) + '] AA_EnableHighDpiScaling: True'))
elif not hasattr(Qt, 'AA_EnableHighDpiScaling'):
    print(str('[' + str(datetime.datetime.now()) + '] AA_EnableHighDpiScaling: False'))
if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    print(str('[' + str(datetime.datetime.now()) + '] AA_UseHighDpiPixmaps: True'))
elif not hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    print(str('[' + str(datetime.datetime.now()) + '] AA_UseHighDpiPixmaps: False'))

# cursor tracking
cur_pos_x = 0
cur_pos_y = 0
self_pos_x = 0
self_pos_y = 0
app_w = 0
app_h = 0
app_x_range = False
app_y_range = False
app_range_xy = False
titlebar_range_xy = False
user_mouse_activity = False

# boolean
first_load = True
app_display_default_bool = True
app_display_stays_on_top_bool = False
app_display_stays_on_bottom_bool = False

# strings prev_event = ''

# lists
class_0_thread = []
ui_object_complete = []
obj_geo_item = []
obj_icon_geo = []
obj_icon = []
ui_object_font_list_s6b = []
ui_object_font_list_s7b = []
ui_object_font_list_s8b = []
ui_object_font_list_s9b = []
debug_messages = []
btnx_var = []
lblx_var = []
btnx_double_var = []
qlex_var = []
qlex_double_var = []
tbx_var = []
btnx_titlebar_toolbar_var = []
tbx_message = []
tbx_timer = []
btnx_double_timer = []
btnx_double_timer_sub = []
btnx_timer = []
btnx_timer_sub = []

# integers
avail_w, avail_h = 2, 2
prev_multiplier_w, prev_multiplier_h = 1, 1
pos_w_prev, pos_h_prev = 2, 2


class ObjEveFilter(QObject):
    def eventFilter(self, obj, event):

        global event_filter_self
        global app_range_xy
        global debug_messages, debug_enable_bool, debug_verbosity_bool
        global app_height_static
        global pos_w_prev, pos_h_prev
        global pin_to_taskbar
        
        obj_eve = obj, event

        # verbose level 2
        # print('-- ObjEveFilter(QObject).eventFilter(self, obj, event):', obj_eve)
        # debug_messages.append(str(datetime.datetime.now()) + ' [ObjEveFilter] object:' + str(obj) + ' event: ' + str(event))

        # verbose level 1
        # if app_range_xy is True:
        #     if debug_enable_bool is True:
        #         if debug_verbosity_bool is True:
                    # print('-- ObjEveFilter(QObject).eventFilter(self, obj, event):', obj_eve)
                    # debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter] object:' + str(obj) + ' event: ' + str(event)))

        # scaling geometry
        pos_w = (QDesktopWidget().availableGeometry().width())
        pos_h = (QDesktopWidget().availableGeometry().height())
        if str(obj_eve[1]).startswith('<PyQt5.QtGui.QResizeEvent') or str(obj_eve[1]).startswith(
                '<PyQt5.QtGui.QMoveEvent'):
            self.scaling_geometry_function()

        # taskbar tracking
        if pos_w != pos_w_prev or pos_h != pos_h_prev:
            print(str('[' + str(datetime.datetime.now()) + '] taskbar may have changed position/resized or other event'))
            pos_w_prev = pos_w
            pos_h_prev = pos_h
            
            # set application window geometry
            if pin_to_taskbar is True:
                app_height_pos = int(QDesktopWidget().availableGeometry().height()) - int(app_height_static)
                event_filter_self[0].setGeometry(0, app_height_pos, app_width_static, app_height_static)
            elif pin_to_taskbar is False:
                app_height_pos = int(QDesktopWidget().availableGeometry().height() / 2) - int(app_height_static / 2)
                app_width_pos = int(QDesktopWidget().availableGeometry().width() / 2) - int(app_width_static / 2)

        return False

    def scaling_geometry_function(self):
        global event_filter_self
        global first_load
        global avail_w, avail_h
        global prev_multiplier_w, prev_multiplier_h
        global ui_object_complete, obj_geo_item, obj_icon_geo, obj_icon
        global ui_object_font_list_s6b, ui_object_font_list_s7b, ui_object_font_list_s8b, ui_object_font_list_s9b
        global debug_messages, debug_enable_bool
        global app_width_static, app_height_static

        # runs once on startup: loads all geometries into separate lists
        if first_load is True:
            first_load = False
            for _ in ui_object_complete:
                obj_geo_width = _.geometry().width()
                obj_geo_height = _.geometry().height()
                obj_geo_pos_w = _.geometry().x()
                obj_geo_pos_h = _.geometry().y()
                var = obj_geo_width, obj_geo_height, obj_geo_pos_w, obj_geo_pos_h
                obj_geo_item.append(var)
                try:
                    obj_icon_geo.append(_.iconSize())
                    obj_icon.append(_)
                except:
                    pass

        # get available geometry
        new_avail_w = QDesktopWidget().availableGeometry().width()
        new_avail_h = QDesktopWidget().availableGeometry().height()

        # obtain a multiplier from the available geometry
        if new_avail_w >= 1000 and new_avail_h >= 1000:
            multiplier_h = int(str(new_avail_h)[0])
        elif new_avail_w < 1000 and new_avail_h < 1000:
            multiplier_h = 1
        else:
            multiplier_h = 1
        multiplier_w = multiplier_h

        # check if multiplier has changed
        if prev_multiplier_w != multiplier_w or prev_multiplier_h != multiplier_h or new_avail_w != avail_w or new_avail_h != avail_h:
            # if debug_enable_bool is True:
                # if debug_verbosity_bool is True:
                #     debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] adjusting application to fit screen geometry'))
                #     debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] prev_multiplier_w: ' + str(prev_multiplier_w)))
                #     debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] prev_multiplier_h: ' + str(prev_multiplier_h)))

            # set new available geometry
            avail_h = new_avail_h
            avail_w = new_avail_w

            # set new application geometry using multiplier
            app_width = app_width_static * multiplier_w
            app_height = app_height_static * multiplier_h

            # if debug_enable_bool is True:
            #     if debug_verbosity_bool is True:
            #         debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] new application app_width: ' + str(app_width)))
            #         debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] new application app_height: ' + str(app_height)))

            # centre application on the screen
            pos_w = (QDesktopWidget().availableGeometry().width())
            pos_h = (QDesktopWidget().availableGeometry().height())

            # if debug_enable_bool is True:
            #     if debug_verbosity_bool is True:
            #         debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] new application pos_w: ' + str(pos_w)))
            #         debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] new application pos_h: ' + str(pos_h)))
            #         debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] attempting to set application geometry'))

            # set application window geometry
            if pin_to_taskbar is True:
                app_height_pos = int(QDesktopWidget().availableGeometry().height()) - int(app_height_static)
                event_filter_self[0].setGeometry(0, app_height_pos, app_width_static, app_height_static)
            elif pin_to_taskbar is False:
                app_height_pos = int(QDesktopWidget().availableGeometry().height() / 2) - int(app_height_static / 2)
                app_width_pos = int(QDesktopWidget().availableGeometry().width() / 2) - int(app_width_static / 2)
                event_filter_self[0].setGeometry(app_width_pos, app_height_pos, app_width_static, app_height_static)
                
            # if debug_enable_bool is True:
            #     if debug_verbosity_bool is True:
            #         debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] now attempting to set object geometries'))
            
            # set application object geometries
            i = 0
            for _ in ui_object_complete:

                # Default Width
                obj_w = obj_geo_item[i]
                obj_w = obj_w[0]

                # Default Height
                obj_h = obj_geo_item[i]
                obj_h = obj_h[1]

                # Default Position Width
                obj_pos_w = obj_geo_item[i]
                obj_pos_w = obj_pos_w[2]

                # Default Position Height
                obj_pos_h = obj_geo_item[i]
                obj_pos_h = obj_pos_h[3]

                # display last know object geometries
                # if debug_enable_bool is True:
                #     if debug_verbosity_bool is True:
                #         debug_messages.append(
                #             str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] last geometry: ' +
                #                 str(_) + ' ' + str(obj_w) + ' ' + str(obj_h) + ' ' + str(obj_pos_w) + ' ' + str(obj_pos_h)))
                
                # set new object geometries using multiplier
                new_obj_w = obj_w * multiplier_w
                new_obj_h = obj_h * multiplier_h
                new_obj_pos_w = obj_pos_w * multiplier_w
                new_obj_pos_h = obj_pos_h * multiplier_h
                # if debug_enable_bool is True:
                #     if debug_verbosity_bool is True:
                #         debug_messages.append(
                #             str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] new geometry: ' +
                #                 str(_) + ' ' + str(new_obj_w) + ' ' + str(new_obj_h) + ' ' + str(new_obj_pos_w) + ' ' + str(new_obj_pos_h)))

                # move and resize object geometries using new geometries
                _.move(new_obj_pos_w, new_obj_pos_h)
                _.resize(new_obj_w, new_obj_h)
                i += 1

            # set icon geometries
            i = 0
            for _ in obj_icon_geo:
                try:
                    # obtain last known geometries
                    geo_var = str(_)
                    geo_var = geo_var.replace('PyQt5.QtCore.QSize(', '')
                    geo_var = geo_var.replace(')', '')
                    geo_var = geo_var.replace(',', '')
                    geo_var_split = geo_var.split()
                    icon_sz_w = int(geo_var_split[0])
                    icon_sz_h = int(geo_var_split[1])
                    # if debug_enable_bool is True:
                    #     if debug_verbosity_bool is True:
                    #         debug_messages.append(
                    #             str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] original icon_sz_w: ' + str(icon_sz_w) +
                    #                 '  original icon_sz_h: ' + str(icon_sz_h)))

                    # set new geometries using multipliers
                    icon_size_w = icon_sz_w * multiplier_w
                    icon_size_h = icon_sz_h * multiplier_h
                    # if debug_enable_bool is True:
                    #     if debug_verbosity_bool is True:
                    #         debug_messages.append(
                    #             str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] [multiply result] new icon_sz_w: ' + str(icon_size_w) +
                    #                 '  new icon_sz_h: ' + str(icon_size_h)))
                    obj_icon[i].setIconSize(QSize(icon_size_w, icon_size_h))

                except Exception as e:
                    print(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] object icon size may be inapplicable: ' + str(_) + ' ' + str(e)))
                    # if debug_enable_bool is True:
                    #     if debug_verbosity_bool is True:
                    #         debug_messages.append(str('[' + str(datetime.datetime.now()) +
                    #                                   '] [ObjEveFilter.eventFilter] object icon size may be inapplicable: ' + str(_) + ' ' + str(e)))
                i += 1

            # set font geometries using multipliers
            font_size_6b = int(6 * multiplier_h)
            font_size_7b = int(7 * multiplier_h)
            font_size_8b = int(8 * multiplier_h)
            font_size_9b = int(9 * multiplier_h)
            font_s6b = QFont("Segoe UI", (font_size_6b), QFont.Bold)
            font_s7b = QFont("Segoe UI", (font_size_7b), QFont.Bold)
            font_s8b = QFont("Segoe UI", (font_size_8b), QFont.Bold)
            font_s9b = QFont("Segoe UI", (font_size_9b), QFont.Bold)
            for _ in ui_object_font_list_s6b:
                _.setFont(font_s6b)
            for _ in ui_object_font_list_s7b:
                _.setFont(font_s7b)
            for _ in ui_object_font_list_s8b:
                _.setFont(font_s8b)
            for _ in ui_object_font_list_s9b:
                _.setFont(font_s9b)

            # finally change previously known multipliers to current multipliers
            prev_multiplier_w = multiplier_w
            prev_multiplier_h = multiplier_h

            # if debug_enable_bool is True:
            #     debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [ObjEveFilter.eventFilter] ui geometry made it through the blender'))


class App(QMainWindow):
    cursorMove = pyqtSignal(object)

    def __init__(self):
        super(App, self).__init__()
        global btnx_var
        global event_filter_self, ui_object_complete
        global ui_object_font_list_s6b, ui_object_font_list_s7b, ui_object_font_list_s8b, ui_object_font_list_s9b
        global debug_enable_bool, debug_messages
        global app_height_static, app_width_static
        global auto_generate, enable_title_bar_toolbar

        self.thread_0 = Class0()
        self.thread_1 = Class1()

        def function_mute_default_player():
            global mute_default_player
            if mute_default_player is False:
                mute_default_player = True
            else:
                mute_default_player = False
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [SYSTEM] mute_default_player: ' + str(mute_default_player)))

        # initiate some basics
        self.setWindowIcon(QIcon(cwd + 'icon.ico'))
        self.title = 'DEFCON ALERT SYSTEM'
        self.setWindowTitle(self.title)

        # main window color & window frame style
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setPalette(p)

        # Stylesheet: self
        self.setStyleSheet(sol_style.self_style)

        # initialize fonts
        self.font_s6b = QFont("Segoe UI", 6, QFont.Bold)
        self.font_s7b = QFont("Segoe UI", 7, QFont.Bold)
        self.font_s8b = QFont("Segoe UI", 8, QFont.Bold)
        self.font_s9b = QFont("Segoe UI", 9, QFont.Bold)

        # initiate object event filter
        event_filter_self.append(self)
        self.filter = ObjEveFilter()
        
        # cursor tracking
        self.cursorMove.connect(self.handle_cursor_move)
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.poll_cursor)
        self.timer.start()
        self.cursor = None

        # button: logo (use main_border_height)
        self.btn_title_logo = QPushButton(self)
        self.btn_title_logo.move(main_border_height, main_border_height)
        self.btn_title_logo.resize(btn_size_titlebar, btn_size_titlebar)
        self.btn_title_logo.setIcon(QIcon("./icon.ico"))
        self.btn_title_logo.setIconSize(QSize(titlebar_height, titlebar_height))
        self.btn_title_logo.setStyleSheet(sol_style.btn_title_bar_style)
        self.btn_title_logo.installEventFilter(self)
        ui_object_complete.append(self.btn_title_logo)

        self.titel_label = QLabel(self)
        self.titel_label.move(main_border_height + btn_size_titlebar + 2, main_border_height)
        self.titel_label.resize((btnx_size * 4) + btnx_sp_size, 24)
        self.titel_label.setText('DEFCON ALERT SYSTEM')
        self.titel_label.setStyleSheet("""QLabel{background-color: rgb(0, 0, 0);
                    color: rgb(255, 255, 255);
                    border-top:2px solid rgb(0, 0, 0);
                    border-bottom:2px solid rgb(0, 0, 0);
                    border-right:2px solid rgb(0, 0, 0);
                    border-left:2px solid rgb(0, 0, 0);}""")
        ui_object_complete.append(self.titel_label)
        self.titel_label.installEventFilter(self.filter)

        self.base_label_0 = QLabel(self)
        self.base_label_0.move(main_border_height, main_border_height + (btn_size_titlebar * 2) + 6)
        self.base_label_0.resize(632 - (main_border_height*2), 938 - (main_border_height*2) - (btn_size_titlebar * 2) - 6)
        self.base_label_0.setStyleSheet("""QLabel{background-color: rgb(12, 12, 12);
                    color: rgb(255, 255, 255);
                    border-top:2px solid rgb(0, 0, 0);
                    border-bottom:2px solid rgb(0, 0, 0);
                    border-right:2px solid rgb(0, 0, 0);
                    border-left:2px solid rgb(0, 0, 0);}""")
        self.base_label_0.setAlignment(Qt.AlignCenter)
        ui_object_complete.append(self.base_label_0)
        self.base_label_0.installEventFilter(self.filter)

        self.titel_label_system = QLabel(self)
        self.titel_label_system.move(main_border_height, main_border_height + (btn_size_titlebar * 3) + 2)
        self.titel_label_system.resize((btnx_size * 6) + (btnx_sp_size * 7), 24)
        self.titel_label_system.setText('SYSTEM')
        self.titel_label_system.setAlignment(Qt.AlignCenter)
        self.titel_label_system.setStyleSheet("""QLabel{background-color: rgb(0, 0, 0);
                    color: rgb(255, 255, 255);
                    border-top:2px solid rgb(0, 0, 0);
                    border-bottom:2px solid rgb(0, 0, 0);
                    border-right:2px solid rgb(0, 0, 0);
                    border-left:2px solid rgb(0, 0, 0);}""")
        ui_object_complete.append(self.titel_label_system)
        self.titel_label_system.installEventFilter(self.filter)

        self.titel_label_defcon = QLabel(self)
        self.titel_label_defcon.move(main_border_height, main_border_height + (btn_size_titlebar * 7) + 10)
        self.titel_label_defcon.resize((btnx_size * 6) + (btnx_sp_size * 7), 24)
        self.titel_label_defcon.setText('DEFCON LEVEL ALERT SYSTEM')
        self.titel_label_defcon.setStyleSheet("""QLabel{background-color: rgb(0, 0, 0);
                    color: rgb(255, 255, 255);
                    border-top:2px solid rgb(0, 0, 0);
                    border-bottom:2px solid rgb(0, 0, 0);
                    border-right:2px solid rgb(0, 0, 0);
                    border-left:2px solid rgb(0, 0, 0);}""")
        self.titel_label_defcon.setAlignment(Qt.AlignCenter)
        ui_object_complete.append(self.titel_label_defcon)
        self.titel_label_defcon.installEventFilter(self.filter)

        self.titel_label_news = QLabel(self)
        self.titel_label_news.move(main_border_height, main_border_height + (btn_size_titlebar * 33) + 10)
        self.titel_label_news.resize((btnx_size * 6) + (btnx_sp_size * 7), 24)
        self.titel_label_news.setText('NASA PLANETARY VITAL SIGNS')
        self.titel_label_news.setStyleSheet("""QLabel{background-color: rgb(0, 0, 0);
                    color: rgb(255, 255, 255);
                    border-top:2px solid rgb(0, 0, 0);
                    border-bottom:2px solid rgb(0, 0, 0);
                    border-right:2px solid rgb(0, 0, 0);
                    border-left:2px solid rgb(0, 0, 0);}""")
        self.titel_label_news.setAlignment(Qt.AlignCenter)
        ui_object_complete.append(self.titel_label_news)
        self.titel_label_news.installEventFilter(self.filter)

        # button: quit (use main_border_height)
        self.btn_quit = QPushButton(self)
        self.btn_quit.move((app_width_static - (titlebar_height + main_border_height)), main_border_height)
        self.btn_quit.resize(titlebar_height, titlebar_height)
        self.btn_quit.setIcon(QIcon("./resources/image/close.png"))
        self.btn_quit.setIconSize(QSize(btn_size_titlebar, btn_size_titlebar - 4))
        self.btn_quit.setStyleSheet(sol_style.btn_title_bar_style)
        self.btn_quit.installEventFilter(self.filter)
        ui_object_complete.append(self.btn_quit)

        # button: minimize (use main_border_height)
        self.btn_minimize = QPushButton(self)
        self.btn_minimize.move((app_width_static - (titlebar_height + main_border_height) * 2), main_border_height)
        self.btn_minimize.resize(btn_size_titlebar, btn_size_titlebar)
        self.btn_minimize.setIcon(QIcon("./resources/image/minimize.png"))
        self.btn_minimize.setIconSize(QSize(24, 16))
        self.btn_minimize.setStyleSheet(sol_style.btn_title_bar_style)
        self.btn_minimize.installEventFilter(self.filter)
        ui_object_complete.append(self.btn_minimize)

        self.btn_NUKE_ALARM = QPushButton(self)
        self.btn_NUKE_ALARM.move(main_border_height, main_border_height + (titlebar_height * 2))
        self.btn_NUKE_ALARM.resize(632 - (main_border_height*2), 20)
        # self.btn_NUKE_ALARM.setIcon(QIcon("./resources/image/minimize.png"))
        # self.btn_NUKE_ALARM.setIconSize(QSize(24, 16))
        self.btn_NUKE_ALARM.setStyleSheet("""QPushButton{background-color: rgb(255, 0, 0);
                color: rgb(255, 255, 0);
                border-top:0px solid rgb(0, 0, 0);
                border-bottom:0px solid rgb(0, 0, 0);
                border-right:0px solid rgb(0, 0, 0);
                border-left:0px solid rgb(0, 0, 0);}
                QPushButton::hover {
                    background-color : rgb(0,0,155);
                }
                QPushButton::pressed {
                    color: rgb(255, 255, 0);
                    background-color : rgb(26,26,26);
                    border-top:8px solid rgb(14, 14, 14);
                    border-bottom:8px solid rgb(14, 14, 14);
                    border-right:8px solid rgb(14, 14, 14);
                    border-left:8px solid rgb(14, 14, 14);}
                }""")
        self.btn_NUKE_ALARM.setText('NUCLEAR STRIKE IMMINENT')
        self.btn_NUKE_ALARM.installEventFilter(self.filter)
        ui_object_complete.append(self.btn_NUKE_ALARM)
        self.btn_NUKE_ALARM.hide()

        self.btn_MUTE_NUKE_ALARM = QPushButton(self)
        self.btn_MUTE_NUKE_ALARM.move(632 - main_border_height - 80, main_border_height + (titlebar_height * 1))
        self.btn_MUTE_NUKE_ALARM.resize(80, 20)
        # self.btn_MUTE_NUKE_ALARM.setIcon(QIcon("./resources/image/minimize.png"))
        # self.btn_MUTE_NUKE_ALARM.setIconSize(QSize(24, 16))
        self.btn_MUTE_NUKE_ALARM.setStyleSheet("""QPushButton{background-color: rgb(255, 0, 0);
                        color: rgb(0, 0, 0);
                        border-top:0px solid rgb(0, 0, 0);
                        border-bottom:0px solid rgb(0, 0, 0);
                        border-right:0px solid rgb(0, 0, 0);
                        border-left:0px solid rgb(0, 0, 0);}
                        QPushButton::hover {
                            background-color : rgb(0,0,155);
                        }
                        QPushButton::pressed {
                            color: rgb(0, 0, 0);
                            background-color : rgb(255,255,0);
                            border-top:8px solid rgb(14, 14, 14);
                            border-bottom:8px solid rgb(14, 14, 14);
                            border-right:8px solid rgb(14, 14, 14);
                            border-left:8px solid rgb(14, 14, 14);}
                        }""")
        self.btn_MUTE_NUKE_ALARM.setText('MUTE')
        self.btn_MUTE_NUKE_ALARM.clicked.connect(function_mute_default_player)
        self.btn_MUTE_NUKE_ALARM.installEventFilter(self.filter)
        ui_object_complete.append(self.btn_MUTE_NUKE_ALARM)
        self.btn_MUTE_NUKE_ALARM.hide()

        self.file_menu = QMenu(self)
        self.edit_menu = QMenu(self)
        self.view_menu = QMenu(self)
        self.help_menu = QMenu(self)
        self.main_menu_bar = QMenuBar(self)

        def app_activate():
            print(str('[' + str(datetime.datetime.now()) + '] [app_activate] plugged in'))
            shell.AppActivate(pid_main)

        def app_display_stays_on_top():
            global app_display_default_bool, app_display_stays_on_top_bool, app_display_stays_on_bottom_bool
            print(str('[' + str(datetime.datetime.now()) + '] [app_display_stays_on_top] plugged in'))

            app_display_default_bool = False
            app_display_stays_on_top_bool = True
            app_display_stays_on_bottom_bool = False

            create_titlebar_menubar()

            self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.show()

        def about_function():
            print(str('[' + str(datetime.datetime.now()) + '] [about_function] plugged in'))
            d1_desc()
            tbx_var[30].append('')
            d2_desc()
            tbx_var[30].append('')
            d3_desc()
            tbx_var[30].append('')
            d4_desc()
            tbx_var[30].append('')
            d5_desc()
            tbx_var[30].verticalScrollBar().setValue(0)

        def app_display_stays_on_bottom():
            global app_display_default_bool, app_display_stays_on_top_bool, app_display_stays_on_bottom_bool
            print(str('[' + str(datetime.datetime.now()) + '] [app_display_stays_on_bottom] plugged in'))

            app_display_default_bool = False
            app_display_stays_on_top_bool = False
            app_display_stays_on_bottom_bool = True

            create_titlebar_menubar()

            self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint)
            self.show()

        def app_display_default():
            global app_display_default_bool, app_display_stays_on_top_bool, app_display_stays_on_bottom_bool
            print(str('[' + str(datetime.datetime.now()) + '] [app_display_default] plugged in'))

            app_display_default_bool = True
            app_display_stays_on_top_bool = False
            app_display_stays_on_bottom_bool = False

            create_titlebar_menubar()

            self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
            self.show()

        def create_vbs():
            print(str('[' + str(datetime.datetime.now()) + '] [create_vbs] plugged in'))
            vbs_f = cwd + program_fname_no_suffix + '.vbs'
            exe_f = cwd + program_fname_no_suffix + '.exe'
            open(vbs_f, 'w').close()
            with open(vbs_f, 'a') as fo:
                fo.write('Set WshShell = CreateObject("WScript.Shell")' + '\n')
                fo.write('WshShell.Run chr(34) & "' + exe_f + '" & Chr(34), 0' + '\n')
                fo.write('Set WshShell = Nothing' + '\n')
            fo.close()

        def create_lnk():
            print(str('[' + str(datetime.datetime.now()) + '] [create_lnk] plugged in'))
            vbs_f = cwd + program_fname_no_suffix + '.vbs'
            lnk_f = cwd + program_fname_no_suffix + '.lnk'
            open(lnk_f, 'w').close()
            icon = cwd + 'icon.ico'
            shortcut = shell.CreateShortCut(lnk_f)
            shortcut.Targetpath = vbs_f
            shortcut.WorkingDirectory = cwd
            shortcut.IconLocation = icon
            shortcut.save()

        def run_at_startup_check():
            global bool_switch_run_at_startup
            print(str('[' + str(datetime.datetime.now()) + '] [run_at_startup_check] plugged in'))
            shortcut_out = os.path.join(os.path.expanduser('~') + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/' + program_fname_no_suffix + '.lnk')
            if os.path.exists(shortcut_out):
                bool_switch_run_at_startup = True
            else:
                bool_switch_run_at_startup = False

        def run_at_startup():
            global bool_switch_run_at_startup
            print(str('[' + str(datetime.datetime.now()) + '] [run_at_startup] plugged in'))
            vbs_f = cwd + program_fname_no_suffix + '.vbs'
            shortcut_out = os.path.join(os.path.expanduser('~') + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/' + program_fname_no_suffix + '.lnk')

            # remove shortcut from startup directory
            if bool_switch_run_at_startup is True:
                if os.path.exists(shortcut_out):
                    os.remove(shortcut_out)
                    bool_switch_run_at_startup = False

            # create shortcut in startup directory
            elif bool_switch_run_at_startup is False:
                icon = cwd + './icon.ico'
                shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = shell.CreateShortCut(shortcut_out)
                shortcut.Targetpath = vbs_f
                shortcut.WorkingDirectory = cwd
                shortcut.IconLocation = icon
                shortcut.save()
                bool_switch_run_at_startup = True

            create_titlebar_menubar()

        create_vbs()
        create_lnk()
        run_at_startup_check()

        def attatch_to_taskbar():
            global pin_to_taskbar, pos_w_prev, pos_h_prev, btnx_double_var
            if pin_to_taskbar is False:
                pin_to_taskbar = True
                pos_w_prev = int()
            elif pin_to_taskbar is True:
                pin_to_taskbar = False
                pos_w_prev = int()

            create_titlebar_menubar()

        def restart_thread_0():
            if self.thread_0.isRunning():
                self.thread_0.stop_thread()
                self.thread_0.start()

        def restart_thread_1():
            if self.thread_1.isRunning():
                self.thread_1.stop_thread()
                self.thread_1.start()

        def function_defcon_update_time_30():
            global defcon_update_time
            defcon_update_time = 30
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] defcon_update_time: ' + str(defcon_update_time)))
            create_titlebar_menubar()
            restart_thread_0()

        def function_defcon_update_time_60():
            global defcon_update_time
            defcon_update_time = 60
            debug_messages.append(
                str('[' + str(datetime.datetime.now()) + '] defcon_update_time: ' + str(defcon_update_time)))
            create_titlebar_menubar()
            restart_thread_0()

        def function_defcon_update_time_120():
            global defcon_update_time
            defcon_update_time = 120
            debug_messages.append(
                str('[' + str(datetime.datetime.now()) + '] defcon_update_time: ' + str(defcon_update_time)))
            create_titlebar_menubar()
            restart_thread_0()

        def function_defcon_update_time_180():
            global defcon_update_time
            defcon_update_time = 180
            debug_messages.append(
                str('[' + str(datetime.datetime.now()) + '] defcon_update_time: ' + str(defcon_update_time)))
            create_titlebar_menubar()
            restart_thread_0()

        def function_defcon_update_time_240():
            global defcon_update_time
            defcon_update_time = 240
            debug_messages.append(
                str('[' + str(datetime.datetime.now()) + '] defcon_update_time: ' + str(defcon_update_time)))
            create_titlebar_menubar()
            restart_thread_0()

        def function_defcon_update_time_300():
            global defcon_update_time
            defcon_update_time = 300
            debug_messages.append(
                str('[' + str(datetime.datetime.now()) + '] defcon_update_time: ' + str(defcon_update_time)))
            create_titlebar_menubar()
            restart_thread_0()

        def function_nasa_update_time_30():
            global nasa_update_time
            nasa_update_time = 30
            debug_messages.append(
                str('[' + str(datetime.datetime.now()) + '] nasa_update_time: ' + str(nasa_update_time)))
            create_titlebar_menubar()
            restart_thread_1()

        def function_nasa_update_time_60():
            global nasa_update_time
            nasa_update_time = 60
            debug_messages.append(
                str('[' + str(datetime.datetime.now()) + '] nasa_update_time: ' + str(nasa_update_time)))
            create_titlebar_menubar()
            restart_thread_1()

        def function_nasa_update_time_300():
            global nasa_update_time
            nasa_update_time = 300
            debug_messages.append(
                str('[' + str(datetime.datetime.now()) + '] nasa_update_time: ' + str(nasa_update_time)))
            create_titlebar_menubar()
            restart_thread_1()

        def function_nasa_update_time_600():
            global nasa_update_time
            nasa_update_time = 600
            debug_messages.append(
                str('[' + str(datetime.datetime.now()) + '] nasa_update_time: ' + str(nasa_update_time)))
            create_titlebar_menubar()
            restart_thread_1()

        def function_nasa_update_time_1800():
            global nasa_update_time
            nasa_update_time = 1800
            debug_messages.append(
                str('[' + str(datetime.datetime.now()) + '] nasa_update_time: ' + str(nasa_update_time)))
            create_titlebar_menubar()
            restart_thread_1()

        def function_nasa_update_time_3600():
            global nasa_update_time
            nasa_update_time = 3600
            debug_messages.append(
                str('[' + str(datetime.datetime.now()) + '] nasa_update_time: ' + str(nasa_update_time)))
            create_titlebar_menubar()
            restart_thread_1()

        def d1_desc():
            tbx_var[30].append(module_help.d1)

        def d2_desc():
            tbx_var[30].append(module_help.d2)

        def d3_desc():
            tbx_var[30].append(module_help.d3)

        def d4_desc():
            tbx_var[30].append(module_help.d4)

        def d5_desc():
            tbx_var[30].append(module_help.d5)

        # title_bar_toolbar
        def create_titlebar_menubar():
            # debug_messages.append(str('[' + str(datetime.datetime.now()) + '] plugged in: create_titlebar_menubar'))
            global btnx_titlebar_toolbar_var, app_display_default_bool, app_display_stays_on_top_bool, app_display_stays_on_bottom_bool, defcon_update_time

            self.main_menu_bar.clear()
            self.file_menu.clear()
            self.edit_menu.clear()
            self.view_menu.clear()
            self.help_menu.clear()

            self.file_menu.setTitle('File')
            self.file_menu.addSeparator()
            if bool_switch_run_at_startup is True:
                self.file_menu.addAction(QIcon('./resources/image/check.png'), ' Run at startup', run_at_startup)
            else:
                self.file_menu.addAction(' Run at startup', run_at_startup)
            self.file_menu.addSeparator()
            self.file_menu.addAction(' Exit', app.quit)
            self.file_menu.addSeparator()

            self.edit_menu.addSeparator()
            self.edit_menu.setTitle('Edit')
            self.edit_menu.addSeparator()
            self.edit_menu.addSeparator()
            self.edit_menu.addAction(' DEFCON')
            if defcon_update_time == 30:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 30 Seconds', function_defcon_update_time_30)
            else:
                self.edit_menu.addAction('       Update time 30 Seconds', function_defcon_update_time_30)

            if defcon_update_time == 60:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 1 minute', function_defcon_update_time_60)
            else:
                self.edit_menu.addAction('       Update time 1 minute', function_defcon_update_time_60)

            if defcon_update_time == 120:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 2 minutes', function_defcon_update_time_120)
            else:
                self.edit_menu.addAction('       Update time 2 minutes', function_defcon_update_time_120)

            if defcon_update_time == 180:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 3 minutes', function_defcon_update_time_180)
            else:
                self.edit_menu.addAction('       Update time 3 minutes', function_defcon_update_time_180)

            if defcon_update_time == 240:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 4 minutes', function_defcon_update_time_240)
            else:
                self.edit_menu.addAction('       Update time 4 minutes', function_defcon_update_time_240)

            if defcon_update_time == 300:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 5 minutes', function_defcon_update_time_300)
            else:
                self.edit_menu.addAction('       Update time 5 minutes', function_defcon_update_time_300)

            self.edit_menu.addSeparator()
            self.edit_menu.addSeparator()
            self.edit_menu.addAction(' NASA')

            if nasa_update_time == 30:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 30 Seconds', function_nasa_update_time_30)
            else:
                self.edit_menu.addAction('       Update time 30 Seconds', function_nasa_update_time_30)

            if nasa_update_time == 60:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 1 minute', function_nasa_update_time_60)
            else:
                self.edit_menu.addAction('       Update time 1 minute', function_nasa_update_time_60)

            if nasa_update_time == 300:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 5 minutes', function_nasa_update_time_300)
            else:
                self.edit_menu.addAction('       Update time 5 minutes', function_nasa_update_time_300)

            if nasa_update_time == 600:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 10 minutes', function_nasa_update_time_600)
            else:
                self.edit_menu.addAction('       Update time 10 minutes', function_nasa_update_time_600)

            if nasa_update_time == 1800:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 30 minutes', function_nasa_update_time_1800)
            else:
                self.edit_menu.addAction('       Update time 30 minutes', function_nasa_update_time_1800)

            if nasa_update_time == 3600:
                self.edit_menu.addAction(QIcon('./resources/image/check.png'), '       Update time 1 hour', function_nasa_update_time_3600)
            else:
                self.edit_menu.addAction('       Update time 1 hour', function_nasa_update_time_3600)

            self.view_menu.setTitle('View')
            self.view_menu.addSeparator()
            if pin_to_taskbar is True:
                self.view_menu.addAction(QIcon('./resources/image/check.png'), ' Attach to taskbar', attatch_to_taskbar)
            else:
                self.view_menu.addAction(' Attach to taskbar', attatch_to_taskbar)
            self.view_menu.addSeparator()

            if app_display_default_bool is True:
                self.view_menu.addAction(QIcon('./resources/image/check.png'), ' Always display default', app_display_default)
            else:
                self.view_menu.addAction(' Always display default', app_display_default)

            if app_display_stays_on_top_bool is True:
                self.view_menu.addAction(QIcon('./resources/image/check.png'), ' Always display on top', app_display_stays_on_top)
            else:
                self.view_menu.addAction(' Always display on top', app_display_stays_on_top)

            if app_display_stays_on_bottom_bool is True:
                self.view_menu.addAction(QIcon('./resources/image/check.png'), ' Always display on bottom', app_display_stays_on_bottom)
            else:
                self.view_menu.addAction(' Always display on bottom', app_display_stays_on_bottom)

            self.view_menu.addSeparator()

            self.help_menu.addSeparator()
            self.help_menu.setTitle('Help')
            self.help_menu.addSeparator()
            self.help_menu.addAction(' About', about_function)
            self.help_menu.addSeparator()

            self.main_menu_bar.resize(200, 28)
            self.main_menu_bar.move(main_border_height + title_bar_toolbar_sp, main_border_height + titlebar_height)
            self.main_menu_bar.addMenu(self.file_menu)
            self.main_menu_bar.addMenu(self.edit_menu)
            self.main_menu_bar.addMenu(self.view_menu)
            self.main_menu_bar.addMenu(self.help_menu)
            
        # Create objects and modules automatically
        def automatic_object_generator():
            global btnx_var, ui_object_complete, debug_messages, debug_enable_bool, app_width_static, app_height_static, pin_to_taskbar, btnx_master
            global auto_generate_lbl, auto_generate_btn, auto_generate_btn_double, auto_generate_qle
            global btnx_var, lblx_var, btnx_double_var, qlex_var, qlex_double_var, tbx_var, tbx_message, tbx_timer, btnx_double_timer
            global reserve_btnx, btnx_double_timer_sub, btnx_timer, btnx_timer_sub
            # debug_messages.append(str('[' + str(datetime.datetime.now()) + '] plugged in: generateButtonFunction'))

            list_import_0 = ['os', 'PyQt5', 'PyQt5.QtCore', 'datetime', 'sol_style']
            list_import_1 = ['auto_gen_main_page', 'auto_gen_btnx_function', 'auto_gen_btnx_double_function',
                           'auto_gen_qle_returnpressed_connect_function', 'auto_gen_qle_double_returnpressed_connect_function',
                           'auto_gen_tbx_update_function',
                           'auto_gen_btnx_bool', 'auto_gen_btnx_double_bool', 'auto_gen_qle_bool', 'auto_gen_qle_double_bool']
            list_objects = ['var_btnx',
                            'var_btnx_double',
                            'var_lblx',
                            'var_qlex',
                            'var_qlex_double',
                            'var_tbx',
                            'var_tbx_timer',
                            'var_btnx_double_timer',
                            'var_btnx_double_timer_sub',
                            'var_btnx_timer',
                            'var_btnx_timer_sub',
                            'var_self']

            if auto_setup is True:
                # wipe modules
                for _ in list_import_1:
                    open(str('./' + _ + '.py'), 'w').close()
                # head clean module files
                for _ in list_import_1:
                    with open(str('./' + _ + '.py'), 'a') as fo:
                        for _ in list_import_0:
                            fo.write('import ' + _ + '\n')
                        for _ in list_import_1:
                            fo.write('import ' + _ + '\n')
                        fo.write('\n')
                        for _ in list_objects:
                            fo.write(_ + ' = []' + '\n')
                        fo.write('\n')
                    fo.close()
                with open('./auto_gen_main_page.py', 'a') as fo:
                    fo.write('main_page = 0\n')
                fo.close()

            # step through btnx_master
            layer_count = 0
            i_btnx_master = 0
            for _ in btnx_master:

                # bring in variables from btnx_master
                btnx_gen_max = btnx_master[i_btnx_master][0]
                btnx_row_idx_max = btnx_master[i_btnx_master][1]
                btnx_position_initialize_x, btnx_position_initialize_y = btnx_master[i_btnx_master][2], btnx_master[i_btnx_master][3]
                btnx_size = btnx_master[i_btnx_master][4]
                btnx_size_Y = btnx_master[i_btnx_master][5]
                btnx_sp_size = btnx_master[i_btnx_master][6]
                btnx_sp_size_Y = btnx_master[i_btnx_master][7]

                # automatically generate objects in a loop
                i = 0
                i_x = 0
                main_page = 0
                btnx_i_timer = 0
                btnx_i_sub_timer = 0
                btnx_double_i_timer = 0
                btnx_double_i_sub_timer = 0
                while i_x < btnx_gen_max:

                    # button intitiation using values from btnx_master
                    if auto_generate_btn is True:
                        btnx_name = 'btnx_' + str(i_x)
                        self.btnx = btnx_name
                        self.btnx = QPushButton(self)
                        self.btnx.resize(btnx_size, btnx_size)
                        self.btnx.setText(btnx_name)
                        btnx_var.append(self.btnx)
                        ui_object_complete.append(self.btnx)
                        self.btnx.installEventFilter(self.filter)
                        self.btnx.hide()

                        # automatically position
                        if i == 0:
                            self.btnx.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i ),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )
                        elif i >= 1:
                            self.btnx.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i ) + (btnx_size * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )

                        if auto_setup is True:

                            # automatically write boolean file
                            with open('./auto_gen_btnx_bool.py', 'a') as fo:
                                fo.write(btnx_name + '_bool = False' + '\n')
                            fo.close()

                            # automatically create functions
                            with open('./auto_gen_btnx_function.py', 'a') as fo:

                                if i_x in turn_page_reserved:
                                    # start timer
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_start_timer_function():' + '\n')
                                    fo.write("    global var_btnx_timer\n")
                                    fo.write("    var_btnx_timer[" + str(btnx_i_timer) + "].start()" + '\n\n')
                                    # stop timer
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_stop_timer_function():' + '\n')
                                    fo.write("    global var_btnx_timer\n")
                                    fo.write("    var_btnx_timer[" + str(btnx_i_timer) + "].stop()" + '\n\n')
                                    # update tbx
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_timer_clicked_function():' + '\n')
                                    fo.write('    print(' + btnx_name + '_timer_clicked_function)\n\n')
                                    btnx_i_timer += 1
                                else:
                                    # automatically create page conditions
                                    inner_loop_i = 0
                                    while inner_loop_i < len(turn_page_reserved):
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_start_timer_function():' + '\n')
                                        fo.write("    global var_btnx_timer_sub\n")
                                        fo.write("    var_btnx_timer_sub[" + str(btnx_i_sub_timer) + "].start()" + '\n\n')
                                        # stop timer
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_stop_timer_function():' + '\n')
                                        fo.write("    global var_btnx_timer_sub\n")
                                        fo.write("    var_btnx_timer_sub[" + str(btnx_i_sub_timer) + "].stop()" + '\n\n')
                                        # update tbx
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_timer_clicked_function():' + '\n')
                                        fo.write('    print(' + btnx_name + '_' + str(inner_loop_i) + '_timer_clicked_function)\n\n')
                                        btnx_i_sub_timer += 1
                                        inner_loop_i += 1

                                fo.write('def ' + btnx_name + '_function():' + '\n')

                                # automatically create page functions
                                if i_x in turn_page_reserved:
                                    fo.write('    auto_gen_main_page.main_page = ' + str(main_page) + '\n')
                                    fo.write('    if auto_gen_btnx_bool.' + btnx_name + '_bool is True:' + '\n')
                                    fo.write('        auto_gen_btnx_bool.' + btnx_name + '_bool = False' + '\n')
                                    fo.write('        # ' + btnx_name + '_stop_timer_function()' + '\n')
                                    fo.write('    elif auto_gen_btnx_bool.' + btnx_name + '_bool is False:' + '\n')
                                    fo.write('        auto_gen_btnx_bool.' + btnx_name + '_bool = True' + '\n')
                                    fo.write('        # ' + btnx_name + '_start_timer_function()' + '\n')
                                    fo.write("    print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool." + btnx_name + "_bool) + ']')\n\n")
                                else:

                                    # automatically create page conditions
                                    inner_loop_i = 0
                                    while inner_loop_i < len(turn_page_reserved):
                                        if inner_loop_i == 0:
                                            fo.write('    if auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                        else:
                                            fo.write('    elif auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                        fo.write('        if auto_gen_btnx_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool is True:' + '\n')
                                        fo.write('            auto_gen_btnx_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                        fo.write("            print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool." + btnx_name + '_' + str(inner_loop_i) + "_bool) + ']')\n")
                                        fo.write('            # ' + btnx_name + '_' + str(inner_loop_i) + '_stop_timer_function()' + '\n\n')
                                        fo.write('        elif auto_gen_btnx_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool is False:' + '\n')
                                        fo.write('            auto_gen_btnx_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool = True' + '\n')
                                        fo.write("            print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool." + btnx_name + '_' + str(inner_loop_i) + "_bool) + ']')\n")
                                        fo.write('            # ' + btnx_name + '_' + str(inner_loop_i) + '_start_timer_function()' + '\n\n')
                                        # automatically write boolean file
                                        with open('./auto_gen_btnx_bool.py', 'a') as fo_bool:
                                            fo_bool.write(btnx_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                        fo_bool.close()
                                        inner_loop_i += 1
                            fo.close()

                        # automatically create timers
                        if i_x in turn_page_reserved:
                            btnx_name_timer = btnx_name + '_timer'
                            btnx_name_timer = QTimer(self)
                            btnx_name_timer.setInterval(0)
                            btnx_timer.append(btnx_name_timer)
                        else:
                            inner_loop_i = 0
                            while inner_loop_i < len(turn_page_reserved):
                                btnx_name_timer = btnx_name + '_' + str(inner_loop_i) + '_timer'
                                btnx_name_timer = QTimer(self)
                                btnx_name_timer.setInterval(0)
                                btnx_timer_sub.append(btnx_name_timer)
                                inner_loop_i += 1

                        # automatically size window per object created
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * btnx_size)
                            app_width_static = app_width_static + (btnx_row_idx_max * btnx_sp_size) + btnx_sp_size

                    # button double initiation using values from btnx_master
                    if auto_generate_btn_double is True:
                        btnx_name = 'btnx_double_' + str(i_x)
                        self.btnx = btnx_name
                        self.btnx = QPushButton(self)
                        self.btnx.resize((btnx_size * 2) + btnx_sp_size, btnx_size)
                        # self.btnx.setText(btnx_name)
                        btnx_double_var.append(self.btnx)
                        ui_object_complete.append(self.btnx)
                        self.btnx.installEventFilter(self.filter)
                        self.btnx.hide()

                        # automatically position
                        if i == 0:
                            self.btnx.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i ),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )
                        elif i >= 1:
                            self.btnx.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i ) + (btnx_size * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )

                        # automatically write boolean file
                        if auto_setup is True:
                            with open('./auto_gen_btnx_double_bool.py', 'a') as fo:
                                fo.write(btnx_name + '_bool = False' + '\n')
                            fo.close()

                            # automatically create functions
                            with open('auto_gen_btnx_double_function.py', 'a') as fo:

                                if i_x in turn_page_reserved:
                                    # start timer
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_start_timer_function():' + '\n')
                                    fo.write("    global var_btnx_double_timer\n")
                                    fo.write("    var_btnx_double_timer[" + str(btnx_double_i_timer) + "].start()" + '\n\n')
                                    # stop timer
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_stop_timer_function():' + '\n')
                                    fo.write("    global var_btnx_double_timer\n")
                                    fo.write("    var_btnx_double_timer[" + str(btnx_double_i_timer) + "].stop()" + '\n\n')
                                    # update tbx
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_timer_clicked_function():' + '\n')
                                    fo.write('    print(' + btnx_name + '_timer_clicked_function)\n\n')
                                    btnx_double_i_timer += 1
                                else:
                                    # automatically create page conditions
                                    inner_loop_i = 0
                                    while inner_loop_i < len(turn_page_reserved):
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_start_timer_function():' + '\n')
                                        fo.write("    global var_btnx_double_timer_sub\n")
                                        fo.write("    var_btnx_double_timer_sub[" + str(btnx_double_i_sub_timer) + "].start()" + '\n\n')
                                        # stop timer
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_stop_timer_function():' + '\n')
                                        fo.write("    global var_btnx_double_timer_sub\n")
                                        fo.write("    var_btnx_double_timer_sub[" + str(btnx_double_i_sub_timer) + "].stop()" + '\n\n')
                                        # update tbx
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_timer_clicked_function():' + '\n')
                                        fo.write('    print(' + btnx_name + '_' + str(inner_loop_i) + '_timer_clicked_function)\n\n')
                                        btnx_double_i_sub_timer += 1
                                        inner_loop_i += 1

                                # automatically create page functions
                                if i_x in turn_page_reserved:
                                    fo.write('def ' + btnx_name + '_function():' + '\n')
                                    fo.write('    auto_gen_main_page.main_page = ' + str(main_page) + '\n')
                                    fo.write('    if auto_gen_btnx_double_bool.' + btnx_name + '_bool is True:' + '\n')
                                    fo.write('        auto_gen_btnx_double_bool.' + btnx_name + '_bool = False' + '\n')
                                    fo.write('        # ' + btnx_name + '_stop_timer_function()' + '\n')
                                    fo.write('    elif auto_gen_btnx_double_bool.' + btnx_name + '_bool is False:' + '\n')
                                    fo.write('        auto_gen_btnx_double_bool.' + btnx_name + '_bool = True' + '\n')
                                    fo.write('        # ' + btnx_name + '_start_timer_function()' + '\n')
                                    fo.write("    print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool." + btnx_name + "_bool) + ']')\n\n")
                                else:
                                    # automatically create page conditions
                                    fo.write('def ' + btnx_name + '_function():' + '\n')
                                    inner_loop_i = 0
                                    while inner_loop_i < len(turn_page_reserved):
                                        if inner_loop_i == 0:
                                            fo.write('    if auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                        else:
                                            fo.write('    elif auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                        fo.write('        if auto_gen_btnx_double_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool is True:' + '\n')
                                        fo.write('            auto_gen_btnx_double_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                        fo.write("            print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool." + btnx_name + '_' + str(inner_loop_i) + "_bool) + ']')\n")
                                        fo.write('            # ' + btnx_name + '_' + str(inner_loop_i) + '_stop_timer_function()' + '\n\n')
                                        fo.write('        elif auto_gen_btnx_double_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool is False:' + '\n')
                                        fo.write('            auto_gen_btnx_double_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool = True' + '\n')
                                        fo.write("            print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool." + btnx_name + '_' + str(inner_loop_i) + "_bool) + ']')\n")
                                        fo.write('            # ' + btnx_name + '_' + str(inner_loop_i) + '_start_timer_function()' + '\n\n')

                                        # automatically write boolean file
                                        with open('./auto_gen_btnx_double_bool.py', 'a') as fo_bool:
                                            fo_bool.write(btnx_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                        fo_bool.close()
                                        inner_loop_i += 1
                            fo.close()

                        # automatically create timers
                        if i_x in turn_page_reserved:
                            btnx_double_name_timer = btnx_name + '_timer'
                            btnx_double_name_timer = QTimer(self)
                            btnx_double_name_timer.setInterval(0)
                            btnx_double_timer.append(btnx_double_name_timer)
                        else:
                            inner_loop_i = 0
                            while inner_loop_i < len(turn_page_reserved):
                                btnx_double_name_timer = btnx_name + '_' + str(inner_loop_i) + '_timer'
                                btnx_double_name_timer = QTimer(self)
                                btnx_double_name_timer.setInterval(0)
                                btnx_double_timer_sub.append(btnx_double_name_timer)
                                inner_loop_i += 1

                        # automatically size window per object created
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * btnx_size)
                            app_width_static = app_width_static + (btnx_row_idx_max * btnx_sp_size) + btnx_sp_size
                    
                    # label initiation using values from btnx_master and multiplied
                    if auto_generate_lbl is True:
                        lblx_name = 'lblx_' + str(i_x)
                        self.lblx = lblx_name
                        self.lblx = QLabel(self)
                        self.lblx.resize((btnx_size * 2) + btnx_sp_size, 24)
                        self.lblx.setText(lblx_name)
                        lblx_var.append(self.lblx)
                        ui_object_complete.append(self.lblx)
                        self.lblx.installEventFilter(self.filter)
                        self.lblx.hide()

                        # automatically position
                        if i == 0:
                            self.lblx.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i ),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )
                        elif i >= 1:
                            self.lblx.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + ((btnx_sp_size*1) * i ) + ((btnx_size*1) * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * (btnx_size*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_size*1)) + btnx_sp_size

                    # qlineedit intitiation using values from btnx_master and multiplied  returnPressed.connect
                    if auto_generate_qle is True:
                        qlex_name = 'qlex_' + str(i_x)
                        self.qlex = qlex_name
                        self.qlex = QLineEdit(self)
                        self.qlex.resize(btnx_size, int(btnx_size / 2))
                        self.qlex.setText(qlex_name)
                        qlex_var.append(self.qlex)
                        ui_object_complete.append(self.qlex)
                        self.qlex.installEventFilter(self.filter)
                        self.qlex.hide()

                        # automatically position button
                        if i == 0:
                            self.qlex.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i ),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )
                        elif i >= 1:
                            self.qlex.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i ) + (btnx_size * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )

                        # automatically create functions
                        if auto_setup is True:
                            with open('./auto_gen_qle_returnpressed_connect_function.py', 'a') as fo:
                                fo.write('def ' + qlex_name + '_returnPressed_connect_function():' + '\n')
                                fo.write("    print(str('[' + str(datetime.datetime.now()) + '] return pressed: " + qlex_name + "'))\n")

                                # automatically create page conditions
                                inner_loop_i = 0
                                while inner_loop_i < len(turn_page_reserved):
                                    if inner_loop_i == 0:
                                        fo.write('    if auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                    else:
                                        fo.write('    elif auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                    fo.write('        if auto_gen_qle_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool is True:' + '\n')
                                    fo.write('            auto_gen_qle_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                    fo.write("            print('[" + qlex_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool." + qlex_name + '_' + str(inner_loop_i) + "_bool) + ']')\n\n")
                                    fo.write('        elif auto_gen_qle_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool is False:' + '\n')
                                    fo.write('            auto_gen_qle_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool = True' + '\n')
                                    fo.write("            print('[" + qlex_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool." + qlex_name + '_' + str(inner_loop_i) + "_bool) + ']')\n\n")

                                    # automatically write boolean file
                                    with open('./auto_gen_qle_bool.py', 'a') as fo_bool:
                                        fo_bool.write(qlex_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                    fo_bool.close()
                                    inner_loop_i += 1
                            fo.close()

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * (btnx_size*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_size*1)) + btnx_sp_size

                    # qlineedit double intitiation using values from btnx_master and multiplied
                    if auto_generate_qle_double is True:
                        qlex_name = 'qlex_double_' + str(i_x)
                        self.qlex = qlex_name
                        self.qlex = QLineEdit(self)
                        self.qlex.resize((btnx_size * 2) + btnx_sp_size, int(btnx_size / 2))
                        self.qlex.setText(qlex_name)
                        qlex_double_var.append(self.qlex)
                        ui_object_complete.append(self.qlex)
                        self.qlex.installEventFilter(self.filter)
                        self.qlex.hide()

                        # automatically position
                        if i == 0:
                            self.qlex.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i ),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )
                        elif i >= 1:
                            self.qlex.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + ((btnx_sp_size*1) * i ) + ((btnx_size*1) * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )

                        # automatically create functions
                        if auto_setup is True:
                            with open('./auto_gen_qle_double_returnpressed_connect_function.py', 'a') as fo:
                                fo.write('def ' + qlex_name + '_returnPressed_connect_function():' + '\n')
                                fo.write("    print(str('[' + str(datetime.datetime.now()) + '] return pressed: " + qlex_name + "'))\n")

                                # automatically create page conditions
                                inner_loop_i = 0
                                while inner_loop_i < len(turn_page_reserved):
                                    if inner_loop_i == 0:
                                        fo.write('    if auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                    else:
                                        fo.write('    elif auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                    fo.write('        if auto_gen_qle_double_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool is True:' + '\n')
                                    fo.write('            auto_gen_qle_double_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                    fo.write("            print('[" + qlex_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool." + qlex_name + '_' + str(inner_loop_i) + "_bool) + ']')\n\n")
                                    fo.write('        elif auto_gen_qle_double_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool is False:' + '\n')
                                    fo.write('            auto_gen_qle_double_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool = True' + '\n')
                                    fo.write("            print('[" + qlex_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool." + qlex_name + '_' + str(inner_loop_i) + "_bool) + ']')\n\n")

                                    # automatically write boolean file
                                    with open('./auto_gen_qle_double_bool.py', 'a') as fo_bool:
                                        fo_bool.write(qlex_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                    fo_bool.close()
                                    inner_loop_i += 1
                            fo.close()

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * (btnx_size*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_size*1)) + btnx_sp_size

                    # auto_generate_tb
                    if auto_generate_tb is True:
                        tbx_name = 'tbx_' + str(i_x)
                        self.tbx = tbx_name
                        self.tbx = QTextBrowser(self)
                        self.tbx.resize((btnx_size * 2) + btnx_sp_size, btnx_size)
                        # self.tbx.setText(tbx_name)
                        # self.tbx.setLineWrapMode(QTextBrowser.NoWrap)  # optional nowrap
                        # self.tbx.horizontalScrollBar().setValue(0)  # optional keep horizontal scroll full left
                        tbx_var.append(self.tbx)
                        ui_object_complete.append(self.tbx)
                        self.tbx.installEventFilter(self.filter)
                        self.tbx.hide()

                        # automatically position
                        if i == 0:
                            self.tbx.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i ),
                                           btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )
                        elif i >= 1:
                            self.tbx.move( main_border_height + btnx_position_initialize_x + btnx_sp_size + ((btnx_sp_size*1) * i ) + ((btnx_size*1) * i),
                                           btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y) )

                        # automatically create functions
                        if auto_setup is True:
                            with open('./auto_gen_tbx_update_function.py', 'a') as fo:

                                # start timer
                                fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                fo.write('def ' + tbx_name + '_start_timer_function():' + '\n')
                                fo.write("    global var_tbx_timer\n")
                                fo.write("    var_tbx_timer[" + str(i_x) + "].start()" + '\n\n')

                                # stop timer
                                fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                fo.write('def ' + tbx_name + '_stop_timer_function():' + '\n')
                                fo.write("    global var_tbx_timer\n")
                                fo.write("    var_tbx_timer[" + str(i_x) + "].stop()" + '\n\n')

                                # update tbx
                                fo.write('message_'+str(i_x)+' = []\n')
                                fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                fo.write('def ' + tbx_name + '_timer_append_function():' + '\n')
                                fo.write("    global message_" + str(i_x) + '\n')
                                fo.write("    global var_tbx\n")
                                fo.write("    if message_" + str(i_x) + ':' + '\n')
                                fo.write("        var_tbx[" + str(i_x) + "].append(" + "message_" + str(i_x) + '[0])' + '\n')
                                fo.write("        message_"+str(i_x)+".remove(message_" + str(i_x) + '[0])' + '\n\n')
                                
                            fo.close()

                        # automatically create timers
                        tbx_name_timer = tbx_name + '_timer'
                        tbx_name_timer = QTimer(self)
                        tbx_name_timer.setInterval(0)
                        tbx_timer.append(tbx_name_timer)

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * (btnx_size*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_size*1)) + btnx_sp_size

                    # add one to row index
                    i += 1

                    # adjust height position for objects after reaching row index max
                    if i == btnx_row_idx_max:
                        i = 0
                        layer_count += 1
                        btnx_size_Y = btnx_size_Y + btnx_size
                        btnx_sp_size_Y = btnx_sp_size_Y + btnx_sp_size

                    # add one every time a button is created that exists in turn_page_reserved
                    if i_x in turn_page_reserved:
                        main_page += 1

                    # add one every time a button is created
                    i_x += 1

                i_btnx_master += 1

            # FINALLY - set application window geometry and position some extras
            app_height_static += (main_border_height)
            app_width_static += (main_border_height * 2)

            # attatch to taskbar
            if pin_to_taskbar is True:
                app_height_pos = int(QDesktopWidget().availableGeometry().height()) - int(app_height_static)
                self.setGeometry(0, app_height_pos, app_width_static, app_height_static)

            # position application center screen
            elif pin_to_taskbar is False:
                app_height_pos = int(QDesktopWidget().availableGeometry().height() / 2) - int(app_height_static / 2)
                app_width_pos = int(QDesktopWidget().availableGeometry().width() / 2) - int(app_width_static / 2)
                self.setGeometry(app_width_pos, app_height_pos, app_width_static, app_height_static)

            # close, minimize
            self.btn_minimize.move((app_width_static - (titlebar_height + main_border_height) * 2), main_border_height)
            self.btn_quit.move((app_width_static - (titlebar_height + main_border_height)), main_border_height)

            # automatically plug everything in
            if auto_generate_btn is True:
                import auto_gen_btnx_bool
                import auto_gen_btnx_function
                auto_gen_btnx_function.var_btnx = btnx_var
                auto_gen_btnx_function.var_btnx_double = btnx_double_var
                auto_gen_btnx_function.var_lblx = lblx_var
                auto_gen_btnx_function.var_qlex = qlex_var
                auto_gen_btnx_function.var_qlex_double = qlex_double_var
                auto_gen_btnx_function.var_tbx = tbx_var
                auto_gen_btnx_function.var_tbx_timer = tbx_timer
                auto_gen_btnx_function.var_btnx_timer = btnx_timer
                auto_gen_btnx_function.var_btnx_timer_sub = btnx_timer_sub
                auto_gen_btnx_function.var_self.append(self)

                i = 0
                for _ in btnx_var:
                    btnx_var[i].clicked.connect(getattr(auto_gen_btnx_function, 'btnx_' + str(i) + '_function'))
                    i += 1

                # timeout connect for btnx_double_var in turn_page_reserved
                i = 0
                i_2 = 0
                for _ in btnx_var:
                    if i in turn_page_reserved:
                        btnx_timer[i_2].timeout.connect(getattr(auto_gen_btnx_function, 'btnx_' + str(i) + '_timer_clicked_function'))
                        print('plugging in btn:', i)
                        i_2 += 1
                    i += 1

                # timeout connect for btnx_double_var not in turn_page_reserved
                i = 0
                i_timer_sub = 0
                for _ in btnx_var:
                    if i not in turn_page_reserved:
                        inner_i_timer_sub = 0
                        while inner_i_timer_sub < len(turn_page_reserved):
                            print(i, i_timer_sub, inner_i_timer_sub, _)
                            btnx_timer_sub[i_timer_sub].timeout.connect(getattr(auto_gen_btnx_function, 'btnx_' + str(i) + '_' + str(inner_i_timer_sub) + '_timer_clicked_function'))
                            inner_i_timer_sub += 1
                            i_timer_sub += 1
                    i += 1

            # automatically plug everything in
            if auto_generate_btn_double is True:
                import auto_gen_btnx_double_bool
                import auto_gen_btnx_double_function
                auto_gen_btnx_double_function.var_btnx = btnx_var
                auto_gen_btnx_double_function.var_btnx_double = btnx_double_var
                auto_gen_btnx_double_function.var_lblx = lblx_var
                auto_gen_btnx_double_function.var_qlex = qlex_var
                auto_gen_btnx_double_function.var_qlex_double = qlex_double_var
                auto_gen_btnx_double_function.var_tbx = tbx_var
                auto_gen_btnx_double_function.var_tbx_timer = tbx_timer
                auto_gen_btnx_double_function.var_btnx_double_timer = btnx_double_timer
                auto_gen_btnx_double_function.var_btnx_double_timer_sub = btnx_double_timer_sub
                auto_gen_btnx_double_function.var_self.append(self)

                print('btnx_double_timer_sub:', btnx_double_timer_sub)
                print('btnx_double_timer_sub len:', len(btnx_double_timer_sub))

                i = 0
                for _ in btnx_double_var:
                    btnx_double_var[i].clicked.connect(getattr(auto_gen_btnx_double_function, 'btnx_double_' + str(i) + '_function'))
                    i += 1

                # timeout connect for btnx_double_var in turn_page_reserved
                i = 0
                i_2 = 0
                for _ in btnx_double_var:
                    if i in turn_page_reserved:
                        btnx_double_timer[i_2].timeout.connect(getattr(auto_gen_btnx_double_function, 'btnx_double_' + str(i) + '_timer_clicked_function'))
                        print('plugging in btn:', i)
                        i_2 += 1
                    i += 1

                # timeout connect for btnx_double_var not in turn_page_reserved
                i = 0
                i_timer_sub = 0
                for _ in btnx_double_var:
                    if i not in turn_page_reserved:
                        inner_i_timer_sub = 0
                        while inner_i_timer_sub < len(turn_page_reserved):
                            print(i, i_timer_sub, inner_i_timer_sub, _)
                            try:
                                btnx_double_timer_sub[i_timer_sub].timeout.connect(getattr(auto_gen_btnx_double_function, 'btnx_double_' + str(i) + '_' + str(inner_i_timer_sub) + '_timer_clicked_function'))
                            except:
                                btnx_double_timer_sub[i_timer_sub].timeout.connect(
                                    getattr(auto_gen_btnx_double_function, 'btnx_double_' + str(i) + '_timer_clicked_function'))
                            inner_i_timer_sub += 1
                            i_timer_sub += 1
                    i += 1

            # automatically plug everything in
            if auto_generate_qle is True:
                import auto_gen_qle_bool
                import auto_gen_qle_returnpressed_connect_function
                auto_gen_qle_returnpressed_connect_function.var_btnx = btnx_var
                auto_gen_qle_returnpressed_connect_function.var_btnx_double = btnx_double_var
                auto_gen_qle_returnpressed_connect_function.var_lblx = lblx_var
                auto_gen_qle_returnpressed_connect_function.var_qlex = qlex_var
                auto_gen_qle_returnpressed_connect_function.var_qlex_double = qlex_double_var
                auto_gen_qle_returnpressed_connect_function.var_tbx = tbx_var
                auto_gen_qle_returnpressed_connect_function.var_tbx_timer = tbx_timer
                i = 0
                for _ in qlex_var:
                    qlex_var[i].returnPressed.connect(getattr(auto_gen_qle_returnpressed_connect_function, 'qlex_' + str(i) + '_returnPressed_connect_function'))
                    i += 1

            # automatically plug everything in
            if auto_generate_qle_double is True:
                import auto_gen_qle_double_bool
                import auto_gen_qle_double_returnpressed_connect_function
                auto_gen_qle_double_returnpressed_connect_function.var_btnx = btnx_var
                auto_gen_qle_double_returnpressed_connect_function.var_btnx_double = btnx_double_var
                auto_gen_qle_double_returnpressed_connect_function.var_lblx = lblx_var
                auto_gen_qle_double_returnpressed_connect_function.var_qlex = qlex_var
                auto_gen_qle_double_returnpressed_connect_function.var_qlex_double = qlex_double_var
                auto_gen_qle_double_returnpressed_connect_function.var_tbx = tbx_var
                auto_gen_qle_double_returnpressed_connect_function.var_tbx_timer = tbx_timer
                i = 0
                for _ in qlex_double_var:
                    qlex_double_var[i].returnPressed.connect(getattr(auto_gen_qle_double_returnpressed_connect_function, 'qlex_double_' + str(i) + '_returnPressed_connect_function'))
                    i += 1

            # automatically plug everything in
            if auto_generate_tb is True:
                import auto_gen_tbx_update_function
                auto_gen_tbx_update_function.var_btnx = btnx_var
                auto_gen_tbx_update_function.var_btnx_double = btnx_double_var
                auto_gen_tbx_update_function.var_lblx = lblx_var
                auto_gen_tbx_update_function.var_qlex = qlex_var
                auto_gen_tbx_update_function.var_qlex_double = qlex_double_var
                auto_gen_tbx_update_function.var_tbx = tbx_var
                auto_gen_tbx_update_function.var_tbx_timer = tbx_timer
                i = 0
                for _ in tbx_timer:
                    tbx_timer[i].timeout.connect(getattr(auto_gen_tbx_update_function, 'tbx_' + str(i) + '_timer_append_function'))
                    i += 1
                
                # TEST
                # tbx_var[16].show()
                # tbx_var[40].show()
                # print('tbx_timer:', tbx_timer)
                # print('auto_gen_tbx_update_function.var_tbx_timer:', auto_gen_tbx_update_function.var_tbx_timer)
                # auto_gen_tbx_update_function.tbx_16_start_timer_function()
                # auto_gen_tbx_update_function.tbx_40_start_timer_function()

                # var_btnx_double_timer_sub

        # automatic object generation
        if enable_title_bar_toolbar is True:
            create_titlebar_menubar()
        if auto_generate is True:
            automatic_object_generator()

        # hide all
        def hide_all_lblx():
            global lblx_var
            for _ in lblx_var:
                _.hide()

        # hide all
        def hide_all_btnx():
            global btnx_var
            for _ in btnx_var:
                _.hide()

        # hide all
        def hide_all_btnx_double():
            global btnx_double_var
            for _ in btnx_double_var:
                _.hide()

        # hide all
        def hide_all_qlex():
            global qlex_var
            for _ in qlex_var:
                _.hide()

        # hide all
        def hide_all_qlex_double():
            global qlex_double_var
            for _ in qlex_double_var:
                _.hide()

        # hide all
        def hide_all_tbx():
            global tbx_var
            for _ in tbx_var:
                _.hide()

        # hide all
        def hide_all_exclude_title():
            hide_all_lblx()
            hide_all_btnx()
            hide_all_btnx_double()
            hide_all_qlex()
            hide_all_qlex_double()
            hide_all_tbx()

        # show all
        def show_all_lblx():
            global lblx_var
            for _ in lblx_var:
                _.show()

        # show all
        def show_all_btnx():
            global btnx_var
            for _ in btnx_var:
                _.show()

        # show all
        def show_all_btnx_double():
            global btnx_double_var
            for _ in btnx_double_var:
                _.show()

        # show all
        def show_all_qlex():
            global qlex_var
            for _ in qlex_var:
                _.show()

        # show all
        def show_all_qlex_double():
            global qlex_double_var
            for _ in qlex_double_var:
                _.show()

        # show all
        def show_all_tbx():
            global tbx_var
            for _ in tbx_var:
                _.show()

        # show reserved
        def show_reserved_btnx():
            global reserve_btnx, btnx_var
            i = 0
            for _ in btnx_var:
                if i in reserve_btnx:
                    _.show()
                i += 1

        # show reserved
        def show_reserved_btnx_double():
            global reserve_btnx_double, btnx_double_var
            i = 0
            for _ in btnx_double_var:
                if i in reserve_btnx_double:
                    _.show()
                i += 1

        # show reserved
        def show_reserved_lblx():
            global reserve_lblx, lblx_var
            i = 0
            for _ in lblx_var:
                if i in reserve_lblx:
                    _.show()
                i += 1

        # show reserved
        def show_reserved_qlex():
            global reserve_qlex, qlex_var
            i = 0
            for _ in qlex_var:
                if i in reserve_qlex:
                    _.show()
                i += 1

        # show reserved
        def show_reserved_qlex_double():
            global reserve_qlex_double, qlex_double_var
            i = 0
            for _ in qlex_double_var:
                if i in reserve_qlex_double:
                    _.show()
                i += 1

        # show reserved
        def show_reserved_tbx():
            global reserve_tbx, tbx_var
            i = 0
            for _ in tbx_var:
                if i in reserve_tbx:
                    _.show()
                i += 1

        # button title bar logo
        def btn_title_logo_function_0():
            global debug_enable_bool, debug_messages
            # if debug_enable_bool is True:
            #     debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.btn_title_logo_function_0] clicked logo button'))
        
        # plug in title bar quit, minimize and logo button
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_title_logo.clicked.connect(btn_title_logo_function_0)

        # display reserved buttons (could be main menu button(s))
        if reserve_btnx_bool is True:
            show_reserved_btnx()
        elif reserve_btnx_double_bool is True:
            show_reserved_btnx_double()

        hide_all_exclude_title()

        defcon_l = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
        defcon_l_title = ['Overall DEFCON Level',
                          'Africa Command',
                          'Central Command',
                          'Cyber Command',
                          'European Command',
                          'Indo-Pacific Command',
                          'Northern Command',
                          'Southern Command',
                          'Space Command',
                          'Special Command',
                          'Strategic Command',
                          'Transportation Command']
        defcon_l_img = ['./resources/image/null-command.webp',
                        './resources/image/africa-command.webp',
                        './resources/image/central-command.webp',
                        './resources/image/cyber-command.webp',
                        './resources/image/european-command.webp',
                        './resources/image/indo-pacific-command.webp',
                        './resources/image/northern-command.webp',
                        './resources/image/southern-command.webp',
                        './resources/image/space-command.webp',
                        './resources/image/special-operations-command.png',
                        './resources/image/strategic-command.png',
                        './resources/image/transportation-command.png']
        for _ in defcon_l:
            lblx_var[_].setText(defcon_l_title[defcon_l.index(_)])
            lblx_var[_].setAlignment(Qt.AlignCenter)
            lblx_var[_].setStyleSheet("""QLabel{background-color: rgb(0, 0, 0);
                color: rgb(255, 255, 255);
                border-top:2px solid rgb(0, 0, 0);
                border-bottom:2px solid rgb(0, 0, 0);
                border-right:2px solid rgb(0, 0, 0);
                border-left:2px solid rgb(0, 0, 0);}""")
            lblx_var[_].show()
            btnx_double_var[_].setIconSize(QSize(64, 64))
            # btnx_double_var[_].setIcon(QIcon(defcon_l_img[defcon_l.index(_)]))
            btnx_double_var[_].setText('--- --- ---')
            btnx_double_var[_].show()

        nasa_l = [36, 38, 40, 42, 44, 46]
        for _ in nasa_l:
            btnx_double_var[_].show()
            btnx_double_var[_].resize((btnx_size * 2) + btnx_sp_size, int((btnx_size / 2) - btnx_sp_size))
            btnx_double_var[_].setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0);
                color: rgb(255, 255, 255);
                border-top:0px solid rgb(0, 0, 0);
                border-bottom:0px solid rgb(0, 0, 0);
                border-right:0px solid rgb(0, 0, 0);
                border-left:0px solid rgb(0, 0, 0);}
                QPushButton::hover {
                    background-color : rgb(0,0,155);
                }
                QPushButton::pressed {
                    color : rgb(255, 255, 255);
                    background-color : rgb(26,26,26);
                    border-top:8px solid rgb(14, 14, 14);
                    border-bottom:8px solid rgb(14, 14, 14);
                    border-right:8px solid rgb(14, 14, 14);
                    border-left:8px solid rgb(14, 14, 14);}
                }""")
            btnx_double_var[_].setText('--- --- ---')

        btnx_double_var[36].move(btnx_double_var[36].geometry().x(), int(btnx_double_var[36].geometry().y()) + int(btnx_size) + btnx_sp_size)
        btnx_double_var[38].move(btnx_double_var[38].geometry().x(), int(btnx_double_var[38].geometry().y()) + int(btnx_size) + btnx_sp_size)
        btnx_double_var[40].move(btnx_double_var[40].geometry().x(), int(btnx_double_var[40].geometry().y()) + int(btnx_size) + btnx_sp_size)
        btnx_double_var[42].move(btnx_double_var[42].geometry().x(), int(btnx_double_var[42].geometry().y()) + int(btnx_size / 2))
        btnx_double_var[44].move(btnx_double_var[44].geometry().x(), int(btnx_double_var[44].geometry().y()) + int(btnx_size / 2))
        btnx_double_var[46].move(btnx_double_var[46].geometry().x(), int(btnx_double_var[46].geometry().y()) + int(btnx_size / 2))

        tbx_var[0].resize((btnx_size * 6) + (btnx_sp_size * 6) - main_border_height * 2, int(btnx_size / 2) - btnx_sp_size + 20)
        tbx_var[0].show()

        tbx_var[30].resize((btnx_size * 6) + (btnx_sp_size * 6) - main_border_height * 2, int(btnx_size + btnx_size / 2) + 10)
        tbx_var[30].show()

        self.titel_label_news.show()

        # install an event filter to self
        self.installEventFilter(self.filter)

        # debug output timer
        self.debug_timer_0 = QTimer(self)
        self.debug_timer_0.setInterval(0)
        self.debug_timer_0.timeout.connect(self.debug_timer_0_function)
        self.debug_timer_0_start_function()

        self.initUI()

    def initUI(self):
        global debug_enable_bool, debug_messages, thread_nuclear_strike_imminent

        thread_nuclear_strike_imminent = NUCLEAR_STRIKE_IMMINENT(self.btn_NUKE_ALARM, self.btn_MUTE_NUKE_ALARM)

        # self.thread_0 = Class0()
        # self.thread_1 = Class1()
        self.thread_0.start()
        self.thread_1.start()

        # if debug_enable_bool is True:
        #     debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [App.initUI] displaying application'))
        self.show()

    @QtCore.pyqtSlot()
    def debug_timer_0_start_function(self):
        self.debug_timer_0.start()

    @QtCore.pyqtSlot()
    def debug_timer_0_stop_function(self):
        self.debug_timer_0.stop()

    @QtCore.pyqtSlot()
    def debug_timer_0_function(self):
        global debug_messages
        if debug_messages:
            print(debug_messages[0])
            tbx_var[0].append(debug_messages[0])
            debug_messages.remove(debug_messages[0])
        if defcon_scraper_module.debug_output:
            tbx_var[0].append(defcon_scraper_module.debug_output[0])
            defcon_scraper_module.debug_output.remove(defcon_scraper_module.debug_output[0])
        if nasa_climate.debug_output:
            tbx_var[0].append(nasa_climate.debug_output[0])
            nasa_climate.debug_output.remove(nasa_climate.debug_output[0])

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.prev_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        global pin_to_taskbar, titlebar_range_xy, prev_event
        delta = QPoint(event.globalPos() - self.prev_pos)
        if pin_to_taskbar is False:
            # uncomment to only move application when cursor is inside title bar area
            # if titlebar_range_xy is True:
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.prev_pos = event.globalPos()

    def poll_cursor(self):
        global user_mouse_activity
        pos = QCursor.pos()
        if pos != self.cursor:
            user_mouse_activity = True
            self.cursor = pos
            self.cursorMove.emit(pos)
        elif pos == self.cursor:
            user_mouse_activity = False

    def get_xy_wh(self):
        global app_height_static, app_width_static
        global cur_pos_x, cur_pos_y
        global self_pos_x, self_pos_y
        global app_w, app_h
        
        # cursor position xy
        cur_pos_x = int(self.cursor.x())
        cur_pos_y = int(self.cursor.y())

        # application position xy
        self_pos_x = int(self.x())
        self_pos_y = int(self.y())

        # application size wh
        app_w = int(app_width_static)
        app_h = int(app_height_static)

    def is_cursor_app_range_xy(self):
        global app_height_static, app_width_static
        global cur_pos_x, cur_pos_y
        global self_pos_x, self_pos_y
        global app_w, app_h
        global app_x_range, app_y_range, app_range_xy

        # get xy wh
        self.get_xy_wh()

        # check x range
        if cur_pos_x > self_pos_x and cur_pos_x < (self_pos_x + app_w):
            app_x_range = True
        else:
            app_x_range = False
            app_range_xy = False
            
        # check y range
        if cur_pos_y > self_pos_y and cur_pos_y < (self_pos_y + app_h):
            app_y_range = True
        else:
            app_x_range = False
            app_range_xy = False
            
        # set app range xy
        if app_x_range is True and app_y_range is True:
            app_range_xy = True
        else:
            app_range_xy = False

    def is_cursor_title_bar_range_xy(self):
        global app_height_static, app_width_static
        global cur_pos_x, cur_pos_y
        global self_pos_x, self_pos_y
        global app_w, app_h
        global titlebar_range_xy
        self.get_xy_wh()
        titlebar_range_xy = False
        if cur_pos_x > self_pos_x and cur_pos_x < (self_pos_x + app_w):
            if cur_pos_y > self_pos_y and cur_pos_y < (self_pos_y + titlebar_height):
                titlebar_range_xy = True

    def handle_cursor_move(self):
        global app_x_range, app_y_range, app_range_xy
        try:
            if self.isMinimized() is False:
                self.is_cursor_app_range_xy()
                self.is_cursor_title_bar_range_xy()
        except Exception as e:
            print(str('[' + str(datetime.datetime.now()) + ']' + str(e)))
            # debug_messages.append(str('[' + str(datetime.datetime.now()) + ']' + str(e)))


class NUCLEAR_STRIKE_IMMINENT(QThread):
    def __init__(self, btn_NUKE_ALARM, btn_MUTE_NUKE_ALARM):
        QThread.__init__(self)

        self.btn_NUKE_ALARM = btn_NUKE_ALARM
        self.btn_MUTE_NUKE_ALARM = btn_MUTE_NUKE_ALARM

    def play_notification_sound(self):
        debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [SYSTEM] [SIREN] Attempting to start'))
        player_default.play()
        time.sleep(1)

    def stop_notification_sound(self):
        debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [SYSTEM] [SIREN] Attempting to stop'))
        player_default.stop()
        time.sleep(1)

    def mute_notification(self):
        player_default.setMuted(True)

    def unmute_notification(self):
        player_default.setMuted(False)

    def check_notification_state(self):
        global mute_default_player
        if player_default.state() == 0:
            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [SYSTEM] [SIREN] Attempting to restart siren'))
            self.play_notification_sound()

        if mute_default_player is True:
            self.mute_notification()
        elif mute_default_player is False:
            self.unmute_notification()

    def run(self):
        debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [SYSTEM] [PLUGGED IN] NUCLEAR_STRIKE_IMMINENT PROCESS'))
        self.btn_NUKE_ALARM.show()
        self.btn_MUTE_NUKE_ALARM.show()

        while True:
            self.check_notification_state()
            self.btn_NUKE_ALARM.setStyleSheet("""QPushButton{background-color: rgb(255, 0, 0);
                            color: rgb(255, 255, 0);
                            border-top:0px solid rgb(0, 0, 0);
                            border-bottom:0px solid rgb(0, 0, 0);
                            border-right:0px solid rgb(0, 0, 0);
                            border-left:0px solid rgb(0, 0, 0);}
                            QPushButton::hover {
                                background-color : rgb(0,0,155);
                            }
                            QPushButton::pressed {
                                color: rgb(255, 255, 0);
                                background-color : rgb(26,26,26);
                                border-top:8px solid rgb(14, 14, 14);
                                border-bottom:8px solid rgb(14, 14, 14);
                                border-right:8px solid rgb(14, 14, 14);
                                border-left:8px solid rgb(14, 14, 14);}
                            }""")
            time.sleep(0.3)
            self.btn_NUKE_ALARM.setStyleSheet("""QPushButton{background-color: rgb(0, 0, 0);
                            color: rgb(255, 255, 0);
                            border-top:0px solid rgb(0, 0, 0);
                            border-bottom:0px solid rgb(0, 0, 0);
                            border-right:0px solid rgb(0, 0, 0);
                            border-left:0px solid rgb(0, 0, 0);}
                            QPushButton::hover {
                                background-color : rgb(0,0,155);
                            }
                            QPushButton::pressed {
                                color: rgb(255, 255, 0);
                                background-color : rgb(26,26,26);
                                border-top:8px solid rgb(14, 14, 14);
                                border-bottom:8px solid rgb(14, 14, 14);
                                border-right:8px solid rgb(14, 14, 14);
                                border-left:8px solid rgb(14, 14, 14);}
                            }""")
            time.sleep(0.3)

    def stop(self):
        debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [SYSTEM] [ABORTING] NUCLEAR_STRIKE_IMMINENT PROCESS'))
        self.stop_notification_sound()
        debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [SYSTEM] [SIREN] Attempting to stop'))
        player_default.stop()
        self.btn_NUKE_ALARM.hide()
        self.btn_MUTE_NUKE_ALARM.hide()
        self.terminate()


class Class0(QThread):
    def __init__(self):
        QThread.__init__(self)

    def set_defcon(self):
        global btnx_double_var, lblx_var, thread_nuclear_strike_imminent, prev_defcon_level

        defcon_level = []

        if os.path.exists('./defcon_level.txt'):
            with open('./defcon_level.txt', 'r') as fo:
                i = 0
                for line in fo:
                    line = line.strip()
                    line = line.split('   ')

                    if line[0].isdigit():
                        defcon_level.append(line[0])

                    if line[0].startswith('[LAST_UPDATED]'):
                        debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [SYSTEM] [DEFCON] changes last made: ' + str(line[1])))
                    else:
                        img = "./resources/image/defcon-" + str(line[0][0]) + ".png"
                        if i == 0:
                            if prev_defcon_level[i] != line[0]:
                                if prev_defcon_level[i] != None:
                                    player_0.play()
                                prev_defcon_level[i] = line[0]
                                btnx_double_var[6].setText('')
                                btnx_double_var[6].setIcon(QIcon(img))

                        if i == 1:
                            if prev_defcon_level[i] != line[0]:
                                if prev_defcon_level[i] != None:
                                    player_0.play()
                                prev_defcon_level[i] = line[0]
                                btnx_double_var[8].setText('')
                                btnx_double_var[8].setIcon(QIcon(img))
                        if i == 2:
                            if prev_defcon_level[i] != line[0]:
                                if prev_defcon_level[i] != None:
                                    player_0.play()
                                prev_defcon_level[i] = line[0]
                                btnx_double_var[10].setText('')
                                btnx_double_var[10].setIcon(QIcon(img))
                        if i == 3:
                            if prev_defcon_level[i] != line[0]:
                                if prev_defcon_level[i] != None:
                                    player_0.play()
                                prev_defcon_level[i] = line[0]
                                btnx_double_var[12].setText('')
                                btnx_double_var[12].setIcon(QIcon(img))
                        if i == 4:
                            if prev_defcon_level[i] != line[0]:
                                if prev_defcon_level[i] != None:
                                    player_0.play()
                                prev_defcon_level[i] = line[0]
                                btnx_double_var[14].setText('')
                                btnx_double_var[14].setIcon(QIcon(img))
                        if i == 5:
                            if prev_defcon_level[i] != line[0]:
                                if prev_defcon_level[i] != None:
                                    player_0.play()
                                prev_defcon_level[i] = line[0]
                                btnx_double_var[16].setText('')
                                btnx_double_var[16].setIcon(QIcon(img))
                        if i == 6:
                            if prev_defcon_level[i] != line[0]:
                                if prev_defcon_level[i] != None:
                                    player_0.play()
                                prev_defcon_level[i] = line[0]
                                btnx_double_var[18].setText('')
                                btnx_double_var[18].setIcon(QIcon(img))
                        if i == 7:
                            if prev_defcon_level[i] != line[0]:
                                if prev_defcon_level[i] != None:
                                    player_0.play()
                                prev_defcon_level[i] = line[0]
                                btnx_double_var[20].setText('')
                                btnx_double_var[20].setIcon(QIcon(img))
                        if i == 8:
                            if prev_defcon_level[i] != line[0]:
                                if prev_defcon_level[i] != None:
                                    player_0.play()
                                prev_defcon_level[i] = line[0]
                                btnx_double_var[22].setText('')
                                btnx_double_var[22].setIcon(QIcon(img))
                        i += 1

        if '1' in defcon_level:
            if not thread_nuclear_strike_imminent.isRunning():
                debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [SYSTEM] [STARTING] NUCLEAR_STRIKE_IMMINENT PROCESS'))
                thread_nuclear_strike_imminent.start()
        else:
            if thread_nuclear_strike_imminent.isRunning():
                thread_nuclear_strike_imminent.stop()

    def run(self):
        global btnx_double_var, lblx_var, defcon_update_time
        time.sleep(3)

        defcon_scraper_module.output = False

        while True:
            t0 = time.time()
            t1 = t0
            next_defcon_update_dttime = datetime.datetime.fromtimestamp(t0 + defcon_update_time)
            next_defcon_update_time = t0 + defcon_update_time
            # set next_defcon_update_time object

            try:
                """ [1] SET DEFCON LEVELS """
                self.set_defcon()

                """ [2] GET DEFCON LEVELS """
                defcon_scraper_module.get_defcon_levels(save_defcon_levels=True)
                self.set_defcon()

                """ [3] GET DEFCON NEWS """
                defcon_scraper_module.defcon_news(save_news=True)

            except Exception as e:
                technical_data = str('[' + str(datetime.datetime.now()) + '] [SYSTEM] [DEFCON] ' + str(e))
                debug_messages.append(technical_data)
                time.sleep(5)
                self.run()

            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [SYSTEM] [DEFCON] next update after: ' + str(next_defcon_update_dttime)))
            while not t1 > next_defcon_update_time:
                next_defcon_update_time = t0 + defcon_update_time
                t1 = time.time()
                time.sleep(1)

    def stop_thread(self):
        print('-- plugged in: Class0(stop_thread)')
        self.terminate()


class Class1(QThread):
    def __init__(self):
        QThread.__init__(self)

    def set_nasa_climate(self):
        global btnx_double_var
        nasa_climate_values = []
        if os.path.exists('./nasa_climate.txt'):
            with open('./nasa_climate.txt', 'r') as fo:
                for line in fo:
                    line = line.strip()
                    nasa_climate_values.append(line)
        if nasa_climate_values:
            last_nasa_climate_value = nasa_climate_values[-1].split('   ')

        if len(nasa_climate_values) >= 2:
            next_1_last_nasa_climate_value = nasa_climate_values[-2].split('   ')
            btnx_double_var[36].setText(last_nasa_climate_value[1] + '\n' + next_1_last_nasa_climate_value[1])
            btnx_double_var[38].setText(last_nasa_climate_value[2] + '\n' + next_1_last_nasa_climate_value[2])
            btnx_double_var[40].setText(last_nasa_climate_value[3] + '\n' + next_1_last_nasa_climate_value[3])
            btnx_double_var[42].setText(last_nasa_climate_value[4].replace(' per year', '') + '\n' + next_1_last_nasa_climate_value[4].replace(' per year', ''))
            btnx_double_var[44].setText(last_nasa_climate_value[5] + '\n' + next_1_last_nasa_climate_value[5])
            btnx_double_var[46].setText(last_nasa_climate_value[6].replace('zettajoules', ' zj') + '\n' + next_1_last_nasa_climate_value[6].replace('zettajoules', ' zj'))

        elif len(nasa_climate_values) == 1:
            btnx_double_var[36].setText(last_nasa_climate_value[1])
            btnx_double_var[38].setText(last_nasa_climate_value[2])
            btnx_double_var[40].setText(last_nasa_climate_value[3])
            btnx_double_var[42].setText(last_nasa_climate_value[4].replace(' per year', ''))
            btnx_double_var[44].setText(last_nasa_climate_value[5])
            btnx_double_var[46].setText(last_nasa_climate_value[6].replace('zettajoules', ' zj'))

    def run(self):
        global btnx_double_var, lblx_var, nasa_update_time
        time.sleep(3)

        nasa_climate.output = True

        while True:
            t0 = time.time()
            t1 = t0
            next_nasa_update_dttime = datetime.datetime.fromtimestamp(t0 + nasa_update_time)
            next_nasa_update_time = t0 + nasa_update_time
            # set next_nasa_update_time object

            try:
                """ [1] SET NASA CLIMATE """
                self.set_nasa_climate()

                """ [2] GET NASA CLIMATE """
                nasa_climate.nasa_climate()
                self.set_nasa_climate()

            except Exception as e:
                technical_data = str('[' + str(datetime.datetime.now()) + '] [SYSTEM]  [NASA] ' + str(e))
                debug_messages.append(technical_data)
                time.sleep(5)
                self.run()

            debug_messages.append(str('[' + str(datetime.datetime.now()) + '] [SYSTEM] [NASA] next update after: ' + str(next_nasa_update_dttime)))
            while not t1 > next_nasa_update_time:
                next_nasa_update_time = t0 + nasa_update_time
                t1 = time.time()
                time.sleep(1)

    def stop_thread(self):
        print('-- plugged in: Class1(stop_thread)')
        self.terminate()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
