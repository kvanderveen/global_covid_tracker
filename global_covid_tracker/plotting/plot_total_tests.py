import plotly.graph_objects as go
from global_covid_tracker.dataframes import tests_dataframe


def plot_total_tests(countries: list, per_1000=True) -> go.Figure:
    title_end = ' Per 1000 Residents' if per_1000 else ''
    fig = go.Figure()
    for country in countries:
        data = tests_dataframe(country)
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=(
                    data['new_tests_smoothed_per_thousand'] if per_1000
                    else data['new_tests_smoothed']
                ),
                text=data['text_new_tests'],
                hoverinfo='text',
                name=country
            )
        )
    fig.update_layout(
        height=600,
        width=900,
        yaxis={'title': f'Number of Daily Tests{title_end}'},
        xaxis={'title': 'Date'},
        title=f'Number of Daily Tests{title_end} in Selected Countries',
        legend={'x': 0.01, 'y': 0.98, 'bordercolor': 'Black', 'borderwidth': 1},
        showlegend=True
    )
    return fig
