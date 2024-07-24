import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def create_receipt(filename):
    store_name = "Super grocery mart"
    store_street = "Janpath, Bhubaneswar"
    store_phone_number = "9348702535"
    cashier_name = "Kalyani"

    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    products = [
        ("White", 30),
        ("Rice", 25),
        ("Dal", 80),
        ("Bread", 20),
        ("Butter", 50),
        ("Jam", 55),
        ("Pasta", 35),
    ]

    items_sold = len(products)
    subtotal = sum(price for name, price in products)
    food_tax = subtotal * 0.06
    grand_total = subtotal + food_tax

    return_message = "No returns on meat, produce, milk products."
    appreciation_message = "Thank you for your business!!"

    # Print to console
    receipt_lines = [
        "*" * 39,
        f"{store_name.title().center(39)}",
        f"{store_street.center(39)}",
        f"{store_phone_number.center(39)}",
        "=" * 39,
        f"Cashier: {cashier_name}",
        f"{date_time[0:10]} {'':>19} {date_time[11:]}",
        "=" * 39,
        "GROCERY",
        " ",
    ]

    for name, price in products:
        receipt_lines.append(f"{name:<20} {'':>10} {price:>5}")

    receipt_lines.extend([
        " ",
        "=" * 39,
        f"Subtotal {'':>23} ${subtotal:.2f}",
        f"Food Tax @ 6% {'':>19} ${food_tax:.2f}",
        f"GRAND TOTAL {'':>20} ${grand_total:.2f}",
        "=" * 39,
        " ",
        f"TOTAL NUMBER OF ITEMS SOLD = {items_sold}",
        " ",
        " ",
        f"\t{return_message}",
        f"\t\t\t{appreciation_message}",
    ])

    for line in receipt_lines:
        print(line)

    # Create the PDF
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Draw the lines in the PDF
    y_position = height - inch
    c.setFont("Helvetica", 12)

    for line in receipt_lines:
        if line.strip() == "":
            y_position -= 0.25 * inch
        else:
            c.drawString(inch, y_position, line)
            y_position -= 0.25 * inch

    c.showPage()
    c.save()

# Create receipt PDF
create_receipt("receipt.pdf")
