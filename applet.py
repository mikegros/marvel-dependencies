from dash import Dash, html, dcc, Input, Output

import numpy                as np
import pandas               as pd
import plotly.express       as px
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

mcu_movies = [
        "Iron Man",
        "The Incredible Hulk",
        "Iron Man 2",
        "Thor",
        "Captain America: The First Avenger",
        "The Avengers",
        "Iron Man 3",
        "Thor: The Dark World",
        "Captain America: The Winter Soldier",
        "Guardians of the Galaxy	",
        "Avengers: Age of Ultron",
        "Ant-Man",
        "Captain America: Civil War",
        "Doctor Strange",
        "Guardians of the Galaxy Vol. 2",
        "Spider-Man: Homecoming",
        "Thor: Ragnarok",
        "Black Panther",
        "Avengers: Infinity War",
        "Ant-Man and the Wasp",
        "Captain Marvel",
        "Avengers: Endgame",
        "Spider-Man: Far From Home",
        "Black Widow",
        "Shang-Chi and the Legend of the Ten Rings",
        "Eternals",
        "Spider-Man: No Way Home",
        "Doctor Strange in the Multiverse of Madness",
        "Thor: Love and Thunder"
        ]

marvel_movies = [
        "Spiderman 1",
        "Spiderman 2",
        "Spiderman 3",
        "Amazing Spider-Man",
        "Amazing Spider-Man 2",
        "Venom",
        "Venom: Let There Be Carnage"
        ]

marvel_tv = [
        "Daredevil",
        "Jessica Jones",
        "Luke Cage",
        "Iron Fist",
        "The Defenders",
        "The Punisher",
        "Cloak & Dagger",
        "Runaways"
        ]

mcu_tv = [
        "Agents of Shield",
        "Agent Carter",
        "Inhumans",
        "WandaVision",
        "The Falcon and the Winter Soldier",
        "Loki",
        "What If...?",
        "Hawkeye",
        "Moon Knight"
        ]

mcu_all    = mcu_movies + mcu_tv
marvel_all = mcu_movies + mcu_tv + marvel_movies + marvel_tv

n_mcu    = len(mcu_all)
n_marvel = len(marvel_all)

# parent_type:
#     0 => Directly follows parent. Not a complete story without it.
#     1 => Parent important for key themes and character developments
#     2 => Parent brings additional context and enjoyment but missing it
#              will not substantially detract from the movie

edge_color = ["rgba(214,39,40,0.8)", "rgba(44,160,44,0.5)", "rgba(31,119,180,0.25)"]
edge_color = ["rgba(214,39,40,0.8)", "rgba(148,103,189,0.5)", "rgba(31,119,180,0.25)"]

###############
# MCU Movies

# Iron Man 
graph_dict = {"Iron Man":{"loc":[2006,0], "parents":[], "parent_type":[], "year":2008}}

# The Incredible Hulk"
graph_dict["The Incredible Hulk"] = {"loc":[2006.5,-6], "parents":["Iron Man"], "parent_type":[2], "year":2008}

# Iron Man 2
graph_dict["Iron Man 2"] = {"loc":[2007,3], "parents":["Iron Man"], "parent_type":[1], "year":2010}

# Thor
graph_dict["Thor"] = {"loc":[2007,-3], "parents":["Iron Man"], "parent_type":[2], "year":2011}

# Captain America: The First Avenger
graph_dict["Captain America: The First Avenger"] = {"loc":[2007,0], "parents":["Iron Man"], "parent_type":[2], "year":2011}

# The Avengers
graph_dict["The Avengers"] = {"loc":[2008,0], "parents":["Iron Man 2", "Thor", "Captain America: The First Avenger"], "parent_type":[1, 1, 1], "year":2012}

# Iron Man 3
graph_dict["Iron Man 3"] = {"loc":[2009,4], "parents":["Iron Man 2", "The Avengers"], "parent_type":[2, 1], "year":2013}

# Thor: The Dark World
graph_dict["Thor: The Dark World"] = {"loc":[2009,-4], "parents":["Thor", "The Avengers"], "parent_type":[1, 1], "year":2013}

# Captain America: The Winter Soldier
graph_dict["Captain America: The Winter Soldier"] = {"loc":[2009,2], "parents":["Captain America: The First Avenger", "The Avengers"], "parent_type":[1, 1], "year":2014}

# Guardians of the Galaxy
graph_dict["Guardians of the Galaxy"] = {"loc":[2010.5,4.5], "parents":[], "parent_type":[], "year":2014}

# Avengers: Age of Ultron
graph_dict["Avengers: Age of Ultron"] = {"loc":[2010,0], "parents":["The Avengers", "Captain America: The Winter Soldier", "Iron Man 3"], "parent_type":[1, 2, 2], "year":2015}

# Ant-Man
graph_dict["Ant-Man"] = {"loc":[2010,-6], "parents":["Captain America: The Winter Soldier"], "parent_type":[2], "year":2015}

# Captain America: Civil War
graph_dict["Captain America: Civil War"] = {"loc":[2011,0], "parents":["Avengers: Age of Ultron", "Captain America: The Winter Soldier", "Ant-Man"], "parent_type":[1, 1, 2], "year":2016}

# Doctor Strange
graph_dict["Doctor Strange"] = {"loc":[2012, 3], "parents":[], "parent_type":[], "year":2016}

# Guardians of the Galaxy Vol. 2
graph_dict["Guardians of the Galaxy Vol. 2"] = {"loc":[2011.5,7], "parents":["Guardians of the Galaxy"], "parent_type":[1], "year":2017}

# Spider-Man: Homecoming
graph_dict["Spider-Man: Homecoming"] = {"loc":[2012, -7], "parents":["Captain America: Civil War"], "parent_type":[1], "year":2018}

# Thor: Ragnarok
graph_dict["Thor: Ragnarok"] = {"loc":[2012.5,-3], "parents":["Thor: The Dark World", "Avengers: Age of Ultron", "Doctor Strange"], "parent_type":[2, 2, 2], "year":2017}

# Black Panther
graph_dict["Black Panther"] = {"loc":[2012.5,8], "parents":["Captain America: Civil War"], "parent_type":[1], "year":2018}

# Avengers: Infinity War
graph_dict["Avengers: Infinity War"] = {"loc":[2014,0], "parents":["The Avengers","Avengers: Age of Ultron", "Captain America: Civil War", "Guardians of the Galaxy Vol. 2", "Black Panther","Thor: Ragnarok", "Doctor Strange", "Spider-Man: Homecoming"], "parent_type":[2,2,1,1,2,2,2,2], "year":2018}

# Ant-Man and the Wasp
graph_dict["Ant-Man and the Wasp"] = {"loc":[2014.5,-5], "parents":["Ant-Man", "Avengers: Infinity War"], "parent_type":[1, 2], "year":2018}

# Captain Marvel
graph_dict["Captain Marvel"] = {"loc":[2014.5,5], "parents":["Avengers: Infinity War"], "parent_type":[2], "year":2019}

# Avengers: Endgame
graph_dict["Avengers: Endgame"] = {"loc":[2015,0], "parents":["The Avengers","Avengers: Age of Ultron", "Captain America: Civil War", "Guardians of the Galaxy Vol. 2", "Black Panther","Thor: Ragnarok", "Doctor Strange", "Spider-Man: Homecoming", "Avengers: Infinity War", "Ant-Man and the Wasp", "Captain Marvel", "Iron Man", "Thor: The Dark World","Captain America: The Winter Soldier"], "parent_type":[2,2,2,2,2,2,2,2,0,1,1,2,2,2], "year":2019}

# Spider-Man: Far From Home
graph_dict["Spider-Man: Far From Home"] = {"loc":[2016,-6], "parents":["Avengers: Endgame", "Spider-Man: Homecoming"], "parent_type":[1,1], "year":2019}

# Black Widow
graph_dict["Black Widow"] = {"loc":[2016,7], "parents":["Avengers: Endgame", "The Avengers", "Captain America: The Winter Soldier"], "parent_type":[2,2,2], "year":2021}

# Shang-Chi and the Legend of the Ten Rings
graph_dict["Shang-Chi and the Legend of the Ten Rings"] = {"loc":[2017.5,10], "parents":[], "parent_type":[], "year":2021}

# Eternals
graph_dict["Eternals"] = {"loc":[2017,-9], "parents":["Avengers: Endgame"], "parent_type":[2], "year":2021}

# Spider-Man: No Way Home
graph_dict["Spider-Man: No Way Home"] = {"loc":[2018,3], "parents":["Doctor Strange", "Avengers: Endgame", "Spider-Man: Far From Home", "Spider-Man 1", "Spider-Man 2", "Spider-Man 3", "Amazing Spider-Man", "Amazing Spider-Man 2", "Daredevil", "Venom: Let There Be Carnage" ], "parent_type":[2,2,0,1,1,2,2,1,2,2], "year":2021}

# Doctor Strange in the Multiverse of Madness
graph_dict["Doctor Strange in the Multiverse of Madness"] = {"loc":[2019,-2], "parents":["Doctor Strange","Avengers: Endgame", "WandaVision", "Spider-Man: No Way Home", "X-Men", "Inhumans", "What If...?"], "parent_type":[1,2,1,2,2,2,2], "year":2022}

for movie in graph_dict.keys():
    graph_dict[movie]["Released"] = True
    graph_dict[movie]["MCU"] = True
    graph_dict[movie]["Format"] = "Movie"

# Thor: Love and Thunder
graph_dict["Thor: Love and Thunder"] = {"loc":[2019,-9], "parents":["Avengers: Endgame", "Thor: Ragnarok"], "parent_type":[1, 1], "Released":True, "MCU":True, "Format":"Movie", "year":2022}


###############
# MCU TV

# Agents of Shield
graph_dict["Agents of Shield"] = {"loc":[2010,5], "parents":["The Avengers", "Captain America: The Winter Soldier"], "parent_type":[1, 1], "Released":True, "MCU":True, "Format":"TV", "year":2013}

# Agent Carter
graph_dict["Agent Carter"] = {"loc":[2008,5], "parents":["Captain America: The First Avenger"], "parent_type":[1], "Released":True, "MCU":True, "Format":"TV", "year":2015}

# Inhumans
graph_dict["Inhumans"] = {"loc":[2018.75,-3.25], "parents":[], "parent_type":[], "Released":True, "MCU":True, "Format":"TV", "year":2017}

# WandaVision
graph_dict["WandaVision"] = {"loc":[2017.75,-2.25], "parents":["Avengers: Age of Ultron","Captain America: Civil War","Avengers: Infinity War", "Avengers: Endgame"], "parent_type":[1,1,1,1], "Released":True, "MCU":True, "Format":"TV", "year":2021}

# The Falcon and the Winter Soldier
graph_dict["The Falcon and the Winter Soldier"] = {"loc":[2016.5,9], "parents":["Captain America: The Winter Soldier", "Avengers: Endgame", "Captain America: Civil War"], "parent_type":[1,1,1], "Released":True, "MCU":True, "Format":"TV", "year":2021}

# Loki
graph_dict["Loki"] = {"loc":[2018,-4], "parents":["Avengers: Endgame", "The Avengers", "Thor: The Dark World"], "parent_type":[2, 2, 2], "Released":True, "MCU":True, "Format":"TV", "year":2021}

# What If...?
graph_dict["What If...?"] = {"loc":[2017,0.5], "parents":["Captain America: The First Avenger", "Avengers: Age of Ultron", "Black Panther", "Guardians of the Galaxy", "Thor", "Doctor Strange", "The Avengers"], "parent_type":[1]*7, "Released":True, "MCU":True, "Format":"TV", "year":2021}

# Hawkeye
graph_dict["Hawkeye"] = {"loc":[2018,6], "parents":["Avengers: Endgame", "Avengers: Age of Ultron", "Daredevil", "Black Widow"], "parent_type":[1, 2, 2, 1], "Released":True, "MCU":True, "Format":"TV", "year":2021}

# Moon Knight
graph_dict["Moon Knight"] = {"loc":[2019,7], "parents":[], "parent_type":[], "Released":True, "MCU":True, "Format":"TV", "year":2022}

# Ms. Marvel
graph_dict["Ms.Marvel"] = {"loc":[2019,4], "parents":["Captain Marvel", "Avengers: Endgame"], "parent_type":[2,2], "Released":True, "MCU":True, "Format":"TV", "year":2022}

################
# Non-MCU Marvel Movies that impact the MCU

# Spiderman 1
graph_dict["Spider-Man 1"] = {"loc":[2017.5,3.5], "parents":[], "parent_type":[], "Released":True, "MCU":False, "Format":"Movie", "year":2002}

# Spiderman 2
graph_dict["Spider-Man 2"] = {"loc":[2017.65,3.65], "parents":["Spider-Man 1"], "parent_type":[1], "Released":True, "MCU":False, "Format":"Movie", "year":2004}

# Spiderman 3
graph_dict["Spider-Man 3"] = {"loc":[2017.75,3.75], "parents":["Spider-Man 2"], "parent_type":[1], "Released":True, "MCU":False, "Format":"Movie", "year":2007}

# Amazing Spider-Man
graph_dict["Amazing Spider-Man"] = {"loc":[2017.5,2.5], "parents":[], "parent_type":[], "Released":True, "MCU":False, "Format":"Movie", "year":2012}

# Amazing Spider-Man 2
graph_dict["Amazing Spider-Man 2"] = {"loc":[2017.65,2.35], "parents":["Amazing Spider-Man"], "parent_type":[1], "Released":True, "MCU":False, "Format":"Movie", "year":2014}

# Venom
graph_dict["Venom"] = {"loc":[2017.65,1.8], "parents":[], "parent_type":[], "Released":True, "MCU":False, "Format":"Movie", "year":2018}

# Venom: Let There Be Carnage
graph_dict["Venom: Let There Be Carnage"] = {"loc":[2017.75,2.25], "parents":["Venom"], "parent_type":[1], "Released":True, "MCU":False, "Format":"Movie", "year":2021}

# X-Men
graph_dict["X-Men"] = {"loc":[2018.5, -3.1], "parents":[], "parent_type":[], "Released": True, "MCU":False, "Format":"Movie", "year":2000}

##############
# Marvel Non-MCU TV
shift = 0.5
# Daredevil
graph_dict["Daredevil"] = {"loc":[2014-shift,10], "parents":[], "parent_type":[], "Released":True, "MCU":False, "Format":"TV", "year":2015}

# Jessica Jones
graph_dict["Jessica Jones"] = {"loc":[2014.5-shift,9], "parents":[], "parent_type":[], "Released":True, "MCU":False, "Format":"TV", "year":2015}

# Luke Cage
graph_dict["Luke Cage"] = {"loc":[2014.85-shift,9], "parents":["Jessica Jones"], "parent_type":[2], "Released":True, "MCU":False, "Format":"TV", "year":2016}

# Iron Fist
graph_dict["Iron Fist"] = {"loc":[2014.5-shift,11], "parents":[], "parent_type":[], "Released":True, "MCU":False, "Format":"TV", "year":2017}

# The Defenders
graph_dict["The Defenders"] = {"loc":[2015.25-shift,11], "parents":["Daredevil", "Jessica Jones", "Luke Cage", "Iron Fist"], "parent_type":[1,2,2,1], "Released":True, "MCU":False, "Format":"TV", "year":2017}

# The Punisher
graph_dict["The Punisher"] = {"loc":[2014.25-shift,12], "parents":["Daredevil"], "parent_type":[1], "Released":True, "MCU":False, "Format":"TV", "year":2017}

# Runaways
graph_dict["Runaways"] = {"loc":[2010.5,9], "parents":["Cloak & Dagger"], "parent_type":[2], "Released":True, "MCU":False, "Format":"TV", "year":2017}

# Cloak & Dagger
graph_dict["Cloak & Dagger"] = {"loc":[2010,9], "parents":[], "parent_type":[], "Released":True, "MCU":False, "Format":"TV", "year":2018}


app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children='MCU Dependency Graph', style={"text-align":"center",  "color":"black"}),

    html.Div(children='''
        A tool to improve your MCU viewing experience. For any MCU property the graph indicates which other shows or movies would benefit your viewing experience. Select a movie or show from the list below to focus on which other properties matter. This list is currently curated only by the author, so please suggest edits through the github issues at the link at the bottom of the page. For movies that have not yet or have just released, the dependencies are based on what is likely from the trailers but is meant to avoid any potential spoiler reveals. Take as a grain of salt.
    ''', style={"margin-bottom": "30px", 'fontSize':20}),

    html.Div('Red edges indicate critical viewing. This is reserved for movies which are a direct sequal such that the movie is not a complete story without having seen the previous.', 
        style={'color': '#d62728', 'fontSize': 18, 'text-align': 'center'}),
    html.Div('Purple edges indicate strongly recommended viewing. The movie can be viewed without seeing the incoming purple edges, but important context or character information is missing.', 
        style={'color': '#9467bd', 'fontSize': 18, 'text-align': 'center'}),
    html.Div('Blue edges indicate that the movie references the previous, but they are not necessary viewing. Having seen the blue edges improves the viewing experience but missing them does not substantially harm it.',
        style={'color': '#1f77b4', 'fontSize': 18, 'text-align': 'center'}),

    html.Div([

        html.Div("Movie: ", style={'fontSize':20}),

        html.Div([
            dcc.Dropdown(
                ["All"] + mcu_all,
                "All",
                id='movie_select',
            )
        ], style={'width': '30%', 'display': 'inline-block'})

        # html.Div([
        #     dcc.Dropdown(
        #         ["All"] + marvel_all,
        #         "All",
        #         id='crossfilter-yaxis-column'
        #     )
        # ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
    ], style={
        'padding': '10px 5px'
    }),

    html.Div([
        dcc.Graph(
            id='crossfilter-indicator-scatter',
            hoverData={'points': [{'customdata': 'Japan'}]}
        )
    ], style={'width': '95%', 'display': 'inline-block'}),

    html.Div([
        html.Div("Link to Github Issues: ",style={"width":'20%', "display":"inline"}),
        dcc.Link("Here", href="https://github.com/mikegros/marvel-dependencies/issues")
    ])

])


@app.callback(
    Output('crossfilter-indicator-scatter', 'figure'),
    Input('movie_select', 'value'))
def update_graph(select_name): 
    edge_trace = []
    edge_text  = []
    for movie in graph_dict.keys():
        if select_name != "All":
            if (select_name != movie):# and (movie not in graph_dict[select_name]["parents"]):
                continue
            print("Selected: ", select_name, " which is ", movie, " or its parent")
        if len(graph_dict[movie]["parents"]) == 0:
            continue
        for ii in range(len(graph_dict[movie]["parents"])):
            movie2 = graph_dict[movie]["parents"][ii]
            c_ind  = graph_dict[movie]["parent_type"][ii]
            x0, y0 = graph_dict[movie2]['loc']
            x1, y1 = graph_dict[movie]["loc"]
            edge_text.append(movie2 + " -> " + movie)
            edge_trace.append(go.Scatter(x=[x0,x1],y=[y0,y1], hoverinfo='text', mode='lines',line=dict(width=3.5-c_ind, color=edge_color[c_ind])))
    
    node_x = []
    node_y = []
    # for node in G.nodes():
    for movie in graph_dict.keys():
        if select_name != "All":
            if (select_name != movie) and (movie not in graph_dict[select_name]["parents"]):
                continue
        x, y = graph_dict[movie]['loc']
        node_x.append(x)
        node_y.append(y)
    
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            # showscale=True,
            # colorscale options
            #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            #colorscale='YlGnBu',
            reversescale=True,
            color="rgba(255,200,200,1.0)",
            size=15,
            # colorbar=dict(
            #     thickness=15,
            #     title='Node Connections',
            #     xanchor='left',
            #     titleside='right'
            # ),
            line_width=2))

    node_text = []
    for movie in graph_dict.keys():
        if select_name != "All":
            if (select_name != movie) and (movie not in graph_dict[select_name]["parents"]):
                continue
        mcu_label = "MCU" if graph_dict[movie]["MCU"] else "Marvel but not MCU"
        node_text.append(movie + "<br>" + mcu_label + " " + graph_dict[movie]["Format"])
    
    #node_trace.marker.color = [0.5]*len(graph_dict.keys())
    node_trace.text = node_text
    # edge_trace.text = edge_text

    fig = go.Figure(data=edge_trace + [node_trace],
             layout=go.Layout(
                #title='Network Example',
                #titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
    return fig

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
    
