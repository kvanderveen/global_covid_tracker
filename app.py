import streamlit as st
from global_covid_tracker.site_components import page_header
from global_covid_tracker.pages import introduction, testing, cases, deaths, growth


def main():
    page_header()
    st.sidebar.subheader('Global COVID Tracker')
    view = st.sidebar.radio('Which data would you like to explore?',
                            ['Introduction', 'Testing Data', 'Case Data',
                             'Death Data', 'Growth Data'])
    if view == 'Introduction':
        introduction()
    elif view == 'Testing Data':
        testing()
    elif view == 'Case Data':
        cases()
    elif view == 'Death Data':
        deaths()
    else:
        growth()


if __name__ == '__main__':
    main()
