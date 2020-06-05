from global_covid_tracker.dataframes import growth_dataframe
import plotly.graph_objects as go


def plot_cases_growth(top_15=True, by_percent=True) -> go.Figure:
    if by_percent:
        column = 'pct_cases_increase'
        data = growth_dataframe.sort_values(by='pct_cases_increase',
                                            ascending=False)
        data = data[:15] if top_15 else data[-15:]
        title = (
            '15 Fastest Growing Countries by Percent Increase in Cases'
            if top_15 else '15 Slowest Growing Countries by Percent Increase '
                           'in Cases'
        )
    else:
        column = 'absolute_cases_increase_per_million'
        data = growth_dataframe.sort_values(
            by='absolute_cases_increase_per_million', ascending=False)
        data = data[:15] if top_15 else data[-15:]
        title = (
            '15 Fastest Growing Countries by Absolute Numbers of Cases per Million'
            if top_15 else '15 Slowest Growing Countries by Absolute Numbers '
                           'of Cases per Million'
        )
    fig = go.Figure(data=[
        go.Bar(
            x=data.index,
            y=data[column],
            marker={'color': 'blue', 'opacity': 0.5},
            text=data['text_pct_cases_increase']
            if by_percent else data['text_absolute_cases_increase_per_million'],
            hoverinfo='text')],
        layout=go.Layout(
            title=title,
            yaxis={
                'title': 'Percent Increase'
                if by_percent else
                'Absolute Increase per Million'},
            xaxis={'title': 'Country'}
        )
    )
    fig.update_layout(height=600, width=900)
    return fig
