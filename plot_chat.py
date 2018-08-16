import matplotlib.pyplot as plt 
import matplotlib
import sys
import os.path

font = {'family' : 'normal',
		 'size'   : 6}
matplotlib.rc('font', **font)

# 08/05/18, 9:44 AM - Person: This is a message
# basic assumption - and : are both present

def plots(txt):
	d = {}
	lmaos = {} # Shashwat :P

	for line in txt:
		if ": " not in line:
			continue
		if "-" not in line:
			continue
		pm = line[line.index("-") + 2 : ].strip('\r\n')
		dots = pm.index(": ") if ": " in pm else -1
		if dots == -1:
			continue
		person, msg = pm[:dots], pm[dots + 2:]
		if person not in d:
			d[person] = []
			lmaos[person] = 0
		
		d[person].append(msg)
		if msg.strip(' ').lower() == 'lmao':
			lmaos[person] += 1

	count = {}
	for name in d:
		count[name] = len(d[name])

	sorted_count = sorted(count.items(), key=lambda kv: kv[1])
	sorted_count.reverse()

	print("\t".join([i[0] for i in sorted_count])) # folks
	print("\t".join([str(i[1]) for i in sorted_count])) # message count
	# for i in sorted_count:
	# 	print (str(lmaos[i[0]]),'\t'),

	# print(lmaos)
	# exit()
	print(sorted_count)


	plt.bar(range(len(sorted_count)), [i[1] for i in sorted_count], align='center')
	plt.xticks(range(len(sorted_count)), [i[0] for i in sorted_count])
	plt.show()

if __name__ == '__main__':
	if len (sys.argv) < 2 :
		print("Usage: python plot_chat.py filename")
		sys.exit(1)

	if not os.path.isfile(sys.argv[1]):
		print("File does not exist!")
		sys.exit(1)

	with open(sys.argv[1], 'r') as f:
		txt = f.readlines()
	
	plots(txt)

	media=input('Show media only ? 1 for yes, anything else for no: ')
	if(media=='1'):
		# keep only messages with <Media omitted>
		txt_media = [t for t in txt if "<Media omitted>" in t]
		plots(txt_media)