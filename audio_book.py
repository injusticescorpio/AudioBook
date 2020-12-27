import pyttsx3
import PyPDF2
book=open('ML.pdf','rb')
pdf_reader=PyPDF2.PdfFileReader(book)
page=pdf_reader.numPages
# print(page)
speaker=pyttsx3.init()
page=pdf_reader.getPage(18)#getting the page 20
text=page.extractText()#extracting the text from page
speaker.say(text)
speaker.runAndWait()



###################inorder to adjust the rate volume and voice in pyttsx3
# use the get getProperty to get the parameters(rate,volume,voice) and use the setProperty to the new value
# use the below the code############
# rate = speaker.getProperty('rate')
# volume = speaker.getProperty('volume')
# voice = speaker.getProperty('voice')
#
# print(rate)
# print(volume)
# print(voice)
#
# rate=50
#
# while(rate<=300):
#     speaker.setProperty('rate', rate)
#     print(f'rate=={rate}')
#     speaker.say("You can't see me ")
#     speaker.runAndWait()
#     rate+=30