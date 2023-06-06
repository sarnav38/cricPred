import streamlit as st
import pandas as pd


def t20WinPred(model, data):
    col1, col2 = st.columns(2)
    with col1:
        team_batting = st.selectbox('Batting Team', sorted(data['t20_teams']))

    with col2:
        team_bowling = st.selectbox('Bowling Team', sorted(data['t20_teams']))

    city = st.selectbox('City', sorted(data['t20_city']))

    col3, col4, col5, col6 = st.columns(4)
    with col3:
        current_score = st.number_input('Current Score', min_value=0, step=1)
    with col4:
        balls = st.number_input('Balls', min_value=0.0, max_value=120.0, step=1.0)
    with col5:
        wickets = st.number_input('Wickets', min_value=0, max_value=10, step=1)
    with col6:
        target = st.number_input('Target', min_value=0, step=1)

    # team_batting	team_bowling	city	runs_left	ball_left	wicket_left	target	crr	rrr	Result
    if st.button('Predict Winner'):
        if team_batting is team_bowling:
            st.error('Team Batting and Team Bowling cannot be same', icon="⚠️")
        else:
            ball_left = 120 - balls
            wicket_left = 10 - wickets
            runs_left = target - current_score
            crr = (current_score * 6) / balls
            rrr = (runs_left * 6) / ball_left

            df = pd.DataFrame(columns=['team_batting', 'team_bowling', 'city', 'runs_left', 'ball_left', 'wicket_left',
                                         'target', 'crr', 'rrr'],
                                data=[[team_batting, team_bowling, city, runs_left,
                                       ball_left, wicket_left, target, crr, rrr]])
            result = model.predict_proba(df)
            result = result[0]
            # print(result)
            # st.write(f"Predicted Score is : {int(result)}")
            batting_prob = result[1]
            bowling_prob = result[0]
            st.subheader(f"{team_batting} Winning Probability : :blue[{round(batting_prob*100)} %]")
            st.subheader(f"{team_bowling} Winning Probability : :blue[{round(bowling_prob*100)} %]")
