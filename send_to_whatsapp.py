from twilio.rest import Client 
 
account_sid = 'ACbc397bfcdd0072d3c32523d3eafc2125' 
auth_token = '4297be973ed1e304ac36eb7d6ed77df6' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',      
                              to='whatsapp:+4917685621749' 
                          ) 
 
print(message.sid)