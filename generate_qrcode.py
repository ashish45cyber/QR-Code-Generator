import qrcode
while True:
 data = input('Please enter the data you want to store in the QR cdoe ').strip()
 file_name = input ('please enter the file name you want to save the QR code as ').strip()
 qr = qrcode.QRCode(box_size=10, border=5)
 qr.add_data(data)
 image = qr.make_image(fill_color = "black", back_color= 'white')
 image.save(file_name)
 print('QR code has been saved as', file_name)
