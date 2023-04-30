from PyQt5 import QtWidgets
from datetime import date
from datetime import timedelta
import random

class CleaningTimeTableUI:
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

    def __init__(self, window: QtWidgets.QMainWindow, hatarakuMembersThisSemester, StartD, EndD):
        self.style()

        self.month = date.today().month # 想show出的月份
        self.members = hatarakuMembersThisSemester
        self.semesterStartD = StartD
        self.semesterEndD = EndD
        self.pickOneColorForaMember = ['#ffdd99', '#99ffbb', '#99bbff', '#ffff99', '#8cd98c', '#cc99ff', '#99ebff', '#ff8080']
        self.member_work = [[member+'倒垃圾', member+'掃+拖', self.pickOneColorForaMember[self.members.index(member)]] for member in self.members]

        retbtn = QtWidgets.QPushButton(window)
        retbtn.setText('返回首頁')
        retbtn.move(10,10) 

        label = QtWidgets.QLabel(window)
        label.setText('打掃排班表')
        label.move(50, 70)
    
        self.label_month = QtWidgets.QLabel(window)
        self.label_month.setText(date(2023, 4, 20).strftime("%m %Y"))
        self.label_month.move(52, 100)

        lastmonthbtn = QtWidgets.QPushButton(window)
        lastmonthbtn.setText('>')
        lastmonthbtn.setGeometry(870,80,30,30)
        lastmonthbtn.clicked.connect(self.changeToNextMonth)
        nextmonthbtn = QtWidgets.QPushButton(window)
        nextmonthbtn.setText('<')
        nextmonthbtn.setGeometry(820,80,30,30)
        nextmonthbtn.clicked.connect(self.changeToLastMonth)

        x = 50
        y = 120
        w = 170
        h = 120

        self.vboxs = {}
        self.v_layouts = {}
        self.Labeldays = {}
        self.Label1s = {}
        self.Label2s = {}
        self.firstrowLabels = {}
        first_row_table = {'0,0':'Mon.', '0,1':'Tue.', '0,2':'Wed.', '0,3':'Thu.', '0,4':'Fri.'}
        for j in range(5): #first row
            label_name ='0,'+str(j)
            self.firstrowLabels[label_name] = QtWidgets.QLabel(window)
            self.firstrowLabels[label_name].setStyleSheet(self.style_firstrowLabel)
            self.firstrowLabels[label_name].setText(first_row_table[label_name])
            self.firstrowLabels[label_name].setGeometry(x + j*w, y, w, h)

        for i in range(1, 6):
            for j in range(5):
                label_name = str(i)+','+str(j)
                self.vboxs[label_name] = QtWidgets.QWidget(window)
                self.vboxs[label_name].setGeometry(x + j*w, y + i*h, w, h)
                self.vboxs[label_name].setStyleSheet(self.style_box)

                self.v_layouts[label_name] = QtWidgets.QVBoxLayout(self.vboxs[label_name])

                self.Labeldays[label_name] = QtWidgets.QLabel(window)
                self.Labeldays[label_name].setStyleSheet(self.style_Labelday)
                self.v_layouts[label_name].addWidget(self.Labeldays[label_name])

                self.Label1s[label_name] = QtWidgets.QLabel(window)
                self.Label1s[label_name].setStyleSheet(self.initstyle_Labels)
                self.v_layouts[label_name].addWidget(self.Label1s[label_name])

                self.Label2s[label_name] = QtWidgets.QLabel(window)
                self.Label2s[label_name].setStyleSheet(self.initstyle_Labels)
                self.v_layouts[label_name].addWidget(self.Label2s[label_name])
        self.setupUI(self.month)

    def setupUI(self, month):
        for i in range(1, 6):
            for j in range(5):
                label_name = str(i)+','+str(j)
                self.Label1s[label_name].setText('')
                self.Label1s[label_name].setStyleSheet(self.initstyle_Labels)
                self.Label2s[label_name].setText('')
                self.Label2s[label_name].setStyleSheet(self.initstyle_Labels)
                self.Labeldays[label_name].setText('')
                self.Labeldays[label_name].setStyleSheet(self.initstyle_Labels)
        # two case
        # 1號在假日 -> firstrow從星期一開始
        # else -> firstrow從一號開始
        if date(2023, month, 1).isoweekday()==6 or date(2023, month, 1).isoweekday()==7:
            self.first_monday = -1
            for i in range(7):
                if date(2023, month, 1+i).weekday() == 0:
                    first_monday = 1+i
                    break
            nextMonth = (date(2023, month, 1)+timedelta(days = 33)).strftime("%m")
            for i in range(1, 6):
                for j in range(5):
                    label_name = str(i)+','+str(j)
                    today = date(2023, month, 1)+timedelta(days=(i-1)*7+j+first_monday-1)
                    if today.strftime("%m") == nextMonth: #換月了
                        self.Labeldays[label_name].setText(today.strftime("%m/%d"))
                        self.Labeldays[label_name].setStyleSheet(self.style_Labelday)
                    else:
                        self.Labeldays[label_name].setText((date(2023, month, 1)+timedelta(days=(i-1)*7+j+first_monday-1)).strftime("%d"))

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
            dayOftheWeek = date(2023, month, 1).isoweekday()
            nextMonth = (date(2023, month, 1)+timedelta(days = 31)).strftime("%m")
            for i in range(1, 6):
                for j in range(5):
                    label_name = str(i)+','+str(j)
                    if i==1 and j<dayOftheWeek-1:
                        continue
                    today = date(2023, month, 1)+timedelta(days=(i-1)*7+(j+1)-(dayOftheWeek-1)-1)
                    if today.strftime("%m") == nextMonth: #換月了
                        self.Labeldays[label_name].setText(today.strftime("%m/%d"))
                        self.Labeldays[label_name].setStyleSheet(self.style_Labelday)
                    else:
                        self.Labeldays[label_name].setText((date(2023, month, 1)+timedelta(days=(i-1)*7+(j+1)-(dayOftheWeek-1)-1)).strftime("%d"))

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

    # 換頁
    def changeToLastMonth(self):
        self.month -= 1
        self.label_month.setText(date(2023, self.month, 20).strftime("%m %Y"))
        self.setupUI(self.month)
    def changeToNextMonth(self):
        self.month += 1
        self.label_month.setText(date(2023, self.month, 20).strftime("%m %Y"))
        self.setupUI(self.month)