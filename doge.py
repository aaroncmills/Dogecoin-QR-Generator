import subprocess
import qrcode
import requests
import json
from PIL import Image

#Enter the amount in USD you would like to embedded in the QR code(s) below
amount = 25

#Replace user_1, user_2, etc with friendly name. These will be viewable in the dogecoin cli with "dogecoin-cli listaccounts"
users = { "user_1": "" , "user_2": "", "user_n": "", "example": ""}

def convert_usd2doge():
    url = "https://web-api.coinmarketcap.com/v1/tools/price-conversion"
    querystring = {"amount":amount,"convert_id":"74","id":"2781"}
    headers = {
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "web-api.coinmarketcap.com",
        'Accept-Encoding': "gzip, deflate",
        'cache-control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    price_json = json.loads(response.text)
    convert_usd2doge.price = str(price_json['data']['quote']['74']['price'])

def make_qr(user):
    qr_payload = (str("dogecoin:" + str(users[user]) + "?amount=" + convert_usd2doge.price))
    filename = str(user + ".png")
    qr = qrcode.make(qr_payload)
    qr.save(filename)
    im1 = Image.open('shiba.jpg') #You can replace this image with something else if you prefer
    im2 = Image.open(filename)
    back_im = im1.copy()
    back_im.paste(im2, (825, 150))
    back_im.save(filename)

def make_address(user):
    cmd = "dogecoin-cli", "getnewaddress", user
    addr = str(subprocess.check_output(cmd))[2:36]
    print("User", user, "address is:", addr, "Wow, much crypto. Very coin.")
    users[user] = addr

def main():
    convert_usd2doge()
    for user in users:
        make_address(user)
        make_qr(user)

if __name__ == "__main__":
    main()