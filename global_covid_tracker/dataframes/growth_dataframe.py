from global_covid_tracker.dataframes import main_dataframe, pd
from datetime import timedelta


def number_formater(number: [int, float]):
    return f'{round(number, 1):,}'


def create_growth_dataframe() -> pd.DataFrame:
    today = main_dataframe['date'].max()
    last_week = today - timedelta(days=7)
    columns = ['location', 'total_deaths', 'total_deaths_per_million',
               'total_cases', 'total_cases_per_million']
    today_df = main_dataframe.loc[
        main_dataframe['date'] == today, columns].set_index('location')
    last_week_df = main_dataframe.loc[
        main_dataframe['date'] == last_week, columns].set_index('location')
    df = today_df.merge(last_week_df, left_index=True, right_index=True,
                        suffixes=['_today', '_last_week']).dropna()
    df['absolute_deaths_increase'] = (
        df['total_deaths_today']
        .sub(df['total_deaths_last_week'])
    )
    df['absolute_deaths_increase_per_million'] = (
        df['total_deaths_per_million_today']
        .sub(df['total_deaths_per_million_last_week'])
    )
    df['pct_deaths_increase'] = (
        df['total_deaths_today']
        .sub(df['total_deaths_last_week'])
        .div(df['total_deaths_last_week'])
        .mul(100).round(1)
    )
    df['absolute_cases_increase'] = (
        df['total_cases_today']
        .sub(df['total_cases_last_week'])
    )
    df['absolute_cases_increase_per_million'] = (
        df['total_cases_per_million_today']
        .sub(df['total_cases_per_million_last_week'])
    )
    df['pct_cases_increase'] = (
        df['total_cases_today']
        .sub(df['total_cases_last_week'])
        .div(df['total_cases_last_week'])
        .mul(100).round(1)
    )
    df = df[((df['total_cases_last_week'] > 100) &
            (df['total_deaths_last_week'] > 100) &
            (df.index != 'World'))]
    df['text_pct_deaths_increase'] = (
        'Country: ' + df.index + '<br>' +
        'Percent Increase in Past Week: ' + df['pct_deaths_increase'].astype(str) + '%<br>' +
        'Absolute Increase in Past Week: ' + df['absolute_deaths_increase'].apply(number_formater) + '<br>' +
        'Latest Total Deaths: ' + df['total_deaths_today'].apply(number_formater) + '<br>' +
        'Total Deaths Last Week: ' + df['total_deaths_last_week'].apply(number_formater)
    )
    df['text_absolute_deaths_increase_per_million'] = (
            'Country: ' + df.index + '<br>' +
            'Increase in Deaths per Million: ' + df['absolute_deaths_increase_per_million'].apply(number_formater) + '<br>' +
            'Latest Deaths per Million: ' + df['total_deaths_per_million_today'].apply(number_formater) + '<br>' +
            'Deaths per Million Last Week: ' + df['total_deaths_per_million_last_week'].apply(number_formater)

    )
    df['text_absolute_cases_increase_per_million'] = (
        'Country: ' + df.index + '<br>' +
        'Increase in Cases per Million: ' + df['absolute_cases_increase_per_million'].apply(number_formater) + '<br>' +
        'Latest Cases per Million: ' + df['total_cases_per_million_today'].apply(number_formater) + '<br>' +
        'Cases per Million Last Week: ' + df['total_cases_per_million_last_week'].apply(number_formater)

    )
    df['text_pct_cases_increase'] = (
        'Country: ' + df.index + '<br>' +
        'Percent Increase in Past Week: ' + df['pct_cases_increase'].astype(str) + '%<br>' +
        'Absolute Increase in Past Week: ' + df['absolute_cases_increase'].apply(number_formater) + '<br>' +
        'Latest Total Cases: ' + df['total_cases_today'].apply(number_formater) + '<br>'
        'Total Cases Last Week: ' + df['total_cases_last_week'].apply(number_formater)
    )
    return df


growth_dataframe = create_growth_dataframe()
