import pandas as pd 
from openpyxl import Workbook
import datetime

def editFileMeteo(df_meteo):

	#Eliminate spaces before and after string
	df_meteo.columns = df_meteo.columns.str.strip()
 
	#Convert into datetime format
	df_meteo['yyyy/mm/dd hh:mm'] = pd.to_datetime(df_meteo['yyyy/mm/dd hh:mm'], format="%Y/%m/%d %H:%M:%S")

	#Eliminate Elev. Sol. columns (NaN)
	del(df_meteo['Elev.Sol'])
	del(df_meteo['Elev.Sol_2'])

	#Change name in colum Temp. Ai 1
	df_meteo = df_meteo.rename(columns={'Temp. Ai 1':'TempAmb'})


	#Create excel writer object
	writer = pd.ExcelWriter('data_meteo.xlsx')

	#Write dataframe to excel
	df_meteo.to_excel(writer)

	#Save the excel
	writer.save()

def editFileTraces(df_traces):
	
	#Eliminate spaces before and after string
	df_traces.columns = df_traces.columns.str.strip()
	df_traces.columns = df_traces.columns.str.replace(' ', '')
 
	#Eliminate spaces in datas
	df_traces["Pmp"] = df_traces["Pmp"].map(str.strip)
	df_traces["Vmp"] = df_traces["Vmp"].map(str.strip)
	df_traces["Imp"] = df_traces["Imp"].map(str.strip)
	df_traces["Isc"] = df_traces["Isc"].map(str.strip)
	df_traces["Voc"] = df_traces["Voc"].map(str.strip)
	df_traces["FF"] = df_traces["FF"].map(str.strip)
	df_traces["Sensor1T"] = df_traces["Sensor1T"].map(str.strip)
	df_traces["Sensor2T"] = df_traces["Sensor2T"].map(str.strip)
	df_traces["Sensor3T"] = df_traces["Sensor3T"].map(str.strip)
	df_traces["Sensor4T"] = df_traces["Sensor4T"].map(str.strip)
	df_traces["Sensor5B"] = df_traces["Sensor5B"].map(str.strip)
	df_traces["Sensor6B"] = df_traces["Sensor6B"].map(str.strip)
	df_traces["Sensor7B"] = df_traces["Sensor7B"].map(str.strip)
	df_traces["Sensor8B"] = df_traces["Sensor8B"].map(str.strip)
	df_traces["Sensor9AI"] = df_traces["Sensor9AI"].map(str.strip)
	df_traces["Sensor10AI"] = df_traces["Sensor10AI"].map(str.strip)
	df_traces["Sensor11AI"] = df_traces["Sensor11AI"].map(str.strip)
	df_traces["Sensor12AI"] = df_traces["Sensor12AI"].map(str.strip)

	#Replace comma by point in decimals
	df_traces['Pmp'] = (df_traces['Pmp'].replace(',','.', regex=True))
	df_traces['Vmp'] = (df_traces['Vmp'].replace(',','.', regex=True))
	df_traces['Imp'] = (df_traces['Imp'].replace(',','.', regex=True))
	df_traces['Isc'] = (df_traces['Isc'].replace(',','.', regex=True))                    
	df_traces['Voc'] = (df_traces['Voc'].replace(',','.', regex=True))
	df_traces['FF'] = (df_traces['FF'].replace(',','.', regex=True))
	df_traces['Sensor1T'] = (df_traces['Sensor1T'].replace(',','.', regex=True))
	df_traces['Sensor2T'] = (df_traces['Sensor2T'].replace(',','.', regex=True))
	df_traces['Sensor3T'] = (df_traces['Sensor3T'].replace(',','.', regex=True))
	df_traces["Sensor4T"] = (df_traces["Sensor4T"].replace(',','.', regex=True))
	df_traces["Sensor5B"] = (df_traces["Sensor5B"].replace(',','.', regex=True))
	df_traces["Sensor6B"] = (df_traces["Sensor6B"].replace(',','.', regex=True))
	df_traces["Sensor7B"] = (df_traces["Sensor7B"].replace(',','.', regex=True))
	df_traces["Sensor8B"] = (df_traces["Sensor8B"].replace(',','.', regex=True))
	df_traces["Sensor9AI"] = (df_traces["Sensor9AI"].replace(',','.', regex=True))
	df_traces["Sensor10AI"] = (df_traces["Sensor10AI"].replace(',','.', regex=True))
	df_traces["Sensor11AI"] = (df_traces["Sensor11AI"].replace(',','.', regex=True))
	df_traces["Sensor12AI"] = (df_traces["Sensor12AI"].replace(',','.', regex=True))

	#Eliminate unnamed column
	del(df_traces['Unnamed:22'])

	#Eliminate Headers (except first header)
	headers_df=df_traces[df_traces["Nombre"]=="Nombre"].index
	df_traces=df_traces.drop(headers_df)

	#Create date and time column
	df_traces['yyyy/mm/dd hh:mm'] = df_traces['Fecha'].str.cat(df_traces['Hora'],sep=" ")

	#Eliminate Fecha and Hora columns (NaN)
	del(df_traces['Fecha'])
	del(df_traces['Hora'])

	#Move datetime column to first position
	first_column = df_traces.pop('yyyy/mm/dd hh:mm')  
	df_traces.insert(0, 'yyyy/mm/dd hh:mm', first_column) 

	#Convert into datetime format
	df_traces['yyyy/mm/dd hh:mm'] = pd.to_datetime(df_traces['yyyy/mm/dd hh:mm'], format="%d/%m/%Y %H:%M:%S")

	#Reset index
	df_traces = df_traces.reset_index(drop=True)

	#Convert string to float
	df_traces["Pmp"] = df_traces.Pmp.astype(float)
	df_traces["Vmp"] = df_traces.Vmp.astype(float)
	df_traces["Imp"] = df_traces.Imp.astype(float)
	df_traces["Isc"] = df_traces.Isc.astype(float)
	df_traces["Voc"] = df_traces.Voc.astype(float)
	df_traces["FF"] = df_traces.FF.astype(float)
	df_traces["Sensor1T"] = df_traces.Sensor1T .astype(float)
	df_traces["Sensor2T"] = df_traces.Sensor2T.astype(float)
	df_traces["Sensor3T"] = df_traces.Sensor3T.astype(float)
	df_traces["Sensor4T"] = df_traces.Sensor4T.astype(float)
	df_traces["Sensor5B"] = df_traces.Sensor5B.astype(float)
	df_traces["Sensor6B"] = df_traces.Sensor6B.astype(float)
	df_traces["Sensor7B"] = df_traces.Sensor7B.astype(float)
	df_traces["Sensor8B"] = df_traces.Sensor8B.astype(float)
	df_traces["Sensor9AI"] = df_traces.Sensor9AI.astype(float)
	df_traces["Sensor10AI"] = df_traces.Sensor10AI.astype(float)
	df_traces["Sensor11AI"] = df_traces.Sensor11AI.astype(float)
	df_traces["Sensor12AI"] = df_traces.Sensor12AI.astype(float)

	df_traces["TempMod"]=(df_traces["Sensor1T"]+df_traces["Sensor2T"]+df_traces["Sensor3T"]+df_traces["Sensor4T"])/4.0



	#EXPORT
	#Create excel writer object
	writer = pd.ExcelWriter('data_traces.xlsx')

	#Write dataframe to excel
	df_traces.to_excel(writer)

	#Save the excel
	writer.save()

def getDataComplete():

	data_meteo=pd.read_excel("data_meteo.xlsx", index_col=0)

	data_traces=pd.read_excel("data_traces.xlsx", index_col=0)


	##DATA_METEO
	datetime_series_1=data_meteo['yyyy/mm/dd hh:mm']

	#Create datetime index passing the datetime series
	datetime_index_1 = pd.DatetimeIndex(datetime_series_1.values)
	data_meteo=data_meteo.set_index(datetime_index_1)

	#Delete datetime column
	data_meteo.drop('yyyy/mm/dd hh:mm',axis=1, inplace=True)

	#Only add rows for missing periods
	data_meteo.sort_index(inplace=True)

	#Fill rows
	data_meteo = data_meteo.asfreq("1S", fill_value=None)

	#Interpolate datas
	data_meteo = data_meteo.interpolate(method='linear')

	#Create excel writer object
	writer = pd.ExcelWriter('data_meteo_edit.xlsx')

	#Write dataframe to excel
	data_meteo.to_excel(writer)

	#Save the excel
	writer.save()



	##DATA_TRACES
	datetime_series_2=data_traces['yyyy/mm/dd hh:mm']

	#Create datetime index passing the datetime series
	datetime_index_2 = pd.DatetimeIndex(datetime_series_2.values)
	data_traces=data_traces.set_index(datetime_index_2)

	#Delete datetime column
	data_traces.drop('yyyy/mm/dd hh:mm',axis=1, inplace=True)

	#Create excel writer object
	writer = pd.ExcelWriter('data_traces_edit.xlsx')

	#Write dataframe to excel
	data_traces.to_excel(writer)

	#Save the excel
	writer.save()
	

	##DATA 
	data=pd.merge(data_meteo,data_traces, left_index=True, right_index=True)

	#Add new column (date)
	data['Date']=data.index

	#Move to first position
	first_column = data.pop('Date')  
	data.insert(0, 'Date', first_column) 


	#Create excel writer object
	writer = pd.ExcelWriter('data.xlsx')

	#Write dataframe to excel
	data.to_excel(writer)

	#Save the excel
	writer.save()
	