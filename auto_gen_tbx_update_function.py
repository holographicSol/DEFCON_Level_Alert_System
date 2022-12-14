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
def tbx_0_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[0].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_0_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[0].stop()

message_0 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_0_timer_append_function():
    global message_0
    global var_tbx
    if message_0:
        var_tbx[0].append(message_0[0])
        message_0.remove(message_0[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_1_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[1].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_1_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[1].stop()

message_1 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_1_timer_append_function():
    global message_1
    global var_tbx
    if message_1:
        var_tbx[1].append(message_1[0])
        message_1.remove(message_1[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_2_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[2].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_2_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[2].stop()

message_2 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_2_timer_append_function():
    global message_2
    global var_tbx
    if message_2:
        var_tbx[2].append(message_2[0])
        message_2.remove(message_2[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_3_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[3].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_3_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[3].stop()

message_3 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_3_timer_append_function():
    global message_3
    global var_tbx
    if message_3:
        var_tbx[3].append(message_3[0])
        message_3.remove(message_3[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_4_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[4].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_4_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[4].stop()

message_4 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_4_timer_append_function():
    global message_4
    global var_tbx
    if message_4:
        var_tbx[4].append(message_4[0])
        message_4.remove(message_4[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_5_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[5].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_5_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[5].stop()

message_5 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_5_timer_append_function():
    global message_5
    global var_tbx
    if message_5:
        var_tbx[5].append(message_5[0])
        message_5.remove(message_5[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_6_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[6].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_6_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[6].stop()

message_6 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_6_timer_append_function():
    global message_6
    global var_tbx
    if message_6:
        var_tbx[6].append(message_6[0])
        message_6.remove(message_6[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_7_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[7].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_7_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[7].stop()

message_7 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_7_timer_append_function():
    global message_7
    global var_tbx
    if message_7:
        var_tbx[7].append(message_7[0])
        message_7.remove(message_7[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_8_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[8].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_8_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[8].stop()

message_8 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_8_timer_append_function():
    global message_8
    global var_tbx
    if message_8:
        var_tbx[8].append(message_8[0])
        message_8.remove(message_8[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_9_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[9].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_9_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[9].stop()

message_9 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_9_timer_append_function():
    global message_9
    global var_tbx
    if message_9:
        var_tbx[9].append(message_9[0])
        message_9.remove(message_9[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_10_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[10].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_10_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[10].stop()

message_10 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_10_timer_append_function():
    global message_10
    global var_tbx
    if message_10:
        var_tbx[10].append(message_10[0])
        message_10.remove(message_10[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_11_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[11].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_11_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[11].stop()

message_11 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_11_timer_append_function():
    global message_11
    global var_tbx
    if message_11:
        var_tbx[11].append(message_11[0])
        message_11.remove(message_11[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_12_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[12].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_12_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[12].stop()

message_12 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_12_timer_append_function():
    global message_12
    global var_tbx
    if message_12:
        var_tbx[12].append(message_12[0])
        message_12.remove(message_12[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_13_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[13].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_13_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[13].stop()

message_13 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_13_timer_append_function():
    global message_13
    global var_tbx
    if message_13:
        var_tbx[13].append(message_13[0])
        message_13.remove(message_13[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_14_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[14].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_14_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[14].stop()

message_14 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_14_timer_append_function():
    global message_14
    global var_tbx
    if message_14:
        var_tbx[14].append(message_14[0])
        message_14.remove(message_14[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_15_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[15].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_15_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[15].stop()

message_15 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_15_timer_append_function():
    global message_15
    global var_tbx
    if message_15:
        var_tbx[15].append(message_15[0])
        message_15.remove(message_15[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_16_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[16].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_16_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[16].stop()

message_16 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_16_timer_append_function():
    global message_16
    global var_tbx
    if message_16:
        var_tbx[16].append(message_16[0])
        message_16.remove(message_16[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_17_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[17].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_17_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[17].stop()

message_17 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_17_timer_append_function():
    global message_17
    global var_tbx
    if message_17:
        var_tbx[17].append(message_17[0])
        message_17.remove(message_17[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_18_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[18].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_18_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[18].stop()

message_18 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_18_timer_append_function():
    global message_18
    global var_tbx
    if message_18:
        var_tbx[18].append(message_18[0])
        message_18.remove(message_18[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_19_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[19].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_19_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[19].stop()

message_19 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_19_timer_append_function():
    global message_19
    global var_tbx
    if message_19:
        var_tbx[19].append(message_19[0])
        message_19.remove(message_19[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_20_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[20].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_20_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[20].stop()

message_20 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_20_timer_append_function():
    global message_20
    global var_tbx
    if message_20:
        var_tbx[20].append(message_20[0])
        message_20.remove(message_20[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_21_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[21].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_21_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[21].stop()

message_21 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_21_timer_append_function():
    global message_21
    global var_tbx
    if message_21:
        var_tbx[21].append(message_21[0])
        message_21.remove(message_21[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_22_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[22].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_22_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[22].stop()

message_22 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_22_timer_append_function():
    global message_22
    global var_tbx
    if message_22:
        var_tbx[22].append(message_22[0])
        message_22.remove(message_22[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_23_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[23].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_23_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[23].stop()

message_23 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_23_timer_append_function():
    global message_23
    global var_tbx
    if message_23:
        var_tbx[23].append(message_23[0])
        message_23.remove(message_23[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_24_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[24].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_24_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[24].stop()

message_24 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_24_timer_append_function():
    global message_24
    global var_tbx
    if message_24:
        var_tbx[24].append(message_24[0])
        message_24.remove(message_24[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_25_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[25].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_25_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[25].stop()

message_25 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_25_timer_append_function():
    global message_25
    global var_tbx
    if message_25:
        var_tbx[25].append(message_25[0])
        message_25.remove(message_25[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_26_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[26].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_26_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[26].stop()

message_26 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_26_timer_append_function():
    global message_26
    global var_tbx
    if message_26:
        var_tbx[26].append(message_26[0])
        message_26.remove(message_26[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_27_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[27].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_27_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[27].stop()

message_27 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_27_timer_append_function():
    global message_27
    global var_tbx
    if message_27:
        var_tbx[27].append(message_27[0])
        message_27.remove(message_27[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_28_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[28].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_28_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[28].stop()

message_28 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_28_timer_append_function():
    global message_28
    global var_tbx
    if message_28:
        var_tbx[28].append(message_28[0])
        message_28.remove(message_28[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_29_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[29].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_29_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[29].stop()

message_29 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_29_timer_append_function():
    global message_29
    global var_tbx
    if message_29:
        var_tbx[29].append(message_29[0])
        message_29.remove(message_29[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_30_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[30].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_30_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[30].stop()

message_30 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_30_timer_append_function():
    global message_30
    global var_tbx
    if message_30:
        var_tbx[30].append(message_30[0])
        message_30.remove(message_30[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_31_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[31].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_31_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[31].stop()

message_31 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_31_timer_append_function():
    global message_31
    global var_tbx
    if message_31:
        var_tbx[31].append(message_31[0])
        message_31.remove(message_31[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_32_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[32].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_32_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[32].stop()

message_32 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_32_timer_append_function():
    global message_32
    global var_tbx
    if message_32:
        var_tbx[32].append(message_32[0])
        message_32.remove(message_32[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_33_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[33].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_33_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[33].stop()

message_33 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_33_timer_append_function():
    global message_33
    global var_tbx
    if message_33:
        var_tbx[33].append(message_33[0])
        message_33.remove(message_33[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_34_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[34].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_34_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[34].stop()

message_34 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_34_timer_append_function():
    global message_34
    global var_tbx
    if message_34:
        var_tbx[34].append(message_34[0])
        message_34.remove(message_34[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_35_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[35].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_35_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[35].stop()

message_35 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_35_timer_append_function():
    global message_35
    global var_tbx
    if message_35:
        var_tbx[35].append(message_35[0])
        message_35.remove(message_35[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_36_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[36].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_36_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[36].stop()

message_36 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_36_timer_append_function():
    global message_36
    global var_tbx
    if message_36:
        var_tbx[36].append(message_36[0])
        message_36.remove(message_36[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_37_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[37].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_37_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[37].stop()

message_37 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_37_timer_append_function():
    global message_37
    global var_tbx
    if message_37:
        var_tbx[37].append(message_37[0])
        message_37.remove(message_37[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_38_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[38].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_38_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[38].stop()

message_38 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_38_timer_append_function():
    global message_38
    global var_tbx
    if message_38:
        var_tbx[38].append(message_38[0])
        message_38.remove(message_38[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_39_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[39].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_39_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[39].stop()

message_39 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_39_timer_append_function():
    global message_39
    global var_tbx
    if message_39:
        var_tbx[39].append(message_39[0])
        message_39.remove(message_39[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_40_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[40].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_40_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[40].stop()

message_40 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_40_timer_append_function():
    global message_40
    global var_tbx
    if message_40:
        var_tbx[40].append(message_40[0])
        message_40.remove(message_40[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_41_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[41].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_41_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[41].stop()

message_41 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_41_timer_append_function():
    global message_41
    global var_tbx
    if message_41:
        var_tbx[41].append(message_41[0])
        message_41.remove(message_41[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_42_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[42].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_42_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[42].stop()

message_42 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_42_timer_append_function():
    global message_42
    global var_tbx
    if message_42:
        var_tbx[42].append(message_42[0])
        message_42.remove(message_42[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_43_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[43].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_43_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[43].stop()

message_43 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_43_timer_append_function():
    global message_43
    global var_tbx
    if message_43:
        var_tbx[43].append(message_43[0])
        message_43.remove(message_43[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_44_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[44].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_44_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[44].stop()

message_44 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_44_timer_append_function():
    global message_44
    global var_tbx
    if message_44:
        var_tbx[44].append(message_44[0])
        message_44.remove(message_44[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_45_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[45].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_45_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[45].stop()

message_45 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_45_timer_append_function():
    global message_45
    global var_tbx
    if message_45:
        var_tbx[45].append(message_45[0])
        message_45.remove(message_45[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_46_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[46].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_46_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[46].stop()

message_46 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_46_timer_append_function():
    global message_46
    global var_tbx
    if message_46:
        var_tbx[46].append(message_46[0])
        message_46.remove(message_46[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_47_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[47].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_47_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[47].stop()

message_47 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_47_timer_append_function():
    global message_47
    global var_tbx
    if message_47:
        var_tbx[47].append(message_47[0])
        message_47.remove(message_47[0])

