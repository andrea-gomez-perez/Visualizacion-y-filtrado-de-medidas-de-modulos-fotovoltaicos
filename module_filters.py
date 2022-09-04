import pandas as pd 
#import numpy as np
from datetime import datetime


def selection(data, item, startdate_str, enddate_str):

	global data_selected

	#FILTER MODULE
	if item=='Module 1':
		data_selected=data[data['Nombre']=='RR1000']
	elif item=='Module 2':
		data_selected=data[data['Nombre']=='RR2000']
	elif  item=='Module 3':
		data_selected=data[data['Nombre']=='RR3000']
	elif item=='Module 4':
		data_selected=data[data['Nombre']=='RRFLAT']


	#FILTER DATE AND TIME
	#Add new column (date)
	data_selected['Date']=data_selected.index

	#Move to first position
	first_column = data_selected.pop('Date')  
	data_selected.insert(0, 'Date', first_column) 

	#Reset index
	data_selected=data_selected.reset_index()
	del(data_selected['index'])


	startdate_format=datetime.strptime(startdate_str,'%d %b %Y %H:%M:%S %z').strftime('%Y-%m-%d %H:%M:%S')
	enddate_format=datetime.strptime(enddate_str,'%d %b %Y %H:%M:%S %z').strftime('%Y-%m-%d %H:%M:%S')


	startdate=datetime.strptime(startdate_format, '%Y-%m-%d %H:%M:%S')
	enddate=datetime.strptime(enddate_format, '%Y-%m-%d %H:%M:%S')


	mask = (data_selected['Date'] > startdate) & (data_selected['Date'] <= enddate)
	data_selected = data_selected.loc[mask]


	#Create excel writer object
	writer = pd.ExcelWriter('data_selected.xlsx')

	#Write dataframe to excel
	data_selected.to_excel(writer)

	#Save the excel
	writer.save()


def filter(param1,param2,param3,param4,param1max_str,param2max_str,param3max_str,param4max_str,param1min_str,param2min_str,param3min_str,param4min_str):


	global data_selected

	if param1max_str=='':
		param1max=float("inf")
	else:
		param1max=float(param1max_str)


	if param2max_str=='':
		param2max=float("inf")
	else:
		param2max=float(param2max_str)

	if param3max_str=='':
		param3max=float("inf")
	else:
		param3max=float(param3max_str)

	if param4max_str=='':
		param4max=float("inf")
	else:
		param4max=float(param4max_str)
	

	if param1min_str=='':
		param1min=float()
	else:
		param1min=float(param1min_str)

	if param2min_str=='':
		param2min=float()
	else:
		param2min=float(param2min_str)

	if param3min_str=='':
		param3min=float()
	else:
		param3min=float(param3min_str)

	if param4min_str=='':
		param4min=float()
	else:
		param4min=float(param4min_str)


	if param1=="Pmp":
		data_selected=data_selected.query("Pmp>@param1min and Pmp<@param1max")
	elif param1=="Vmp":
		data_selected=data_selected.query("Vmp>@param1min and Vmp<@param1max")
	elif param1=="Imp":
		data_selected=data_selected.query("Imp>@param1min and Imp<@param1max")
	elif param1=="Isc":
		data_selected=data_selected.query("Isc>@param1min and Isc<@param1max")
	elif param1=="Voc":
		data_selected=data_selected.query("Voc>@param1min and Voc<@param1max")
	elif param1=="Bn":
		data_selected=data_selected.query("Bn>@param1min and Bn<@param1max")
	elif param1=="Dh":
		data_selected=data_selected.query("Dh>@param1min and Dh<@param1max")
	elif param1=="Gn":
		data_selected=data_selected.query("Gn>@param1min and Gn<@param1max")
	elif param1=="TempAmb":
		data_selected=data_selected.query("TempAmb>@param1min and TempAmb<@param1max")
	elif param1=="TempMod":
		data_selected=data_selected.query("TempMod>@param1min and TempMod<@param1max")


	if param2=="Pmp":
		data_selected=data_selected.query("Pmp>@param2min and Pmp<@param2max")
	elif param2=="Vmp":
		data_selected=data_selected.query("Vmp>@param2min and Vmp<@param2max")
	elif param2=="Imp":
		data_selected=data_selected.query("Imp>@param2min and Imp<@param2max")
	elif param2=="Isc":
		data_selected=data_selected.query("Isc>@param2min and Isc<@param2max")
	elif param2=="Voc":
		data_selected=data_selected.query("Voc>@param2min and Voc<@param2max")
	elif param2=="Bn":
		data_selected=data_selected.query("Bn>@param2min and Bn<@param2max")
	elif param2=="Dh":
		data_selected=data_selected.query("Dh>@param2min and Dh<@param2max")
	elif param2=="Gn":
		data_selected=data_selected.query("Gn>@param2min and Gn<@param2max")
	elif param2=="TempAmb":
		data_selected=data_selected.query("TempAmb>@param2min and TempAmb<@param2max")
	elif param2=="TempMod":
		data_selected=data_selected.query("TempMod>@param2min and TempMod<@param2max")


	if param3=="Pmp":
		data_selected=data_selected.query("Pmp>@param3min and Pmp<@param3max")
	elif param3=="Vmp":
		data_selected=data_selected.query("Vmp>@param3min and Vmp<@param3max")
	elif param3=="Imp":
		data_selected=data_selected.query("Imp>@param3min and Imp<@param3max")
	elif param3=="Isc":
		data_selected=data_selected.query("Isc>@param3min and Isc<@param3max")
	elif param3=="Voc":
		data_selected=data_selected.query("Voc>@param3min and Voc<@param3max")
	elif param3=="Bn":
		data_selected=data_selected.query("Bn>@param3min and Bn<@param3max")
	elif param3=="Dh":
		data_selected=data_selected.query("Dh>@param3min and Dh<@param3max")
	elif param3=="Gn":
		data_selected=data_selected.query("Gn>@param3min and Gn<@param3max")
	elif param3=="TempAmb":
		data_selected=data_selected.query("TempAmb>@param3min and TempAmb<@param3max")
	elif param3=="TempMod":
		data_selected=data_selected.query("TempMod>@param3min and TempMod<@param3max")


	if param4=="Pmp":
		data_selected=data_selected.query("Pmp>@param4min and Pmp<@param4max")
	elif param4=="Vmp":
		data_selected=data_selected.query("Vmp>@param4min and Vmp<@param4max")
	elif param4=="Imp":
		data_selected=data_selected.query("Imp>@param4min and Imp<@param4max")
	elif param4=="Isc":
		data_selected=data_selected.query("Isc>@param4min and Isc<@param4max")
	elif param4=="Voc":
		data_selected=data_selected.query("Voc>@param4min and Voc<@param4max")
	elif param4=="Bn":
		data_selected=data_selected.query("Bn>@param4min and Bn<@param4max")
	elif param4=="Dh":
		data_selected=data_selected.query("Dh>@param4min and Dh<@param4max")
	elif param4=="Gn":
		data_selected=data_selected.query("Gn>@param4min and Gn<@param4max")
	elif param4=="TempAmb":
		data_selected=data_selected.query("TempAmb>@param4min and TempAmb<@param4max")
	elif param4=="TempMod":
		data_selected=data_selected.query("TempMod>@param4min and TempMod<@param4max")


	#Create excel writer object
	writer = pd.ExcelWriter('data_filtered.xlsx')

	#Write dataframe to excel
	data_selected.to_excel(writer)

	#Save the excel
	writer.save()