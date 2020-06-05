from global_covid_tracker.dataframes import pd, main_dataframe


def format_number(number: [int, float]) -> str:
    return f'{int(number):,}'


def cases_dataframe(country: str) -> pd.DataFrame:
    mask = (
        (main_dataframe.location == country)
        & (main_dataframe['total_cases'] > 0)
    )
    columns = ['date', 'total_cases', 'new_cases', 'total_cases_per_million',
               'new_cases_per_million']
    cases = main_dataframe.loc[mask, columns].set_index('date').dropna()
    cases['new_cases_7d_rolling_mean'] = cases['new_cases'].rolling(
        '7d').mean().round(1)
    cases['text_total_cases'] = (
            f'Country: {country} <br>' +
            'Date: ' + cases.index.strftime('%B %d, %Y') + '<br>' +
            'Total Cases: ' + cases['total_cases'].apply(format_number) + '<br>' +
            'Total Cases per Million: ' + cases['total_cases_per_million'].apply(format_number) + '<br>'
    )
    cases['text_new_cases'] = (
            f'Country {country} <br>' +
            'Date: ' + cases.index.strftime('%B %d, %Y') + '<br>' +
            'New Cases: ' + cases['new_cases'].apply(format_number) + '<br>' +
            'New Cases per Million: ' + cases['new_cases_per_million'].round(1).astype(str)
    )
    cases['text_new_cases_7d_rolling_mean'] = (
        f'Country: {country} <br>' +
        'Date: ' + cases.index.strftime('%B %d, %Y') + '<br>' +
        'New Cases (7 day mean): ' + cases['new_cases_7d_rolling_mean'].astype(str)
    )
    return cases
