from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure

import pandas as pd

def plot(self):
        df_original = pd.read_excel("data_selected.xlsx")
        df_filtered = pd.read_excel("data_filtered.xlsx")

        varX=self.varX.currentText()
        varY=self.varY.currentText()

        varX_original = df_original[varX]
        varY_original = df_original[varY]
        varX_filtered = df_filtered[varX]
        varY_filtered = df_filtered[varY]

        self.figure.clear() 
   
        ax1 = self.figure.add_subplot(211) 
        ax2 = self.figure.add_subplot(212,sharex=ax1,sharey=ax1)
        self.figure.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.55)

        ax1.set_title('Original data')
        ax2.set_title('Filtered data')

        ax1.set_xlabel(varX)
        ax1.set_ylabel(varY)
        ax2.set_xlabel(varX)
        ax2.set_ylabel(varY)

        ax1.scatter(varX_original, varY_original,s=10) 
        ax2.scatter(varX_filtered, varY_filtered,s=10) 
     
        self.canvas.draw() 