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
import codecs

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
def btnx_double_0_start_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[0].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_0_stop_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[0].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_0_timer_clicked_function():
    print(btnx_double_0_timer_clicked_function)

def btnx_double_0_function():
    auto_gen_main_page.main_page = 0
    if auto_gen_btnx_double_bool.btnx_double_0_bool is True:
        auto_gen_btnx_double_bool.btnx_double_0_bool = False
        # btnx_double_0_stop_timer_function()
    elif auto_gen_btnx_double_bool.btnx_double_0_bool is False:
        auto_gen_btnx_double_bool.btnx_double_0_bool = True
        # btnx_double_0_start_timer_function()
    print('[btnx_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_0_bool) + ']')

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[0].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[0].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_0_timer_clicked_function():
    print(btnx_double_1_0_timer_clicked_function)

def btnx_double_1_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_1_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_1_0_bool = False
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_0_bool) + ']')
            # btnx_double_1_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_1_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_1_0_bool = True
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_0_bool) + ']')
            # btnx_double_1_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[1].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[1].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_0_timer_clicked_function():
    print(btnx_double_2_0_timer_clicked_function)

def btnx_double_2_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_2_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_2_0_bool = False
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_0_bool) + ']')
            # btnx_double_2_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_2_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_2_0_bool = True
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_0_bool) + ']')
            # btnx_double_2_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[2].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[2].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_0_timer_clicked_function():
    print(btnx_double_3_0_timer_clicked_function)

def btnx_double_3_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_3_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_3_0_bool = False
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_0_bool) + ']')
            # btnx_double_3_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_3_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_3_0_bool = True
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_0_bool) + ']')
            # btnx_double_3_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[3].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[3].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_0_timer_clicked_function():
    print(btnx_double_4_0_timer_clicked_function)

def btnx_double_4_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_4_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_4_0_bool = False
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_0_bool) + ']')
            # btnx_double_4_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_4_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_4_0_bool = True
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_0_bool) + ']')
            # btnx_double_4_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[4].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[4].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_0_timer_clicked_function():
    print(btnx_double_5_0_timer_clicked_function)

def btnx_double_5_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_5_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_5_0_bool = False
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_0_bool) + ']')
            # btnx_double_5_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_5_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_5_0_bool = True
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_0_bool) + ']')
            # btnx_double_5_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[5].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[5].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_0_timer_clicked_function():
    print(btnx_double_6_0_timer_clicked_function)

def btnx_double_6_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_6_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_6_0_bool = False
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_0_bool) + ']')
            var_tbx[30].setText("")

        elif auto_gen_btnx_double_bool.btnx_double_6_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_6_0_bool = True
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_0_bool) + ']')
            if os.path.exists('./defcon_news_current_news.txt'):
                var_tbx[30].setText("")
                with codecs.open('./defcon_news_current_news.txt', 'r', encoding='utf8') as fo:
                    for line in fo:
                        line = line.strip()
                        var_tbx[30].append(line)
                var_tbx[30].verticalScrollBar().setValue(0)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[6].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[6].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_0_timer_clicked_function():
    print(btnx_double_7_0_timer_clicked_function)

def btnx_double_7_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_7_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_7_0_bool = False
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_0_bool) + ']')
            # btnx_double_7_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_7_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_7_0_bool = True
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_0_bool) + ']')
            # btnx_double_7_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[7].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[7].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_0_timer_clicked_function():
    print(btnx_double_8_0_timer_clicked_function)

def btnx_double_8_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_8_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_8_0_bool = False
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_0_bool) + ']')
            var_tbx[30].setText("")

        elif auto_gen_btnx_double_bool.btnx_double_8_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_8_0_bool = True
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_0_bool) + ']')
            if os.path.exists('./defcon_news_africa-command-news.txt'):
                var_tbx[30].setText("")
                with codecs.open('./defcon_news_africa-command-news.txt', 'r', encoding='utf8') as fo:
                    for line in fo:
                        line = line.strip()
                        var_tbx[30].append(line)
                var_tbx[30].verticalScrollBar().setValue(0)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[8].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[8].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_0_timer_clicked_function():
    print(btnx_double_9_0_timer_clicked_function)

def btnx_double_9_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_9_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_9_0_bool = False
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_0_bool) + ']')
            # btnx_double_9_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_9_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_9_0_bool = True
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_0_bool) + ']')
            # btnx_double_9_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[9].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[9].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_0_timer_clicked_function():
    print(btnx_double_10_0_timer_clicked_function)

def btnx_double_10_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_10_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_10_0_bool = False
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_0_bool) + ']')
            var_tbx[30].setText("")

        elif auto_gen_btnx_double_bool.btnx_double_10_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_10_0_bool = True
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_0_bool) + ']')
            if os.path.exists('./defcon_news_central-command-news.txt'):
                var_tbx[30].setText("")
                with codecs.open('./defcon_news_central-command-news.txt', 'r', encoding='utf8') as fo:
                    for line in fo:
                        line = line.strip()
                        var_tbx[30].append(line)
                var_tbx[30].verticalScrollBar().setValue(0)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[10].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[10].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_0_timer_clicked_function():
    print(btnx_double_11_0_timer_clicked_function)

def btnx_double_11_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_11_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_11_0_bool = False
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_0_bool) + ']')
            # btnx_double_11_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_11_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_11_0_bool = True
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_0_bool) + ']')
            # btnx_double_11_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_12_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[11].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_12_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[11].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_12_0_timer_clicked_function():
    print(btnx_double_12_0_timer_clicked_function)

def btnx_double_12_function():
    if auto_gen_main_page.main_page == 0:

        if auto_gen_btnx_double_bool.btnx_double_12_bool is True:
            auto_gen_btnx_double_bool.btnx_double_12_bool = False
            print('[btnx_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_12_bool) + ']')
            var_tbx[30].setText("")

        elif auto_gen_btnx_double_bool.btnx_double_12_bool is False:
            auto_gen_btnx_double_bool.btnx_double_12_bool = True
            print('[btnx_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_12_bool) + ']')
            if os.path.exists('./defcon_news_cyber-command-news.txt'):
                var_tbx[30].setText("")
                with codecs.open('./defcon_news_cyber-command-news.txt', 'r', encoding='utf8') as fo:
                    for line in fo:
                        line = line.strip()
                        var_tbx[30].append(line)
                var_tbx[30].verticalScrollBar().setValue(0)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[12].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[12].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_0_timer_clicked_function():
    print(btnx_double_13_0_timer_clicked_function)

def btnx_double_13_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_13_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_13_0_bool = False
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_0_bool) + ']')
            # btnx_double_13_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_13_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_13_0_bool = True
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_0_bool) + ']')
            # btnx_double_13_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[13].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[13].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_0_timer_clicked_function():
    print(btnx_double_14_0_timer_clicked_function)

def btnx_double_14_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_14_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_14_0_bool = False
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_0_bool) + ']')
            var_tbx[30].setText("")

        elif auto_gen_btnx_double_bool.btnx_double_14_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_14_0_bool = True
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_0_bool) + ']')
            if os.path.exists('./defcon_news_european-command-news.txt'):
                var_tbx[30].setText("")
                with codecs.open('./defcon_news_european-command-news.txt', 'r', encoding='utf8') as fo:
                    for line in fo:
                        line = line.strip()
                        var_tbx[30].append(line)
                var_tbx[30].verticalScrollBar().setValue(0)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[14].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[14].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_0_timer_clicked_function():
    print(btnx_double_15_0_timer_clicked_function)

def btnx_double_15_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_15_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_15_0_bool = False
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_0_bool) + ']')
            # btnx_double_15_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_15_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_15_0_bool = True
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_0_bool) + ']')
            # btnx_double_15_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[15].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[15].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_0_timer_clicked_function():
    print(btnx_double_16_0_timer_clicked_function)

def btnx_double_16_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_16_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_16_0_bool = False
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_0_bool) + ']')
            var_tbx[30].setText("")

        elif auto_gen_btnx_double_bool.btnx_double_16_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_16_0_bool = True
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_0_bool) + ']')
            if os.path.exists('./defcon_news_indo-pacific-command-news.txt'):
                var_tbx[30].setText("")
                with codecs.open('./defcon_news_indo-pacific-command-news.txt', 'r', encoding='utf8') as fo:
                    for line in fo:
                        line = line.strip()
                        var_tbx[30].append(line)
                var_tbx[30].verticalScrollBar().setValue(0)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[16].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[16].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_0_timer_clicked_function():
    print(btnx_double_17_0_timer_clicked_function)

def btnx_double_17_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_17_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_17_0_bool = False
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_0_bool) + ']')
            # btnx_double_17_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_17_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_17_0_bool = True
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_0_bool) + ']')
            # btnx_double_17_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[17].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[17].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_0_timer_clicked_function():
    print(btnx_double_18_0_timer_clicked_function)

def btnx_double_18_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_18_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_18_0_bool = False
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_0_bool) + ']')
            var_tbx[30].setText("")

        elif auto_gen_btnx_double_bool.btnx_double_18_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_18_0_bool = True
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_0_bool) + ']')
            if os.path.exists('./defcon_news_northern-command-news.txt'):
                var_tbx[30].setText("")
                with codecs.open('./defcon_news_northern-command-news.txt', 'r', encoding='utf8') as fo:
                    for line in fo:
                        line = line.strip()
                        var_tbx[30].append(line)
                var_tbx[30].verticalScrollBar().setValue(0)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[18].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[18].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_0_timer_clicked_function():
    print(btnx_double_19_0_timer_clicked_function)

def btnx_double_19_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_19_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_19_0_bool = False
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_0_bool) + ']')
            # btnx_double_19_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_19_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_19_0_bool = True
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_0_bool) + ']')
            # btnx_double_19_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[19].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[19].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_0_timer_clicked_function():
    print(btnx_double_20_0_timer_clicked_function)

def btnx_double_20_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_20_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_20_0_bool = False
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_0_bool) + ']')
            var_tbx[30].setText("")

        elif auto_gen_btnx_double_bool.btnx_double_20_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_20_0_bool = True
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_0_bool) + ']')
            if os.path.exists('./defcon_news_southern-command-news.txt'):
                var_tbx[30].setText("")
                with codecs.open('./defcon_news_southern-command-news.txt', 'r', encoding='utf8') as fo:
                    for line in fo:
                        line = line.strip()
                        var_tbx[30].append(line)
                var_tbx[30].verticalScrollBar().setValue(0)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[20].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[20].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_0_timer_clicked_function():
    print(btnx_double_21_0_timer_clicked_function)

def btnx_double_21_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_21_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_21_0_bool = False
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_0_bool) + ']')
            # btnx_double_21_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_21_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_21_0_bool = True
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_0_bool) + ']')
            # btnx_double_21_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[21].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[21].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_0_timer_clicked_function():
    print(btnx_double_22_0_timer_clicked_function)

def btnx_double_22_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_22_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_22_0_bool = False
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_0_bool) + ']')
            var_tbx[30].setText("")

        elif auto_gen_btnx_double_bool.btnx_double_22_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_22_0_bool = True
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_0_bool) + ']')
            if os.path.exists('./defcon_news_space-command-news.txt'):
                var_tbx[30].setText("")
                with codecs.open('./defcon_news_space-command-news.txt', 'r', encoding='utf8') as fo:
                    for line in fo:
                        line = line.strip()
                        var_tbx[30].append(line)
                var_tbx[30].verticalScrollBar().setValue(0)


@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[22].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[22].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_0_timer_clicked_function():
    print(btnx_double_23_0_timer_clicked_function)

def btnx_double_23_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_23_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_23_0_bool = False
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_0_bool) + ']')
            # btnx_double_23_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_23_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_23_0_bool = True
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_0_bool) + ']')
            # btnx_double_23_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_24_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[23].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_24_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[23].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_24_0_timer_clicked_function():
    print(btnx_double_24_0_timer_clicked_function)

def btnx_double_24_function():
    if auto_gen_btnx_double_bool.btnx_double_24_0_bool is True:
        auto_gen_btnx_double_bool.btnx_double_24_0_bool = False
        print('[btnx_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_24_0_bool) + ']')
        var_tbx[30].setText("")

    elif auto_gen_btnx_double_bool.btnx_double_24_0_bool is False:
        auto_gen_btnx_double_bool.btnx_double_24_0_bool = True
        print('[btnx_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_24_0_bool) + ']')
        if os.path.exists('./defcon_news_special-operations-command-news.txt'):
            var_tbx[30].setText("")
            with codecs.open('./defcon_news_special-operations-command-news.txt', 'r', encoding='utf8') as fo:
                for line in fo:
                    line = line.strip()
                    var_tbx[30].append(line)
            var_tbx[30].verticalScrollBar().setValue(0)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[24].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[24].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_0_timer_clicked_function():
    print(btnx_double_25_0_timer_clicked_function)

def btnx_double_25_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_25_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_25_0_bool = False
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_0_bool) + ']')
            # btnx_double_25_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_25_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_25_0_bool = True
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_0_bool) + ']')
            # btnx_double_25_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[25].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[25].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_0_timer_clicked_function():
    print(btnx_double_26_0_timer_clicked_function)

def btnx_double_26_function():
    if auto_gen_btnx_double_bool.btnx_double_26_0_bool is True:
        auto_gen_btnx_double_bool.btnx_double_26_0_bool = False
        print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_0_bool) + ']')
        var_tbx[30].setText("")

    elif auto_gen_btnx_double_bool.btnx_double_26_0_bool is False:
        auto_gen_btnx_double_bool.btnx_double_26_0_bool = True
        print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_0_bool) + ']')
        if os.path.exists('./defcon_news_strategic-command-news.txt'):
            var_tbx[30].setText("")
            with codecs.open('./defcon_news_strategic-command-news.txt', 'r', encoding='utf8') as fo:
                for line in fo:
                    line = line.strip()
                    var_tbx[30].append(line)
            var_tbx[30].verticalScrollBar().setValue(0)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[26].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[26].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_0_timer_clicked_function():
    print(btnx_double_27_0_timer_clicked_function)

def btnx_double_27_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_27_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_27_0_bool = False
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_0_bool) + ']')
            # btnx_double_27_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_27_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_27_0_bool = True
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_0_bool) + ']')
            # btnx_double_27_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[27].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[27].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_0_timer_clicked_function():
    print(btnx_double_28_0_timer_clicked_function)

def btnx_double_28_function():
    if auto_gen_main_page.main_page == 0:

        if auto_gen_btnx_double_bool.btnx_double_28_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_28_0_bool = False
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_0_bool) + ']')
            var_tbx[30].setText("")

        elif auto_gen_btnx_double_bool.btnx_double_28_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_28_0_bool = True
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_0_bool) + ']')
            if os.path.exists('./defcon_news_transportation-command-news.txt'):
                var_tbx[30].setText("")
                with codecs.open('./defcon_news_transportation-command-news.txt', 'r', encoding='utf8') as fo:
                    for line in fo:
                        line = line.strip()
                        var_tbx[30].append(line)
                var_tbx[30].verticalScrollBar().setValue(0)

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[28].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[28].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_0_timer_clicked_function():
    print(btnx_double_29_0_timer_clicked_function)

def btnx_double_29_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_29_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_29_0_bool = False
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_0_bool) + ']')
            # btnx_double_29_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_29_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_29_0_bool = True
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_0_bool) + ']')
            # btnx_double_29_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[29].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[29].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_0_timer_clicked_function():
    print(btnx_double_30_0_timer_clicked_function)

def btnx_double_30_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_30_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_30_0_bool = False
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_0_bool) + ']')
            # btnx_double_30_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_30_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_30_0_bool = True
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_0_bool) + ']')
            # btnx_double_30_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[30].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[30].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_0_timer_clicked_function():
    print(btnx_double_31_0_timer_clicked_function)

def btnx_double_31_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_31_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_31_0_bool = False
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_0_bool) + ']')
            # btnx_double_31_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_31_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_31_0_bool = True
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_0_bool) + ']')
            # btnx_double_31_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[31].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[31].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_0_timer_clicked_function():
    print(btnx_double_32_0_timer_clicked_function)

def btnx_double_32_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_32_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_32_0_bool = False
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_0_bool) + ']')
            # btnx_double_32_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_32_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_32_0_bool = True
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_0_bool) + ']')
            # btnx_double_32_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[32].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[32].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_0_timer_clicked_function():
    print(btnx_double_33_0_timer_clicked_function)

def btnx_double_33_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_33_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_33_0_bool = False
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_0_bool) + ']')
            # btnx_double_33_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_33_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_33_0_bool = True
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_0_bool) + ']')
            # btnx_double_33_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[33].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[33].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_0_timer_clicked_function():
    print(btnx_double_34_0_timer_clicked_function)

def btnx_double_34_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_34_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_34_0_bool = False
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_0_bool) + ']')
            # btnx_double_34_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_34_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_34_0_bool = True
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_0_bool) + ']')
            # btnx_double_34_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[34].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[34].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_0_timer_clicked_function():
    print(btnx_double_35_0_timer_clicked_function)

def btnx_double_35_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_35_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_35_0_bool = False
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_0_bool) + ']')
            # btnx_double_35_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_35_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_35_0_bool = True
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_0_bool) + ']')
            # btnx_double_35_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_36_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[35].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_36_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[35].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_36_0_timer_clicked_function():
    print(btnx_double_36_0_timer_clicked_function)

def btnx_double_36_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_36_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_36_0_bool = False
            print('[btnx_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_36_0_bool) + ']')
            # btnx_double_36_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_36_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_36_0_bool = True
            print('[btnx_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_36_0_bool) + ']')
            # btnx_double_36_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[36].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[36].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_0_timer_clicked_function():
    print(btnx_double_37_0_timer_clicked_function)

def btnx_double_37_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_37_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_37_0_bool = False
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_0_bool) + ']')
            # btnx_double_37_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_37_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_37_0_bool = True
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_0_bool) + ']')
            # btnx_double_37_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[37].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[37].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_0_timer_clicked_function():
    print(btnx_double_38_0_timer_clicked_function)

def btnx_double_38_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_38_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_38_0_bool = False
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_0_bool) + ']')
            # btnx_double_38_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_38_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_38_0_bool = True
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_0_bool) + ']')
            # btnx_double_38_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[38].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[38].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_0_timer_clicked_function():
    print(btnx_double_39_0_timer_clicked_function)

def btnx_double_39_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_39_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_39_0_bool = False
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_0_bool) + ']')
            # btnx_double_39_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_39_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_39_0_bool = True
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_0_bool) + ']')
            # btnx_double_39_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[39].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[39].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_0_timer_clicked_function():
    print(btnx_double_40_0_timer_clicked_function)

def btnx_double_40_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_40_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_40_0_bool = False
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_0_bool) + ']')
            # btnx_double_40_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_40_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_40_0_bool = True
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_0_bool) + ']')
            # btnx_double_40_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[40].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[40].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_0_timer_clicked_function():
    print(btnx_double_41_0_timer_clicked_function)

def btnx_double_41_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_41_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_41_0_bool = False
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_0_bool) + ']')
            # btnx_double_41_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_41_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_41_0_bool = True
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_0_bool) + ']')
            # btnx_double_41_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[41].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[41].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_0_timer_clicked_function():
    print(btnx_double_42_0_timer_clicked_function)

def btnx_double_42_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_42_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_42_0_bool = False
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_0_bool) + ']')
            # btnx_double_42_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_42_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_42_0_bool = True
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_0_bool) + ']')
            # btnx_double_42_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[42].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[42].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_0_timer_clicked_function():
    print(btnx_double_43_0_timer_clicked_function)

def btnx_double_43_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_43_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_43_0_bool = False
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_0_bool) + ']')
            # btnx_double_43_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_43_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_43_0_bool = True
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_0_bool) + ']')
            # btnx_double_43_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[43].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[43].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_0_timer_clicked_function():
    print(btnx_double_44_0_timer_clicked_function)

def btnx_double_44_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_44_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_44_0_bool = False
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_0_bool) + ']')
            # btnx_double_44_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_44_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_44_0_bool = True
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_0_bool) + ']')
            # btnx_double_44_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[44].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[44].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_0_timer_clicked_function():
    print(btnx_double_45_0_timer_clicked_function)

def btnx_double_45_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_45_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_45_0_bool = False
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_0_bool) + ']')
            # btnx_double_45_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_45_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_45_0_bool = True
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_0_bool) + ']')
            # btnx_double_45_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[45].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[45].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_0_timer_clicked_function():
    print(btnx_double_46_0_timer_clicked_function)

def btnx_double_46_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_46_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_46_0_bool = False
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_0_bool) + ']')
            # btnx_double_46_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_46_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_46_0_bool = True
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_0_bool) + ']')
            # btnx_double_46_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[46].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[46].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_0_timer_clicked_function():
    print(btnx_double_47_0_timer_clicked_function)

def btnx_double_47_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_47_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_47_0_bool = False
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_0_bool) + ']')
            # btnx_double_47_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_47_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_47_0_bool = True
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_0_bool) + ']')
            # btnx_double_47_0_start_timer_function()

