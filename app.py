from dash import Dash
from dash_html_components import H1

app = Dash(__name__)
server = app.server

app.layout = H1('Hello World.')

if __name__ == '__main__':
    app.run_server(debug=True)