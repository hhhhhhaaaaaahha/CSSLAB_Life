from PyQt5 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('blhablha')
        self.resize(950, 900)
        self.style()
        self.vboxs = {}
        self.v_layouts = {}
        self.Labels = {}
        self.firstrowLabels = {}
        self.ui()


    def style(self):
        self.style_box = '''
            background:#fff;
            border:1px solid #000;
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

    def ui(self):
        retbtn = QtWidgets.QPushButton(self)
        retbtn.setText('返回首頁')
        retbtn.move(10,10) 

        label = QtWidgets.QLabel(self)
        label.setText('meeting時間表')
        label.move(50, 70)

        x = 70
        y = 120
        w = 170
        h = 50

        first_row_table = {'0,0':'Mon.', '0,1':'Tue.', '0,2':'Wed.', '0,3':'Thu.', '0,4':'Fri.'}
        col_time = ['11:00', '12:00', '13:00', '14:00', '15:00','16:00', '17:00']
        meeting_time = [['子瑩', '1', '16:00'], ['上澤', '1', '17:00'], ['宇翔', '2', '11:00'], ['如儀', '2', '12:00'], ['宗霖', '2', '16:00'], ['晨睿', '3', '11:00'], ['華暄', '3', '16:00'], ['聖翊', '3', '17:00'], ['成彥', '4', '17:00'], ['永誠', '5', '13:00'], ['立軒', '5', '14:00'], ['振洋', '5', '15:00']]

        for i in range(1, 8): #first col
            label_name ='-1,'+str(i)
            self.firstrowLabels[label_name] = QtWidgets.QLabel(self)
            self.firstrowLabels[label_name].setStyleSheet(self.style_firstcolLabel)
            self.firstrowLabels[label_name].setText(col_time[i-1])
            self.firstrowLabels[label_name].setGeometry(15, y+ i*h, 50, h)
        for j in range(5): #first row
            label_name ='0,'+str(j)
            self.firstrowLabels[label_name] = QtWidgets.QLabel(self)
            self.firstrowLabels[label_name].setStyleSheet(self.style_firstrowLabel)
            self.firstrowLabels[label_name].setText(first_row_table[label_name])
            self.firstrowLabels[label_name].setGeometry(x + j*w, y, w, h)
        for i in range(1, 8):
            for j in range(1, 6):
                label_name = str(i)+','+str(j)
                # print(label_name)
                self.vboxs[label_name] = QtWidgets.QWidget(self)
                self.vboxs[label_name].setGeometry(x + (j-1)*w, y + i*h, w, h)
                self.vboxs[label_name].setStyleSheet(self.style_box)

                self.v_layouts[label_name] = QtWidgets.QVBoxLayout(self.vboxs[label_name])

                self.Labels[label_name] = QtWidgets.QLabel(self)
                self.Labels[label_name].setWordWrap(True) 
                # self.Labels[label_name].setText('1')
                self.Labels[label_name].setStyleSheet(self.initstyle_Labels)
                self.v_layouts[label_name].addWidget(self.Labels[label_name])
        for member in meeting_time:
            meeting_day_time = member[1]+','+str(col_time.index(member[2])+1)
            self.Labels[meeting_day_time[len(meeting_day_time)::-1]].setText(member[0]) #reverse
            



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec_())