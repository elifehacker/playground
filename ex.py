import requests,os,re
URL = 'https://www.cse.unsw.edu.au/~cs9315/20T1/lectures/week0'
U_trailer = '/exercises/'
for i in range(6,10):
	ex = URL+str(i)+U_trailer
	#print(ex)
	folder = 'week0'+str(i)
	try:
		os.mkdir(folder)
	except Exception as e:
		print(e)
	for k in range(1,10):
		sub_folder = 'Ex0'+str(k)
		ex_dir = ex+sub_folder+'/'
		try:
			os.mkdir(folder+'/'+sub_folder)
		except Exception as e:
			print(e)
		resp = requests.get(url = ex_dir) 
		href = set(re.findall(r"A HREF=\"[\w\-\d]*", resp.text, re.I))
		for ref in href:
			if len(ref) <= len("A HREF=\""):
				continue
			title = ref.split('"')[1]
			content = requests.get(url = ex_dir+title) 
			with open(folder+'/'+sub_folder+'/'+title, 'w') as file:
				file.write(content.text)

