from geopy.geocoders import Nominatim
from subprocess import Popen, PIPE, STDOUT
from geolite2 import geolite2

print('Program Started...')
addressList = list()
cmd = ['tshark', 'udp']
process = Popen(cmd, stdout=PIPE, stderr=STDOUT)
geolocator = Nominatim(user_agent="Python-IPLocation")
reader = geolite2.reader()


def ipLocation(ip):
    location = reader.get(ip)

    try:
        latitude = location['location']['latitude']
    except:
        latitude = 'Unknown'

    try:
        longitude = location['location']['longitude']
    except:
        longitude = 'Unknown'

    return latitude, longitude


for line in iter(process.stdout.readline, b""):
    columns = str(line).split(" ")
    ipAddress = ''
    if "SKYPE" in columns or "UDP" in columns:
        if "->" in columns:
            ipAddress = columns[columns.index("->") - 1]

        elif "\\xe2\\x86\\x92" in columns:
            ipAddress = columns[columns.index("\\xe2\\x86\\x92") - 1]

        if ipAddress not in addressList:
            addressList.append(ipAddress)
            latitude,longitude = ipLocation(ipAddress)
            try:
                location = geolocator.reverse(f"{latitude}, {longitude}")
                address = location.address
            except:
                address = 'Unknown'
            output = f'''
---------------------------------------------
IP Address: {ipAddress}
Latitude: {latitude}
Longitude: {longitude}
Address: {address}
            '''
            print(output)
