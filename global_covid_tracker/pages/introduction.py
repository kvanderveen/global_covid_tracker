from app import st
from global_covid_tracker.site_components.introduction_data import \
    introduction_data
from global_covid_tracker.content import introduction_content


def introduction():
    st.subheader('Introduction')
    st.markdown(introduction_content.opening_content1)
    st.markdown(introduction_content.opening_content2)

    st.subheader(introduction_content.cases_content)
    cases_per_million = st.checkbox('View Cases per Million')
    if cases_per_million:
        st.table(introduction_data.top_10_cases_per_million)
    else:
        st.table(introduction_data.top_10_cases)

    st.subheader(introduction_content.deaths_content)
    deaths_per_million = st.checkbox('View Deaths per Million')
    if deaths_per_million:
        st.table(introduction_data.top_10_deaths_per_million)
    else:
        st.table(introduction_data.top_10_deaths)
