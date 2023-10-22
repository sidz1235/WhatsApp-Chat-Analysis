import re
import pandas as pd


def preprocessy12(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s[APap][Mm]\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern,data)
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')
    df.rename(columns={'message_date': 'date'}, inplace=True)
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)
    df['day_name']=df['date'].dt.day_name()
    df['only_date']=df['date'].dt.date
    df['YEAR'] = df['date'].dt.year
    df['month_num']=df['date'].dt.month
    df['MONTH'] = df['date'].dt.month_name()
    df['DAY'] = df['date'].dt.day
    df['HOUR'] = df['date'].dt.hour
    df['MINUTE'] = df['date'].dt.minute

    period=[]
    for hour in df[['day_name','HOUR']]['HOUR']:
        if hour==23:
            period.append(str(hour)+"-"+str('00'))
        elif hour==0:
            period.append(str(hour)+"-"+str(hour+1))
        else:
            period.append(str(hour)+"-"+str(hour+1))
    df['period']=period

    return df

def preprocessy24(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern,data)
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M - ', )
    df.rename(columns={'message_date': 'date'}, inplace=True)
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)
    df['day_name']=df['date'].dt.day_name()
    df['only_date']=df['date'].dt.date
    df['YEAR'] = df['date'].dt.year
    df['month_num']=df['date'].dt.month
    df['MONTH'] = df['date'].dt.month_name()
    df['DAY'] = df['date'].dt.day
    df['HOUR'] = df['date'].dt.hour
    df['MINUTE'] = df['date'].dt.minute

    period=[]
    for hour in df[['day_name','HOUR']]['HOUR']:
        if hour==23:
            period.append(str(hour)+"-"+str('00'))
        elif hour==0:
            period.append(str(hour)+"-"+str(hour+1))
        else:
            period.append(str(hour)+"-"+str(hour+1))
    df['period']=period

    return df

def preprocessY24(data):
    pattern = '\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern,data)
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ', )
    df.rename(columns={'message_date': 'date'}, inplace=True)
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)
    df['day_name']=df['date'].dt.day_name()
    df['only_date']=df['date'].dt.date
    df['YEAR'] = df['date'].dt.year
    df['month_num']=df['date'].dt.month
    df['MONTH'] = df['date'].dt.month_name()
    df['DAY'] = df['date'].dt.day
    df['HOUR'] = df['date'].dt.hour
    df['MINUTE'] = df['date'].dt.minute

    period=[]
    for hour in df[['day_name','HOUR']]['HOUR']:
        if hour==23:
            period.append(str(hour)+"-"+str('00'))
        elif hour==0:
            period.append(str(hour)+"-"+str(hour+1))
        else:
            period.append(str(hour)+"-"+str(hour+1))
    df['period']=period

    return df



def preprocessY12(data):
    

    pattern = r'\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}\s[APap][Mm]\s-\s'


    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %I:%M %p - ')
    df.rename(columns={'message_date': 'date'}, inplace=True)
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)
    df['day_name'] = df['date'].dt.day_name()
    df['only_date'] = df['date'].dt.date
    df['YEAR'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['MONTH'] = df['date'].dt.month_name()
    df['DAY'] = df['date'].dt.day
    df['HOUR'] = df['date'].dt.hour
    df['MINUTE'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'HOUR']]['HOUR']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str(hour) + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))
    df['period'] = period

    return df

'''
def preprocess(data):
    if re.match(r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s[APap][Mm]\s-\s',(data.split("\n")[0])):
        return preprocessy12(data)
    elif re.match(r'\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}\s[APap][Mm]\s-\s',(data.split("\n")[0])):
        return preprocessY12(data)
    elif re.match('\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s-\s',(data.split("\n")[0])):
        return preprocessy24(data)
    elif re.match('\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}\s-\s',(data.split("\n")[0])):
        return preprocessY24(data)
'''
