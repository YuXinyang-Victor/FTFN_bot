URL = "https://coubic.com/Embassy-of-Japan/booking_pages#pageContent"
KEY1 = "\"name\":\"Visa (Sightseeing)\",\"paymentMethods\":{\"onlinePaymentEnabled\":false,\"onsitePaymentEnabled\":false,\"payableWithPrepayment\":false,\"payableWithSubscription\":false,\"payableWithTicket\":false},\"lowestPrice\":null,\"uniquePricing\":true,\"publicId\":\"948169\",\"primaryImage\":null,\"scheme\":\"EVENT_SCHEME\",\"status\":\"fully_booked\",\"tagNames\":[],\"vacancyVisibility\":\"hidden\",\"waitingListProvided\":false,\"thumbnailUrl\":\"\""
KEY3 = "\"name\":\"Visa (Sightseeing)\",\"paymentMethods\":{\"onlinePaymentEnabled\":false,\"onsitePaymentEnabled\":false,\"payableWithPrepayment\":false,\"payableWithSubscription\":false,\"payableWithTicket\":false},\"lowestPrice\":null,\"uniquePricing\":true,\"publicId\":\"948169\",\"primaryImage\":null,\"scheme\":\"EVENT_SCHEME\",\"status\":\"closed\",\"tagNames\":[],\"vacancyVisibility\":\"hidden\",\"waitingListProvided\":false,\"thumbnailUrl\":\"\""
KEY2 = "\"name\":\"VISA (Sightseeing)\",\"paymentMethods\":{\"onlinePaymentEnabled\":false,\"onsitePaymentEnabled\":false,\"payableWithPrepayment\":false,\"payableWithSubscription\":false,\"payableWithTicket\":false},\"lowestPrice\":null,\"uniquePricing\":true,\"publicId\":\"914977\",\"primaryImage\":null,\"scheme\":\"EVENT_SCHEME\",\"status\":\"fully_booked\",\"tagNames\":[],\"vacancyVisibility\":\"hidden\",\"waitingListProvided\":false,\"thumbnailUrl\":\"\""
#KEY4 = ""name":"VISA (Sightseeing)","paymentMethods":{"onlinePaymentEnabled":false,"onsitePaymentEnabled":false,"payableWithPrepayment":false,"payableWithSubscription":false,"payableWithTicket":false},"lowestPrice":null,"uniquePricing":true,"publicId":"914977","primaryImage":null,"scheme":"EVENT_SCHEME","status":"fully_booked","tagNames":[],"vacancyVisibility":"hidden","waitingListProvided":false,"thumbnailUrl":""},{"coverContentType":"upload_image","description":{"text":"! Visa applicant who made the appointment booking must be present during application submission !\n\n※Please only book this slot if your travel purpose matches the visa type. Otherwise, your visa application will not be accepted.\n\n※Please only make a booking for ONE appointment slot even if you are submitting multiple visa applications, and fill in the number of applicants accordingly.\n\n\n\nChecklists of Required Documents can be found here\n\n※Please prepare required documents according to the correct checklist by travel purpose and nationality\n\n\n\nNotes:\n\n・Please note that in the event of insufficient documents, the Embassy has the right to not accept your application\n\n・Depending on individual circumstances, additional documents may be requested by the Embassy on a case-by-case basis\n\n・General processing time for visa application is 5 working days. The Embassy does not accommodate to expedite requests"}"
KEY = "<span class=\"Tag_Tag__MEuQu MerchantTag_MerchantTag__gr0Qn MerchantTag_isAccepting__Hr8x5\">Accepting</span>"
CLASS = ['Tag_Tag__MEuQu', 'MerchantTag_MerchantTag__gr0Qn', 'MerchantTag_isAccepting__Hr8x5']

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

should_continue = 0

def check_number_accepting():
    #ignore ssl certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    LoopCount = 0
    #messagebox.showinfo("Start","Tracker in operation!")
    html = urllib.request.urlopen(URL, context=ctx).read() #takes input url
    soup = BeautifulSoup(html, 'html.parser') #returns a soup object

    #Search for number of accepting:
    count = 0
    for i in soup.find_all('span'):
        #print(i.get('class'))
        if i.get('class') == CLASS:
            count += 1
    return count

#Update checking function after Feb 2 update
def check_accepting_script():
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
    print(str_soup)
    print(KEY1 in str_soup)
    print(KEY2 in str_soup)

    if (KEY1 in str_soup or KEY3 in str_soup) and KEY2 in str_soup:
        return False
    else:
        return True