import requests

def generate_long_lived_token(short_token, app_id, app_secret):

	gl_token = requests.get('https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id='+app_id+'&client_secret='+app_secret+'&fb_exchange_token='+short_token) 

	if gl_token.status_code == 200:
		token = gl_token.json().get('access_token')
		# print(token)
		return token
	else:
		return gl_token.text