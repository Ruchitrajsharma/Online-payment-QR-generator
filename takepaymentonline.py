import qrcode
#Taking UPI ID As a input
upi_id=input("Enter your UPI ID=")
#Definig the paytemt URL based on the UPI ID and the payment app
phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20name&mc=1234'
#Create QR Codes for each payment app
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)
#Save the Qr image file 
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')
#display the qr code
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()