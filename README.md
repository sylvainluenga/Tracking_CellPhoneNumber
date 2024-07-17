 # Tracking_CellPhoneNumbers
From country name, Network /Service and location

 ### Architecture

Before you start this project you will need an API key
```sh  
for the API key go to : https://opencagedata.com/dashboad  create an account copy the key,
then past it on line 27
you will also need this site : to get the lng&lat of the city, country https://www.latlong.net/
then past it on line 29
```
```sh
If you do download all the file just start yarn install
  Then use all the pip install
  But if you want to follow line by line all you need is to create a folder and have to file on it
   1. main.py
    install all dependancied mention on #pip install
    you will have to run it 3 times
    A. on line 20 print(locations) 
     just to make sure that you do not have any error to identify the correct country
    B. on line print(carrier.name_for_number(service_pro, "en")) 
         just to make sure that you do not have any error to identify the correct network/service
    C. on line print(lng, lat) 
         just to make sure that you do not have any error to identify the exact location 

```

```sh
   2. myphone.py
   on this file you just need onbe line of code
   numer = "type the numbee with country code"

```

 ## Last steps

```sh
the html file one line 41 myMap.save("mylocation.html")
Will created itself automatically after running the project
you will need to open it with any browser of your choice 
```

```sh
By Alex Sylvain Luenga
```
