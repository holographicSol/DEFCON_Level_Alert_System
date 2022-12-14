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

btnx_double_0_bool = False
btnx_double_1_bool = False
btnx_double_1_0_bool = False
btnx_double_2_bool = False
btnx_double_2_0_bool = False
btnx_double_3_bool = False
btnx_double_3_0_bool = False
btnx_double_4_bool = False
btnx_double_4_0_bool = False
btnx_double_5_bool = False
btnx_double_5_0_bool = False
btnx_double_6_bool = False
btnx_double_6_0_bool = False
btnx_double_7_bool = False
btnx_double_7_0_bool = False
btnx_double_8_bool = False
btnx_double_8_0_bool = False
btnx_double_9_bool = False
btnx_double_9_0_bool = False
btnx_double_10_bool = False
btnx_double_10_0_bool = False
btnx_double_11_bool = False
btnx_double_11_0_bool = False
btnx_double_12_bool = False
btnx_double_12_0_bool = False
btnx_double_13_bool = False
btnx_double_13_0_bool = False
btnx_double_14_bool = False
btnx_double_14_0_bool = False
btnx_double_15_bool = False
btnx_double_15_0_bool = False
btnx_double_16_bool = False
btnx_double_16_0_bool = False
btnx_double_17_bool = False
btnx_double_17_0_bool = False
btnx_double_18_bool = False
btnx_double_18_0_bool = False
btnx_double_19_bool = False
btnx_double_19_0_bool = False
btnx_double_20_bool = False
btnx_double_20_0_bool = False
btnx_double_21_bool = False
btnx_double_21_0_bool = False
btnx_double_22_bool = False
btnx_double_22_0_bool = False
btnx_double_23_bool = False
btnx_double_23_0_bool = False
btnx_double_24_bool = False
btnx_double_24_0_bool = False
btnx_double_25_bool = False
btnx_double_25_0_bool = False
btnx_double_26_bool = False
btnx_double_26_0_bool = False
btnx_double_27_bool = False
btnx_double_27_0_bool = False
btnx_double_28_bool = False
btnx_double_28_0_bool = False
btnx_double_29_bool = False
btnx_double_29_0_bool = False
btnx_double_30_bool = False
btnx_double_30_0_bool = False
btnx_double_31_bool = False
btnx_double_31_0_bool = False
btnx_double_32_bool = False
btnx_double_32_0_bool = False
btnx_double_33_bool = False
btnx_double_33_0_bool = False
btnx_double_34_bool = False
btnx_double_34_0_bool = False
btnx_double_35_bool = False
btnx_double_35_0_bool = False
btnx_double_36_bool = False
btnx_double_36_0_bool = False
btnx_double_37_bool = False
btnx_double_37_0_bool = False
btnx_double_38_bool = False
btnx_double_38_0_bool = False
btnx_double_39_bool = False
btnx_double_39_0_bool = False
btnx_double_40_bool = False
btnx_double_40_0_bool = False
btnx_double_41_bool = False
btnx_double_41_0_bool = False
btnx_double_42_bool = False
btnx_double_42_0_bool = False
btnx_double_43_bool = False
btnx_double_43_0_bool = False
btnx_double_44_bool = False
btnx_double_44_0_bool = False
btnx_double_45_bool = False
btnx_double_45_0_bool = False
btnx_double_46_bool = False
btnx_double_46_0_bool = False
btnx_double_47_bool = False
btnx_double_47_0_bool = False
