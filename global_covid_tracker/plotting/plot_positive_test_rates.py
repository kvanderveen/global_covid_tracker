import plotly.graph_objects as go
from global_covid_tracker.dataframes import tests_dataframe


def plot_positive_test_rates(countries: list, cumulative=False) -> go.Figure:
    title_start = (
        'Cumulative Percent' if cumulative
        else 'Daily Percent (7 day average)'
    )
    fig = go.Figure()
    for country in countries:
        data = tests_dataframe(country)
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=(
                    data['positive_rate_cumulative'] if cumulative
                    else data['positive_rate_daily']
                ),
                text=(
                    data['text_positive_rate_cumulative'] if cumulative
                    else data['text_positive_rate_daily']
                ),
                hoverinfo='text',
                name=country
            )
        )
    fig.update_layout(
        height=600,
        width=900,
        yaxis={'title': 'Percent of Tests (positives)'},
        xaxis={'title': 'Date'},
        title=f'{title_start} of Tests that are Positive in Selected Countries',
        legend={'x': 0.01, 'y': 0.98, 'bordercolor': 'Black', 'borderwidth': 1},
        showlegend=True
    )
    return fig
