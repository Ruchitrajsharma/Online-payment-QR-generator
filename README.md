# Online-payment-QR-generator
This project is a Python-based application that generates QR codes for seamless online payments by using upi_id.  The project employs popular Python libraries to generate and display the QR codes, while also ensuring the security and accuracy of payment information.
Description: This Python application generates QR codes for UPI-based payments, supporting popular payment apps like PhonePe, Paytm, and Google Pay. By simply entering a UPI ID, users can create unique payment QR codes for each platform. These QR codes can be saved as image files and scanned to facilitate quick and secure payments. The app makes use of the qrcode library to generate QR codes and provides a simple interface to display them.
Key Featurea:
Input UPI ID: The application takes the user’s UPI ID as input to generate payment URLs.
Multi-App Support: QR codes are generated for three popular UPI-based payment apps: PhonePe, Paytm, and Google Pay.
Customizable Payment Information: The generated QR codes include placeholder recipient names and merchant codes (can be modified for specific use).
QR Code Generation: Each payment app has its unique QR code, generated using the qrcode library.
QR Code Storage: The QR codes are saved as PNG image files, ready for use.
QR Code Display: The generated QR codes are displayed to the user for quick scanning.
Technologies Used:
Python: The main programming language used for developing the application.
qrcode library: For generating and displaying the QR codes.
Workflow:

The user inputs their UPI ID.
Payment URLs are created for PhonePe, Paytm, and Google Pay using the UPI ID.
QR codes are generated for each payment app.
The QR codes are saved as PNG files and displayed to the user for scanning.
This project can be enhanced by adding features like custom recipient names, dynamic merchant codes, and support for other payment apps.
