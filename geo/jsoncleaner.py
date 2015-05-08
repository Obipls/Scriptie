import json
import re

def cleanup():
	with open('alerts_test.json') as data_file:
		alerts = json.load(data_file)
	
	# Remove all empty causes from the list of alerts
	alerts = [d for d in alerts if d.get('cause') != []]
	
	# Remove all alerts or other lines without a time
	alerts = [d for d in alerts if ':' in ''.join(d.get('time'))] 
	
	# Remove all alerts without a priority index (Capital letter followed by a space and one number)
	alerts = [d for d in alerts if re.search('[A-P]\s[0-9]', ''.join(d.get('cause')))]

	# Gather all causes in 1 list for geosnatcher
	causes= [d.split() for d in [''.join(d) for d in [d.get('cause') for d in alerts]]]

	return causes

#cleanup()