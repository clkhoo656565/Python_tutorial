import pandas as pd
n = ['$75 $66 / night', '$43 $34 / night', '$80 $72 / night', '$63 / night', '$135 / night', '$71 / night', '$65 $58 / night', '$100 / night', '$75 $68 / night', '$117 / night']
print(type(n))
df = pd.DataFrame(n)
print(type(df))
print(df)

df2 = df.str[1:4]
print(type(df2))
print(df2)

# from ssl import create_default_context
# import pandas as pd
# import smtplib, ssl
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# from email.mime.text import MIMEText
# import password

# class Traveler:

#     # Email Address so user can received the filtered data
#     # Stay: checks if it will be a week, month or weekend
#     def __init__(self, email, stay):
#         self.email = email
#         self.stay = stay

#     # This functtion creates a new csv file based on the options
#     # that the user can afford
#     def price_filter(self, amount):

#         # The user will stay a month
#         if self.stay in ['Month', 'month']:
#             data = pd.read_csv('Airbnb_data.csv')

#             # Monthly prices are usually over a $1,000.
#             # Airbnb includes a comma in thousands making it hard to transform it 
#             # from string to int.

#             # This will create a column that takes only the digits
#             # For example: $1,600 / month, this slicing will only take 1,600
#             print(f"data price {data['Price']}")
#             data['cleaned price'] = data['Price'].str[1:6]
#             print(f"cleaned price {data['cleaned Price']}")

            

#         # The user will stay a weekend
#         elif self.stay in ['Weekend', 'weekend', 'week', 'Week']:
#             data = pd.read_csv('Airbnb_data.csv')

#             # Prices per night are usually between 2 and 3 digits. Example: $50 or $100

#             # This will create a column that takes only the digits
#             # For example: $80 / night, this slicing will only take 80
#             print(f"data type of price {type(data['Price'])}")
#             print(f"data price {data['Price']}")
#             # print(f"This is data in price {data['Price'].str[1:4]}")
#             data['cleaned price'] = data['Price'].str[1:4]
#             print(f"data type of cleaned price {type(data['cleaned price'])}")
#             print(f"cleaned price {data['cleaned price']}")
#             # This time I used the map() instead of list comp but it does the same thing.
#             #data['cleaned price'] = list(map(int, data['cleaned price']))
 
#             # We look for prices that are within the user's range
#             # and save that to a new csv file
#             # filtered_data = data[data['cleaned price'] <= amount]
#             # return filtered_data.to_csv('filtered_data.csv', index=False)

#         else:
#             pass

#     def send_mail(self):
#         # Create a multipart message
#         # It takes the message body, subject, sender, receiver
#         msg = MIMEMultipart()
#         MESSAGE_BODY = 'Here is the list with possible options for your dream vacation'
#         body_part = MIMEText(MESSAGE_BODY, 'plain')
#         msg['Subject'] = "Filtered list of possible airbnb's"
#         msg['From'] = 'clkhoo656565@gmail.com'
#         msg['To'] =  self.email

#         # Attaching the body part to the message
#         msg.attach(body_part)

#         # open and read the CSV file in binary
#         with open('filtered_data.csv','rb') as file:

#             # Attach the file with filename to the email
#             msg.attach(MIMEApplication(file.read(), Name='filtered_data.csv'))

#         context = ssl.create_default_context()
        
        
#         try:
#         # Create SMTP object
#             smtp_obj = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
#         #smtp_obj.starttls()
#             smtp_obj.ehlo()
#             # smtp_obj.starttls(context=context)
#             # smtp_obj.ehlo()
#         # Login to the server, email and password of the sender
#             smtp_obj.login('smtppython502@gmail.com', 'Khoocheelong1')
#             smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
#         except smtplib.SMTPAuthenticationError:
#             print('SMTPAuthenticationError')
#         # Convert the message to a string and send it
#         finally:
#             smtp_obj.quit()

   



# if __name__ == "__main__":
#     my_traveler = Traveler( 'clkhoo656565@hotmail.com', 'week' )
#     my_traveler.price_filter(80)
#     #my_traveler.send_mail()