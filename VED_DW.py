from pafy import new
import youtube_dl,requests
print("""                                                                                       
██╗   ██╗███████╗██████╗       ██████╗ ██╗    ██╗
██║   ██║██╔════╝██╔══██╗      ██╔══██╗██║    ██║
██║   ██║█████╗  ██║  ██║█████╗██║  ██║██║ █╗ ██║
╚██╗ ██╔╝██╔══╝  ██║  ██║╚════╝██║  ██║██║███╗██║
 ╚████╔╝ ███████╗██████╔╝      ██████╔╝╚███╔███╔╝
  ╚═══╝  ╚══════╝╚═════╝       ╚═════╝  ╚══╝╚══╝               """)
print(f"By @TweakPY  -  @vv1ck")
print('')
c=int(input('1- YouTube Video\n2- Hammel App Search\n:'))
if c==1:
	url=input('[?] Video Url\n:')
	try:
		vedio=new(url)		
		vedi=vedio.getbest()		
		vedi.download()				
		print("\n[+] Done , Video is downloaded Successfly ..")	
	except KeyError:print("[!] pafy Error , youtube_dl Error Please Go to https://github.com/Filza2/VED-DW To slove this ..")
	except:print("[!] Error")	
elif c==2:
	Linkurl=input("[?] URL : ")
	req=requests.post('https://hammel.in/star/index.php',headers={'Host': 'hammel.in','Accept': '*/*','Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip, deflate','User-Agent': 'Hammel/2.1 CFNetwork/1120 Darwin/19.0.0','Content-Length': '141','Accept-Language': 'ar','Connection': 'close'},data=f"version=6.3&token=f679e989f9b44a60562ec6749d89a8cf9e3c6b6a364b626c1c7800411d8d0a25&vpn=0&country=ns&page=0&url={Linkurl}")
	print(req.text)
else:exit('By @TweakPY  -  @vv1ck')
