from PyQt5 import QtWidgets
import sys
import random

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('blhablha')
        self.resize(950, 1200)
        self.style()
        self.Combobox = QtWidgets.QComboBox(self)   # 下拉選單
        self.vboxs = {}
        self.v_layouts = {}
        self.Labels = {}
        self.firstrowLabels = {}
        self.ClassTimeScedual = {'子瑩':[['檔案與儲存系統', ['2,5', '2,6', '2,7']], ['機器學習', ['2,8', '3,8', '3,9']], ['物件導向分析與設計', ['4,3', '4,4', '4,6']], ['專題討論', ['4,7', '4,8']], ['字體設計與文字編碼', ['5,5', '5,6', '5,7']]], 
                                 '成彥':[['安全程式設計', ['1,2', '1,3', '1,4']], ['檔案與儲存系統', ['2,5', '2,6', '2,7']], ['物件導向分析與設計', ['4,3', '4,4', '4,6']]]}
        self.pick_background_color = ['#ffb366', '#ffff66', '#8cff66', '#d9ff66', '#66ffff', '#668cff', '#66d9ff']
        self.ui()
        self.changeClassTimeScedual()

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

    def ui(self):
        
        retbtn = QtWidgets.QPushButton(self)
        retbtn.setText('返回首頁')
        retbtn.move(10,10) 

        label = QtWidgets.QLabel(self)
        label.setText('我的課表')
        label.move(50, 70)

        #self.Combobox = QtWidgets.QComboBox(self)   # 下拉選單
        self.Combobox.addItems(['子瑩','成彥'])   # 加入選項
        #self.Combobox.setCurrentText('子瑩')
        self.Combobox.setGeometry(800,60,70,30)
        self.Combobox.currentIndexChanged.connect(self.changeClassTimeScedual)

        x = 50
        y = 120
        w = 170
        h = 100

        # [[member名, [[課1, [時間1, 時間2, ...]], [課2, [時間1, 時間2, ...]]...]...], ...]
        # self.ClassTimeScedual = {'子瑩':[['檔案與儲存系統', ['2,5', '2,6', '2,7']], ['機器學習', ['2,8', '3,8', '3,9']], ['物件導向分析與設計', ['4,3', '4,4', '4,6']], ['專題討論', ['4,7', '4,8']], ['字體設計與文字編碼', ['5,5', '5,6', '5,7']]], 
        #                     '成彥':[['安全程式設計', ['1,2', '1,3', '1,4']], ['檔案與儲存系統', ['2,5', '2,6', '2,7']], ['物件導向分析與設計', ['4,3', '4,4', '4,6']]]}
        first_row_table = {'0,0':'Mon.', '0,1':'Tue.', '0,2':'Wed.', '0,3':'Thu.', '0,4':'Fri.'}
        # self.pick_background_color = ['#ffb366', '#ffff66', '#8cff66', '#d9ff66', '#66ffff', '#668cff', '#66d9ff']

        # self.vboxs = {}
        # self.v_layouts = {}
        # self.Labels = {}
        # self.firstrowLabels = {}
        for i in range(1, 10): #first col
            label_name ='-1,'+str(i)
            self.firstrowLabels[label_name] = QtWidgets.QLabel(self)
            self.firstrowLabels[label_name].setStyleSheet(self.style_firstcolLabel)
            self.firstrowLabels[label_name].setText(str(i))
            self.firstrowLabels[label_name].setGeometry(25, y+ i*h, 25, h) # 
        for j in range(5): #first row
            label_name ='0,'+str(j)
            self.firstrowLabels[label_name] = QtWidgets.QLabel(self)
            self.firstrowLabels[label_name].setStyleSheet(self.style_firstrowLabel)
            self.firstrowLabels[label_name].setText(first_row_table[label_name])
            self.firstrowLabels[label_name].setGeometry(x + j*w, y, w, h)

        for i in range(1, 10):
            for j in range(1, 6):
                label_name = str(i)+','+str(j)
                self.vboxs[label_name] = QtWidgets.QWidget(self)
                self.vboxs[label_name].setGeometry(x + (j-1)*w, y + i*h, w, h)
                self.vboxs[label_name].setStyleSheet(self.style_box)

                self.v_layouts[label_name] = QtWidgets.QVBoxLayout(self.vboxs[label_name])

                self.Labels[label_name] = QtWidgets.QLabel(self)
                self.Labels[label_name].setWordWrap(True) 
                # self.Labels[label_name].setText('1')
                self.Labels[label_name].setStyleSheet(self.initstyle_Labels)
                self.v_layouts[label_name].addWidget(self.Labels[label_name])

        # init 顯示yuko課表 '子瑩':[['檔案與儲存系統', ['2,5', '2,6', '2,7']], ['機器學習', ['2,8', '3,8', '3,9']], ['物件導向分析與設計', ['4,3', '4,4', '4,6']], ['專題討論', ['4,7', '4,8']], ['字體設計與文字編碼', ['5,5', '5,6', '5,7']]]
        name = self.Combobox.currentText()
        random.shuffle(self.pick_background_color)
        for i, classes in enumerate(self.ClassTimeScedual[name]):
            for classTime in classes[1]:
                self.Labels[classTime[len(classTime)::-1]].setText(classes[0]) #reverse
                self.Labels[classTime[len(classTime)::-1]].setStyleSheet(self.showupstyle_Labels+'background:'+self.pick_background_color[i]+';')

    def changeClassTimeScedual(self):
        name = self.Combobox.currentText()
        for i in range(1, 10):
            for j in range(1, 6):
                label_name = str(i)+','+str(j)
                self.Labels[label_name].setText('')
                self.Labels[label_name].setStyleSheet(self.initstyle_Labels)
        random.shuffle(self.pick_background_color)
        for i, classes in enumerate(self.ClassTimeScedual[name]):
            for classTime in classes[1]:
                self.Labels[classTime[len(classTime)::-1]].setText(classes[0]) #reverse
                self.Labels[classTime[len(classTime)::-1]].setStyleSheet(self.showupstyle_Labels+'background:'+self.pick_background_color[i]+';')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())