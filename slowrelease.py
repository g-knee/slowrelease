import glob
import os
# import tumblr api

# important settings
## frequency
## folder

def app():
	direct = rawinput("Directory: ")
	print(direct)
	print(type(direct))
	os.chdir(direct)

	for file in glob.glob("*.jpg"):
		print(file)

if __name__ == "__main__":
	app()
