from global_covid_tracker.dataframes import main_dataframe


def get_top_10_cases():
    mask = main_dataframe['location'] != 'World'
    top_10_cases = (
        main_dataframe.loc[mask]
        .groupby('location')[['total_cases']].max()
        .sort_values(by='total_cases', ascending=False)
    )
    top_10_cases['rank'] = range(1, len(top_10_cases) + 1)
    top_10_cases = (
        top_10_cases.reset_index()
        .set_index('rank').iloc[:10, :]
    )
    top_10_cases['total_cases'] = (
        top_10_cases['total_cases']
        .apply(lambda x: f'{x:,}')
    )
    top_10_cases.columns = ['Country', 'Total Cases']
    return top_10_cases


def get_top_10_cases_per_million():
    mask = main_dataframe['location'] != 'World'
    top_10_cases_per_million = (
        main_dataframe.loc[mask]
        .groupby('location')[['total_cases_per_million']].max()
        .sort_values(by='total_cases_per_million', ascending=False)
    )
    top_10_cases_per_million['rank'] = range(
        1, len(top_10_cases_per_million) + 1)
    top_10_cases_per_million = (
        top_10_cases_per_million
        .reset_index()
        .set_index('rank').iloc[:10, :]
    )
    top_10_cases_per_million['total_cases_per_million'] = (
        top_10_cases_per_million['total_cases_per_million']
        .apply(lambda x: f'{round(x):,}')
    )
    top_10_cases_per_million.columns = ['Country', 'Total Cases per Million']
    return top_10_cases_per_million


def get_top_10_deaths():
    mask = main_dataframe['location'] != 'World'
    top_10_deaths = (
        main_dataframe.loc[mask]
        .groupby('location')[['total_deaths']].max()
        .sort_values(by='total_deaths', ascending=False)
    )
    top_10_deaths['rank'] = range(1, len(top_10_deaths) + 1)
    top_10_deaths = top_10_deaths.reset_index().set_index('rank').iloc[:10, :]
    top_10_deaths['total_deaths'] = (
        top_10_deaths['total_deaths']
        .apply(lambda x: f'{x:,}')
    )
    top_10_deaths.columns = ['Country', 'Total Deaths']
    return top_10_deaths


def get_top_10_deaths_per_million():
    mask = main_dataframe['location'] != 'World'
    top_10_deaths_per_million = (
        main_dataframe.loc[mask]
        .groupby('location')[['total_deaths_per_million']].max()
        .sort_values(by='total_deaths_per_million', ascending=False)
    )
    top_10_deaths_per_million['rank'] = range(
        1, len(top_10_deaths_per_million) + 1)
    top_10_deaths_per_million = (
        top_10_deaths_per_million
        .reset_index()
        .set_index('rank').iloc[:10, :]
    )
    top_10_deaths_per_million['total_deaths_per_million'] = (
        top_10_deaths_per_million['total_deaths_per_million']
        .apply(lambda x: f'{round(x):,}')
    )
    top_10_deaths_per_million.columns = ['Country', 'Total Deaths per Million']
    return top_10_deaths_per_million


class IntroductionData:
    latest_date = main_dataframe['date'].max().strftime('%B %d, %Y')
    world_cases = f"{main_dataframe['total_cases'].max():,}"
    world_deaths = f"{main_dataframe['total_deaths'].max():,}"
    top_10_cases = get_top_10_cases()
    top_10_cases_per_million = get_top_10_cases_per_million()
    top_10_deaths = get_top_10_deaths()
    top_10_deaths_per_million = get_top_10_deaths_per_million()


introduction_data = IntroductionData()
