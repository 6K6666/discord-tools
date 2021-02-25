import requests
import time

fuckytoken = "user_token"

r2 = requests.post("https://discord.com/api/v8/applications", headers={'authorization':fuckytoken}, json={"name": "sup robot","team_id": None})



if r2.status_code != 201:
	print(f"ERROR ///// {r2.text}")
else:
	print("Successfully created a project.")
	botid = r2.json()['id']
	r3 = requests.post(f'https://discord.com/api/v8/applications/{botid}/bot', headers={'authorization':fuckytoken}, json={})

	if r3.status_code != 200:
		print(f"ERROR ///// {r3.text}")
	else: 
		print("Successfully created a bot.")
		bottoken = r3.json()['token']
		print(f"Bot token: {bottoken}")

		d2CAPIKEY = '2captcha API key'

		twoCaptchaPostData = {
			'key': d2CAPIKEY,
			'method': 'userrecaptcha',
			'googlekey': "6Lef5iQTAAAAAKeIvIY-DeexoO3gj7ryl9rLMEnn",
		    'pageurl': f"https://discord.com/oauth2/authorize?client_id={botid}&scope=bot&permissions=8",
		}
		sendpostdata = requests.post("https://2captcha.com/in.php", json=twoCaptchaPostData)


		if "OK|" in sendpostdata.text:

			d2cid = sendpostdata.text.replace('OK|', '')

			time.sleep(15)

			getdata = requests.get("https://2captcha.com/res.php?key="+d2CAPIKEY+"&action=get&id="+d2cid)

			def loginworked(text):
				r4 = requests.post(f"https://discord.com/api/v8/oauth2/authorize?client_id={botid}&scope=bot", headers={'authorization':fuckytoken}, 
					json={'authorize': True, 'bot_guild_id': guild_id_here, 'captcha_key': text, '': '8'})

				print(r4.status_code)
				print(r4.text)
				

			if "OK|" in getdata.text:
				loginworked(getdata.text.replace('OK|', ''))

			elif "CAPCHA_NOT_READY" in getdata.text:
				checkinteg = 1
				while True:
					d2cid = sendpostdata.text.replace('OK|', '')
					time.sleep(5)
					print("Hey")
					getdata = requests.get("https://2captcha.com/res.php?key="+d2CAPIKEY+"&action=get&id="+d2cid)
					checkinteg = checkinteg + 1
					if not "CAPCHA_NOT_READY" in getdata.text:
						loginworked(getdata.text.replace('OK|', ''))
						print(getdata.text.replace('OK|', ''))
						print("loop bo")
						break

		