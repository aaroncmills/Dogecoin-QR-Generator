# Dogecoin-QR-Generator
A way to create many accounts and associated QR codes 

To run this project you will need to have the dogecoin daemon, dogecoin-cli, python3, and install the requests, qrcode and pillow libraries. This can be done with `pip install requests qrcode pillow`.

With dogecoind running and the dogecoin-cli added to your path, run the python script (after changing the values in the dictionary at the top of the script) and it will create a unique account for each entry, then create and save a corresponding qr code with a nice picture of a doge. Photo by Evgeny Tchebotarev from Pexels.

The script will add a payment amount to the qr code, this amount is set in USD and has an initial value of $25, change this to whatever suits your use case. This conversion is powered by the coinmarketcap API, if you don't want the conversion to be in USD they probably have another pair you can use.

The final output of the script will be a nice payment request like so.

![Alt text](example.png?raw=true "Doge")
