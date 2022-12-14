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

def qlex_0_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_0'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_0_0_bool is True:
            auto_gen_qle_bool.qlex_0_0_bool = False
            print('[qlex_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_0_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_0_0_bool is False:
            auto_gen_qle_bool.qlex_0_0_bool = True
            print('[qlex_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_0_0_bool) + ']')

def qlex_1_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_1'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_1_0_bool is True:
            auto_gen_qle_bool.qlex_1_0_bool = False
            print('[qlex_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_1_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_1_0_bool is False:
            auto_gen_qle_bool.qlex_1_0_bool = True
            print('[qlex_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_1_0_bool) + ']')

def qlex_2_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_2'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_2_0_bool is True:
            auto_gen_qle_bool.qlex_2_0_bool = False
            print('[qlex_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_2_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_2_0_bool is False:
            auto_gen_qle_bool.qlex_2_0_bool = True
            print('[qlex_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_2_0_bool) + ']')

def qlex_3_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_3'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_3_0_bool is True:
            auto_gen_qle_bool.qlex_3_0_bool = False
            print('[qlex_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_3_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_3_0_bool is False:
            auto_gen_qle_bool.qlex_3_0_bool = True
            print('[qlex_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_3_0_bool) + ']')

def qlex_4_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_4'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_4_0_bool is True:
            auto_gen_qle_bool.qlex_4_0_bool = False
            print('[qlex_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_4_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_4_0_bool is False:
            auto_gen_qle_bool.qlex_4_0_bool = True
            print('[qlex_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_4_0_bool) + ']')

def qlex_5_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_5'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_5_0_bool is True:
            auto_gen_qle_bool.qlex_5_0_bool = False
            print('[qlex_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_5_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_5_0_bool is False:
            auto_gen_qle_bool.qlex_5_0_bool = True
            print('[qlex_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_5_0_bool) + ']')

def qlex_6_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_6'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_6_0_bool is True:
            auto_gen_qle_bool.qlex_6_0_bool = False
            print('[qlex_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_6_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_6_0_bool is False:
            auto_gen_qle_bool.qlex_6_0_bool = True
            print('[qlex_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_6_0_bool) + ']')

def qlex_7_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_7'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_7_0_bool is True:
            auto_gen_qle_bool.qlex_7_0_bool = False
            print('[qlex_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_7_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_7_0_bool is False:
            auto_gen_qle_bool.qlex_7_0_bool = True
            print('[qlex_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_7_0_bool) + ']')

def qlex_8_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_8'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_8_0_bool is True:
            auto_gen_qle_bool.qlex_8_0_bool = False
            print('[qlex_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_8_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_8_0_bool is False:
            auto_gen_qle_bool.qlex_8_0_bool = True
            print('[qlex_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_8_0_bool) + ']')

def qlex_9_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_9'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_9_0_bool is True:
            auto_gen_qle_bool.qlex_9_0_bool = False
            print('[qlex_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_9_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_9_0_bool is False:
            auto_gen_qle_bool.qlex_9_0_bool = True
            print('[qlex_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_9_0_bool) + ']')

def qlex_10_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_10'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_10_0_bool is True:
            auto_gen_qle_bool.qlex_10_0_bool = False
            print('[qlex_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_10_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_10_0_bool is False:
            auto_gen_qle_bool.qlex_10_0_bool = True
            print('[qlex_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_10_0_bool) + ']')

def qlex_11_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_11'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_11_0_bool is True:
            auto_gen_qle_bool.qlex_11_0_bool = False
            print('[qlex_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_11_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_11_0_bool is False:
            auto_gen_qle_bool.qlex_11_0_bool = True
            print('[qlex_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_11_0_bool) + ']')

def qlex_12_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_12'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_12_0_bool is True:
            auto_gen_qle_bool.qlex_12_0_bool = False
            print('[qlex_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_12_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_12_0_bool is False:
            auto_gen_qle_bool.qlex_12_0_bool = True
            print('[qlex_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_12_0_bool) + ']')

def qlex_13_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_13'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_13_0_bool is True:
            auto_gen_qle_bool.qlex_13_0_bool = False
            print('[qlex_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_13_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_13_0_bool is False:
            auto_gen_qle_bool.qlex_13_0_bool = True
            print('[qlex_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_13_0_bool) + ']')

def qlex_14_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_14'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_14_0_bool is True:
            auto_gen_qle_bool.qlex_14_0_bool = False
            print('[qlex_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_14_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_14_0_bool is False:
            auto_gen_qle_bool.qlex_14_0_bool = True
            print('[qlex_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_14_0_bool) + ']')

def qlex_15_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_15'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_15_0_bool is True:
            auto_gen_qle_bool.qlex_15_0_bool = False
            print('[qlex_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_15_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_15_0_bool is False:
            auto_gen_qle_bool.qlex_15_0_bool = True
            print('[qlex_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_15_0_bool) + ']')

def qlex_16_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_16'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_16_0_bool is True:
            auto_gen_qle_bool.qlex_16_0_bool = False
            print('[qlex_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_16_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_16_0_bool is False:
            auto_gen_qle_bool.qlex_16_0_bool = True
            print('[qlex_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_16_0_bool) + ']')

def qlex_17_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_17'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_17_0_bool is True:
            auto_gen_qle_bool.qlex_17_0_bool = False
            print('[qlex_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_17_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_17_0_bool is False:
            auto_gen_qle_bool.qlex_17_0_bool = True
            print('[qlex_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_17_0_bool) + ']')

def qlex_18_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_18'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_18_0_bool is True:
            auto_gen_qle_bool.qlex_18_0_bool = False
            print('[qlex_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_18_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_18_0_bool is False:
            auto_gen_qle_bool.qlex_18_0_bool = True
            print('[qlex_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_18_0_bool) + ']')

def qlex_19_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_19'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_19_0_bool is True:
            auto_gen_qle_bool.qlex_19_0_bool = False
            print('[qlex_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_19_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_19_0_bool is False:
            auto_gen_qle_bool.qlex_19_0_bool = True
            print('[qlex_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_19_0_bool) + ']')

def qlex_20_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_20'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_20_0_bool is True:
            auto_gen_qle_bool.qlex_20_0_bool = False
            print('[qlex_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_20_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_20_0_bool is False:
            auto_gen_qle_bool.qlex_20_0_bool = True
            print('[qlex_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_20_0_bool) + ']')

def qlex_21_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_21'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_21_0_bool is True:
            auto_gen_qle_bool.qlex_21_0_bool = False
            print('[qlex_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_21_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_21_0_bool is False:
            auto_gen_qle_bool.qlex_21_0_bool = True
            print('[qlex_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_21_0_bool) + ']')

def qlex_22_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_22'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_22_0_bool is True:
            auto_gen_qle_bool.qlex_22_0_bool = False
            print('[qlex_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_22_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_22_0_bool is False:
            auto_gen_qle_bool.qlex_22_0_bool = True
            print('[qlex_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_22_0_bool) + ']')

def qlex_23_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_23'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_23_0_bool is True:
            auto_gen_qle_bool.qlex_23_0_bool = False
            print('[qlex_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_23_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_23_0_bool is False:
            auto_gen_qle_bool.qlex_23_0_bool = True
            print('[qlex_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_23_0_bool) + ']')

def qlex_24_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_24'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_24_0_bool is True:
            auto_gen_qle_bool.qlex_24_0_bool = False
            print('[qlex_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_24_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_24_0_bool is False:
            auto_gen_qle_bool.qlex_24_0_bool = True
            print('[qlex_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_24_0_bool) + ']')

def qlex_25_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_25'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_25_0_bool is True:
            auto_gen_qle_bool.qlex_25_0_bool = False
            print('[qlex_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_25_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_25_0_bool is False:
            auto_gen_qle_bool.qlex_25_0_bool = True
            print('[qlex_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_25_0_bool) + ']')

def qlex_26_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_26'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_26_0_bool is True:
            auto_gen_qle_bool.qlex_26_0_bool = False
            print('[qlex_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_26_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_26_0_bool is False:
            auto_gen_qle_bool.qlex_26_0_bool = True
            print('[qlex_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_26_0_bool) + ']')

def qlex_27_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_27'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_27_0_bool is True:
            auto_gen_qle_bool.qlex_27_0_bool = False
            print('[qlex_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_27_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_27_0_bool is False:
            auto_gen_qle_bool.qlex_27_0_bool = True
            print('[qlex_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_27_0_bool) + ']')

def qlex_28_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_28'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_28_0_bool is True:
            auto_gen_qle_bool.qlex_28_0_bool = False
            print('[qlex_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_28_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_28_0_bool is False:
            auto_gen_qle_bool.qlex_28_0_bool = True
            print('[qlex_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_28_0_bool) + ']')

def qlex_29_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_29'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_29_0_bool is True:
            auto_gen_qle_bool.qlex_29_0_bool = False
            print('[qlex_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_29_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_29_0_bool is False:
            auto_gen_qle_bool.qlex_29_0_bool = True
            print('[qlex_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_29_0_bool) + ']')

def qlex_30_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_30'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_30_0_bool is True:
            auto_gen_qle_bool.qlex_30_0_bool = False
            print('[qlex_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_30_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_30_0_bool is False:
            auto_gen_qle_bool.qlex_30_0_bool = True
            print('[qlex_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_30_0_bool) + ']')

def qlex_31_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_31'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_31_0_bool is True:
            auto_gen_qle_bool.qlex_31_0_bool = False
            print('[qlex_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_31_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_31_0_bool is False:
            auto_gen_qle_bool.qlex_31_0_bool = True
            print('[qlex_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_31_0_bool) + ']')

def qlex_32_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_32'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_32_0_bool is True:
            auto_gen_qle_bool.qlex_32_0_bool = False
            print('[qlex_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_32_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_32_0_bool is False:
            auto_gen_qle_bool.qlex_32_0_bool = True
            print('[qlex_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_32_0_bool) + ']')

def qlex_33_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_33'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_33_0_bool is True:
            auto_gen_qle_bool.qlex_33_0_bool = False
            print('[qlex_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_33_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_33_0_bool is False:
            auto_gen_qle_bool.qlex_33_0_bool = True
            print('[qlex_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_33_0_bool) + ']')

def qlex_34_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_34'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_34_0_bool is True:
            auto_gen_qle_bool.qlex_34_0_bool = False
            print('[qlex_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_34_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_34_0_bool is False:
            auto_gen_qle_bool.qlex_34_0_bool = True
            print('[qlex_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_34_0_bool) + ']')

def qlex_35_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_35'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_35_0_bool is True:
            auto_gen_qle_bool.qlex_35_0_bool = False
            print('[qlex_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_35_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_35_0_bool is False:
            auto_gen_qle_bool.qlex_35_0_bool = True
            print('[qlex_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_35_0_bool) + ']')

def qlex_36_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_36'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_36_0_bool is True:
            auto_gen_qle_bool.qlex_36_0_bool = False
            print('[qlex_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_36_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_36_0_bool is False:
            auto_gen_qle_bool.qlex_36_0_bool = True
            print('[qlex_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_36_0_bool) + ']')

def qlex_37_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_37'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_37_0_bool is True:
            auto_gen_qle_bool.qlex_37_0_bool = False
            print('[qlex_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_37_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_37_0_bool is False:
            auto_gen_qle_bool.qlex_37_0_bool = True
            print('[qlex_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_37_0_bool) + ']')

def qlex_38_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_38'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_38_0_bool is True:
            auto_gen_qle_bool.qlex_38_0_bool = False
            print('[qlex_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_38_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_38_0_bool is False:
            auto_gen_qle_bool.qlex_38_0_bool = True
            print('[qlex_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_38_0_bool) + ']')

def qlex_39_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_39'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_39_0_bool is True:
            auto_gen_qle_bool.qlex_39_0_bool = False
            print('[qlex_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_39_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_39_0_bool is False:
            auto_gen_qle_bool.qlex_39_0_bool = True
            print('[qlex_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_39_0_bool) + ']')

def qlex_40_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_40'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_40_0_bool is True:
            auto_gen_qle_bool.qlex_40_0_bool = False
            print('[qlex_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_40_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_40_0_bool is False:
            auto_gen_qle_bool.qlex_40_0_bool = True
            print('[qlex_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_40_0_bool) + ']')

def qlex_41_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_41'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_41_0_bool is True:
            auto_gen_qle_bool.qlex_41_0_bool = False
            print('[qlex_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_41_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_41_0_bool is False:
            auto_gen_qle_bool.qlex_41_0_bool = True
            print('[qlex_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_41_0_bool) + ']')

def qlex_42_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_42'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_42_0_bool is True:
            auto_gen_qle_bool.qlex_42_0_bool = False
            print('[qlex_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_42_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_42_0_bool is False:
            auto_gen_qle_bool.qlex_42_0_bool = True
            print('[qlex_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_42_0_bool) + ']')

def qlex_43_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_43'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_43_0_bool is True:
            auto_gen_qle_bool.qlex_43_0_bool = False
            print('[qlex_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_43_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_43_0_bool is False:
            auto_gen_qle_bool.qlex_43_0_bool = True
            print('[qlex_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_43_0_bool) + ']')

def qlex_44_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_44'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_44_0_bool is True:
            auto_gen_qle_bool.qlex_44_0_bool = False
            print('[qlex_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_44_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_44_0_bool is False:
            auto_gen_qle_bool.qlex_44_0_bool = True
            print('[qlex_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_44_0_bool) + ']')

def qlex_45_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_45'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_45_0_bool is True:
            auto_gen_qle_bool.qlex_45_0_bool = False
            print('[qlex_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_45_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_45_0_bool is False:
            auto_gen_qle_bool.qlex_45_0_bool = True
            print('[qlex_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_45_0_bool) + ']')

def qlex_46_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_46'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_46_0_bool is True:
            auto_gen_qle_bool.qlex_46_0_bool = False
            print('[qlex_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_46_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_46_0_bool is False:
            auto_gen_qle_bool.qlex_46_0_bool = True
            print('[qlex_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_46_0_bool) + ']')

def qlex_47_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_47'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_47_0_bool is True:
            auto_gen_qle_bool.qlex_47_0_bool = False
            print('[qlex_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_47_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_47_0_bool is False:
            auto_gen_qle_bool.qlex_47_0_bool = True
            print('[qlex_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_47_0_bool) + ']')

