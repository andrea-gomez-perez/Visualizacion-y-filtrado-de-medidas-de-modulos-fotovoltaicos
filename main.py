import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDateTime,Qt
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtGui 

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure

import pandas as pd

import module_load
import module_filters
import module_graph

name_file_meteo=""
name_file_traces=""

df_meteo=""
df_traces=""

item=""

class Window(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("MainWindow.ui",self)

		self.setFixedWidth(800)
		self.setFixedHeight(700)

		self.setWindowIcon(QtGui.QIcon('app.png')) 

		self.graphWindow=GraphWindow()
		
		self.meteoButton.clicked.connect(self.openFileMeteo)
		self.tracesButton.clicked.connect(self.openFileTraces)
		self.loadButton.clicked.connect(self.loadFiles)

		self.filterButton.clicked.connect(self.filterData)
		self.visualizeButton.clicked.connect(self.visualizeGraph)

	def openFileMeteo(self):


		global name_file_meteo

		name_file_meteo=QFileDialog.getOpenFileName(self, "Select file", "","File txt (*.txt);; All files (*)")

		aux=os.path.split(name_file_meteo[0])
		name=aux[1]
		
		if name_file_meteo[0]=="":
			QMessageBox.warning(self,"Warning", "No file selected")
		else:
			if name.startswith("meteo")==True:
				QMessageBox.information(self,"Information", "File selected")
			elif name.startswith("meteo")==False:
				QMessageBox.warning(self,"Warning", "Invalid file")
		


		


	def openFileTraces(self):

		global name_file_traces

		name_file_traces=QFileDialog.getOpenFileName(self, "Select file", "","File txt (*.dat);; All files (*)")

		aux=os.path.split(name_file_traces[0])
		name=aux[1]
		
		if name_file_traces[0]=="":
			QMessageBox.warning(self,"Warning", "No file selected")
		else:
			if name.startswith("summary")==True:
				QMessageBox.information(self,"Information", "File selected")
			elif name.startswith("summary")==False:
				QMessageBox.warning(self,"Warning", "Invalid file")


	def loadFiles(self):


		try:
			df_meteo=pd.read_csv(name_file_meteo[0], '\t')
			module_load.editFileMeteo(df_meteo)

			df_traces=pd.read_csv(name_file_traces[0],'\t', encoding='unicode_escape')
			module_load.editFileTraces(df_traces)

			module_load.getDataComplete()
				
		except IndexError:
			QMessageBox.warning(self,"Warning", "¡Error! Please select files")

		


	def filterData(self):

		global item
		data=pd.read_excel("data.xlsx", index_col=0)
		data_selected=pd.DataFrame()

		item=self.moduleBox.currentText()

	
		startValue= self.startDateTime.dateTime()
		endValue = self.endDateTime.dateTime()

		
		startdate_str=startValue.toString(Qt.RFC2822Date)
		enddate_str=endValue.toString(Qt.RFC2822Date)

		module_filters.selection(data, item, startdate_str, enddate_str)

		param1=self.parameter1.currentText()
		param2=self.parameter2.currentText()
		param3=self.parameter3.currentText()
		param4=self.parameter4.currentText()

		param1max_str=self.parameter1_max.text()
		param2max_str=self.parameter2_max.text()
		param3max_str=self.parameter3_max.text()
		param4max_str=self.parameter4_max.text()

		param1min_str=self.parameter1_min.text()
		param2min_str=self.parameter2_min.text()
		param3min_str=self.parameter3_min.text()
		param4min_str=self.parameter4_min.text()


		module_filters.filter(param1,param2,param3,param4,param1max_str,param2max_str,param3max_str,param4max_str,param1min_str,param2min_str,param3min_str,param4min_str)


	def visualizeGraph(self):

		self.graphWindow.exec_()




class GraphWindow(QDialog): 
       
    
    def __init__(self, parent=None): 
        super(GraphWindow, self).__init__(parent) 

        self.setWindowIcon(QtGui.QIcon('graph.png'))   
        self.setWindowTitle("Graph") 
        
        self.figure = plt.figure() 
        self.canvas = FigureCanvas(self.figure) 
        self.toolbar = NavigationToolbar(self.canvas, self) 
        self.button = QPushButton('Plot') 
        self.button.clicked.connect(self.onClick) 

        self.varX=QComboBox()
        self.varX.addItem("Pmp")
        self.varX.addItem("Vmp")
        self.varX.addItem("Imp")
        self.varX.addItem("Voc")
        self.varX.addItem("Isc")
        self.varX.addItem("TempMod")
        self.varX.addItem("Date")

        self.varX.addItem("Bn")
        self.varX.addItem("Gn")
        self.varX.addItem("Dh")
        self.varX.addItem("TempAmb")

        self.varY=QComboBox()
        self.varY.addItem("Pmp")
        self.varY.addItem("Vmp")
        self.varY.addItem("Imp")
        self.varY.addItem("Voc")
        self.varY.addItem("Isc")
        self.varY.addItem("TempMod")
        self.varY.addItem("Date")

        self.varY.addItem("Bn")
        self.varY.addItem("Gn")
        self.varY.addItem("Dh")
        self.varY.addItem("TempAmb")

        self.labelX=QLabel('Axis X:')
        self.labelY=QLabel('Axis Y:')
        
        self.mainLayout = QGridLayout()
        self.plotLayout = QVBoxLayout()
        self.widgetLayout = QGridLayout()

        self.mainLayout.addLayout(self.plotLayout, 0, 0)
        self.mainLayout.addLayout(self.widgetLayout, 1, 0)
        
        self.plotLayout.addWidget(self.toolbar) 
        self.plotLayout.addWidget(self.canvas) 
            
        self.widgetLayout.addWidget(self.labelX,1,1,alignment=QtCore.Qt.AlignCenter)
        self.widgetLayout.addWidget(self.varX,1,2)
        self.widgetLayout.addWidget(self.labelY,1,3,alignment=QtCore.Qt.AlignCenter)
        self.widgetLayout.addWidget(self.varY,1,4)
        self.widgetLayout.addWidget(self.button,2,1,1,4)
           
        self.setLayout(self.mainLayout)

    
    def onClick(self): 
           
        module_graph.plot(self)


app=QApplication(sys.argv)
_window=Window()
_window.show()
app.exec_()