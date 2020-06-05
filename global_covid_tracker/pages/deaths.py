from app import st
from global_covid_tracker.dataframes import countries_deaths
from global_covid_tracker.plotting import plot_total_deaths, \
    plot_deaths_by_country
from global_covid_tracker.content import deaths_content


def deaths():
    st.subheader('Death Data')
    st.markdown(deaths_content.introduction)

    st.subheader(deaths_content.death_count_data)
    nations = st.multiselect('Countries', countries_deaths,
                             default=['United States'], key='deaths')
    per_million = st.radio(
        'How to view deaths?', ['Raw Count', 'Per Million'], key='deaths'
    ) == 'Per Million'
    plot_deaths = plot_total_deaths(nations, per_million)
    st.plotly_chart(plot_deaths)

    st.subheader(deaths_content.death_country_data)
    country = st.selectbox('Country', countries_deaths, key='deaths')
    plot_daily_deaths = plot_deaths_by_country(country)
    st.plotly_chart(plot_daily_deaths)
