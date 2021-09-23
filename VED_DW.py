import requests
from colorama import Fore
print("""                                                                                       
██╗   ██╗███████╗██████╗       ██████╗ ██╗    ██╗
██║   ██║██╔════╝██╔══██╗      ██╔══██╗██║    ██║
██║   ██║█████╗  ██║  ██║█████╗██║  ██║██║ █╗ ██║
╚██╗ ██╔╝██╔══╝  ██║  ██║╚════╝██║  ██║██║███╗██║
 ╚████╔╝ ███████╗██████╔╝      ██████╔╝╚███╔███╔╝
  ╚═══╝  ╚══════╝╚═════╝       ╚═════╝  ╚══╝╚══╝               """)
print(f"By {Fore.RED}@TweakPY{Fore.RESET} - And Thx For This Api By Dev {Fore.RED}[@RRLRR]{Fore.RESET}")
print('')
Song_down=int(input('1) Sound Cloud\n2) Facebook Ved Download\n3) IG & IGTV\n4) Search YouTube\n5) Hammel App Search\n6) TikTok Ved Download\n~~~~~~~~~~~~~~~~\n>'))
if Song_down==1:
	song_url=input("[?] Song Url:\n")
	req=requests.post(f'http://cvcbnhfuu.ml/HMD/api/SoundCloud.php?url={song_url}')
	print("----------------------------------------")
	print("Photo Of the song: ",req.json()['Photo'])
	print("----------------------------------------")
	print("Name Of the song: ",req.json()['Name'])
	print("----------------------------------------")
	print("Link Of the song: ",req.json()['Link'])
	print("----------------------------------------")
elif Song_down==2:
	ved_Url=input("[?] Type the Video Url:\n")
	req2=requests.post(f'https://cvcbnhfuu.ml/HMD/api/faecbook.php?url={ved_Url}')
	print("----------------------------------------")
	print("Download Video: ",req2.json()['Video']['HD'])
	print("----------------------------------------")
	print("Download Audio: ",req2.json()['Audio'])
	print("----------------------------------------")
elif Song_down==3:
	ved_URL=input('[?] Type The Video URL:\n')
	req3=requests.post(f'https://cvcbnhfuu.ml/HMD/api/insta.php?url={ved_URL}')
	print("--------------------------------------")
	print("Link of Video: ",req3.json()['DownloadLink'])
	print("--------------------------------------")
elif Song_down==4:
	ser=input("[?] Type The Search Word")
	req=requests.post(f'https://cvcbnhfuu.ml/HMD/api/youtube.php?q={ser}')
	print(req.text)
elif Song_down==5:
	Linkurl=input("[?] URL : ")
	url="https://hammel.in/star/index.php"
	head={
	'Host': 'hammel.in',
	'Accept': '*/*',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Accept-Encoding': 'gzip, deflate',
	'User-Agent': 'Hammel/2.1 CFNetwork/1120 Darwin/19.0.0',
	'Content-Length': '141',
	'Accept-Language': 'ar',
	'Connection': 'close'}
	data=f"version=6.3&token=f679e989f9b44a60562ec6749d89a8cf9e3c6b6a364b626c1c7800411d8d0a25&vpn=0&country=ns&page=0&url={Linkurl}"
	req=requests.post(url,headers=head,data=data)
	print(req.text)
elif Song_down==6:
	Ved=input('[?] Type The Ved Link:\n')
	req=requests.post(f'https://hamod.ga/api/tiktok?url={Ved}')
	print(req.text)
else:exit('Alright ..')
