# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)
import resources_rc

class Ui_ToolPanel(object):
    def setupUi(self, ToolPanel):
        if not ToolPanel.objectName():
            ToolPanel.setObjectName(u"ToolPanel")
        ToolPanel.setEnabled(True)
        ToolPanel.resize(200, 350)
        ToolPanel.setMinimumSize(QSize(200, 350))
        ToolPanel.setMaximumSize(QSize(200, 350))
        palette = QPalette()
        brush = QBrush(QColor(235, 235, 235, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        ToolPanel.setPalette(palette)
        ToolPanel.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/assets/empty.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ToolPanel.setWindowIcon(icon)
        ToolPanel.setAutoFillBackground(False)
        ToolPanel.setStyleSheet(u"QWidget#ToolPanel{\n"
"	background-color: #ebebeb\n"
"}\n"
"\n"
"QFrame#frm_top{\n"
"	background-color: transparent\n"
"}\n"
"\n"
"QFrame#frm_buttons{\n"
"	background-color: transparent\n"
"}\n"
"\n"
"QFrame#frm_palette QPushButton{\n"
"	margin: 0px;\n"
"	border: 2px solid transparent;\n"
"	border-radius: 0px\n"
"}\n"
"\n"
"QFrame#frm_buttons QPushButton{\n"
"	background-color: #dbdbdb;\n"
"	border: 2px solid transparent;\n"
"	border-radius: 5px;\n"
"	padding: 3px\n"
"\n"
"}\n"
"\n"
"QFrame#frm_buttons QPushButton:hover{\n"
"	background-color: #808080;\n"
"}\n"
"\n"
"QFrame#frm_buttons QPushButton:pressed{\n"
"	background-color: #dbdbdb;\n"
"}\n"
"\n"
"QFrame#frm_buttons QPushButton:checked{\n"
"	background-color: #808080;\n"
"}\n"
"\n"
"QFrame#frm_rgb_sliders,\n"
"QFrame#frm_brush_size{\n"
"	background-color: #dbdbdb;\n"
"	border-radius: 8px\n"
"}\n"
"\n"
"QSlider{\n"
"	background-color: transparent\n"
"}\n"
"\n"
"QSlider#slider_brush_size {\n"
"	padding: 0\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(ToolPanel)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.frm_top = QFrame(ToolPanel)
        self.frm_top.setObjectName(u"frm_top")
        self.frm_top.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_top.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_top)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frm_rgb_sliders = QFrame(self.frm_top)
        self.frm_rgb_sliders.setObjectName(u"frm_rgb_sliders")
        self.frm_rgb_sliders.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_rgb_sliders.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frm_rgb_sliders)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 0, 4, 0)
        self.slider_red = QSlider(self.frm_rgb_sliders)
        self.slider_red.setObjectName(u"slider_red")
        palette1 = QPalette()
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush2)
        self.slider_red.setPalette(palette1)
        self.slider_red.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slider_red.setAutoFillBackground(False)
        self.slider_red.setMaximum(15)
        self.slider_red.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_red)

        self.slider_green = QSlider(self.frm_rgb_sliders)
        self.slider_green.setObjectName(u"slider_green")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(0, 255, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush3)
        self.slider_green.setPalette(palette2)
        self.slider_green.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slider_green.setAutoFillBackground(False)
        self.slider_green.setMaximum(15)
        self.slider_green.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_green)

        self.slider_blue = QSlider(self.frm_rgb_sliders)
        self.slider_blue.setObjectName(u"slider_blue")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 0, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Accent, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Accent, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Accent, brush4)
        self.slider_blue.setPalette(palette3)
        self.slider_blue.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slider_blue.setAutoFillBackground(False)
        self.slider_blue.setMaximum(15)
        self.slider_blue.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_blue)


        self.horizontalLayout_2.addWidget(self.frm_rgb_sliders)

        self.brush_preview = QWidget(self.frm_top)
        self.brush_preview.setObjectName(u"brush_preview")
        self.verticalLayout_3 = QVBoxLayout(self.brush_preview)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_preview = QLabel(self.brush_preview)
        self.lbl_preview.setObjectName(u"lbl_preview")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_preview.sizePolicy().hasHeightForWidth())
        self.lbl_preview.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.lbl_preview)


        self.horizontalLayout_2.addWidget(self.brush_preview)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 6)

        self.verticalLayout.addWidget(self.frm_top)

        self.frm_palette = QFrame(ToolPanel)
        self.frm_palette.setObjectName(u"frm_palette")
        self.frm_palette.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_palette.setFrameShadow(QFrame.Shadow.Plain)
        self.frm_palette.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frm_palette)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frm_palette)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_9, 1, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.frm_palette)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_8, 1, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frm_palette)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_7, 0, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.frm_palette)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.frm_palette)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_14, 2, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.frm_palette)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.frm_palette)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_12, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.frm_palette)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_10, 1, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.frm_palette)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_11, 1, 3, 1, 1)

        self.pushButton_15 = QPushButton(self.frm_palette)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_15, 2, 3, 1, 1)

        self.pushButton_17 = QPushButton(self.frm_palette)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_17, 4, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.frm_palette)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_13, 2, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.frm_palette)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_16, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.frm_palette)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.frm_palette)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_18, 5, 0, 1, 1)

        self.pushButton_19 = QPushButton(self.frm_palette)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_19, 3, 1, 1, 1)

        self.pushButton_20 = QPushButton(self.frm_palette)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_20, 4, 1, 1, 1)

        self.pushButton_21 = QPushButton(self.frm_palette)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_21, 5, 1, 1, 1)

        self.pushButton_22 = QPushButton(self.frm_palette)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_22, 3, 2, 1, 1)

        self.pushButton_23 = QPushButton(self.frm_palette)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_23, 4, 2, 1, 1)

        self.pushButton_24 = QPushButton(self.frm_palette)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_24, 5, 2, 1, 1)

        self.pushButton_25 = QPushButton(self.frm_palette)
        self.pushButton_25.setObjectName(u"pushButton_25")
        sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        self.pushButton_25.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_25, 3, 3, 1, 1)

        self.pushButton_26 = QPushButton(self.frm_palette)
        self.pushButton_26.setObjectName(u"pushButton_26")
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        self.pushButton_26.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_26, 4, 3, 1, 1)

        self.pushButton_27 = QPushButton(self.frm_palette)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy)
        self.pushButton_27.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_27, 5, 3, 1, 1)


        self.verticalLayout.addWidget(self.frm_palette)

        self.frm_brush_size = QFrame(ToolPanel)
        self.frm_brush_size.setObjectName(u"frm_brush_size")
        self.frm_brush_size.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_brush_size.setFrameShadow(QFrame.Shadow.Plain)
        self.frm_brush_size.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_brush_size)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 5, -1, 5)
        self.slider_brush_size = QSlider(self.frm_brush_size)
        self.slider_brush_size.setObjectName(u"slider_brush_size")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Accent, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Accent, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Accent, brush5)
        self.slider_brush_size.setPalette(palette4)
        self.slider_brush_size.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.slider_brush_size.setAutoFillBackground(True)
        self.slider_brush_size.setMinimum(20)
        self.slider_brush_size.setMaximum(100)
        self.slider_brush_size.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.slider_brush_size)


        self.verticalLayout.addWidget(self.frm_brush_size)

        self.frm_buttons = QFrame(ToolPanel)
        self.frm_buttons.setObjectName(u"frm_buttons")
        self.frm_buttons.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_buttons.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.frm_buttons)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_brush = QPushButton(self.frm_buttons)
        self.btn_brush.setObjectName(u"btn_brush")
        self.btn_brush.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/assets/brush.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_brush.setIcon(icon1)
        self.btn_brush.setIconSize(QSize(20, 20))
        self.btn_brush.setCheckable(True)
        self.btn_brush.setChecked(True)
        self.btn_brush.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_brush)

        self.btn_eraser = QPushButton(self.frm_buttons)
        self.btn_eraser.setObjectName(u"btn_eraser")
        self.btn_eraser.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/assets/eraser.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_eraser.setIcon(icon2)
        self.btn_eraser.setIconSize(QSize(20, 20))
        self.btn_eraser.setCheckable(True)
        self.btn_eraser.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_eraser)

        self.btn_clear = QPushButton(self.frm_buttons)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/assets/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clear.setIcon(icon3)
        self.btn_clear.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_clear)


        self.verticalLayout.addWidget(self.frm_buttons)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(ToolPanel)

        QMetaObject.connectSlotsByName(ToolPanel)
    # setupUi

    def retranslateUi(self, ToolPanel):
        ToolPanel.setWindowTitle(QCoreApplication.translate("ToolPanel", u"Tool Panel", None))
        self.lbl_preview.setText("")
        self.pushButton_9.setText("")
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.pushButton_5.setText("")
        self.pushButton_14.setText("")
        self.pushButton_6.setText("")
        self.pushButton_12.setText("")
        self.pushButton_10.setText("")
        self.pushButton_11.setText("")
        self.pushButton_15.setText("")
        self.pushButton_17.setText("")
        self.pushButton_13.setText("")
        self.pushButton_16.setText("")
        self.pushButton_4.setText("")
        self.pushButton_18.setText("")
        self.pushButton_19.setText("")
        self.pushButton_20.setText("")
        self.pushButton_21.setText("")
        self.pushButton_22.setText("")
        self.pushButton_23.setText("")
        self.pushButton_24.setText("")
        self.pushButton_25.setText("")
        self.pushButton_26.setText("")
        self.pushButton_27.setText("")
        self.btn_brush.setText("")
        self.btn_eraser.setText("")
        self.btn_clear.setText("")
    # retranslateUi

