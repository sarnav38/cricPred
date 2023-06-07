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

models = ['IPL 1st Innings Prediction', 'IPL Win Probability Prediction',
         'T20 1st Innings Prediction', 'T20 Win Probability Prediction']

with open('./script/data.json') as f:
        data = json.load(f)


st.title('Select Cricket Predation Model')
modelSelected = st.selectbox("", models)

if modelSelected == models[0]:
    st.title(models[0])
    with open ('./Models/IPL_1st_Inn_ModelPred.pkl', 'rb') as f:
        IPL_1st_Inn_ModelPred = pickle.load(f)
    #IPL_1st_Inn_ModelPred = pickle.load(open('./Models/IPL_1st_Inn_ModelPred.pkl', 'rb'))
    ipl_scorePred.iplScorePred(IPL_1st_Inn_ModelPred, data)

if modelSelected == models[1]:
    st.title(models[1])
    with open ('./Models/IPL_WinProb_ModelPred.pkl', 'rb') as f:
        IPL_WinProb_ModelPred = pickle.load(f)
    #IPL_WinProb_ModelPred = pickle.load(open('./Models/IPL_WinProb_ModelPred.pkl', 'rb'))
    ipl_winPred.iplWinPred(IPL_WinProb_ModelPred, data)

if modelSelected == models[2]:
    st.title(models[2])
    with open ('./Models/T20_1st_Inn_ModelPred.pkl', 'rb') as f:
        T20_1st_Inn_ModelPred = pickle.load(f)
    #T20_1st_Inn_ModelPred = pickle.load(open('./Models/T20_1st_Inn_ModelPred.pkl', 'rb'))
    t20_scorePred.t20ScorePred(T20_1st_Inn_ModelPred, data)

if modelSelected == models[3]:
    st.title(models[3])
    with open ('./Models/T20_WinProb_ModelPred.pkl', 'rb') as f:
        T20_WinProb_ModelPred = pickle.load(f)
    #T20_WinProb_ModelPred = pickle.load(open('./Models/T20_WinProb_ModelPred.pkl', 'rb'))
    t20_winPred.t20WinPred(T20_WinProb_ModelPred, data)
