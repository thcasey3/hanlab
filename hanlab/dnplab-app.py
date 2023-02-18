import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("hanlab", className="display-4"),
        html.Hr(),
        html.P("Use DNPLab to process ODNP, NMR, and DNP data", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("cnsi workups", href="/cnsi-workups", active="exact"),
                dbc.NavLink("DNPLab", href="/DNPLab", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(
    id="page-content",
    children=[
        html.Div([dcc.Upload(id="upload-data")]),
        html.Span(id="cnsi-output", style={"verticalAlign": "middle"}),
    ],
    style=CONTENT_STYLE,
)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("Documentation here")
    elif pathname == "/cnsi-workups":
        return html.Div(
            [
                html.Div(
                    [
                        dcc.Upload(
                            id="upload-data",
                            children=html.Div(
                                ["Drag and Drop or ", html.A("Select Files")]
                            ),
                            style={
                                "width": "100%",
                                "height": "60px",
                                "lineHeight": "60px",
                                "borderWidth": "1px",
                                "borderStyle": "dashed",
                                "borderRadius": "5px",
                                "textAlign": "center",
                                "margin": "10px",
                            },
                            # Allow multiple files to be uploaded
                            multiple=True,
                        ),
                        html.Div(id="output-data-upload"),
                    ]
                ),
                html.Span(id="cnsi-output", style={"verticalAlign": "middle"}),
                html.P("cnsi workup processing here"),
            ]
        )
    elif pathname == "/DNPLab":
        return html.P("DNPLab general processing here")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


@app.callback(Output("cnsi-output", "children"), [Input("upload-data", "filename")])
def cnsi_button(filename):
    return filename


def main_func():
    app.run_server(debug=True, port=8888)


if __name__ == "__main__":
    main_func()
