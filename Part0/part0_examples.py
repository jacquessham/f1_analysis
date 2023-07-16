from sys import argv
import pandas as pd
import fastf1


def get_session():
	session = fastf1.get_session(2022, 18, 'R')
	print(f"The name of this session is: {session.name}")
	print(f"It happened: {session.event['EventDate']}")

def get_event_schedule():
	schedule = fastf1.get_event_schedule(2021)
	print(schedule)

def main(choice):
	if choice == 'get_session':
		get_session()
	elif choice == 'get_event_schedule':
		get_event_schedule


main(argv[1])
