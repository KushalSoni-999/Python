import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Analyze Price Differences
def analyze_price_change(file):
    df = pd.read_excel(file)

    # Sort dataframe by Title and Date to ensure latest data is at the bottom
    df_sorted = df.sort_values(by=['Title', 'Date', 'Time'], ascending=[True, True, True])

    # Group the data by Title to check for the latest price difference
    grouped = df_sorted.groupby('Title')

    # Dictionary to hold titles and price differences
    price_diff = {}

    for title, group in grouped:
        latest_row = group.iloc[-1]  # Get the latest entry
        second_latest_row = group.iloc[-2] if len(group) > 1 else None  # Get the second latest entry if available

        if second_latest_row is not None:
            latest_price = float(latest_row['Price'].replace(',', '').replace('₹', '').replace('.', ''))
            prev_price = float(second_latest_row['Price'].replace(',', '').replace('₹', '').replace('.', ''))

            # Calculate price difference
            difference = latest_price - prev_price
            price_diff[title] = difference

    return price_diff

# 2. Send Email Notification
def send_email(subject, body, to_email):
    from_email = "maticauto894@gmail.com"
    password = "jpxoeffmqteyaret"

    # Setup the MIME
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body to the message
    msg.attach(MIMEText(body, 'plain'))

    # Create the server connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    # Send the email
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# 3. Main Function to Perform Analysis and Trigger Email if Needed
def main():
    file_path = 'C:/Users/sonik/python/projects/Amazon data scrapping/laptops.xlsx'  # Path to your Excel file
    df = pd.read_excel(file_path)
    df['Price'] = df['Price'].replace(',', '').replace('₹', '').replace('.', '')
    df.to_excel(file_path, index=False)
    price_changes = analyze_price_change(file_path)

    # Iterate through price changes and check if there is a negative price difference
    for title, difference in price_changes.items():
        if difference < 0:
            subject = f"Price Drop Alert for {title}"
            body = f"The price of {title} has dropped by ₹{-difference}.\nCheck it out!"
            send_email(subject, body, "sonikushal2411@gmail.com")
            print(f"Email sent for {title}.")

if __name__ == '__main__':
    main()
