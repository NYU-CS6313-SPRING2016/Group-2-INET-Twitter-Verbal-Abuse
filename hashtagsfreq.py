import json
import operator

#Reading in the json file with tweets
json_data=open('./input_files/Coordinates_15Keywords_Works.json').read()
Tweets = json.loads(json_data)

#tags = []
tagsset = set()

count = 0
for tweet in Tweets:
	if tweet['entities']['hashtags']:
		count +=1 
		for tag in tweet['entities']['hashtags']:
			try:

				if str(tag['text']) not in tagsset:
					#tags.append(str(tag['text']))
 					tagsset.add('#'+str(tag['text']))

			except:

				pass

print count
#Initializing a dictionary with keywords used for queries
hashtags = dict.fromkeys(tagsset)

for k, v in hashtags.iteritems():
	if v == None:
		hashtags[k] = 0

for key in hashtags.iterkeys():
	for tweet in Tweets:
		if tweet['entities']['hashtags']:
			for tag in tweet['entities']['hashtags']:
				if str(key) == '#'+str(tag['text']):
					hashtags[key] += 1


print sum(hashtags.itervalues())
    
    
if len(hashtags.keys())>10:
    with open('./input_files/twtCount-hashtags.json', 'w') as fp:
        json.dump(dict( sorted(hashtags.items(), key=operator.itemgetter(1))[-11:]), fp)
else:
    with open('./input_files/twtCount-hashtags.json', 'w') as fp:
        json.dump(hashtags, fp)
#print hashtags