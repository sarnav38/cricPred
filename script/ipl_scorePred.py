import streamlit as st
import pandas as pd


def iplScorePred(model, data):
    col1, col2 = st.columns(2)

    with col1:
        team_batting = st.selectbox('Batting Team', sorted(data['ipl_teams']))

    with col2:
        team_bowling = st.selectbox('Bowling Team', sorted(data['ipl_teams']))

    city = st.selectbox('City', sorted(data['ipl_city']))

    col3, col4, col5, col6 = st.columns(4)

    with col3:
        current_score = st.number_input('Current Score', min_value=0, step=1)
    with col4:
        balls = st.number_input('Balls above 30', min_value=30, max_value=120, step=1)
    with col5:
        wickets = st.number_input('Wickets', min_value=0, max_value=10, step=1)

    with col6:
        last_five = st.number_input('Last Five Over Runs', min_value=0.0, step=1.0)

    if st.button('Predict Score'):
        if team_batting is team_bowling:
            st.error('Team Batting and Team Bowling cannot be same', icon="⚠️")
        else:
            ball_left = 120 - balls
            wicket_left = 10 - wickets
            crr = (current_score * 6) / balls
            df = pd.DataFrame(columns=['team_batting', 'team_bowling', 'current_score', 'wicket_left', 'crr',
                                         'city', 'balls_left', 'Rlast_fiveO'],
                                data=[[team_batting, team_bowling, current_score, wicket_left,
                                       crr, city, ball_left, last_five]])
            result = model.predict(df)
            result = result[0]
            st.subheader(f"{team_batting} Predicted Score : :blue[{int(result)}]")
