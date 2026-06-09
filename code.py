chatbot ="I am your chatbot \nTell me what do you want?"
print(chatbot)

def chat_bot():
 while True:
  msg=str(input("You :"))
  if(msg=="Hii"or msg=="Hello"):
    print("Bot : Hello!")
  elif(msg=="How are you?"):
    print("Bot : I am fine , Thank You!")
  elif(msg=="Bye"):
    print("Bot : GoodBye!")
  else:
   print("Bot : Sorry , I don't understand")


chat_bot()