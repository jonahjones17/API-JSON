import urllib.parse
import requests

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Address: ')

    if address == 'q':
        break

    url = main_api + urllib.parse.urlencode({'address': address})
    print(url)

    json_data = requests.get(url).json()
    json_type = json_data['results'][0]['address_components'][0]['types']
    json_type_single = json_type[0]

    json_status = json_data['status']
    print('API Status: ' + json_status)


    if json_status == 'OK':
        print()
        for each in json_data['results'][0]['address_components']:
            if ['long_name'] == ['short_name']:
                print (each['long_name'])
            else:
                print (json_type_single)
                
            

        formatted_address = json_data['results'][0]['formatted_address']
        print()
        print('Acual address is ' + formatted_address)
        
            
        
