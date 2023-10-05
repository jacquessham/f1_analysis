# Part 0 - Understand Fast F1 Package
In this section, we will go over how to use the Python API: <i>FastF1</i>. As the <i>FastF1</i> documentation stated:

```
"FastF1 is largely built ontop of Pandas DataFrames and Series. But It adds its own convenient methods for working specifically with F1 data. This makes it much easier to get started and work with the data in general. Still, you have all the capabilities of Pandas at hand whenever you need them." 
```

Therefore, it is very easy to utilize with Pandas syntax.
<br><br>
<b>Note: This API is only available in Python 3.0+</b>

## Object Types

### Session
Coming soon...

### Event
This object represent a single event on a race weekend or testing event unit. Here are the methods available to the object:

<ul>
	<li>is_testing() - Whether the event is a testing event</li>
	<li>get_session_name() - Return event name</li>
	<li>get_session_date()</li>
	<li>get_session() - Return a Session object</li>
	<li>get_race() - Return a Session object with the race statistics</li>
	<li>get_qualifying() - Return a Session object with qualifying statistics</li>
	<li>get_sprint() - Return a Session object with sprint statistics</li>
	<li>get_sprint_shootout() - Return a Session object with sprint shootout statistics</li>
	<li>get_practice() - Return a Session object with sprint practice statistics, pass the practice session number as parameter</li>
</ul>

<br>
The details can be found in this <a href="https://docs.fastf1.dev/events.html#fastf1.events.Event">documenation link</a>.

## One Event/Session
You may use <b>get_session()</b> with the following arguements: <b>Year</b>, <b>Round Number</b>, <b>Session</b> (FP1, FP2, FP3, Q, S, SS, R), and it will return an object to access the information of such event or session. Once you have the object, you may access to the following attributes but not limited to:
<ul>
	<li>name (str)</li>
	<li>date (timestamp)</li>
	<li>event (Pandas Series)</li>
	<li>And more...</li>
</ul>

<br>
It will return a <b>Session</b> object type.
<br><br>

<a href="https://docs.fastf1.dev/fastf1.html#fastf1.get_session">Documentation</a> for <i>get_session()</i>

<br><br>
Example:

```
session = fastf1.get_session(2022, 18, 'R')
print(f"The name of this session is: {session.name}")
print(f"It happened: {session.event['EventDate']}")
```

## Event Schedule
You may use <b>get_event_schedule()</b> to obtain a dataframe of the information of a series of Grands Prix. If you want to get the statistics during the testing session, you may use <b>get_testing_session()</b>..
<br><br>
Available columns:
<ul>
	<li>RoundNumber (#0 is Testing)</li>
	<li>Country</li>
	<li>Location</li>
	<li>OfficialEventName</li>
	<li>EventDate</li>
	<li>EventName</li>
	<li>EventFormat</li>
	<li>Session1</li>
	<li>Session1Date</li>
	<li>Session2</li>
	<li>Session2Date</li>
	<li>Session3</li>
	<li>Session3Date</li>
	<li>Session4</li>
	<li>Session4Date</li>
	<li>Session5</li>
	<li>Session5Date</li>
	<li>F1ApiSupport<li>
</ul>
<br>
The method return a FastF1 object based on Pandas, you may access the object with Pandas syntax. It will return a <b>Session</b> object type.

<br><br>
Example:

```
>>> schedule = fastf1.get_event_schedule(2021)
>>> print(schedule)
    RoundNumber        Country  ...        Session5Date F1ApiSupport
0             0        Bahrain  ...                 NaT        False
1             1        Bahrain  ... 2021-03-28 18:00:00         True
2             2          Italy  ... 2021-04-18 15:00:00         True
3             3       Portugal  ... 2021-05-02 15:00:00         True
4             4          Spain  ... 2021-05-09 15:00:00         True
5             5         Monaco  ... 2021-05-23 15:00:00         True
6             6     Azerbaijan  ... 2021-06-06 16:00:00         True
7             7         France  ... 2021-06-20 15:00:00         True
8             8        Austria  ... 2021-06-27 15:00:00         True
9             9        Austria  ... 2021-07-04 15:00:00         True
10           10  Great Britain  ... 2021-07-18 15:00:00         True
11           11        Hungary  ... 2021-08-01 15:00:00         True
12           12        Belgium  ... 2021-08-29 15:00:00         True
13           13    Netherlands  ... 2021-09-05 15:00:00         True
14           14          Italy  ... 2021-09-12 15:00:00         True
15           15         Russia  ... 2021-09-26 15:00:00         True
16           16         Turkey  ... 2021-10-10 15:00:00         True
17           17  United States  ... 2021-10-24 14:00:00         True
18           18         Mexico  ... 2021-11-07 13:00:00         True
19           19         Brazil  ... 2021-11-14 14:00:00         True
20           20          Qatar  ... 2021-11-21 17:00:00         True
21           21   Saudi Arabia  ... 2021-12-05 20:30:00         True
22           22      Abu Dhabi  ... 2021-12-12 17:00:00         True
```

<br>
Link here: <a href="https://theoehrly.github.io/Fast-F1/examples/basics.html#working-with-the-event-schedule">Working with the event schedule</a>

## Example Script
You may execute <i>part0_examples.py</i> stated with an arguement of which example for demostration, with the following options:

<ul>
	<li>get_session</li>
	<li>get_event_schedule</li>
	<li>get_testing_session</li>
	<li></li>
</ul>

For example, I would like to display an example of <i>get_session()</i>, I would execute this on the command line:

```
python3 part0_examples.py get_session
```
