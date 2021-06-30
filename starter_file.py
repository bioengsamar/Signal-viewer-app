from PyQt5 import QtWidgets,QtCore
from des1 import Ui_MainWindow
import sys
import numpy as np
from  PyQt5.QtWidgets  import QFileDialog
import pandas as pd
from numpy import genfromtxt
class ApplicationWindow(QtWidgets.QMainWindow):
   
    def __init__(self):
        self.y1=[]
        self.y2=[]
        self.y3=[]
        self.y4=[]
        self.y5=[]
        
        self.i1=0
        self.i2=0
        self.i3=0
        self.i4=0
        self.i5=0
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.MplWid1.close()
        self.ui.MplWid2.close()
        self.ui.MplWid3.close()
        self.ui.MplWid4.close()
        self.ui.MplWid5.close()
        
        
        
    def openFile(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open file','','*.txt *.csv *.xls')[0]
       
        
        #print(self.file)
        #print(self.file[len(self.file)-1])
        if 'xls' in self.file:
            #print("xls")
            self.data=pd.read_excel(self.file)
            
        else:
            self.data=genfromtxt(self.file)
        
    def open2(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open file','','*.txt *.csv *.xls')[0]
   
        if 'xls' in self.file:
    
            self.data1=pd.read_excel(self.file)
        
        else:
            self.data1=genfromtxt(self.file)
    
    def openn(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open file','','*.txt *.csv *.xls')[0]
   
        if 'xls' in self.file:
    
            self.data2=pd.read_excel(self.file)
        
        else:
            self.data2=genfromtxt(self.file)
    
    def open4(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open file','','*.txt *.csv *.xls')[0]
   
        if 'xls' in self.file:
    
            self.data3=pd.read_excel(self.file)
        
        else:
            self.data3=genfromtxt(self.file)
            
    def open5(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open file','','*.txt *.csv *.xls')[0]
   
        if 'xls' in self.file:
    
            self.data4=pd.read_excel(self.file)
        
        else:
            self.data4=genfromtxt(self.file)
            
            
        
            
    
    def play1(self):
        self.i1+=1
        self.y1=self.data[:self.i1]
        self .ui. MplWid1 . canvas . axes . clear () 
        self.ui.MplWid1 . canvas. axes .plot(self.y1,'r-',color='blue')
        self .ui. MplWid1 . canvas . axes . legend ((  'Signal_1' ,  ),loc = 'upper right' ) 
        self .ui. MplWid1 . canvas . draw ()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.play1)
        self.timer.start()
        
    def stop(self):
         self.timer.stop()
         
         
    
         
    def play2(self):
        self.i2+=1
        self.y2=self.data1[:self.i2]
        self .ui. MplWid2 . canvas . axes . clear () 
        self.ui.MplWid2 . canvas. axes .plot(self.y2,'r-',color='green')
        self .ui. MplWid2 . canvas . axes . legend ((  'Signal_2' ,),loc = 'upper right' ) 
        self .ui. MplWid2 . canvas . draw ()
        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(100)
        self.timer2.timeout.connect(self.play2)
        self.timer2.start()  
         
    def stop2(self):
         self.timer2.stop()
    
         
    def play3(self):
        self.i3+=1
        self.y3=self.data2[:self.i3]
        self .ui. MplWid3 . canvas . axes . clear () 
        self.ui.MplWid3 . canvas. axes .plot(self.y3,'r-')
        self .ui. MplWid3 . canvas . axes . legend ((  'Signal_3' ,  ),loc = 'upper right' ) 
        self .ui. MplWid3 . canvas . draw ()
        self.timer3 = QtCore.QTimer()
        self.timer3.setInterval(100)
        self.timer3.timeout.connect(self.play3)
        self.timer3.start()
        
    def stop3(self):
        self.timer3.stop()
    
    def play4(self):
        self.i4+=1
        self.y4=self.data3[:self.i4]
        self .ui. MplWid4 . canvas . axes . clear () 
        self.ui.MplWid4 . canvas. axes .plot(self.y4,'r-',color='yellow')
        self .ui. MplWid4 . canvas . axes . legend ((  'Signal_4' , ),loc = 'upper right' ) 
        self .ui. MplWid4 . canvas . draw ()
        self.timer4 = QtCore.QTimer()
        self.timer4.setInterval(100)
        self.timer4.timeout.connect(self.play4)
        self.timer4.start()
        
    def stop4(self):
        self.timer4.stop() 


    def play5(self):
        self.i5+=1
        self.y5=self.data4[:self.i5]
        self .ui. MplWid5 . canvas . axes . clear () 
        self.ui.MplWid5 . canvas. axes .plot(self.y5,'r-', color='black' )
        self .ui. MplWid5 . canvas . axes . legend ((  'Signal_5' , ),loc = 'upper right' ) 
        self .ui. MplWid5 . canvas . draw ()
        self.timer5 = QtCore.QTimer()
        self.timer5.setInterval(100)
        self.timer5.timeout.connect(self.play5)
        self.timer5.start()    
    
    def stop5(self):
        self.timer5.stop()  
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()
    

if __name__ == "__main__":
    main()