import os
import qrcode


def normalize_filename(filename: str) -> str:
    filename = filename.strip()
    if not filename:
        return ""
    root, ext = os.path.splitext(filename)
    if not ext:
        filename += ".png"
    return filename


def main():
    while True:
        data = input("Please enter the data you want to store in the QR code (or type 'q' to quit): ").strip()

        if data.lower() in {"q", "quit", "exit"}:
            print("Exiting program. Goodbye!")
            break

        if not data:
            print("Data cannot be empty. Please try again.")
            continue

        file_name = input("Please enter the file name to save the QR code as: ").strip()

        if file_name.lower() in {"q", "quit", "exit"}:
            print("Exiting program. Goodbye!")
            break

        file_name = normalize_filename(file_name)

        if not file_name:
            print("File name cannot be empty. Please try again.")
            continue

        qr = qrcode.QRCode(box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)

        image = qr.make_image(fill_color="black", back_color="white")
        image.save(file_name)

        print(f"QR code has been saved as {file_name}")


if __name__ == "__main__":
    main()
