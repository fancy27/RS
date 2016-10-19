import numpy as np

def user_rating(file_dir):
	user_rating = {}
	with open(file_dir) as fin:
		for line in fin:
			(userId, itemId, rating, timestamp) = line.strip().split('\t')
			rating = int(rating)
			if user_rating.has_key(userId):
				pass
			else:
				user_rating[userId] = []
			user_rating[userId].append(rating)
	return user_rating
	#print user_rating['196']

def get_pref_C(user_rating):
	pref_C_all = {}
	for userId in user_rating:
		C = [0,0,0,0,0]
		pref_C = [0,0,0,0,0]
		for c in xrange(5):
			C[c] = user_rating[userId].count(c+1)

		length = sum(C)

		for c in xrange(5):
			temp_bf = 0
			for i in xrange(c):
				temp_bf += C[i]
			pref_C[c] = (1.0 * temp_bf + 0.5 * C[c]) / length
			pref_C[c] = round(pref_C[c], 2)
		#print C,length,pref_C
		pref_C_all[userId] = pref_C
	return pref_C_all

def change_data(pref_C):
	fout = open('data/u.changed','w')
	with open('data/u.data') as fin:
		for line in fin:
			(userId, itemId, rating, timestamp) = line.strip().split('\t')
			rating = int(rating)
			new_line = ('%s\t%s\t%s\t%s\t\n' % (userId, itemId, pref_C[userId][rating-1], timestamp))
			fout.write(new_line)
	fout.close()


if __name__ == '__main__':
	user_rating = user_rating('data/u.data')
	pref_C = get_pref_C(user_rating)
	change_data(pref_C)