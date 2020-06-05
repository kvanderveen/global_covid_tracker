from global_covid_tracker.dataframes import pd, main_dataframe


def format_number(number: [int, float]) -> str:
    return f'{int(number):,}'


def deaths_dataframe(country: str) -> pd.DataFrame:
    mask = (
        (main_dataframe.location == country)
        & (main_dataframe['total_deaths'] > 0)
    )
    columns = ['date', 'total_deaths', 'new_deaths', 'total_deaths_per_million',
               'new_deaths_per_million']
    deaths = main_dataframe.loc[mask, columns].set_index('date').dropna()
    deaths['new_deaths_7d_rolling_mean'] = deaths['new_deaths'].rolling(
        '7d').mean().round(1)
    deaths['text_total_deaths'] = (
            f'Country: {country} <br>' +
            'Date: ' + deaths.index.strftime('%B %d, %Y') + '<br>' +
            'Total Deaths: ' + deaths['total_deaths'].apply(format_number) + '<br>' +
            'Total Deaths per Million: ' + deaths['total_deaths_per_million'].apply(format_number) + '<br>'
    )
    deaths['text_new_deaths'] = (
            f'Country {country} <br>' +
            'Date: ' + deaths.index.strftime('%B %d, %Y') + '<br>' +
            'New Deaths: ' + deaths['new_deaths'].apply(format_number) + '<br>' +
            'New Deaths per Million: ' + deaths[
                'new_deaths_per_million'].round(1).astype(str)
    )
    deaths['text_new_deaths_7d_rolling_mean'] = (
        f'Country: {country} <br>' +
        'Date: ' + deaths.index.strftime('%B %d, %Y') + '<br>' +
        'New Deaths (7 day mean): ' + deaths['new_deaths_7d_rolling_mean'].astype(str)
    )
    return deaths
