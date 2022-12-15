import requests
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title('Exploring ICT Data for Program Design')
st.write('Are you designing an educational program using information communication technologies (ICTs)?')
st.write('Use this data exploration tool to gain important insights on how students in your country of implementation access, use, and perceive ICTs.')
          


lottie_url = "https://assets8.lottiefiles.com/packages/lf20_mq11wjtp.json"
lottie_animation = load_lottieurl(lottie_url)
st_lottie(lottie_animation, key="animation", height=200)


st.header('Where in the world are you designing a program?')


#DATAFRAMES
availability = pd.read_csv('data/Available at home v2.csv')
use_during= pd.read_csv('data/ICT use during school v2.csv')
use_outside = pd.read_csv('data/ICT use outside of school v2.csv')
autonomy = pd.read_csv('data/Perceived ICT autonomy v2.csv')
competence = pd.read_csv('data/Perceived ICT competence v2.csv')

#select country
country = st.selectbox('', options=availability["Country"].unique())

#GO BUTTON
go_button = st.button("Let's go")

#Filter by country
mask = availability['Country']== country
availability = availability[mask]
mask = use_during['Country']== country
use_during = use_during[mask]
mask = use_outside['Country']== country
use_during = use_outside[mask]
mask = competence['Country']== country
competence = competence[mask]
mask = autonomy['Country']== country
autonomy = autonomy[mask]


if go_button:
    st.header(country)
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["ICT Availability at Home","Use During School", "Use Outside School","ICT Autonomy","ICT Competence"])
    with tab1:

        st.write('Several PISA measures reflect indices that summarize responses to questions asked on a scale. The below represents a composite score summarizing questions pertaining to ICT Availability at Home.')
        col1, col2 =st.columns(2)
        with col1:
            fig = px.bar(data_frame=availability.groupby(['Gender']).mean().reset_index(), x='Gender', y='Score by Gender', color='Gender', title='Gender',
                         labels={
                "Gender":"",
                "Score by Gender":"Score"})
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
            fig = px.bar(data_frame=availability.groupby(['Language']).mean().reset_index(), x='Language', y='Score by Language', color='Language', title="Language at Home",
                         labels={
                             "Language":"",
                             "Score by Language":"Score"
                         })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
        with col2:
            fig = px.bar(data_frame=availability.groupby(['Immigration Status']).mean().reset_index(), x='Immigration Status', y='Score by Immigration', color='Immigration Status', title='Immigration Status',
                         labels={
                             "Immigration Status":"",
                             "Score by Immigration":"Score"
                         })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
            fig = px.bar(data_frame=availability.groupby(['Internet: Y/N']).mean().reset_index(), x='Internet: Y/N', y='Score by Internet', color='Internet: Y/N', title='Internet at Home',
                         labels={
                             "Internet: Y/N": "",
                             "Score by Internet": "Score"
                         })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
    with tab2:
        st.write('Several PISA measures reflect indices that summarize responses to Likert-scale questions. The below represents a composite score summarizing questions pertaining to ICT Use During School.')
        col1, col2 =st.columns(2)
        with col1:
            fig = px.bar(data_frame=use_during.groupby(['Gender']).mean().reset_index(), x='Gender', y='Score by Gender', color='Gender', title='Gender',
                         labels={
                             "Gender":"",
                             "Score by Gender":"Score"
                         })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
            fig = px.bar(data_frame=use_during.groupby(['Language']).mean().reset_index(), x='Language', y='Score by Language', color='Language', title="Language at Home",
                         labels={
                             "Language":"",
                             "Score by Language":"Score"
                         })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
        with col2:
            fig = px.bar(data_frame=use_during.groupby(['Immigration Status']).mean().reset_index(), x='Immigration Status', y='Score by Immigration', color='Immigration Status', title='Immigration Status',
                         labels={
                             "Immigration Status":"",
                             "Score by Immigration":"Score"
                         })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
            fig = px.bar(data_frame=use_during.groupby(['Internet: Y/N']).mean().reset_index(), x='Internet: Y/N', y='Score by Internet', color='Internet: Y/N', title='Internet at Home',
                         labels={
                             "Internet: Y/N": "",
                             "Score by Internet": "Score"})
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)

    with tab3:
        st.write('Several PISA measures reflect indices that summarize responses to Likert-scale questions. The below represents a composite score summarizing questions pertaining to ICT Use Outside School.')
        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(data_frame=use_outside.groupby(['Gender']).mean().reset_index(), x='Gender', y='Score by Gender', color='Gender', title='Gender', labels={
                "Gender":"",
                "Score by Gender":"Score"})
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
            fig = px.bar(data_frame=use_outside.groupby(['Language']).mean().reset_index(), x='Language', y='Score by Language', color='Language', title="Language at Home",
                         labels={
                             "Language":"",
                             "Score by Language":"Score"
                         })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
        with col2:
            fig = px.bar(data_frame=use_outside.groupby(['Immigration Status']).mean().reset_index(), x='Immigration Status', y='Score by Immigration', color='Immigration Status', title='Immigration Status',
                         labels={
                             "Immigration Status":"",
                             "Score by Immigration":"Score"
                         })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
            fig = px.bar(data_frame=use_outside.groupby(['Internet: Y/N']).mean().reset_index(), x='Internet: Y/N', y='Score by Internet', color='Internet: Y/N', title='Internet at Home',
                         labels={
                             "Internet: Y/N": "",
                             "Score by Internet": "Score"})
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)

    with tab4:
        st.write('Several PISA measures reflect indices that summarize responses to Likert-scale questions. The below represents a composite score summarizing questions pertaining to ICT Autonomy.')
        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(data_frame=autonomy.groupby(['Gender']).mean().reset_index(), x='Gender', y='Score by Gender', color='Gender', title='Gender', labels={
                "Gender":"",
                "Score by Gender":"Score"})
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
            fig = px.bar(data_frame=autonomy.groupby(['Language']).mean().reset_index(), x='Language', y='Score by Language', color='Language', title='Language at Home',
                         labels={
                             "Language":"",
                             "Score by Language":"Score"
                         })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
        with col2:
            fig = px.bar(data_frame=autonomy.groupby(['Immigration Status']).mean().reset_index(), x='Immigration Status', y='Score by Immigration',
                                     color='Immigration Status', title='Immigration Status',
                         labels={
                             "Immigration Status":"",
                             "Score by Immigration":"Score"
                         })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
            fig = px.bar(data_frame=autonomy.groupby(['Internet: Y/N']).mean().reset_index(), x='Internet: Y/N', y='Score by Internet', color='Internet: Y/N', title='Internet at Home',
                         labels={
                             "Internet: Y/N": "",
                             "Score by Internet": "Score"})
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)


    #Use facets to -- px.bar(use_during, facet_col="Gender", use color to create


    with tab5:
        st.write('Several PISA measures reflect indices that summarize responses to Likert-scale questions. The below represents a composite score summarizing questions pertaining to ICT Competence.')
        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(data_frame=competence.groupby(['Gender']).mean().reset_index(), x='Gender', y='Score by Gender', color='Gender', title='Gender', labels={
                "Gender": "",
                "Score by Gender": "Score"})
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
            fig = px.bar(data_frame=competence.groupby(['Language']).mean().reset_index(), x='Language', y='Score by Language', color='Language',
            title='Language at Home',
            labels={
            "Language": "",
            "Score by Language": "Score"
                                 })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
        with col2:
            fig = px.bar(data_frame=competence.groupby(['Immigration Status']).mean().reset_index(), x='Immigration Status', y='Score by Immigration',
                                 color='Immigration Status', title='Immigration Status',
                                 labels={
                                     "Immigration Status": "",
                                     "Score by Immigration": "Score"
                                 })
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)
            fig = px.bar(data_frame=competence.groupby(['Internet: Y/N']).mean().reset_index(), x='Internet: Y/N', y='Score by Internet', color='Internet: Y/N',
                                 title='Internet at Home',
                                 labels={
                                     "Internet: Y/N": "",
                                     "Score by Internet": "Score"})
            fig.update_layout(width=350, height=400)
            st.plotly_chart(fig)

        #Sort the dropdown list
        #Add map