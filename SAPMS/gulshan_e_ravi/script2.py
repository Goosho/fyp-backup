import pandas as pd
import calendar
import math

dataset = pd.read_csv("gulshan_e_ravi.csv")
dataset['Aqi_PM']=0
dataset['Aqi_CO']=0
dataset['Aqi_NOx']=0
dataset.insert(0, column = "year", value = 0)
dataset.insert(1, column = "month", value = 0)
dataset.insert(2, column = "day_num", value = 0)
dataset.insert(3, column = "day", value = 0)
dataset.insert(4, column = "hours", value = 0)
dataset.insert(5, column = "minutes", value = 0)
dataset.insert(6, column = "AM", value = 0)
dataset['Date'] =dataset['Date'].str.replace("-","")
#dataset['Time'] = dataset.Time.str.slice(0,5)
dataset['day_num']= dataset.Date.str.slice(6,8)
dataset['month'] = dataset.Date.str.slice(4,6)
dataset['year'] = dataset.Date.str.slice(0,4)

dataset['hours'] = dataset.Time.str.slice(0,2)
dataset['minutes'] = dataset.Time.str.slice(3,5)
dataset['AM'] = dataset.Time.str.slice(8,10)
dataset['PM2.5_prev_1'] = 0
dataset['PM2.5_prev_2'] = 0

dataset['CO_prev_1'] = 0
dataset['CO_prev_2'] = 0

dataset['NOx_prev_1'] = 0
dataset['NOx_prev_2'] = 0
x = float('NaN')
dataset['TimeStamp'] = 0

AQI_max = [50,100,150,200,300,500]
AQI_min = [0,51,101,151,201,301]
PM_max = [15.4,40.4,65.4,150.4,250.4,500.4]
PM_min = [0,15.5,40.5,65.5,150.5,250.5]

PM_obs = 0
value = 0
days =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]
for index,row in dataset.iterrows():

    a = dataset['day_num'][index]
    b =  dataset['month'][index]
    c = dataset['year'][index]
    dayNumber = calendar.weekday(int(c),int(b),int(a))
    dataset['day'][index] = days[dayNumber]

    if (dataset['AM'][index] == 'pm'):
	if  (int (dataset['hours'][index])) != 12:
            dataset['hours'][index] = int (dataset['hours'][index]) +12;

    else:
	if  (int (dataset['hours'][index])) == 12:
            dataset['hours'][index] = 0 ;

    if (dataset['AM'][index] == 'am'):
        dataset['AM'][index] = '1';
    else:
        dataset['AM'][index] = '0';

    if dataset['day'][index] == 'Monday':
        dataset['day'][index] = 1
    if dataset['day'][index] == 'Tuesday':
        dataset['day'][index] = 2
    if dataset['day'][index] == 'Wednesday':
        dataset['day'][index] = 3
    if dataset['day'][index] == 'Thursday':
        dataset['day'][index] = 4
    if dataset['day'][index] == 'Friday':
        dataset['day'][index] = 5
    if dataset['day'][index] == 'Saturday':
        dataset['day'][index] = 6
    if dataset['day'][index] == 'Sunday':
        dataset['day'][index] = 7

    if dataset['PM2.5'][index] >1000 :
        dataset['PM2.5'][index] = dataset['PM2.5'][index-1]

    if  math.isnan(dataset['Temperature'][index]) == True:
        dataset['Temperature'][index] = dataset['Temperature'][index-1];
        dataset['Humidity'][index] = dataset['Humidity'][index-1];


    if index <= 5 :
        dataset['Aqi_PM'][index] = dataset['PM2.5'][index]
    else :
	PM_obs = (dataset['PM2.5'][index-5] +dataset['PM2.5'][index-4] +dataset['PM2.5'][index-3] +dataset['PM2.5'][index-2] +dataset['PM2.5'][index-1] +dataset['PM2.5'][index-0])/6
        PM_obs = (PM_obs*0.856) + 1.16
        if PM_obs >=PM_min[0]  and PM_obs <= PM_max[0]:
            value  = 0
        if PM_obs >=PM_min[1]  and PM_obs <= PM_max[1]:
            value  = 1
        if PM_obs >=PM_min[2]  and PM_obs <= PM_max[2]:
            value  = 2
        if PM_obs >=PM_min[3]  and PM_obs <= PM_max[3]:
            value  = 3
        if PM_obs >=PM_min[4]  and PM_obs <= PM_max[4]:
            value  = 4
        if PM_obs >=PM_min[5]  and PM_obs <= PM_max[5]:
            value  = 5
        if PM_obs >= 500.5:
            value = 5

        value_1 = PM_obs - PM_min[value]
        value_2 = AQI_max[value] - AQI_min[value]
        value_3 = PM_max[value] - PM_min[value]
        dataset['Aqi_PM'][index] = ((value_1 * value_2)/value_3)+ AQI_min[value]
    dataset['TimeStamp'][index] = (int(dataset['month'][index])*43800) + (int(dataset['day_num'][index])*1440) + (int(dataset['hours'][index])*60)+  (int(dataset['minutes'][index] ))
    if index > 5:
        dataset['PM2.5_prev_1'][index] =  (dataset['PM2.5'][index-5] +dataset['PM2.5'][index-4] +dataset['PM2.5'][index-3] +dataset['PM2.5'][index-2] +dataset['PM2.5'][index-1] +dataset['PM2.5'][index-0])/6
        dataset['CO_prev_1'][index] = (dataset['CO'][index-5] +dataset['CO'][index-4] +dataset['CO'][index-3] +dataset['CO'][index-2] +dataset['CO'][index-1] +dataset['CO'][index-0])/6 
	dataset['NOx_prev_1'][index] = (dataset['NOx'][index-5] +dataset['NOx'][index-4] +dataset['NOx'][index-3] +dataset['NOx'][index-2] +dataset['NOx'][index-1] +dataset['NOx'][index-0])/6 
    else:
        dataset['PM2.5_prev_1'][index] =  dataset['PM2.5'][index]
	dataset['CO_prev_1'][index] =  dataset['CO'][index] 
	dataset['NOx_prev_1'][index] =  dataset['NOx'][index] 
    if index >11:
	dataset['CO_prev_2'][index] = (dataset['CO'][index-11] +dataset['CO'][index-10] +dataset['CO'][index-9] +dataset['CO'][index-8] +dataset['CO'][index-7] +dataset['CO'][index-6])/6 
        dataset['NOx_prev_2'][index] = (dataset['NOx'][index-11] +dataset['NOx'][index-10] +dataset['NOx'][index-9] +dataset['NOx'][index-8] +dataset['NOx'][index-7] +dataset['NOx'][index-6])/6 
	dataset['PM2.5_prev_2'][index] =  (dataset['PM2.5'][index-11] +dataset['PM2.5'][index-10] +dataset['PM2.5'][index-9] +dataset['PM2.5'][index-8] +dataset['PM2.5'][index-7] +dataset['PM2.5'][index-6])/6
    else:
	dataset['PM2.5_prev_2'][index] = dataset['PM2.5_prev_1'][index] 
	dataset['CO_prev_2'][index] = dataset['CO_prev_1'][index] 
        dataset['NOx_prev_2'][index] = dataset['NOx_prev_1'][index]


dataset.drop(['PM1', 'PM10','Date','Time','month','minutes'], axis='columns', inplace=True)

dataset.to_csv(r'AQI.csv', index = False)
#print(dataset)
