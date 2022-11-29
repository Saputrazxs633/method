import os, re, requests, random, json, time
from rich import print as cetak
from rich.panel import Panel as nel
from rich.tree import Tree
from rich.console import Console as sol
from rich.markdown import Markdown as mark
os.system("clear")

ses = requests.Session()
idf = "id lu"
pw = "pw lu"
ua = "Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36"


ses.headers.update({
	"authority":				"free.facebook.com",
	"method":				"GET",
	"path":					"https://free.facebook.com/?_rdc=1&_rdr",
	"Host":					"free.facebook.com",
	"cache-control":			"max-age=0",
	"upgrade-insecure-requests":		"1",
	"user-agent":				ua,
	"accept":				"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"sec-fetch-site":			"same-site",
	"sec-fetch-mode":			"navigate",
	"sec-fetch-user":			"?1",
	"sec-fetch-dest":			"document",
	"referer":				"https://free.facebook.com/",
	"accept-encoding":			"gzip, deflate",
	"accept-language":			"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
})
link = ses.get(
	f"https://free.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fguides%2Faccess-tokens%2F&ref=dbl&fl&login_from_aymh=1"
)
response = ses.post(
	"https://free.facebook.com/login/device-based/regular/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fguides%2Faccess-tokens%2F&refsrc=deprecated&lwv=100&ref=dbl",
	data = {
		"lsd":				re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
		"jazoest":			re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
		"m_ts":				re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
		"li":				re.search('name="li" value="(.*?)"', str(link.text)).group(1),
		"try_number":			re.search('name="try_number" value="(.*?)"', str(link.text)).group(1),
		"unrecognized_tries":		re.search('name="unrecognized_tries" value="(.*?)"', str(link.text)).group(1),
		"email":			idf,
		"pass":				pw,
		"login":			"Masuk",
		"bi_xrwh":			"0"
	},
	cookies = {
		"cookie":			" m_pixel_ratio=2.625; wd=412x756",
		"cookie":			";".join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items()])
	}
)



if "checkpoint" in ses.cookies.get_dict().keys():
	cepeh = Tree(mark("# Akun checkpoint",style="yellow"),style="bold cyan")
	cepe = cepeh.add("[magenta]Detail akun")
	cepe.add(f"[white]{idf}|{pw}")
	cepe.add("[white]Tahun pembuatan akun 2022")
	cepeh.add(nel(f"[red]{ua}"),style="white")
	sol().print(nel(cepeh))
if "c_user" in ses.cookies.get_dict().keys():
	coli = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
	okei = Tree(mark("# Akun ok",style="green"),style="magenta")
	oke = okei.add("[bold cyan]Detail akun")
	oke.add(f"[white]{idf}|{pw}")
	oke.add("[white]Tahun pembuatan akun 2022")
	okei.add(nel(f"[green]{coli}"),style="white")
	sol().print(nel(okei))

