import streamlit as st
import json
import pickle
from PIL import Image
from script import ipl_scorePred, ipl_winPred, t20_scorePred, t20_winPred

img = Image.open('./favicon_io/favicon.ico')
er = Image.open('./favicon_io/error.ico')

st.set_page_config(
    page_title="CricPred",
    page_icon=img,
    layout="centered",
    initial_sidebar_state="collapsed"
)

with open('css/style.css') as f:
    d = f.read()
st.markdown(f'<style>{d}</style>', unsafe_allow_html=True)
# st.markdown(f'<link rel="icon" type="image/png" sizes="32x32" href="./favicon_io/favicon-32x32.png">',
#             unsafe_allow_html=True)

models = ['IPL 1st Innings Prediction', 'IPL Win Probability Prediction',
         'T20 1st Innings Prediction', 'T20 Win Probability Prediction']

with open('./script/data.json') as f:
        data = json.load(f)
IPL_1st_Inn_ModelPred = pickle.load(open('./Models/IPL_1st_Inn_ModelPred.pkl', 'rb'))
IPL_WinProb_ModelPred = pickle.load(open('./Models/IPL_WinProb_ModelPred.pkl', 'rb'))
T20_1st_Inn_ModelPred = pickle.load(open('./Models/T20_1st_Inn_ModelPred.pkl', 'rb'))
T20_WinProb_ModelPred = pickle.load(open('./Models/T20_WinProb_ModelPred.pkl', 'rb'))

st.title('Select Cricket Predation Model')
modelSelected = st.selectbox("", models)

if modelSelected == models[0]:
    st.title(models[0])
    ipl_scorePred.iplScorePred(IPL_1st_Inn_ModelPred, data)

if modelSelected == models[1]:
    st.title(models[1])
    ipl_winPred.iplWinPred(IPL_WinProb_ModelPred, data)

if modelSelected == models[2]:
    st.title(models[2])
    t20_scorePred.t20ScorePred(T20_1st_Inn_ModelPred, data)

if modelSelected == models[3]:
    st.title(models[3])
    t20_winPred.t20WinPred(T20_WinProb_ModelPred, data)
