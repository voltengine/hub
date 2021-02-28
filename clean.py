import shutil

def rmtree(path):
	try:
		shutil.rmtree(path)
	except OSError:
		pass

rmtree('bin')
rmtree('cache')

input('Press ENTER to continue...')
