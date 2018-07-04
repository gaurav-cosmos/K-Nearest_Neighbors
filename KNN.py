def KNN(data, predict, k=3):
	import numpy as np
	import pandas a pd
	from collections import Counter
	float(k)
	if len(data)>=k:
		warnings.warn('K is set less than length of features')
	distances = []
	for group in data:
		for features in data[group]:
			euclidian_distance = np.linalg.norm(np.array(features)-np.array(predict))
			distances.append([euclidian_distance, group])

	votes = [i[1] for i in sorted(distances)[:k]]
	
	vote_result = Counter(votes).most_common(1)[0][0]
	print(Counter(votes))
	confidence = Counter(votes).most_common(1)[0][1]
	confidence = float(confidence)
	confidence = confidence/k

	# print(vote_result,confidence)
	return vote_result,confidence
