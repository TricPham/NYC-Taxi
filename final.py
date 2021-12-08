import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table 
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__)


moneyTimeAr = []
tripTimeAr = []

taxiData = pd.read_csv('out.csv', header = 0)
taxiZone = pd.read_csv('taxizone.csv', header = 0)
taxiData['tpep_pickup_datetime'] = pd.to_datetime(taxiData['tpep_pickup_datetime'])
taxiData.set_index(keys='tpep_pickup_datetime', inplace = True)

moneyTimeAr.append(round(taxiData['total_amount'].between_time('0:00','0:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('1:00','1:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('2:00','2:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('3:00','3:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('4:00','4:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('5:00','5:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('6:00','6:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('7:00','7:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('8:00','8:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('9:00','9:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('10:00','10:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('11:00','11:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('12:00','12:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('13:00','13:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('14:00','14:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('15:00','15:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('16:00','16:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('17:00','17:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('18:00','18:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('19:00','19:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('20:00','20:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('21:00','21:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('22:00','22:59').sum(),2))
moneyTimeAr.append(round(taxiData['total_amount'].between_time('23:00','23:59').sum(),2))


tripTimeAr.append(len(taxiData.between_time('0:00','0:59')))
tripTimeAr.append(len(taxiData.between_time('1:00','1:59')))
tripTimeAr.append(len(taxiData.between_time('2:00','2:59')))
tripTimeAr.append(len(taxiData.between_time('3:00','3:59')))
tripTimeAr.append(len(taxiData.between_time('4:00','4:59')))
tripTimeAr.append(len(taxiData.between_time('5:00','5:59')))
tripTimeAr.append(len(taxiData.between_time('6:00','6:59')))
tripTimeAr.append(len(taxiData.between_time('7:00','7:59')))
tripTimeAr.append(len(taxiData.between_time('8:00','8:59')))
tripTimeAr.append(len(taxiData.between_time('9:00','9:59')))
tripTimeAr.append(len(taxiData.between_time('10:00','10:59')))
tripTimeAr.append(len(taxiData.between_time('11:00','11:59')))
tripTimeAr.append(len(taxiData.between_time('12:00','12:59')))
tripTimeAr.append(len(taxiData.between_time('13:00','13:59')))
tripTimeAr.append(len(taxiData.between_time('14:00','14:59')))
tripTimeAr.append(len(taxiData.between_time('15:00','15:59')))
tripTimeAr.append(len(taxiData.between_time('16:00','16:59')))
tripTimeAr.append(len(taxiData.between_time('17:00','17:59')))
tripTimeAr.append(len(taxiData.between_time('18:00','18:59')))
tripTimeAr.append(len(taxiData.between_time('19:00','19:59')))
tripTimeAr.append(len(taxiData.between_time('20:00','20:59')))
tripTimeAr.append(len(taxiData.between_time('21:00','21:59')))
tripTimeAr.append(len(taxiData.between_time('22:00','22:59')))
tripTimeAr.append(len(taxiData.between_time('23:00','23:59')))


moneyFrame = pd.DataFrame(moneyTimeAr, columns = ["money"])
moneyFrame = moneyFrame.rename_axis("time").reset_index()

timeFrame = pd.DataFrame(tripTimeAr, columns = ["number_of_trips"])
timeFrame = timeFrame.rename_axis("time").reset_index()


a = taxiData['Zone'].value_counts().rename_axis('location').reset_index(name = 'count')
newdf = a.merge(taxiZone, left_on='location', right_on='Zone', how = 'inner')

b = taxiData.groupby('PULocationID').sum()
newtip = b.merge(taxiZone, left_on='PULocationID', right_on='LocationID', how = 'inner')

map = px.scatter_mapbox(newdf, lat = 'lat', lon = 'lon',  color = 'count', hover_name = 'location',
						color_continuous_scale=px.colors.sequential.Turbo, zoom = 9)
map.update_layout(mapbox_style="carto-positron")

mapTip = px.scatter_mapbox(newtip, lat = 'lat_y', lon = 'lon_y',  color = 'tip_amount', hover_name = 'Zone',
						color_continuous_scale=px.colors.sequential.Turbo, zoom = 9)
mapTip.update_layout(mapbox_style="carto-positron")


#moneyfig = go.Figure()
#moneyfig.add_trace(go.Bar(x=moneyFrame['time'], y = moneyFrame['money'], base = 0, marker_color = 'green', name='hour',))

moneyfig = px.bar(moneyFrame, x = 'time', y = 'money',color = 'money',color_continuous_scale=px.colors.sequential.Blugrn,
					labels ={'money':'US Dollars','time':'hour in 24H'})

#tripfig = go.Figure()
#tripfig.add_trace(go.Bar(x=timeFrame['time'], y = timeFrame['number_of_trips'], base = 0, marker_color = 'darkgoldenrod', name='hour'))

tripfig = px.bar(timeFrame, x = 'time', y = 'number_of_trips',color= 'number_of_trips',
					labels ={'time':'hour in 24H', 'number_of_trips':'Number of trips'})

body = html.Div([
	html.H1('NYC April 2020 Taxi Record'),
	html.Div(children=[
		html.H2('Introduction'),
		html.P('New York City is one of the most busiest city in the world. WIth all of the moving and hustling of people, there are a ton of movement'),
		html.P('Taxi cabs are one many mode of transportation. Using the data provided to us, we made these visualization to help identify places to make more profits.'),
		html.P('This is only the month of April of 2020, so there are a little less data due to covid.')
		]
	)
	,
	
	html.Div(children=[
		html.H2('Number of taxi trip in a given locations'),
		html.Div(children=[
			dcc.Graph(
				id='map',
				figure=map
				),
			html.P('In this month, the area within New York City had the most trips. a good amount of the averaging around 2-6 thouands trips.Other places seeing sub 2 thouands'),
			]
			)
			]
		),
	html.Div(children=[
		html.H2('Total amount of tip in a month in a given locations'),
		dcc.Graph(
			id='mapTip',
			figure=mapTip
			),
			html.P('Similar to the visualization above, more trips means more chances for tip money. Two good place outside the city are the airports')
			]
		),
	html.Div(children=[
		html.H2('Total amount of taxi trips in a month per hour'),
		dcc.Graph(
			id = 'tripBar',
			figure = tripfig
			),
			html.P('This seems normal with activites picking up during the day and dying out at night. Kind of busy at the 6,7 am mark and 3 and 4 pm mark.')
			]
		),
	html.Div(children=[
		html.H2('Total amount of money earned in a month per hour'),
		dcc.Graph(
			id = 'moneyBar',
			figure = moneyfig
			),
			html.P('there is a slight shift in the amount of money earned. the busiest time of the day is 3 pm but 4 pm brings in more money. It might be due to the congestion fee.')
			]
		),
		
	html.Div(children=[ 
		html.H2('About Team Solo',style ={'text-align':'center'}),
		html.P('Team solo is a one map group, that was not able to make this into a website. Instead it is a simple python based web app that kind of looks like a website.', style = {'text-align':'center'}),
		dcc.Link(html.P('The dataset comes from TLC'), href = 'https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page',style = {'text-align':'center'}),
		html.P('It provided taxi trip information such as the pickup locations, trip distances, total trip cost, and more.', style = {'text-align':'center'}),
		], 
		
	),
	
	html.Div(children=[
		html.H2('Team Member',style ={'text-align':'center'}),
		dcc.Link(html.P('Github page'), href = 'https://tricpham.github.io/',style = {'text-align':'center'})
	]
	),
		
	html.Footer(
		html.P('University of Hawaii at Manoa ICS484 / ACM 484 Data Visualization Project', style = {'text-align':'center'})
		),
	]	
)



app.layout = html.Div([body])


if __name__ == '__main__':
	app.run_server(debug =True)