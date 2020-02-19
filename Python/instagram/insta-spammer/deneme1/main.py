import requests

mail = "gavs123gavs@hotmail.com"
name = "Fatih furkan"
username = "gavs123gavsqt"
password = "Hatipoglu68"
istek = requests.post("https://www.instagram.com/",data={'emailOrPhone':mail,'fullName':name,'username':username,'password':password})

print(istek)