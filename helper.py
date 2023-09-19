from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import unicodedata

extract=URLExtract()
def fetch_stats(selected_user,df):
    if selected_user=='Overall':
        num_messages=df.shape[0]
        words = []
        for message in df['message']:
            words.extend(message.split())
        num_media = df[df['message'] == '<Media omitted>\n'].shape[0]
        links = []
        for message in df['message']:
            links.extend(extract.find_urls(message))
        return num_messages, len(words), num_media,len(links)
    else:
        n_df=df[df['user']==selected_user]
        num_messages=n_df.shape[0]
        words = []
        for message in n_df['message']:
            words.extend(message.split())
        num_media=n_df[n_df['message']=='<Media omitted>\n'].shape[0]
        links=[]
        for message in n_df['message']:
            links.extend(extract.find_urls(message))
        return num_messages,len(words),num_media,len(links)
def busy_users(df):
    x= df['user'].value_counts().head()
    df=round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x,df
def create_worldcloud(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
        
    # Exclude common words
    common_words = ['message', 'deleted']  # Add more common words if needed
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    words = []
    
    for message in temp['message']:
        for word in message.lower().split():
            if word not in common_words:  # Exclude common words
                words.append(word)
                
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(" ".join(words))
    
    return df_wc

def common_words(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
        
    common_words = ['message', 'deleted']  # Add more common words if needed
    
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    words = []
    
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words and word not in common_words:  # Exclude stop words and common words
                words.append(word)
                
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    emojis = []

    for message in df['message']:
        emojis_in_message = [c for c in message if unicodedata.category(c) == 'So']
        emojis.extend(emojis_in_message)

    emoji_counter = Counter(emojis)
    emoji_df = pd.DataFrame(emoji_counter.most_common(), columns=['Emoji', 'Count'])

    return emoji_df

def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    timeline=df.groupby(['YEAR','month_num','MONTH']).count()['message'].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['MONTH'][i]+"-"+str(timeline['YEAR'][i]))
    timeline['time']=time
    return timeline
def daily_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    daily_timeline=df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline
def week_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['day_name'].value_counts()
def month_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    return df['MONTH'].value_counts()
def activity_heatmap(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    user_heatmap=df.pivot_table(index='day_name',columns='period',values='message',aggfunc='count').fillna(0)
    return user_heatmap
