from global_covid_tracker.dataframes import cases_dataframe
import plotly.graph_objects as go


def plot_cases_by_country(country: str) -> go.Figure:
    data = cases_dataframe(country)
    fig = go.Figure(data=[
        go.Bar(
            x=data.index,
            y=data['new_cases'],
            name='New Daily Cases',
            marker={'color': 'blue', 'opacity': 0.5},
            text=data['text_new_cases'],
            hoverinfo='text',)],
        layout=go.Layout(
            title=f'Daily New COVID-19 Cases for {country}',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Daily Cases'}
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data['new_cases_7d_rolling_mean'],
            name='7 Day Rolling Mean',
            marker={'color': 'blue'},
            text=data['text_new_cases_7d_rolling_mean'],
            hoverinfo='text'
        )
    )
    fig.update_layout(height=600, width=900,
                      legend={'x': 0.01, 'y': 0.98, 'bordercolor': 'Black',
                              'borderwidth': 1})
    return fig
