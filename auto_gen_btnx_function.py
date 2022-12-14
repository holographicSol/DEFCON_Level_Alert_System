import os
import PyQt5
import PyQt5.QtCore
import datetime
import sol_style
import auto_gen_main_page
import auto_gen_btnx_function
import auto_gen_btnx_double_function
import auto_gen_qle_returnpressed_connect_function
import auto_gen_qle_double_returnpressed_connect_function
import auto_gen_tbx_update_function
import auto_gen_btnx_bool
import auto_gen_btnx_double_bool
import auto_gen_qle_bool
import auto_gen_qle_double_bool

var_btnx = []
var_btnx_double = []
var_lblx = []
var_qlex = []
var_qlex_double = []
var_tbx = []
var_tbx_timer = []
var_btnx_double_timer = []
var_btnx_double_timer_sub = []
var_btnx_timer = []
var_btnx_timer_sub = []
var_self = []

@PyQt5.QtCore.pyqtSlot()
def btnx_0_start_timer_function():
    global var_btnx_timer
    var_btnx_timer[0].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_0_stop_timer_function():
    global var_btnx_timer
    var_btnx_timer[0].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_0_timer_clicked_function():
    print(btnx_0_timer_clicked_function)

def btnx_0_function():
    auto_gen_main_page.main_page = 0
    if auto_gen_btnx_bool.btnx_0_bool is True:
        auto_gen_btnx_bool.btnx_0_bool = False
        # btnx_0_stop_timer_function()
    elif auto_gen_btnx_bool.btnx_0_bool is False:
        auto_gen_btnx_bool.btnx_0_bool = True
        # btnx_0_start_timer_function()
    print('[btnx_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_0_bool) + ']')

@PyQt5.QtCore.pyqtSlot()
def btnx_1_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[0].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_1_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[0].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_1_0_timer_clicked_function():
    print(btnx_1_0_timer_clicked_function)

def btnx_1_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_1_0_bool is True:
            auto_gen_btnx_bool.btnx_1_0_bool = False
            print('[btnx_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_1_0_bool) + ']')
            # btnx_1_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_1_0_bool is False:
            auto_gen_btnx_bool.btnx_1_0_bool = True
            print('[btnx_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_1_0_bool) + ']')
            # btnx_1_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_2_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[1].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_2_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[1].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_2_0_timer_clicked_function():
    print(btnx_2_0_timer_clicked_function)

def btnx_2_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_2_0_bool is True:
            auto_gen_btnx_bool.btnx_2_0_bool = False
            print('[btnx_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_2_0_bool) + ']')
            # btnx_2_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_2_0_bool is False:
            auto_gen_btnx_bool.btnx_2_0_bool = True
            print('[btnx_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_2_0_bool) + ']')
            # btnx_2_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_3_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[2].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_3_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[2].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_3_0_timer_clicked_function():
    print(btnx_3_0_timer_clicked_function)

def btnx_3_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_3_0_bool is True:
            auto_gen_btnx_bool.btnx_3_0_bool = False
            print('[btnx_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_3_0_bool) + ']')
            # btnx_3_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_3_0_bool is False:
            auto_gen_btnx_bool.btnx_3_0_bool = True
            print('[btnx_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_3_0_bool) + ']')
            # btnx_3_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_4_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[3].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_4_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[3].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_4_0_timer_clicked_function():
    print(btnx_4_0_timer_clicked_function)

def btnx_4_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_4_0_bool is True:
            auto_gen_btnx_bool.btnx_4_0_bool = False
            print('[btnx_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_4_0_bool) + ']')
            # btnx_4_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_4_0_bool is False:
            auto_gen_btnx_bool.btnx_4_0_bool = True
            print('[btnx_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_4_0_bool) + ']')
            # btnx_4_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_5_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[4].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_5_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[4].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_5_0_timer_clicked_function():
    print(btnx_5_0_timer_clicked_function)

def btnx_5_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_5_0_bool is True:
            auto_gen_btnx_bool.btnx_5_0_bool = False
            print('[btnx_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_5_0_bool) + ']')
            # btnx_5_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_5_0_bool is False:
            auto_gen_btnx_bool.btnx_5_0_bool = True
            print('[btnx_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_5_0_bool) + ']')
            # btnx_5_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_6_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[5].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_6_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[5].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_6_0_timer_clicked_function():
    print(btnx_6_0_timer_clicked_function)

def btnx_6_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_6_0_bool is True:
            auto_gen_btnx_bool.btnx_6_0_bool = False
            print('[btnx_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_6_0_bool) + ']')
            # btnx_6_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_6_0_bool is False:
            auto_gen_btnx_bool.btnx_6_0_bool = True
            print('[btnx_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_6_0_bool) + ']')
            # btnx_6_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_7_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[6].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_7_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[6].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_7_0_timer_clicked_function():
    print(btnx_7_0_timer_clicked_function)

def btnx_7_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_7_0_bool is True:
            auto_gen_btnx_bool.btnx_7_0_bool = False
            print('[btnx_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_7_0_bool) + ']')
            # btnx_7_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_7_0_bool is False:
            auto_gen_btnx_bool.btnx_7_0_bool = True
            print('[btnx_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_7_0_bool) + ']')
            # btnx_7_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_8_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[7].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_8_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[7].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_8_0_timer_clicked_function():
    print(btnx_8_0_timer_clicked_function)

def btnx_8_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_8_0_bool is True:
            auto_gen_btnx_bool.btnx_8_0_bool = False
            print('[btnx_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_8_0_bool) + ']')
            # btnx_8_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_8_0_bool is False:
            auto_gen_btnx_bool.btnx_8_0_bool = True
            print('[btnx_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_8_0_bool) + ']')
            # btnx_8_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_9_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[8].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_9_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[8].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_9_0_timer_clicked_function():
    print(btnx_9_0_timer_clicked_function)

def btnx_9_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_9_0_bool is True:
            auto_gen_btnx_bool.btnx_9_0_bool = False
            print('[btnx_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_9_0_bool) + ']')
            # btnx_9_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_9_0_bool is False:
            auto_gen_btnx_bool.btnx_9_0_bool = True
            print('[btnx_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_9_0_bool) + ']')
            # btnx_9_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_10_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[9].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_10_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[9].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_10_0_timer_clicked_function():
    print(btnx_10_0_timer_clicked_function)

def btnx_10_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_10_0_bool is True:
            auto_gen_btnx_bool.btnx_10_0_bool = False
            print('[btnx_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_10_0_bool) + ']')
            # btnx_10_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_10_0_bool is False:
            auto_gen_btnx_bool.btnx_10_0_bool = True
            print('[btnx_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_10_0_bool) + ']')
            # btnx_10_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_11_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[10].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_11_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[10].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_11_0_timer_clicked_function():
    print(btnx_11_0_timer_clicked_function)

def btnx_11_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_11_0_bool is True:
            auto_gen_btnx_bool.btnx_11_0_bool = False
            print('[btnx_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_11_0_bool) + ']')
            # btnx_11_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_11_0_bool is False:
            auto_gen_btnx_bool.btnx_11_0_bool = True
            print('[btnx_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_11_0_bool) + ']')
            # btnx_11_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_12_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[11].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_12_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[11].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_12_0_timer_clicked_function():
    print(btnx_12_0_timer_clicked_function)

def btnx_12_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_12_0_bool is True:
            auto_gen_btnx_bool.btnx_12_0_bool = False
            print('[btnx_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_12_0_bool) + ']')
            # btnx_12_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_12_0_bool is False:
            auto_gen_btnx_bool.btnx_12_0_bool = True
            print('[btnx_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_12_0_bool) + ']')
            # btnx_12_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_13_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[12].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_13_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[12].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_13_0_timer_clicked_function():
    print(btnx_13_0_timer_clicked_function)

def btnx_13_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_13_0_bool is True:
            auto_gen_btnx_bool.btnx_13_0_bool = False
            print('[btnx_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_13_0_bool) + ']')
            # btnx_13_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_13_0_bool is False:
            auto_gen_btnx_bool.btnx_13_0_bool = True
            print('[btnx_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_13_0_bool) + ']')
            # btnx_13_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_14_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[13].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_14_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[13].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_14_0_timer_clicked_function():
    print(btnx_14_0_timer_clicked_function)

def btnx_14_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_14_0_bool is True:
            auto_gen_btnx_bool.btnx_14_0_bool = False
            print('[btnx_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_14_0_bool) + ']')
            # btnx_14_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_14_0_bool is False:
            auto_gen_btnx_bool.btnx_14_0_bool = True
            print('[btnx_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_14_0_bool) + ']')
            # btnx_14_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_15_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[14].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_15_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[14].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_15_0_timer_clicked_function():
    print(btnx_15_0_timer_clicked_function)

def btnx_15_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_15_0_bool is True:
            auto_gen_btnx_bool.btnx_15_0_bool = False
            print('[btnx_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_15_0_bool) + ']')
            # btnx_15_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_15_0_bool is False:
            auto_gen_btnx_bool.btnx_15_0_bool = True
            print('[btnx_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_15_0_bool) + ']')
            # btnx_15_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_16_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[15].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_16_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[15].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_16_0_timer_clicked_function():
    print(btnx_16_0_timer_clicked_function)

def btnx_16_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_16_0_bool is True:
            auto_gen_btnx_bool.btnx_16_0_bool = False
            print('[btnx_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_16_0_bool) + ']')
            # btnx_16_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_16_0_bool is False:
            auto_gen_btnx_bool.btnx_16_0_bool = True
            print('[btnx_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_16_0_bool) + ']')
            # btnx_16_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_17_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[16].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_17_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[16].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_17_0_timer_clicked_function():
    print(btnx_17_0_timer_clicked_function)

def btnx_17_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_17_0_bool is True:
            auto_gen_btnx_bool.btnx_17_0_bool = False
            print('[btnx_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_17_0_bool) + ']')
            # btnx_17_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_17_0_bool is False:
            auto_gen_btnx_bool.btnx_17_0_bool = True
            print('[btnx_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_17_0_bool) + ']')
            # btnx_17_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_18_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[17].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_18_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[17].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_18_0_timer_clicked_function():
    print(btnx_18_0_timer_clicked_function)

def btnx_18_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_18_0_bool is True:
            auto_gen_btnx_bool.btnx_18_0_bool = False
            print('[btnx_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_18_0_bool) + ']')
            # btnx_18_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_18_0_bool is False:
            auto_gen_btnx_bool.btnx_18_0_bool = True
            print('[btnx_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_18_0_bool) + ']')
            # btnx_18_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_19_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[18].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_19_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[18].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_19_0_timer_clicked_function():
    print(btnx_19_0_timer_clicked_function)

def btnx_19_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_19_0_bool is True:
            auto_gen_btnx_bool.btnx_19_0_bool = False
            print('[btnx_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_19_0_bool) + ']')
            # btnx_19_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_19_0_bool is False:
            auto_gen_btnx_bool.btnx_19_0_bool = True
            print('[btnx_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_19_0_bool) + ']')
            # btnx_19_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_20_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[19].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_20_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[19].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_20_0_timer_clicked_function():
    print(btnx_20_0_timer_clicked_function)

def btnx_20_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_20_0_bool is True:
            auto_gen_btnx_bool.btnx_20_0_bool = False
            print('[btnx_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_20_0_bool) + ']')
            # btnx_20_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_20_0_bool is False:
            auto_gen_btnx_bool.btnx_20_0_bool = True
            print('[btnx_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_20_0_bool) + ']')
            # btnx_20_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_21_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[20].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_21_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[20].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_21_0_timer_clicked_function():
    print(btnx_21_0_timer_clicked_function)

def btnx_21_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_21_0_bool is True:
            auto_gen_btnx_bool.btnx_21_0_bool = False
            print('[btnx_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_21_0_bool) + ']')
            # btnx_21_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_21_0_bool is False:
            auto_gen_btnx_bool.btnx_21_0_bool = True
            print('[btnx_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_21_0_bool) + ']')
            # btnx_21_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_22_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[21].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_22_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[21].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_22_0_timer_clicked_function():
    print(btnx_22_0_timer_clicked_function)

def btnx_22_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_22_0_bool is True:
            auto_gen_btnx_bool.btnx_22_0_bool = False
            print('[btnx_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_22_0_bool) + ']')
            # btnx_22_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_22_0_bool is False:
            auto_gen_btnx_bool.btnx_22_0_bool = True
            print('[btnx_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_22_0_bool) + ']')
            # btnx_22_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_23_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[22].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_23_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[22].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_23_0_timer_clicked_function():
    print(btnx_23_0_timer_clicked_function)

def btnx_23_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_23_0_bool is True:
            auto_gen_btnx_bool.btnx_23_0_bool = False
            print('[btnx_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_23_0_bool) + ']')
            # btnx_23_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_23_0_bool is False:
            auto_gen_btnx_bool.btnx_23_0_bool = True
            print('[btnx_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_23_0_bool) + ']')
            # btnx_23_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_24_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[23].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_24_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[23].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_24_0_timer_clicked_function():
    print(btnx_24_0_timer_clicked_function)

def btnx_24_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_24_0_bool is True:
            auto_gen_btnx_bool.btnx_24_0_bool = False
            print('[btnx_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_24_0_bool) + ']')
            # btnx_24_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_24_0_bool is False:
            auto_gen_btnx_bool.btnx_24_0_bool = True
            print('[btnx_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_24_0_bool) + ']')
            # btnx_24_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_25_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[24].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_25_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[24].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_25_0_timer_clicked_function():
    print(btnx_25_0_timer_clicked_function)

def btnx_25_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_25_0_bool is True:
            auto_gen_btnx_bool.btnx_25_0_bool = False
            print('[btnx_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_25_0_bool) + ']')
            # btnx_25_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_25_0_bool is False:
            auto_gen_btnx_bool.btnx_25_0_bool = True
            print('[btnx_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_25_0_bool) + ']')
            # btnx_25_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_26_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[25].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_26_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[25].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_26_0_timer_clicked_function():
    print(btnx_26_0_timer_clicked_function)

def btnx_26_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_26_0_bool is True:
            auto_gen_btnx_bool.btnx_26_0_bool = False
            print('[btnx_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_26_0_bool) + ']')
            # btnx_26_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_26_0_bool is False:
            auto_gen_btnx_bool.btnx_26_0_bool = True
            print('[btnx_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_26_0_bool) + ']')
            # btnx_26_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_27_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[26].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_27_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[26].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_27_0_timer_clicked_function():
    print(btnx_27_0_timer_clicked_function)

def btnx_27_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_27_0_bool is True:
            auto_gen_btnx_bool.btnx_27_0_bool = False
            print('[btnx_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_27_0_bool) + ']')
            # btnx_27_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_27_0_bool is False:
            auto_gen_btnx_bool.btnx_27_0_bool = True
            print('[btnx_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_27_0_bool) + ']')
            # btnx_27_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_28_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[27].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_28_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[27].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_28_0_timer_clicked_function():
    print(btnx_28_0_timer_clicked_function)

def btnx_28_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_28_0_bool is True:
            auto_gen_btnx_bool.btnx_28_0_bool = False
            print('[btnx_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_28_0_bool) + ']')
            # btnx_28_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_28_0_bool is False:
            auto_gen_btnx_bool.btnx_28_0_bool = True
            print('[btnx_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_28_0_bool) + ']')
            # btnx_28_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_29_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[28].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_29_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[28].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_29_0_timer_clicked_function():
    print(btnx_29_0_timer_clicked_function)

def btnx_29_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_29_0_bool is True:
            auto_gen_btnx_bool.btnx_29_0_bool = False
            print('[btnx_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_29_0_bool) + ']')
            # btnx_29_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_29_0_bool is False:
            auto_gen_btnx_bool.btnx_29_0_bool = True
            print('[btnx_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_29_0_bool) + ']')
            # btnx_29_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_30_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[29].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_30_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[29].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_30_0_timer_clicked_function():
    print(btnx_30_0_timer_clicked_function)

def btnx_30_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_30_0_bool is True:
            auto_gen_btnx_bool.btnx_30_0_bool = False
            print('[btnx_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_30_0_bool) + ']')
            # btnx_30_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_30_0_bool is False:
            auto_gen_btnx_bool.btnx_30_0_bool = True
            print('[btnx_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_30_0_bool) + ']')
            # btnx_30_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_31_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[30].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_31_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[30].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_31_0_timer_clicked_function():
    print(btnx_31_0_timer_clicked_function)

def btnx_31_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_31_0_bool is True:
            auto_gen_btnx_bool.btnx_31_0_bool = False
            print('[btnx_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_31_0_bool) + ']')
            # btnx_31_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_31_0_bool is False:
            auto_gen_btnx_bool.btnx_31_0_bool = True
            print('[btnx_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_31_0_bool) + ']')
            # btnx_31_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_32_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[31].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_32_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[31].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_32_0_timer_clicked_function():
    print(btnx_32_0_timer_clicked_function)

def btnx_32_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_32_0_bool is True:
            auto_gen_btnx_bool.btnx_32_0_bool = False
            print('[btnx_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_32_0_bool) + ']')
            # btnx_32_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_32_0_bool is False:
            auto_gen_btnx_bool.btnx_32_0_bool = True
            print('[btnx_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_32_0_bool) + ']')
            # btnx_32_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_33_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[32].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_33_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[32].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_33_0_timer_clicked_function():
    print(btnx_33_0_timer_clicked_function)

def btnx_33_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_33_0_bool is True:
            auto_gen_btnx_bool.btnx_33_0_bool = False
            print('[btnx_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_33_0_bool) + ']')
            # btnx_33_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_33_0_bool is False:
            auto_gen_btnx_bool.btnx_33_0_bool = True
            print('[btnx_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_33_0_bool) + ']')
            # btnx_33_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_34_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[33].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_34_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[33].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_34_0_timer_clicked_function():
    print(btnx_34_0_timer_clicked_function)

def btnx_34_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_34_0_bool is True:
            auto_gen_btnx_bool.btnx_34_0_bool = False
            print('[btnx_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_34_0_bool) + ']')
            # btnx_34_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_34_0_bool is False:
            auto_gen_btnx_bool.btnx_34_0_bool = True
            print('[btnx_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_34_0_bool) + ']')
            # btnx_34_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_35_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[34].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_35_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[34].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_35_0_timer_clicked_function():
    print(btnx_35_0_timer_clicked_function)

def btnx_35_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_35_0_bool is True:
            auto_gen_btnx_bool.btnx_35_0_bool = False
            print('[btnx_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_35_0_bool) + ']')
            # btnx_35_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_35_0_bool is False:
            auto_gen_btnx_bool.btnx_35_0_bool = True
            print('[btnx_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_35_0_bool) + ']')
            # btnx_35_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_36_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[35].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_36_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[35].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_36_0_timer_clicked_function():
    print(btnx_36_0_timer_clicked_function)

def btnx_36_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_36_0_bool is True:
            auto_gen_btnx_bool.btnx_36_0_bool = False
            print('[btnx_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_36_0_bool) + ']')
            # btnx_36_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_36_0_bool is False:
            auto_gen_btnx_bool.btnx_36_0_bool = True
            print('[btnx_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_36_0_bool) + ']')
            # btnx_36_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_37_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[36].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_37_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[36].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_37_0_timer_clicked_function():
    print(btnx_37_0_timer_clicked_function)

def btnx_37_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_37_0_bool is True:
            auto_gen_btnx_bool.btnx_37_0_bool = False
            print('[btnx_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_37_0_bool) + ']')
            # btnx_37_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_37_0_bool is False:
            auto_gen_btnx_bool.btnx_37_0_bool = True
            print('[btnx_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_37_0_bool) + ']')
            # btnx_37_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_38_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[37].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_38_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[37].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_38_0_timer_clicked_function():
    print(btnx_38_0_timer_clicked_function)

def btnx_38_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_38_0_bool is True:
            auto_gen_btnx_bool.btnx_38_0_bool = False
            print('[btnx_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_38_0_bool) + ']')
            # btnx_38_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_38_0_bool is False:
            auto_gen_btnx_bool.btnx_38_0_bool = True
            print('[btnx_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_38_0_bool) + ']')
            # btnx_38_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_39_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[38].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_39_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[38].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_39_0_timer_clicked_function():
    print(btnx_39_0_timer_clicked_function)

def btnx_39_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_39_0_bool is True:
            auto_gen_btnx_bool.btnx_39_0_bool = False
            print('[btnx_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_39_0_bool) + ']')
            # btnx_39_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_39_0_bool is False:
            auto_gen_btnx_bool.btnx_39_0_bool = True
            print('[btnx_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_39_0_bool) + ']')
            # btnx_39_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_40_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[39].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_40_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[39].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_40_0_timer_clicked_function():
    print(btnx_40_0_timer_clicked_function)

def btnx_40_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_40_0_bool is True:
            auto_gen_btnx_bool.btnx_40_0_bool = False
            print('[btnx_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_40_0_bool) + ']')
            # btnx_40_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_40_0_bool is False:
            auto_gen_btnx_bool.btnx_40_0_bool = True
            print('[btnx_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_40_0_bool) + ']')
            # btnx_40_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_41_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[40].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_41_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[40].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_41_0_timer_clicked_function():
    print(btnx_41_0_timer_clicked_function)

def btnx_41_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_41_0_bool is True:
            auto_gen_btnx_bool.btnx_41_0_bool = False
            print('[btnx_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_41_0_bool) + ']')
            # btnx_41_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_41_0_bool is False:
            auto_gen_btnx_bool.btnx_41_0_bool = True
            print('[btnx_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_41_0_bool) + ']')
            # btnx_41_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_42_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[41].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_42_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[41].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_42_0_timer_clicked_function():
    print(btnx_42_0_timer_clicked_function)

def btnx_42_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_42_0_bool is True:
            auto_gen_btnx_bool.btnx_42_0_bool = False
            print('[btnx_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_42_0_bool) + ']')
            # btnx_42_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_42_0_bool is False:
            auto_gen_btnx_bool.btnx_42_0_bool = True
            print('[btnx_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_42_0_bool) + ']')
            # btnx_42_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_43_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[42].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_43_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[42].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_43_0_timer_clicked_function():
    print(btnx_43_0_timer_clicked_function)

def btnx_43_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_43_0_bool is True:
            auto_gen_btnx_bool.btnx_43_0_bool = False
            print('[btnx_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_43_0_bool) + ']')
            # btnx_43_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_43_0_bool is False:
            auto_gen_btnx_bool.btnx_43_0_bool = True
            print('[btnx_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_43_0_bool) + ']')
            # btnx_43_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_44_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[43].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_44_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[43].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_44_0_timer_clicked_function():
    print(btnx_44_0_timer_clicked_function)

def btnx_44_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_44_0_bool is True:
            auto_gen_btnx_bool.btnx_44_0_bool = False
            print('[btnx_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_44_0_bool) + ']')
            # btnx_44_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_44_0_bool is False:
            auto_gen_btnx_bool.btnx_44_0_bool = True
            print('[btnx_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_44_0_bool) + ']')
            # btnx_44_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_45_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[44].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_45_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[44].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_45_0_timer_clicked_function():
    print(btnx_45_0_timer_clicked_function)

def btnx_45_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_45_0_bool is True:
            auto_gen_btnx_bool.btnx_45_0_bool = False
            print('[btnx_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_45_0_bool) + ']')
            # btnx_45_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_45_0_bool is False:
            auto_gen_btnx_bool.btnx_45_0_bool = True
            print('[btnx_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_45_0_bool) + ']')
            # btnx_45_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_46_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[45].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_46_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[45].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_46_0_timer_clicked_function():
    print(btnx_46_0_timer_clicked_function)

def btnx_46_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_46_0_bool is True:
            auto_gen_btnx_bool.btnx_46_0_bool = False
            print('[btnx_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_46_0_bool) + ']')
            # btnx_46_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_46_0_bool is False:
            auto_gen_btnx_bool.btnx_46_0_bool = True
            print('[btnx_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_46_0_bool) + ']')
            # btnx_46_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_47_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[46].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_47_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[46].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_47_0_timer_clicked_function():
    print(btnx_47_0_timer_clicked_function)

def btnx_47_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_47_0_bool is True:
            auto_gen_btnx_bool.btnx_47_0_bool = False
            print('[btnx_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_47_0_bool) + ']')
            # btnx_47_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_47_0_bool is False:
            auto_gen_btnx_bool.btnx_47_0_bool = True
            print('[btnx_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_47_0_bool) + ']')
            # btnx_47_0_start_timer_function()

