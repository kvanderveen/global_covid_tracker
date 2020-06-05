from app import st
from global_covid_tracker.plotting import plot_cases_growth, plot_deaths_growth
from global_covid_tracker.content import growth_content


def growth():
    st.subheader('Growth Data')
    st.markdown(growth_content.introduction)

    st.subheader(growth_content.case_growth_data)
    by_percent_cases = st.radio('How to view data?',
                                ['by percent', 'absolute per million'],
                                key='by percent cases') == 'by percent'
    top_15_cases = st.radio('Top or bottom 15?', ['top 15', 'bottom 15'],
                            key='top 15 cases') == 'top 15'
    plot_growth_cases = plot_cases_growth(top_15_cases, by_percent_cases)
    st.plotly_chart(plot_growth_cases)

    st.subheader(growth_content.death_growth_data)
    by_percent_deaths = st.radio('How to view data?',
                                 ['by percent', 'absolute per million'],
                                 key='by percent deaths') == 'by percent'
    top_15_deaths = st.radio('Top or bottom 15?', ['top 15', 'bottom 15'],
                             key='top 15 deaths') == 'top 15'
    plot_growth_deaths = plot_deaths_growth(top_15_deaths, by_percent_deaths)
    st.plotly_chart(plot_growth_deaths)
