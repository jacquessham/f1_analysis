import pandas as pd
import fastf1
from dashboard_helpers.Plotly_helpers.call_plotly import *



def fig():
	session = fastf1.get_session(2021, 'Spanish Grand Prix', 'Q')
	session.load()

	df = []

	for driver in session.drivers:
		driver_fastestlap = session.laps.pick_driver(driver).pick_fastest()
		driver_tel = driver_fastestlap.get_car_data().add_distance()
		driver_tel['Driver'] = driver

		df.append(driver_tel)

	df = pd.concat(df)

	return generate_fig(df)
