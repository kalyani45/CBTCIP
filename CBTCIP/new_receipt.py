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

    p1_name, p1_price = "white", 4.99
    p2_name, p2_price = "Rice", 1.99
    p3_name, p3_price = "Dal", 0.96
    p4_name, p4_price = "Bread", 5.96
    p5_name, p5_price = "Butter", 1.99
    p6_name, p6_price = "Jam", 1.99
    p7_name, p7_price = "Pasta", 4.99

    items_sold = 7
    subtotal = p1_price + p2_price + p3_price + p4_price + p5_price + p6_price + p7_price
    food_tax = (subtotal * 0.06)
    grand_total = subtotal + food_tax

    return_message = "No returns on meat, produce, milk products."
    appreciation_message = "Thank you for your business!!"

    # Print to console
    print("*" * 49)
    print(f"\t\t\t\t{store_name.title()}")
    print(f"\t\t\t\t{store_street}")
    print(f"\t\t\t\t{store_phone_number}")
    print("=" * 49)
    print(f"Cashier: {cashier_name}")
    print(f"{date_time[0:10]}\t\t\t\t{date_time[11:]}")
    print("=" * 49)
    print("GROCERY")
    print(" ")
    print(f"{p1_name.upper()}\t\t\t\t{p1_price}")
    print(f"{p2_name.upper()}\t\t\t\t{p2_price}")
    print(f"{p3_name.upper()}\t\t\t\t{p3_price}")
    print(f"{p4_name.upper()}\t\t\t\t{p4_price}")
    print(f"{p5_name.upper()}\t\t\t\t{p5_price}")
    print(f"{p6_name.upper()}\t\t\t\t{p6_price}")
    print(f"{p7_name.upper()}\t\t\t\t{p7_price}")
    print(" ")
    print("=" * 49)
    print(f"Subtotal\t\t\t\t\t\t   ${subtotal:.2f}")
    print(f"Food Tax @ 6%\t\t\t\t\t   ${food_tax:.2f}")
    print(f"GRAND TOTAL\t\t\t\t\t   ${grand_total:.2f}")
    print("=" * 49)
    print(" ")
    print(f"TOTAL NUMBER OF ITEMS SOLD =\t   {items_sold}")
    print(" ")
    print(" ")
    print(f"\t{return_message}")
    print(f"\t\t\t{appreciation_message}")

    # Create the PDF
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Items
    y_position = height - 3.25 * inch
    c.setFont("Helvetica", 12)
    items = [
        (p1_name.upper(), p1_price),
        (p2_name.upper(), p2_price),
        (p3_name.upper(), p3_price),
        (p4_name.upper(), p4_price),
        (p5_name.upper(), p5_price),
        (p6_name.upper(), p6_price),
        (p7_name.upper(), p7_price),
    ]

    for name, price in items:
        c.drawString(inch, y_position, name)
        c.drawRightString(width - inch, y_position, f"${price:.2f}")
        y_position -= 0.25 * inch


# Create receipt PDF and print to console
create_receipt("receipt.pdf")
