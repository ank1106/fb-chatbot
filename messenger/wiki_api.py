import requests

chk_dsmbgtn = lambda x, k : 1 if x.startswith(k+" (") else 0

def searchWiki(query):
	"""Search wiki api for query, returns multiple result set if disambugity found"""

	if isinstance(query, str):
		url = "https://en.wikipedia.org/w/api.php?action=opensearch&search={}&limit=4&namespace=0&format=json".format(query)
		res = requests.get(url)
		if res.status_code == 200:
			data = res.json()
			
			# get index of results if having ambuigation except first 
			tmp_res = [i for i in range(1,len(data[1])) if chk_dsmbgtn(data[1][i], data[1][0])]
			
			if tmp_res:
				# ambuigation found, add the first result to list
				tmp_res.insert(0, 0)
				result = [dict(zip(["title","des","link"],[data[1][_id], data[2][_id], data[3][_id]])) for _id in tmp_res] 
			else:
				result = [dict(zip(["title","des","link"],[data[1][0], data[2][0], data[3][0]]))]
			return result
		else:
			return False
	else:
		raise ValueError("query must be string")

