import os
import sys



def submit_point(point, time, category, gift):
	print "Reaching Points Center.."
	try:
		file = open("points.point", "wb"); print 'Reached To Points Center.\n\n'
	except Exception as ReachError:
		print ReachError
	try:
		file.write(str('point: %s\n time: %s\n category:%s\n gift:%s' % (point, time, category, gift)))
		print "Point Created Sucessfully As:\n point: %s\n and it will end at date: %s\n category: %s\n gift: %s" % (point, time, category, gift)
	except Exception as CreatePointError:
		print CreatePointError


def trended_points(category):
	print "Searching in your category.."
	try:
		file = open('trended.point', 'rb')
		for search in file.readlines():
			if category in file:
				print category
			else:
				print 'No treneded category in this time'
	except Exception as SearchError:
		print SearchError



def signup():
	print "Pointer Signup\n"
	user = raw_input('username: ')
	pwd = raw_input('Password: ')
	userchecker = open('fellas.db', 'rb')
	if user in userchecker.readlines():
		userchecker.close()
		sys.close('This user was taken, try another.')
	else:
		userchecker.close()	
		try:
			db = open('fellas.db', 'wb')
			db.write('%s:' % user)
			db.write('%s' % pwd)
			print '%s Joined!' % str(user)
			db.close()
		except Exception as SignupError:
			print 'err:'+str(SignupError)

	

def login():
	print "Pointer Login\n"
	user = raw_input('Username: ')
	userchecker = open('fellas.db', 'rb')
	try:
		if user in userchecker.readlines():
			pwd = raw_input('Password: ')
			if pwd in userchecker.readlines():
				print 'Logined as %s' % str(user)
			else:
				print 'user not found.'
	except Exception as LoginError:
		print LoginError


def gift(point, winer, loser):
	try:
		db = open('gift.db', 'wb')
		db.write('%s Finished.\n Winer: %s\n loser:%s' % (point, winer, loser))
		db.close()
		print('%s Finished.\n Winer: %s\n loser:%s' % (point, winer, loser))
	except Exception as giftError:
		print giftError

	
submit_point('Gym', '180 day', 'Health', '500$')
#trended_points('Health')
#gift('gym', 'MyBetterHalf', 'MyBadHalf')

