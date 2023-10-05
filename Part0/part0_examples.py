from sys import argv
import pandas as pd
import fastf1


def get_session():
	session = fastf1.get_session(2022, 18, 'R')
	print(f"The name of this session is: {session.name}")
	print(f"It happened: {session.event['EventDate']}")

def get_event_schedule():
	schedule = fastf1.get_event_schedule(2023)
	session = schedule.get_event_by_round(18)
	print(f"The name of this session is: {session.EventName}")
	print(f"It happened: {session['EventDate']}")

def get_testing_session():
	session = fastf1.get_testing_session(2023, 1, 1)
	print(f"The name of this session is: {session.name}")
	print(f"It happened: {session.event['EventDate']}")

def main(choice):
	if choice == 'get_session':
		get_session()
	elif choice == 'get_event_schedule':
		get_event_schedule()
	elif choice == 'get_testing_session':
		get_testing_session()


main(argv[1])
