#!/usr/bin/python3
import random

names = ["joao", "maria", "claus", "julie", "Ashley", "Noah"]
selected = []
i=0

while(len(selected) < len(names)): 
	name = names[i]
	randomName=(random.choice(names))
	if(randomName != name):
		if(randomName not in selected):
			i += 1
			print("The Secret friend of",name, "is", randomName)
			selected.append(randomName)
			continue
