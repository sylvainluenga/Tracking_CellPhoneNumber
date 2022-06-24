import phonenumbers #pip install phonenumbers
import opencage     #pip install opencage
import folium       #pip install folium
import pyparsing    #pip install pyparsing
import pygame       #pip install pygame

from phonenumbers import carrier
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

#here you need to create a second file name myphone.py
#and it will need only one line of code which is: number = "type phone number with country code" 
from myphone import number


pepnumber = phonenumbers.parse(number)
locations = geocoder.description_for_number(pepnumber, "en")

#this is to tell us the country even if the person is on roaming it will tell the original country of the number
print(locations) 

service_pro = phonenumbers.parse(number)
#her it will tell the the phone number network/service
print(carrier.name_for_number(service_pro, "en")) 

#now go to https://opencagedata.com/dashboad to key API key copy and use it on the next line
geocoder = OpenCageGeocode('past API key here')
geocoder.geocode("South Gate, ZA") #to get the lng & lat of the city, country https://www.latlong.net/
geocoder.reverse_geocode(25.330999, -33.898418) # then copy it on the next line

results = geocoder.geocode('query') 

lng = results[0]['geometry']['lng']
lat = results[0]['geometry']['lat']

print(lng, lat) #remember this project need access to internet to get the last location access

myMap = folium.Map(locations=[lng, lat], zoom_start= 9)
folium.Marker([lng, lat], popup=locations).add_to(myMap)

myMap.save("mylocation.html")
