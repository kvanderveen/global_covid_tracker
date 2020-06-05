from global_covid_tracker.site_components.introduction_data import introduction_data


class IntroductionContent:
    opening_content1 = (
        f'Among the sites dedicated to better understanding the global impact '
        f'of the COVID-19 pandemic, [Our World in Data]'
        f'(https://ourworldindata.org/coronavirus) stands out. Last updated '
        f'{introduction_data.latest_date}, the site tallies the latest data '
        f'collected around the world.  As of the last update, a total of '
        f'{introduction_data.world_cases} confirmed cases and '
        f'{introduction_data.world_deaths} deaths from this novel virus have '
        f'been documented. The tables and plots on this site were generated '
        f'from data made publicly [available]'
        f'(https://github.com/owid/covid-19-data/tree/master/public/data) by '
        f'Our World in Data.'
    )
    opening_content2 = (
        f'To navigate this site, select one of the radio buttons on the '
        f'sidebar on the left side of this page. Explore COVID-19 testing, '
        f'case, death, and growth data.'
    )
    cases_content = (
        f'Below is a table of the 10 countries with the greatest number '
        f'of confirmed COVID-19 cases.  The default table represents the raw '
        f'number of total cases. To view the 10 countries with the greatest '
        f'number of COVID-19 cases per million residents, select the checkbox '
        f'below.'
    )
    deaths_content = (
        f'Below is a table of the 10 countries with the greatest number '
        f'of confirmed COVID-19 deaths.  The default table represents the raw '
        f'number of total deaths. To view the 10 countries with the greatest '
        f'number of COVID-19 deaths per million residents, select the checkbox '
        f'below.'
    )


introduction_content = IntroductionContent()
