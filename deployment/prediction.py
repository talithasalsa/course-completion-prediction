import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

#Load All files
#Load model

def run():
    
    st.title('Online Course Completion Prediction')

    with open('best_estimator_rf.pkl', 'rb') as file_1:
      best_estimator_rf = pickle.load(file_1)

    with st.form('course_completion_status'):
       UserID = st.number_input('User ID', value= 0)
       CourseCategory = st.selectbox('Course category',('Programming', 'Health', 'Science', 'Arts', 'Business'), index=1)
       TimeSpentOnCourse = st.slider('Hours spent on course', value= 40, min_value=0, max_value=100)
       NumberOfVideosWatched = st.number_input('Number of videos watched', value= 12)
       NumberOfQuizzesTaken = st.number_input('Number of quizzes taken', value= 10)
       QuizScores = st.number_input('Quiz scores', value= 80)
       CompletionRate = st.slider('Completion rate', value= 10, min_value=0, max_value=100)
       DeviceType = st.radio('Device type', ('0','1'), index=1, help = '0 = dekstop, 1 = mobile')

       #bikin submit button form
       submitted = st.form_submit_button('Predict')

    data_inf = {
    'UserID' : UserID,
    'CourseCategory': CourseCategory,
    'TimeSpentOnCourse' : TimeSpentOnCourse,
    'NumberOfVideosWatched' : NumberOfVideosWatched,
    'NumberOfQuizzesTaken' : NumberOfQuizzesTaken,
    'QuizScores' : QuizScores,
    'CompletionRate': CompletionRate,
    'DeviceType': DeviceType

}
    
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:

        y_pred_inf = best_estimator_rf.predict(data_inf)

        st.write('## Completion status : ', str(int(y_pred_inf)))

if __name__ == '__main__':
   run()