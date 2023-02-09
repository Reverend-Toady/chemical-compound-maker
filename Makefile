PROJECT := ConstructingChemistry

all:
	flask --app $(PROJECT)/app.py --debug run