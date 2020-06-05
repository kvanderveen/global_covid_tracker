import pandas as pd

url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'


def create_main_dataframe():
    df = pd.read_csv(url, parse_dates=['date'])
    df['positive_rate_cumulative'] = (
        df['total_cases']
        .div(df['total_tests'])
        .mul(100).round(1)
    )
    df['positive_rate_daily'] = (
        df['new_cases']
        .div(df['new_tests'])
        .mul(100).round(1)
    )
    return df


main_dataframe = create_main_dataframe()

countries_testing = sorted(
    main_dataframe
    .loc[(
        (main_dataframe['positive_rate_cumulative'].notna()) &
        (main_dataframe['positive_rate_daily'].notna())
     ), 'location']
    .unique()
)

countries_cases = sorted(
    main_dataframe
    .loc[(
        (main_dataframe['total_cases'].notna()) &
        (main_dataframe['new_cases'].notna()) &
        (main_dataframe['total_cases_per_million'].notna()) &
        (main_dataframe['new_cases_per_million'].notna())
    ), 'location']
    .unique()
)

countries_deaths = sorted(
    main_dataframe
    .loc[(
        (main_dataframe['total_deaths'].notna()) &
        (main_dataframe['new_deaths'].notna()) &
        (main_dataframe['total_deaths_per_million'].notna()) &
        (main_dataframe['new_deaths_per_million'].notna())
    ), 'location']
    .unique()
)
