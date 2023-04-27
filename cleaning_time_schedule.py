from PyQt5 import QtWidgets
import sys
from datetime import date
from datetime import timedelta

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.month = 4 # global var 想show出的月份
        self.semesterStartD = [2, 19]
        self.semesterEndD = [6, 21]
        self.setWindowTitle('blhablha')
        self.resize(950, 1000)
        self.style()
        self.ui()

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
        # self.style_nextMonth = '''
        #     background:#fff;
        #     text-align:center;
        #     border:0px solid #000;
        #     color:#cccccc;
        # '''

    def ui(self):
        retbtn = QtWidgets.QPushButton(self)
        retbtn.setText('返回首頁')
        retbtn.move(10,10) 

        label = QtWidgets.QLabel(self)
        label.setText('打掃排班表')
        label.move(50, 70)
    
        self.label_month = QtWidgets.QLabel(self)
        self.label_month.setText(date(2023, 4, 20).strftime("%m %Y"))
        self.label_month.move(52, 100)

        lastmonthbtn = QtWidgets.QPushButton(self)
        lastmonthbtn.setText('>')
        lastmonthbtn.setGeometry(870,80,30,30)
        lastmonthbtn.clicked.connect(self.changeToNextMonth)
        nextmonthbtn = QtWidgets.QPushButton(self)
        nextmonthbtn.setText('<')
        nextmonthbtn.setGeometry(820,80,30,30)
        nextmonthbtn.clicked.connect(self.changeToLastMonth)

        x = 50
        y = 120
        w = 170
        h = 120

        self.member_work = [['成彥倒垃圾', '成彥掃+拖', '#ffdd99'], ['晨睿倒垃圾', '晨睿掃+拖', '#99ffbb'], ['旻昌倒垃圾', '旻昌掃+拖', '#99bbff'], ['上澤倒垃圾', '上澤掃+拖', '#ffff99'], ['宇翔倒垃圾', '宇翔掃+拖', '#8cd98c'], ['駿頤倒垃圾', '駿頤掃+拖', '#cc99ff'], ['韋豪倒垃圾', '韋豪掃+拖', '#99ebff'], ['子龍倒垃圾', '子龍掃+拖', '#ff8080']]
        first_row_table = {'0,0':'Mon.', '0,1':'Tue.', '0,2':'Wed.', '0,3':'Thu.', '0,4':'Fri.'}

        self.vboxs = {}
        self.v_layouts = {}
        self.Labeldays = {}
        self.Label1s = {}
        self.Label2s = {}
        self.firstrowLabels = {}
        for j in range(5): #first row
            label_name ='0,'+str(j)
            self.firstrowLabels[label_name] = QtWidgets.QLabel(self)
            self.firstrowLabels[label_name].setStyleSheet(self.style_firstrowLabel)
            self.firstrowLabels[label_name].setText(first_row_table[label_name])
            self.firstrowLabels[label_name].setGeometry(x + j*w, y, w, h)

        for i in range(1, 6):
            for j in range(5):
                label_name = str(i)+','+str(j)
                self.vboxs[label_name] = QtWidgets.QWidget(self)
                self.vboxs[label_name].setGeometry(x + j*w, y + i*h, w, h)
                self.vboxs[label_name].setStyleSheet(self.style_box)

                self.v_layouts[label_name] = QtWidgets.QVBoxLayout(self.vboxs[label_name])

                self.Labeldays[label_name] = QtWidgets.QLabel(self)
                #self.Labeldays[label_name].setText('day')
                self.Labeldays[label_name].setStyleSheet(self.style_Labelday)
                self.v_layouts[label_name].addWidget(self.Labeldays[label_name])

                self.Label1s[label_name] = QtWidgets.QLabel(self)
                #self.Label1s[label_name].setText('1')
                self.Label1s[label_name].setStyleSheet(self.initstyle_Labels)
                self.v_layouts[label_name].addWidget(self.Label1s[label_name])

                self.Label2s[label_name] = QtWidgets.QLabel(self)
                #self.Label2s[label_name].setText('2')
                self.Label2s[label_name].setStyleSheet(self.initstyle_Labels)
                self.v_layouts[label_name].addWidget(self.Label2s[label_name])

        # init找4月第一個星期一是幾號
        self.first_monday = -1
        for i in range(7):
            if date(2023, 4, 1+i).weekday() == 0:
                first_monday = 1+i
                break
        for i in range(1, 6):
            for j in range(5):
                label_name = str(i)+','+str(j)
                today = date(2023, 4, 1)+timedelta(days=(i-1)*7+j+first_monday-1)
                if today.strftime("%m") == '05': #換月了
                    self.Labeldays[label_name].setText(today.strftime("%m/%d"))
                    self.Labeldays[label_name].setStyleSheet(self.style_Labelday)
                else:
                    self.Labeldays[label_name].setText((date(2023, 4, 1)+timedelta(days=(i-1)*7+j+first_monday-1)).strftime("%d"))

        count_member = 0
        two_days_flag = 0
        for i in range(1, 6):
            for j in range(5):
                label_name = str(i)+','+str(j)
                if j==2:
                    self.Label2s[label_name].setStyleSheet('''
                    background:'''+self.member_work[count_member][2]+''';
                    ''')
                    self.Label2s[label_name].setText(self.member_work[count_member][1])
                    if count_member == 7:
                        count_member = 0
                    else:
                        count_member += 1
                if two_days_flag == 1 or two_days_flag == 2:
                    two_days_flag = 0                    
                else:
                    self.Label1s[label_name].setStyleSheet('''
                    background:'''+self.member_work[count_member][2]+''';
                    ''')
                    self.Label1s[label_name].setText(self.member_work[count_member][0])
                    two_days_flag += 1
                    if count_member == 7:
                        count_member = 0
                    else:
                        count_member += 1
    # 換頁
    def changeToLastMonth(self):
        self.month -= 1
        self.label_month.setText(date(2023, self.month, 20).strftime("%m %Y"))
        self.changeMonth()
    def changeToNextMonth(self):
        self.month += 1
        self.label_month.setText(date(2023, self.month, 20).strftime("%m %Y"))
        self.changeMonth()
    def changeMonth(self):
        #清掉之前的紀錄
        for i in range(1, 6):
            for j in range(5):
                label_name = str(i)+','+str(j)
                self.Label1s[label_name].setText('')
                self.Label1s[label_name].setStyleSheet(self.initstyle_Labels)
                self.Label2s[label_name].setText('')
                self.Label2s[label_name].setStyleSheet(self.initstyle_Labels)
                self.Labeldays[label_name].setText('')
                self.Labeldays[label_name].setStyleSheet(self.initstyle_Labels)
        # if 學期結束
        if date(2023, self.month, 1).isoweekday()==6 or date(2023, self.month, 1).isoweekday()==7:
            # init找4月第一個星期一是幾號 (跟4月的case一樣)
            self.first_monday = -1
            for i in range(7):
                if date(2023, self.month, 1+i).weekday() == 0:
                    first_monday = 1+i
                    break
            nextMonth = (date(2023, self.month, 1)+timedelta(days = 33)).strftime("%m")
            for i in range(1, 6):
                for j in range(5):
                    label_name = str(i)+','+str(j)
                    today = date(2023, self.month, 1)+timedelta(days=(i-1)*7+j+first_monday-1)
                    if today.strftime("%m") == nextMonth: #換月了
                        self.Labeldays[label_name].setText(today.strftime("%m/%d"))
                        self.Labeldays[label_name].setStyleSheet(self.style_Labelday)
                    else:
                        self.Labeldays[label_name].setText((date(2023, self.month, 1)+timedelta(days=(i-1)*7+j+first_monday-1)).strftime("%d"))

            count_member = 0
            two_days_flag = 0
            for i in range(1, 6):
                for j in range(5):
                    label_name = str(i)+','+str(j)
                    today_month = int(self.label_month.text().split()[0])
                    today_day =  1 #init
                    try:
                        today_day = int(self.Labeldays[label_name].text().split()[0])
                    except:
                        pass
                    if date(2023, today_month, today_day) < date(2023, self.semesterStartD[0], self.semesterStartD[1]) or date(2023, today_month, today_day) > date(2023, self.semesterEndD[0], self.semesterEndD[1]):
                        break
                    if j==2:
                        self.Label2s[label_name].setStyleSheet('''
                        background:'''+self.member_work[count_member][2]+''';
                        ''')
                        self.Label2s[label_name].setText(self.member_work[count_member][1])
                        if count_member == 7:
                            count_member = 0
                        else:
                            count_member += 1
                    if two_days_flag == 1 or two_days_flag == 2:
                        two_days_flag = 0                    
                    else:
                        self.Label1s[label_name].setStyleSheet('''
                        background:'''+self.member_work[count_member][2]+''';
                        ''')
                        self.Label1s[label_name].setText(self.member_work[count_member][0])
                        two_days_flag += 1
                        if count_member == 7:
                            count_member = 0
                        else:
                            count_member += 1
        else:
            dayOftheWeek = date(2023, self.month, 1).isoweekday()
            nextMonth = (date(2023, self.month, 1)+timedelta(days = 31)).strftime("%m")
            for i in range(1, 6):
                for j in range(5):
                    label_name = str(i)+','+str(j)
                    if i==1 and j<dayOftheWeek-1:
                        continue
                    today = date(2023, self.month, 1)+timedelta(days=(i-1)*7+(j+1)-(dayOftheWeek-1)-1)
                    if today.strftime("%m") == nextMonth: #換月了
                        self.Labeldays[label_name].setText(today.strftime("%m/%d"))
                        self.Labeldays[label_name].setStyleSheet(self.style_Labelday)
                    else:
                        self.Labeldays[label_name].setText((date(2023, self.month, 1)+timedelta(days=(i-1)*7+(j+1)-(dayOftheWeek-1)-1)).strftime("%d"))

            count_member = 0
            two_days_flag = 0
            for i in range(1, 6):
                for j in range(5):
                    label_name = str(i)+','+str(j)
                    today_month = int(self.label_month.text().split()[0])
                    today_day =  1 #init
                    try:
                        today_day = int(self.Labeldays[label_name].text().split()[0])
                    except:
                        pass
                    if (date(2023, today_month, today_day) < date(2023, self.semesterStartD[0], self.semesterStartD[1])) or (date(2023, today_month, today_day) > date(2023, self.semesterEndD[0], self.semesterEndD[1])):
                        break
                    label_name = str(i)+','+str(j)
                    if i==1 and j<dayOftheWeek-1:
                        continue
                    if j==2:
                        self.Label2s[label_name].setStyleSheet('''
                        background:'''+self.member_work[count_member][2]+''';
                        ''')
                        self.Label2s[label_name].setText(self.member_work[count_member][1])
                        if count_member == 7:
                            count_member = 0
                        else:
                            count_member += 1
                    if two_days_flag == 1 or two_days_flag == 2:
                        two_days_flag = 0                    
                    else:
                        self.Label1s[label_name].setStyleSheet('''
                        background:'''+self.member_work[count_member][2]+''';
                        ''')
                        self.Label1s[label_name].setText(self.member_work[count_member][0])
                        two_days_flag += 1
                        if count_member == 7:
                            count_member = 0
                        else:
                            count_member += 1
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())