import plotly.graph_objects as go
from global_covid_tracker.dataframes import deaths_dataframe


def plot_total_deaths(countries: list, per_million: bool = True) -> go.Figure:
    fig = go.Figure()
    per_million_text = 'Per Million ' if per_million else ''
    for country in countries:
        data = deaths_dataframe(country)
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data['total_deaths_per_million'] if per_million else data['total_deaths'],
                text=data['text_total_deaths'],
                hoverinfo='text',
                name=country
            )
        )
    fig.update_layout(
        height=600,
        width=900,
        yaxis_type='log',
        yaxis={'title': f'Cumulative Deaths {per_million_text}(log scale)'},
        xaxis={'title': 'Date'},
        title=f'Cumulative COVID Deaths {per_million_text}in Selected Countries',
        legend={'x': 0.01, 'y': 0.98, 'bordercolor': 'Black', 'borderwidth': 1},
        showlegend=True
    )
    return fig