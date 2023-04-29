from PyQt5 import QtWidgets
import random

class ShoolTimeTableUI:
    def style(self):
        self.style_box = '''
            background:#fff;
            border:1px solid #000;
        '''
        self.style_Labelday = '''
            background:#fff;
            text-align:center;
            border:0px solid #000;
        '''
        self.style_firstrowLabel = '''
            background:#fff;
            font-weight:bold;
            border:1px solid #000;
            text-align:center;
        '''
        self.style_firstcolLabel = '''
            font-weight:bold;
            border:0px solid #000;
            text-align:center;
        '''
        self.initstyle_Labels = '''
            background:#fff;
            border:0px solid #000;
            text-align:center;
        '''
        self.showupstyle_Labels = '''
            background:#fff;
            border:1px solid #000;
            text-align:center;
        '''

    def __init__(self, window: QtWidgets.QMainWindow):
        self.style()

        self.retbtn = QtWidgets.QPushButton(window)
        self.retbtn.setText('返回首頁')
        self.retbtn.move(10,10) 

        self.label = QtWidgets.QLabel(window)
        self.label.setText('我的課表')
        self.label.move(50, 70)
        
        self.Combobox = QtWidgets.QComboBox(window)   # 下拉選單
        self.Combobox.setGeometry(700,60,70,30)
        
        x = 50
        y = 120
        w = 150
        h = 70
        self.pick_background_color = ['#ffb366', '#ffff66', '#8cff66', '#d9ff66', '#66ffff', '#668cff', '#66d9ff']

        self.vboxs = {}
        self.v_layouts = {}
        self.Labels = {}
        self.firstrowLabels = {}

        first_row_table = {'0,0':'Mon.', '0,1':'Tue.', '0,2':'Wed.', '0,3':'Thu.', '0,4':'Fri.'}
        for i in range(1, 10): #first col
            label_name ='-1,'+str(i)
            self.firstrowLabels[label_name] = QtWidgets.QLabel(window)
            self.firstrowLabels[label_name].setStyleSheet(self.style_firstcolLabel)
            self.firstrowLabels[label_name].setText(str(i))
            self.firstrowLabels[label_name].setGeometry(25, y+ i*h, 25, h) # 
        for j in range(5): #first row
            label_name ='0,'+str(j)
            self.firstrowLabels[label_name] = QtWidgets.QLabel(window)
            self.firstrowLabels[label_name].setStyleSheet(self.style_firstrowLabel)
            self.firstrowLabels[label_name].setText(first_row_table[label_name])
            self.firstrowLabels[label_name].setGeometry(x + j*w, y, w, h)
        for i in range(1, 10):
            for j in range(1, 6):
                label_name = str(i)+','+str(j)
                self.vboxs[label_name] = QtWidgets.QWidget(window)
                self.vboxs[label_name].setGeometry(x + (j-1)*w, y + i*h, w, h)
                self.vboxs[label_name].setStyleSheet(self.style_box)

                self.v_layouts[label_name] = QtWidgets.QVBoxLayout(self.vboxs[label_name])

                self.Labels[label_name] = QtWidgets.QLabel(window)
                self.Labels[label_name].setWordWrap(True)
                self.Labels[label_name].setStyleSheet(self.initstyle_Labels)
                self.v_layouts[label_name].addWidget(self.Labels[label_name])

    def initailize(self, members, iniMemberScedual):
        self.Combobox.addItems(members)
        random.shuffle(self.pick_background_color)
        for i, classes in enumerate(iniMemberScedual):
            for classTime in classes[1]:
                self.Labels[classTime[len(classTime)::-1]].setText(classes[0]) #reverse
                self.Labels[classTime[len(classTime)::-1]].setStyleSheet(self.showupstyle_Labels+'background:'+self.pick_background_color[i]+';')

    def ComboBoxGetter(self):
        return self.Combobox.currentText()

    def setComboBoxLisener(self, lisenerfun):
        self.Combobox.currentIndexChanged.connect(lisenerfun)

    def change(self, MemberScedual):
        for i in range(1, 10):
            for j in range(1, 6):
                label_name = str(i)+','+str(j)
                self.Labels[label_name].setText('')
                self.Labels[label_name].setStyleSheet(self.initstyle_Labels)
        random.shuffle(self.pick_background_color)
        for i, classes in enumerate(MemberScedual):
            for classTime in classes[1]:
                self.Labels[classTime[len(classTime)::-1]].setText(classes[0]) #reverse
                self.Labels[classTime[len(classTime)::-1]].setStyleSheet(self.showupstyle_Labels+'background:'+self.pick_background_color[i]+';')
