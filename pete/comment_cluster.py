"""
a song would contain...
song.length
song.comments

(example) song = [60000 * 3 + 1000, [ ["barry", 30000],["andy", 33500], ["betty", 25000], ["sandy", 34100], ["pete", 398000],
				["Mary", 90000], ["Kate", 92000], ["James", 94000], ["Sam", 96000], ["Muhammad", 84000],
				["Jane", 150000], ["Sean", 153000], ["Patty", 153000], ["George", 142000], ["Aidan", 158000]] ]
"""
import math

class song:
	comments = [ ("barry", 30000),("andy", 33500), ("betty", 25000), ("sandy", 34100), ("pete", 39800),
				("Mary", 90000), ("Kate", 92000), ("James", 94000), ("Sam", 96000), ("Muhammad", 84000),
				("Jane", 150000), ("Sean", 153000), ("Patty", 153000), ("George", 142000), ("Aidan", 158000)]
	length = 60000 * 3 + 1000
	
	def __init__(self):
		self.data = []
		
	def getAnalyzed(self):
		print 'analysis starts'
		cluster_comments(song);



	
def cluster_comments(song):

	num_centroids = int(round(song.length/1000/60))
	
	centroid_positions = []
	for i in range(num_centroids):
		centroid_positions.append(30000 + 60000 *i)
	
	#assuming that a song has as an attribute a list of comments
	#a comment is a tuple (username, timestamp)
	
	comments = song.comments
	#we got comments clustered around the current centroid position
	while True:
		clusters = cluster(comments, centroid_positions)
		#based on current clusters, recalculate position of centroids
		new_positions = average(clusters)
#		print new_positions
		if len(new_positions) == len(centroid_positions) and all(new_positions[i] == centroid_positions[i] for i in range(len(new_positions))):
			return clusters
		centroid_positions = new_positions
	
	
	
	
	
	"""
	for (usrname, timestmp) in comments:
		closest_dist = song.length
		closest_id = 0
		for cent_id in range(num_centroids):
			distance = math.fabs(centroids[cent_id][0] - timestmp)
			#print centroids[cent_id][0], timestmp, distance, closest_dist
			if distance < closest_dist:
				#print "set"
				closest_id = cent_id
				closest_dist = distance
		centroids[closest_id][1].append((timestmp, usrname))
		
	print centroids
	#
	
	moved = True

	while moved:
		moved = False
		for centroid in centroids:
			totalstamp = 0
			for [tstamp, usr] in centroid[1]:
				totalstamp += tstamp
			newpos = totalstamp/len(centroid[1])
			print newpos, len(centroid[1])
			if(newpos != centroid[0]):
				moved = True
				centroid[0] = newpos
	"""

#this method takes in list of comment tuples and centroid positions
#and outputs a tuple (centroid position, list of tuples)

def cluster(comments, centroid_positions):
	clusters = []
	for cent_id in range(len(centroid_positions)):
		clusters.append((centroid_positions[cent_id], []));

	for (usrname, timestmp) in comments:
		closest_dist = song.length
		closest_id = 0
		for cent_id in range(len(clusters)):
			distance = math.fabs(centroid_positions[cent_id] - timestmp)
			if distance < closest_dist:
				closest_id = cent_id
				closest_dist = distance
		clusters[closest_id][1].append((timestmp,usrname))
	
	return clusters

def average(clusters):
	changed = False
	new_positions = []
	for cluster in clusters:
		totaltime = 0
		for [tstamp, usr] in cluster[1]:
			totaltime += tstamp
		new_positions.append(totaltime/len(cluster[1]))
	return new_positions