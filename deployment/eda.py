import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():

    st.title('Online Course Completion Prediction')

    st.subheader('Exploratory Data Analysis')

     #menambahkan deskripsi
    st.write('''PT. Ruangkelas merupakan perusahaan di bidang pendidikan digital. Salah satu program yang ditawarkannya ialah menyediakan kelas online dengan cakupan topik cukup luas, yaitu di bidang kesehatan, seni, sains, programming, dan bisnis. PT. Ruangkelas menyadari bahwa completion rates dari tiap materi / course berhubungan dengan kepuasan user dan berpengaruh kepada retention rates.
                Untuk itu, penting bagi perusahaan untuk memprediksi murid yang memiliki resiko gagal menyelesaikan materi (non-completers). Identifikasi murid yang beresiko besar tidak menyelesaikan materi penting supaya murid dapat mendapatkan bimbingan / support tambahan sejak dini.  Model prediksi yang diharapkan ialah model yang dapat dengan baik mengidentifikasi true non-completers, dan juga memiliki presisi yang baik supaya bantuan berupa bimbingan tambahan menjadi tepat sasaran.
             ''')
    
    #mmebuat batas dengan garis lurus
    st.markdown('---')
    
    #show dataframe
    st.write('## Data frame')
    data = pd.read_csv('online_course_engagement_data.csv')
    st.dataframe(data)

    #membuat pie chart
    st.write('#### Course completion status')
    labels = ['Not completed', 'Completed']
    size = data['CourseCompletion'].value_counts()
    colors = ['green', 'orange']
    explode = [0.1, 0]

    fig = plt.figure(figsize=(10,5))
    plt.pie(size, colors = colors, explode = explode,
        labels = labels, shadow = True, startangle = 90, autopct = '%.2f%%')
    plt.legend()
    st.pyplot(fig)

    st.write('Berdasarkan dataset, terdapat lebih banyak orang yang tidak menyelesaikan kursus (56.05%) dibanding yang menyelesaikan kursus (43.92%).')


    #melihat distribusi data
    st.write('#### Data distribution')
    fig = plt.figure(figsize=(20,40))
    for i, col in enumerate(data.columns):
        ax = plt.subplot(7, 3, i+1)
        sns.histplot(data[col], kde=True, ax=ax)
        plt.xlabel(col)
    st.pyplot(fig)

    st.write('Distribusi data tiap feature terlihat normal. Hal yang sama juga teramati pada data kategorik, yaitu course category, dimana jumlah orang pada masing-masing kategori hampir seimbang.')

    #melihat korelasi antar feature

    st.write('#### Correlation between features')
    mask = np.triu(np.ones_like(data.select_dtypes(exclude='object').corr(), dtype=bool))
    fig = fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(data.select_dtypes(exclude='object').corr(), annot=True, mask=mask)
    st.pyplot(fig)

    st.write('Korelasi antar features teramati sangat rendah atau hampir tidak berkorelasi. Sedangkan, korelasi antara feature dengan target (Course Completion), terlihat lebih tinggi, walaupun masih tergolong rendah.')

    #melihat trend pada non-completers dan completers
    st.write('#### Trends between completers and non-completers')
    i = 1
    fig = plt.figure(figsize=(25, 90))

    features = data[['TimeSpentOnCourse', 'NumberOfVideosWatched', 'NumberOfQuizzesTaken', 'QuizScores', 'CompletionRate']]

    for col in features:
        plt.subplot(11, 2, i)
        sns.kdeplot(data=data, hue="CourseCompletion", x=col, fill=True)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.xlabel(col, fontsize=20)
        plt.ylabel("Count", fontsize=20)
        i = i + 1
    
        plt.subplot(11, 2, i)
        sns.boxplot(x="CourseCompletion", y=col, data=data)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.xlabel("CourseCompletion", fontsize=20)
        plt.ylabel(col, fontsize=20)
        i = i + 1

    st.pyplot(fig)

if __name__ == '__main__':
    run()