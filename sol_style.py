"""
Written by Benjamin Jack Cullen aka Holographic_Sol
"""

btn_title_bar_style = """QPushButton{background-color: rgb(0, 0, 0);
border:0px solid rgb(0, 0, 0);
outline: 0;}"""

main_border_height = 2
self_style = """

QMainWindow {background-color: rgb(0, 0, 0);
color: rgb(200, 200, 200);
border-top:"""+str(main_border_height)+"""px solid rgb(20, 20, 50);
border-bottom:"""+str(main_border_height)+"""px solid rgb(20, 20, 50);
border-right:"""+str(main_border_height)+"""px solid rgb(20, 20, 50);
border-left:"""+str(main_border_height)+"""px solid rgb(20, 20, 50);
}

QToolTip {background-color: rgb(35, 35, 35);
color: rgb(200, 200, 200);
border-top:0px solid rgb(35, 35, 35);
border-bottom:0px solid rgb(35, 35, 35);
border-right:0px solid rgb(0, 0, 0);
border-left:0px solid rgb(0, 0, 0);
}

QScrollBar:vertical {
width: 20px;
margin: 20px 0px 20px 0px;
background-color: rgb(18, 18, 18);
}
QScrollBar:horizontal {
height: 20px;
margin: 0px 20px 0px 20px;
background-color: rgb(18, 18, 18);
}

QScrollBar::handle:vertical {
background-color: rgb(18, 18, 18);
border-bottom:4px solid rgb(0, 0, 0);
border-top:4px solid rgb(0, 0, 0);
min-height: 10px;
}
QScrollBar::handle:horizontal {
background-color: rgb(18, 18, 18);
border-left:4px solid rgb(0, 0, 0);
border-right:4px solid rgb(0, 0, 0);
min-width: 2px;
}

QScrollBar::add-line:vertical {
background-color: rgb(18, 18, 18);
height: 20px;
width: 20px;
subcontrol-position: bottom;
subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
background-color: rgb(18, 18, 18);
height: 20px;
width: 20px;
subcontrol-position: top;
subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal {
background-color: rgb(18, 18, 18);
height: 20px;
width: 20px;
subcontrol-position: right;
subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
background-color: rgb(20, 20, 20);
height: 20px;
width: 20px;
subcontrol-position: top left;
subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical {
image:url('./resources/image/scroll_white.png');
height: 20px;
width: 20px;
}
QScrollBar::down-arrow:vertical {
image:url('./resources/image/scroll_white.png');
height: 20px;
width: 20px;
}

QScrollBar::left-arrow:horizontal {
image:url('./resources/image/scroll_white.png');
height: 20px;
width: 20px;
}
QScrollBar::right-arrow:horizontal {
image:url('./resources/image/scroll_white.png');
height: 20px;
width: 20px;
}

QScrollBar::add-page:vertical {
background-color: rgb(0, 0, 0);
width: 20px;
height: 20px;
}
QScrollBar::sub-page:vertical {
background-color: rgb(8, 8, 8);
width: 20px;
height: 20px;
}

QScrollBar::add-page:horizontal {
background-color: rgb(8, 8, 8);
width: 20px;
height: 20px;
}
QScrollBar::sub-page:horizontal {
background-color: rgb(8, 8, 8);
width: 20px;
height: 20px;
}

QMenuBar {
    background-color: rgb(0,0,0);
    color: rgb(255,255,255);
}

QMenuBar::item {
    background-color: rgb(0,0,0);
    color: rgb(255,255,255);
}

QMenuBar::item::selected {
    background-color: rgb(0,0,155);
}

QMenu {
    background-color: rgb(16,16,16);
    color: rgb(255,255,255);
}

QMenu::item::selected {
    background-color: rgb(0,0,155);
}

QPushButton{background-color: rgb(0, 0, 0);
color: rgb(255, 255, 255);
border-top:20px solid rgb(0, 0, 0);
border-bottom:0px solid rgb(0, 0, 0);
border-right:0px solid rgb(0, 0, 0);
border-left:0px solid rgb(0, 0, 0);
outline: 0;}

QPushButton::hover {
    background-color : rgb(0,0,155);
}

QPushButton::pressed {
    color : rgb(255, 255, 255);
    background-color : rgb(26,26,26);
    border-top:28px solid rgb(14, 14, 14);
    border-bottom:8px solid rgb(14, 14, 14);
    border-right:8px solid rgb(14, 14, 14);
    border-left:8px solid rgb(14, 14, 14);}
}

QLabel{background-color: rgb(0, 0, 0);
color: rgb(255, 255, 255);
border-top:4px solid rgb(0, 0, 0);
border-bottom:4px solid rgb(0, 0, 0);
border-right:4px solid rgb(0, 0, 0);
border-left:4px solid rgb(0, 0, 0);}

QLineEdit{background-color: rgb(16, 16, 16);
color: rgb(255, 255, 255);
border-top:4px solid rgb(14, 14, 14);
border-bottom:4px solid rgb(14, 14, 14);
border-right:4px solid rgb(14, 14, 14);
border-left:4px solid rgb(14, 14, 14);}

QTextBrowser {background-color: rgb(0, 0, 0);
selection-color: black;
selection-background-color: rgb(0, 180, 0);
color: rgb(255, 255, 255);
border-bottom:0px solid rgb(5, 5, 5);
border-right:0px solid rgb(5, 5, 5);
border-top:0px solid rgb(5, 5, 5);
border-left:0px solid rgb(5, 5, 5);}

QComboBox {background-color: rgb(0, 0, 0);
selection-color: black;
selection-background-color: rgb(255, 0, 0);
color: rgb(0, 255, 0);
border-bottom:0px solid rgb(5, 5, 5);
border-right:0px solid rgb(5, 5, 5);
border-top:0px solid rgb(5, 5, 5);
border-left:0px solid rgb(5, 5, 5);}

"""
