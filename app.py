import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
import re

st.sidebar.title("Whatsapp Chat Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")

    for i in range(10):
        if re.match(r'\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s[APap][Mm] - .*',(data.split("\n")[0])):
            df=preprocessor.preprocessy12(data)
            break
        elif re.match(r'\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}\s[APap][Mm] - .*',(data.split("\n")[0])):
            df=preprocessor.preprocessY12(data)
            break
        elif re.match('\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2} - .*',(data.split("\n")[0])):
            df=preprocessor.preprocessy24(data)
            break
        elif re.match('\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2} - .*',(data.split("\n")[0])):
            df=preprocessor.preprocessY24(data)
            break
    #df=preprocessor.preprocess(data)

    st.dataframe(df)

    user_list=df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user=st.sidebar.selectbox("Show analysis wrt",user_list)
    if st.sidebar.button("Show Analysis"):
        num_messages,words,media,links=helper.fetch_stats(selected_user,df)
        st.title("Top statistics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Total media")
            st.title(media)
        with col4:
            st.header("Links Shared")
            st.title(links)

        #monthly timeline
        st.header("Monthly Timeline")
        timeline=helper.monthly_timeline(selected_user,df)
        fig,ax=plt.subplots()
        ax.plot(timeline['time'],timeline['message'],color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #daily timeline
        st.header(" Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='red')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #activity map
        st.title("Activity Map")
        col1,col2=st.columns(2)
        with col1:
            st.header("Most Busy Day")
            busy_day=helper.week_activity_map(selected_user,df)
            fig,ax=plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.header("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='pink')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap=helper.activity_heatmap(selected_user,df)
        fig,ax=plt.subplots()
        ax=sns.heatmap(user_heatmap)
        st.pyplot(fig)

        if selected_user=='Overall':
            x,new_df=helper.busy_users(df)
            fig, ax=plt.subplots()
            col1,col2=st.columns(2)
            with col1:
                st.header("Most Busy Users")
                ax.bar(x.index, x.values,color='blue')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.header("Count")
                st.dataframe(new_df)
        #WordCloud
        st.header("WordCloud")
        df_wc=helper.create_worldcloud(selected_user,df)
        fig,ax=plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        #most common words
        st.header("Most Common Words")
        most_common_df=helper.common_words(selected_user,df)
        fig,ax=plt.subplots()
        ax.barh(most_common_df[0],most_common_df[1])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        
        #emoji analysis
        st.header("Most Used Emoji")
        emoji_df=helper.emoji_helper(selected_user,df)
        st.dataframe(emoji_df)
