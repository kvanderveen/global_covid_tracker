from app import st
from global_covid_tracker.dataframes import countries_cases
from global_covid_tracker.plotting import plot_total_cases, \
    plot_cases_by_country
from global_covid_tracker.content import cases_content


def cases():
    st.subheader('Case Data')
    st.markdown(cases_content.introduction)

    st.subheader(cases_content.case_count_data)
    nations = st.multiselect('Countries', countries_cases,
                             default=['United States'], key='cases')
    per_million = st.radio(
        'How to view cases?', ['Raw Count', 'Per Million'], key='cases'
    ) == 'Per Million'
    plot_cases = plot_total_cases(nations, per_million)
    st.plotly_chart(plot_cases)

    st.subheader(cases_content.case_country_data)
    country = st.selectbox('Country', countries_cases, key='cases')
    plot_daily_cases = plot_cases_by_country(country)
    st.plotly_chart(plot_daily_cases)
