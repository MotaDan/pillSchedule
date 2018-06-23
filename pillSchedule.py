from datetime import datetime, timedelta
from collections import namedtuple
import argparse

def pillSchedule(numPills, pillSize, startTime, frequency):
	currentTime = startTime
	TakeTime = namedtuple("TakeTime", ["Time", "Pill", "Leftover"])
	schedule = []

	for pill in (x * pillSize for x in range(0, int(numPills / pillSize))):
		#Need to shift pill beucase of ranges start
		pill += pillSize
		schedule.append(TakeTime(currentTime, pill, numPills - pill))
		currentTime += timedelta(hours=frequency)

	return schedule

def printSchedule(schedule):
	print("{} {:0>2} {:0>2}".format(schedule.Time.strftime('%a %I:%M'), schedule.Pill, schedule.Leftover))

def main():
	parser = argparse.ArgumentParser(description="Determine how long pills last")
	parser.add_argument('-n', '--numPills', default=21, help='number of pills remaining')
	parser.add_argument('-s', '--pillSize', default=1, help='The size of each pill; Half(0.5) a pill or a full(1) pill')
	parser.add_argument('-f', '--frequency', default=6, help='The freuency that the pills are taken in hours')
	args = parser.parse_args()

	for schedule in pillSchedule(float(args.numPills), float(args.pillSize), datetime.now(), args.frequency):
		printSchedule(schedule)

if __name__ == "__main__":
	main()