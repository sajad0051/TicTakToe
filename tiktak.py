from PySide6.QtWidgets import QApplication,QWidget,QMessageBox
from PySide6.QtUiTools import QUiLoader
from functools import partial
import random
class Tictaktoe(QWidget):
    def __init__(self):
        super().__init__()
        self.loader=QUiLoader()
        self.ui=self.loader.load('from.ui')
        self.player=1
        self.pl1=self.pl2=self.draw=0
        self.ui.btn_new.clicked.connect(self.new)
        self.game=[[None for i in range(3)]for j in range(3)]
        self.game[0][0]=self.ui.btn00
        self.game[0][1]=self.ui.btn01
        self.game[0][2]=self.ui.btn02
        self.game[1][0]=self.ui.btn10
        self.game[1][1]=self.ui.btn11
        self.game[1][2]=self.ui.btn12
        self.game[2][0]=self.ui.btn20
        self.game[2][1]=self.ui.btn21
        self.game[2][2]=self.ui.btn22 
        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.play,i,j))

        self.ui.show()


    def play(self,i,j):
        self.ui.rbtn_pc.setEnabled(False)
        self.ui.rbtn_pl.setEnabled(False)
        if self.game[i][j].text()=='':
            if self.player ==1:
                self.game[i][j].setStyleSheet('color: rgb(255, 255, 0);background-color: rgb(0, 85, 255);  border: 2px solid rgb(150,70,255);border-radius: 25px;')
                self.game[i][j].setText('X')
                self.player=2
                self.pc_play()
            elif self.player ==2 and self.ui.rbtn_pl.isChecked() == True:
                self.game[i][j].setStyleSheet('color: rgb(85, 0, 0);background-color: rgb(255, 170, 127); border: 2px solid rgb(150,70,255);border-radius: 25px;')
                self.game[i][j].setText('O')
                self.player=1
        self.check()
    def check(self):
        self.winner=''
        p=''
        for i in range(3):
            if self.game[i][0].text()==self.game[i][1].text() and self.game[i][1].text()==self.game[i][2].text():
                p=self.game[i][0].text()
            if self.game[0][i].text()==self.game[1][i].text() and self.game[1][i].text()==self.game[2][i].text():
                p=self.game[0][i].text()

        if self.game[0][0].text()==self.game[1][1].text() and self.game[1][1].text()==self.game[2][2].text():
            p=self.game[0][0].text()
        if self.game[0][2].text()==self.game[1][1].text() and self.game[1][1].text()==self.game[2][0].text():
            p=self.game[0][2].text()

        f=True
        for i in range(3):
            for j in range(3):
                if self.game[i][j].text() == '':
                    f=False
                    break
            if f==False:
                break
        else:
            if p== '':
                self.draw+=1
                self.ui.lbld.setText(str(self.draw))
                self.winner=''
                self.win('n')


        if p=='X':
            self.pl1+=1
            self.ui.lbl1.setText(str(self.pl1))
            self.winner=''
            self.win(str(1))
        elif p=='O':
            self.pl2+=1
            self.ui.lbl2.setText(str(self.pl2))
            self.winner=''
            self.win(str(2))
    def new(self):
        self.pl1=self.pl2=self.draw=0
        for i in range(3):
            for j in range(3):
                self.game[i][j].setStyleSheet('border: 2px solid rgb(244,157,255);border-radius: 25px;color: rgb(255,255,255);')
                self.game[i][j].setText('')
                self.ui.lbl2.setText(str(self.pl2))
                self.ui.lbl1.setText(str(self.pl1))
                self.ui.lbld.setText(str(self.draw))

    def win(self,w):
        if w=='n':
            msg=QMessageBox()
            msg.setText('nobody wins')
            msg.exec()
        else:
            msg=QMessageBox()
            msg.setText(f'player {w} wins')
            msg.exec()

        for i  in range(3):
            for j in range(3):
                self.game[i][j].setStyleSheet('border: 2px solid rgb(244,157,255);border-radius: 25px;color: rgb(255,255,255);')
                self.game[i][j].setText('')


    def pc_play(self):
        if self.player==2 and self.ui.rbtn_pc.isChecked()==True:
            while True:
                r=random.randint(0,2)
                c=random.randint(0,2)
                if self.game[r][c].text()=='':
                    self.game[r][c].setStyleSheet('color: rgb(85, 0, 0);background-color: rgb(255, 170, 127); border: 2px solid rgb(150,70,255);border-radius: 25px;')
                    self.game[r][c].setText('O')
                    self.player=1
                    break


    

app=QApplication()
main=Tictaktoe()
app.exit(app.exec())