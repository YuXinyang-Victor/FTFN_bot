URL = "https://coubic.com/Embassy-of-Japan/booking_pages#pageContent"
KEY1 = "\"name\":\"Visa (Sightseeing)\",\"paymentMethods\":{\"onlinePaymentEnabled\":false,\"onsitePaymentEnabled\":false,\"payableWithPrepayment\":false,\"payableWithSubscription\":false,\"payableWithTicket\":false},\"lowestPrice\":null,\"publicId\":\"948169\",\"primaryImage\":null,\"scheme\":\"EVENT_SCHEME\",\"status\":\"fully_booked\",\"tagNames\":[],\"vacancyVisibility\":\"hidden\",\"waitingListProvided\":false,\"thumbnailUrl\":\"\""
KEY2 = "\"name\":\"VISA (Sightseeing)\",\"paymentMethods\":{\"onlinePaymentEnabled\":false,\"onsitePaymentEnabled\":false,\"payableWithPrepayment\":false,\"payableWithSubscription\":false,\"payableWithTicket\":false},\"lowestPrice\":null,\"publicId\":\"914977\",\"primaryImage\":null,\"scheme\":\"EVENT_SCHEME\",\"status\":\"fully_booked\",\"tagNames\":[],\"vacancyVisibility\":\"hidden\",\"waitingListProvided\":false,\"thumbnailUrl\":\"\""
CLASS = ['Tag_Tag__MEuQu', 'MerchantTag_MerchantTag__gr0Qn', 'MerchantTag_isAccepting__Hr8x5']

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

should_continue = 0

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

LoopCount = 0
#messagebox.showinfo(\"Start\",\"Tracker in operation!\")
html = urllib.request.urlopen(URL, context=ctx).read() #takes input url
soup = BeautifulSoup(html, 'html.parser') #returns a soup object

#Search for number of accepting:
str_soup = str(soup)
#print(str_soup)

if KEY1 in str_soup and KEY2 in str_soup:
    print(True)