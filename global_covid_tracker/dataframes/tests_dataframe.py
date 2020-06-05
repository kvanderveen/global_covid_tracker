from global_covid_tracker.dataframes.main_dataframe import main_dataframe, pd


def format_number(number: [float, int]) -> str:
    return f'{int(number):,}'


def tests_dataframe(country: str) -> pd.DataFrame:
    mask = main_dataframe.location == country
    columns = ['date', 'positive_rate_cumulative', 'positive_rate_daily',
               'total_cases', 'total_tests', 'total_cases_per_million',
               'new_cases', 'new_tests_smoothed', 'new_tests',
               'new_tests_smoothed_per_thousand']
    positive_tests = main_dataframe.loc[mask, columns].set_index('date').dropna()
    positive_tests['positive_rate_daily'] = positive_tests[
        'positive_rate_daily'].rolling('7d').mean().round(1)
    positive_tests['text_positive_rate_cumulative'] = (
            f'Country: {country} <br>' +
            'Date: ' + positive_tests.index.strftime('%B %d, %Y') + '<br>' +
            'Positive Test Rate: ' + positive_tests['positive_rate_cumulative'].astype(str) + '%<br>' +
            'Total Positives: ' + positive_tests['total_cases'].apply(format_number) + '<br>' +
            'Total Tests: ' + positive_tests['total_tests'].apply(format_number)
    )
    positive_tests['text_positive_rate_daily'] = (
            f'Country: {country} <br>' +
            'Date: ' + positive_tests.index.strftime('%B %d, %Y') + '<br>' +
            'Positive Test Rate: ' + positive_tests['positive_rate_daily'].astype(str) + '%<br>' +
            'Daily Positives: ' + positive_tests['new_cases'].apply(format_number) + '<br>' +
            'Daily Tests: ' + positive_tests['new_tests'].apply(format_number)
    )
    positive_tests['text_new_tests'] = (
            f'Country {country} <br>' +
            'Date: ' + positive_tests.index.strftime('%B %d, %Y') + '<br>' +
            'Daily Tests: ' + positive_tests['new_tests_smoothed'].apply(format_number) + '<br>' +
            'New Tests per 1000: ' + positive_tests['new_tests_smoothed_per_thousand'].round(2).astype(str)
    )
    return positive_tests
