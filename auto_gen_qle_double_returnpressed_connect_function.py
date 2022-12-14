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

def qlex_double_0_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_0'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_0_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_0_0_bool = False
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_0_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_0_0_bool = True
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_0_bool) + ']')

def qlex_double_1_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_1'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_1_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_1_0_bool = False
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_1_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_1_0_bool = True
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_0_bool) + ']')

def qlex_double_2_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_2'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_2_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_2_0_bool = False
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_2_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_2_0_bool = True
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_0_bool) + ']')

def qlex_double_3_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_3'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_3_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_3_0_bool = False
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_3_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_3_0_bool = True
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_0_bool) + ']')

def qlex_double_4_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_4'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_4_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_4_0_bool = False
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_4_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_4_0_bool = True
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_0_bool) + ']')

def qlex_double_5_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_5'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_5_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_5_0_bool = False
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_5_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_5_0_bool = True
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_0_bool) + ']')

def qlex_double_6_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_6'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_6_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_6_0_bool = False
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_6_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_6_0_bool = True
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_0_bool) + ']')

def qlex_double_7_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_7'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_7_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_7_0_bool = False
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_7_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_7_0_bool = True
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_0_bool) + ']')

def qlex_double_8_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_8'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_8_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_8_0_bool = False
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_8_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_8_0_bool = True
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_0_bool) + ']')

def qlex_double_9_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_9'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_9_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_9_0_bool = False
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_9_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_9_0_bool = True
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_0_bool) + ']')

def qlex_double_10_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_10'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_10_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_10_0_bool = False
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_10_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_10_0_bool = True
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_0_bool) + ']')

def qlex_double_11_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_11'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_11_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_11_0_bool = False
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_11_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_11_0_bool = True
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_0_bool) + ']')

def qlex_double_12_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_12'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_12_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_12_0_bool = False
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_12_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_12_0_bool = True
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_0_bool) + ']')

def qlex_double_13_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_13'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_13_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_13_0_bool = False
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_13_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_13_0_bool = True
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_0_bool) + ']')

def qlex_double_14_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_14'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_14_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_14_0_bool = False
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_14_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_14_0_bool = True
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_0_bool) + ']')

def qlex_double_15_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_15'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_15_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_15_0_bool = False
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_15_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_15_0_bool = True
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_0_bool) + ']')

def qlex_double_16_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_16'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_16_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_16_0_bool = False
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_16_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_16_0_bool = True
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_0_bool) + ']')

def qlex_double_17_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_17'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_17_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_17_0_bool = False
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_17_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_17_0_bool = True
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_0_bool) + ']')

def qlex_double_18_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_18'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_18_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_18_0_bool = False
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_18_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_18_0_bool = True
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_0_bool) + ']')

def qlex_double_19_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_19'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_19_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_19_0_bool = False
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_19_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_19_0_bool = True
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_0_bool) + ']')

def qlex_double_20_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_20'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_20_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_20_0_bool = False
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_20_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_20_0_bool = True
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_0_bool) + ']')

def qlex_double_21_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_21'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_21_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_21_0_bool = False
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_21_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_21_0_bool = True
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_0_bool) + ']')

def qlex_double_22_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_22'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_22_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_22_0_bool = False
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_22_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_22_0_bool = True
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_0_bool) + ']')

def qlex_double_23_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_23'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_23_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_23_0_bool = False
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_23_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_23_0_bool = True
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_0_bool) + ']')

def qlex_double_24_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_24'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_24_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_24_0_bool = False
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_24_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_24_0_bool = True
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_0_bool) + ']')

def qlex_double_25_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_25'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_25_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_25_0_bool = False
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_25_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_25_0_bool = True
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_0_bool) + ']')

def qlex_double_26_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_26'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_26_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_26_0_bool = False
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_26_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_26_0_bool = True
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_0_bool) + ']')

def qlex_double_27_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_27'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_27_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_27_0_bool = False
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_27_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_27_0_bool = True
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_0_bool) + ']')

def qlex_double_28_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_28'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_28_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_28_0_bool = False
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_28_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_28_0_bool = True
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_0_bool) + ']')

def qlex_double_29_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_29'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_29_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_29_0_bool = False
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_29_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_29_0_bool = True
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_0_bool) + ']')

def qlex_double_30_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_30'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_30_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_30_0_bool = False
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_30_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_30_0_bool = True
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_0_bool) + ']')

def qlex_double_31_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_31'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_31_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_31_0_bool = False
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_31_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_31_0_bool = True
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_0_bool) + ']')

def qlex_double_32_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_32'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_32_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_32_0_bool = False
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_32_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_32_0_bool = True
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_0_bool) + ']')

def qlex_double_33_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_33'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_33_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_33_0_bool = False
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_33_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_33_0_bool = True
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_0_bool) + ']')

def qlex_double_34_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_34'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_34_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_34_0_bool = False
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_34_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_34_0_bool = True
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_0_bool) + ']')

def qlex_double_35_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_35'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_35_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_35_0_bool = False
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_35_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_35_0_bool = True
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_0_bool) + ']')

def qlex_double_36_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_36'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_36_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_36_0_bool = False
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_36_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_36_0_bool = True
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_0_bool) + ']')

def qlex_double_37_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_37'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_37_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_37_0_bool = False
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_37_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_37_0_bool = True
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_0_bool) + ']')

def qlex_double_38_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_38'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_38_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_38_0_bool = False
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_38_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_38_0_bool = True
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_0_bool) + ']')

def qlex_double_39_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_39'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_39_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_39_0_bool = False
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_39_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_39_0_bool = True
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_0_bool) + ']')

def qlex_double_40_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_40'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_40_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_40_0_bool = False
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_40_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_40_0_bool = True
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_0_bool) + ']')

def qlex_double_41_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_41'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_41_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_41_0_bool = False
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_41_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_41_0_bool = True
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_0_bool) + ']')

def qlex_double_42_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_42'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_42_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_42_0_bool = False
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_42_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_42_0_bool = True
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_0_bool) + ']')

def qlex_double_43_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_43'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_43_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_43_0_bool = False
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_43_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_43_0_bool = True
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_0_bool) + ']')

def qlex_double_44_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_44'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_44_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_44_0_bool = False
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_44_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_44_0_bool = True
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_0_bool) + ']')

def qlex_double_45_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_45'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_45_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_45_0_bool = False
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_45_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_45_0_bool = True
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_0_bool) + ']')

def qlex_double_46_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_46'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_46_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_46_0_bool = False
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_46_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_46_0_bool = True
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_0_bool) + ']')

def qlex_double_47_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_47'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_47_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_47_0_bool = False
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_47_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_47_0_bool = True
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_0_bool) + ']')

