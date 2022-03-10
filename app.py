import dash
from dash import html
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import utils
from datetime import datetime
from dash_table import DataTable
import datetime

df = pd.DataFrame()
list_press = []
list_time = []
list_p = []
list_t = []

card = html.Div(children = [
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Epreuve 1", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '1'),
                dbc.ListGroupItem("Etape 2", id = '2'),
                dbc.ListGroupItem("Etape 3", id = '3'),
                dbc.ListGroupItem("Etape 4", id = '4'),
                dbc.ListGroupItem("Etape 5", id = '5'),
            ],
            flush=True,
        ),
        style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '20%', 'display': 'inline-block', 'textAlign' : 'center'},
    ),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Epreuve 2", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '6'),
                dbc.ListGroupItem("Etape 2", id = '7'),
                dbc.ListGroupItem("Etape 3", id = '8'),
                dbc.ListGroupItem("Etape 4", id = '9'),
                dbc.ListGroupItem("Etape 5", id = '10'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '20%', 'display': 'inline-block', 'textAlign' : 'center'},
),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Epreuve 3", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '11'),
                dbc.ListGroupItem("Etape 2", id = '12'),
                dbc.ListGroupItem("Etape 3", id = '13'),
                dbc.ListGroupItem("Etape 4", id = '14'),
                dbc.ListGroupItem("Etape 5", id = '15'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '20%', 'display': 'inline-block', 'textAlign' : 'center'},
),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Epreuve 4", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '16'),
                dbc.ListGroupItem("Etape 2", id = '17'),
                dbc.ListGroupItem("Etape 3", id = '18'),
                dbc.ListGroupItem("Etape 4", id = '19'),
                dbc.ListGroupItem("Etape 5", id = '20'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '20%', 'display': 'inline-block', 'textAlign' : 'center'},
),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Epreuve 5", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '21'),
                dbc.ListGroupItem("Etape 2", id = '22'),
                dbc.ListGroupItem("Etape 3", id = '23'),
                dbc.ListGroupItem("Etape 4", id = '24'),
                dbc.ListGroupItem("Etape 5", id = '25'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '20%', 'display': 'inline-block', 'textAlign' : 'center'},
)
], id = "step_card")

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div(
    children=[
        html.H1(children="Espace chronomètre", style = {'textAlign' : 'center'}),
        html.P(
            children="Appuyez sur le buzzer pour débuter l'enregistrement. Une fois l'étape terminée, rappuyez sur le buzzer afin d'arrêter l'enregistrement. Veillez à terminer les 5 épreuves.",
        style = {'textAlign' : 'center', 'margin-left' : '2%', 'margin-right' : '2%'}),
        html.Div([html.P(id = "text_green"),
        html.Div(dbc.Button('Buzzer', size="lg", color="primary", className="me-1", id = "green")),
        ], style={'textAlign': 'center'}),
        html.Div(children = card, id = "table", style = {'margin-top' : '10px'}),
        html.Div(dbc.Button('Résultats', id = "button", color="info", className="me-1")),
        html.Div(dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Attention")),
                dbc.ModalBody("Veuillez terminer toutes les épreuves pour obtenir les résultats."),
            ],
            id="modal",
            is_open=False,
        )),
        html.Div(dbc.Button('Recommencer', id = "button_reset", color="warning", className="me-1")),
        html.Div(DataTable(id = "result", data = [])),
        
        ]
        , style = {'background' : 'CadetBlue'})
        
@app.callback(
    Output(component_id='green', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if n_clicks % 2 != 0:
        return {'height':'8%', 'width':'8%'}
    else:
        return {'height':'10%', 'width':'10%'}

@app.callback(
    Output(component_id='text_green', component_property='children'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if n_clicks % 10 == 0 and n_clicks != 0:
        return ("Epreuve terminée.")
    if n_clicks % 2 != 0:
        return ("Enregistrement en cours...")
    else:
        return ("Il n'y a pas d'enregistrement en cours.")

@app.callback(
    Output(component_id='1', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)


def update_output(n_clicks):
    if n_clicks != None and n_clicks != 0:
        list_p, list_t = utils.step_timer(n_clicks, list_press, list_time)
    if len(list_time) >= 2:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='2', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 4:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='3', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 6:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='4', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 8:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='5', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 10:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='6', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 12:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='7', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 14:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='8', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 16:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='9', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 18:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='10', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 20:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='11', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 22:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='12', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 24:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='13', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 26:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='14', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 28:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='15', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 30:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='16', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 32:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='17', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 34:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='18', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 36:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='19', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 38:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='20', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 40:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='21', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 42:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='22', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 44:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='23', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 46:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='24', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 48:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='25', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(list_time) >= 50:
        return {'background-color' : 'green'}
    
@app.callback(
    [Output("result", "data"), Output('result', 'columns')],
    Input(component_id='button', component_property='n_clicks')
)

def table(n_clicks):
    print('table nclicks = ', n_clicks)
    if n_clicks != None and n_clicks != 0:
        i = 0
        j = 0
        list_delta = []  
        print('list time = ', len(list_time))
        while j < 25:
            item1 = datetime.datetime.strptime(list_time[i], '%Y-%m-%d %H:%M:%S.%f')
            item2 = datetime.datetime.strptime(list_time[i+1], '%Y-%m-%d %H:%M:%S.%f')
            delta = (item2 - item1)
            list_delta.append(delta.total_seconds())
            j += 1
            i += 2
        print('len delta = ',len(list_delta))
        list_index = [1, 2, 3, 4, 5, 6]
        df.index = list_index
        list_delta.insert(5, sum(list_delta[0:5]))
        list_delta.insert(11, sum(list_delta[6:11]))
        list_delta.insert(17, sum(list_delta[12:17]))
        list_delta.insert(23, sum(list_delta[18:23]))
        list_delta.insert(29, sum(list_delta[24:29]))
        df['Epreuve 1'] = list_delta[0:6]
        df['Epreuve 2'] = list_delta[6:12]
        df['Epreuve 3'] = list_delta[12:18]
        df['Epreuve 4'] = list_delta[18:24]
        df['Epreuve 5'] = list_delta[24:30]
        print(df)
        return (df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])


@app.callback(
    Output(component_id='green', component_property='n_clicks'),
    Input(component_id='button_reset', component_property='n_clicks')
)

def reset(n_clicks):
    print('nclick reset = ', n_clicks)
    if n_clicks != None:
        list_t.clear()
        list_time.clear()
        return (0)

@app.callback(
    Output("modal", "is_open"),
    [Input("button", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, is_open):
    if n1 and len(list_time) < 50:
        return True
    return False

if __name__ == "__main__":
    app.run_server(debug=False)