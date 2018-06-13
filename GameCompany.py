
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import SetComboBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 321, 221))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.SearchLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.SearchLayout.setContentsMargins(0, 0, 0, 0)
        self.SearchLayout.setObjectName("SearchLayout")

        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_2.setObjectName("groupBox_2")



        self.comboBox_Area = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_Area.setGeometry(QtCore.QRect(80, 60, 231, 21))
        self.comboBox_Area.setObjectName("comboBox_Area")

        self.comboBox_Area.addItem("선택", 1)
        self.comboBox_Area.addItem("전체", 0)
        self.comboBox_Area.addItem("고양시", 41280)
        self.comboBox_Area.addItem("과천시", 41290)
        self.comboBox_Area.addItem("광명시", 41210)
        self.comboBox_Area.addItem("광주시", 41610)
        self.comboBox_Area.addItem("구리시", 41310)
        self.comboBox_Area.addItem("군포시", 41410)
        self.comboBox_Area.addItem("김포시", 41570)
        self.comboBox_Area.addItem("남양주시", 41360)
        self.comboBox_Area.addItem("부천시", 41190)
        self.comboBox_Area.addItem("성남시", 41130)
        self.comboBox_Area.addItem("수원시", 41110)
        self.comboBox_Area.addItem("시흥시", 41390)
        self.comboBox_Area.addItem("안산시", 41270)
        self.comboBox_Area.addItem("안성시", 41550)
        self.comboBox_Area.addItem("안양시", 41170)
        self.comboBox_Area.addItem("양주시", 41630)
        self.comboBox_Area.addItem("양평군", 41830)
        self.comboBox_Area.addItem("오산시", 41370)
        self.comboBox_Area.addItem("용인시", 41460)
        self.comboBox_Area.addItem("의왕시", 41430)
        self.comboBox_Area.addItem("의정부시", 41150)
        self.comboBox_Area.addItem("이천시", 41500)
        self.comboBox_Area.addItem("파주시", 41480)
        self.comboBox_Area.addItem("평택시", 41220)
        self.comboBox_Area.addItem("포천시", 41650)
        self.comboBox_Area.addItem("하남시", 41450)
        self.comboBox_Area.addItem("화성시", 41590)








        self.label_Area = QtWidgets.QLabel(self.groupBox_2)
        self.label_Area.setGeometry(QtCore.QRect(20, 60, 50, 21))
        self.label_Area.setObjectName("label_Area")





        self.labelName1 = QtWidgets.QLabel(self.groupBox_2)
        self.labelName1.setGeometry(QtCore.QRect(20, 140, 50, 21))
        self.labelName1.setObjectName("labelName")

        self.comboBox_Company = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_Company.setGeometry(QtCore.QRect(80, 140, 231, 21))
        self.comboBox_Company.setObjectName("comboBox_Company")

        def on_comboBox_currentIndexChanged_Company():
            sigunCode = self.comboBox_Area.currentData()

            self.comboBox_Company.clear()
            self.comboBox_Company.addItem("선택", 0)
            SetComboBox.CompanySettingFunc(sigunCode,  self.comboBox_Company)

        self.comboBox_Area.currentIndexChanged.connect(on_comboBox_currentIndexChanged_Company)

        self.SearchLayout.addWidget(self.groupBox_2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 240, 780, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 778, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")





        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 760, 250))
        self.groupBox.setObjectName("groupBox")

        self.labelName = QtWidgets.QLabel(self.groupBox)
        self.labelName.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.labelName.setObjectName("labelName")

        self.labelProduct = QtWidgets.QLabel(self.groupBox)
        self.labelProduct.setGeometry(QtCore.QRect(10, 60, 100, 20))
        self.labelProduct.setObjectName("labelProduct")

        self.labelDate = QtWidgets.QLabel(self.groupBox)
        self.labelDate.setGeometry(QtCore.QRect(10, 100, 100, 20))
        self.labelDate.setObjectName("labelDate")

        self.labelStatus = QtWidgets.QLabel(self.groupBox)
        self.labelStatus.setGeometry(QtCore.QRect(10, 140, 100, 20))
        self.labelStatus.setObjectName("labelStatus")


        self.labelZipcode = QtWidgets.QLabel(self.groupBox)
        self.labelZipcode.setGeometry(QtCore.QRect(10, 180, 100, 20))
        self.labelZipcode.setObjectName("labelZipcode")

        self.labelAddress = QtWidgets.QLabel(self.groupBox)
        self.labelAddress.setGeometry(QtCore.QRect(10, 220, 100, 20))
        self.labelAddress.setObjectName("labelAddress")

    ####################

        self.lineEditName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditName.setGeometry(QtCore.QRect(100, 20, 621, 20))
        self.lineEditName.setObjectName("lineEditName")

        self.lineEditProduct = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditProduct.setGeometry(QtCore.QRect(100, 60, 621, 20))
        self.lineEditProduct.setObjectName("lineEditProduct")

        self.lineEditDate = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditDate.setGeometry(QtCore.QRect(100, 100, 621, 20))
        self.lineEditDate.setObjectName("lineEditDate")

        self.lineEditStatus = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditStatus.setGeometry(QtCore.QRect(100, 140, 621, 20))
        self.lineEditStatus.setObjectName("lineEditStatus")

        self.lineEditZipcode = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditZipcode.setGeometry(QtCore.QRect(100, 180, 621, 20))
        self.lineEditZipcode.setObjectName("lineEditZipcode")

        self.lineEditAddress = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditAddress.setGeometry(QtCore.QRect(100, 220, 621, 20))
        self.lineEditAddress.setObjectName("lineEditAddress")



        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.MapView = QtWidgets.QLabel(self.centralwidget)
        self.MapView.setGeometry(QtCore.QRect(350, 10, 471, 221))
        self.MapView.setObjectName("MapView")

        def showInformation():
            sigunCode = self.comboBox_Area.currentData()
            company = self.comboBox_Company.currentData()
            self.lineEditAddress.clear()
            self.lineEditZipcode.clear()
            self.lineEditStatus.clear()
            self.lineEditProduct.clear()
            self.lineEditDate.clear()
            self.lineEditName.clear()

            self.MapView.clear()
            if company != 0 and company != None:
                SetComboBox.InformationSettingFunc(sigunCode, company, self.lineEditZipcode, self.lineEditAddress,  self.lineEditStatus,  self.lineEditProduct, self.lineEditDate,self.lineEditName , self.MapView)
        self.comboBox_Company.currentIndexChanged.connect(showInformation)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "경기도 내 게임회사 찾기 프로그램"))
        self.groupBox_2.setTitle(_translate("MainWindow", "검색"))

        self.label_Area.setText(_translate("MainWindow", "시군명"))



        self.labelName1.setText(_translate("MainWindow", "회사명"))

        self.groupBox.setTitle(_translate("MainWindow", "상세 정보"))
        self.labelProduct.setText(_translate("MainWindow", "취급품목"))
        self.labelName.setText(_translate("MainWindow", "회사이름"))
        self.labelDate.setText(_translate("MainWindow", "설립일자"))

        self.labelZipcode.setText(_translate("MainWindow", "우편번호"))
        self.labelStatus.setText(_translate("MainWindow", "영업 상태"))
        self.labelAddress.setText(_translate("MainWindow", "    주소"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

