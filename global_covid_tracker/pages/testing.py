from app import st
from global_covid_tracker.plotting import plot_positive_test_rates, \
    plot_total_tests
from global_covid_tracker.dataframes import countries_testing
from global_covid_tracker.content import testing_content


def testing():
    st.subheader('Testing Data')
    st.markdown(testing_content.introduction)

    st.subheader(testing_content.testing_rate_data)
    nations_rates = st.multiselect('Countries', countries_testing,
                                   default=['United States'], key='rates')
    cumulative = st.radio(
        'Cumulative or daily (7 day average)?',
        ['Cumulative', 'Daily'], key='cumulative'
    ) == 'Cumulative'
    plot_rates = plot_positive_test_rates(nations_rates, cumulative)
    st.plotly_chart(plot_rates)

    st.subheader(testing_content.testing_volume_data)
    nations_tests = st.multiselect('Countries', countries_testing,
                                   default=['United States'], key='tests')
    per_1000 = st.radio(
        'Raw tests or tests per 1000?',
        ['Raw Tests', 'Tests per 1000'], key='raw'
    ) == 'Tests per 1000'
    plot_tests = plot_total_tests(nations_tests, per_1000)
    st.plotly_chart(plot_tests)
