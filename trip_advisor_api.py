import requests
from pyzipcode import ZipCodeDatabase

api_key = os.environ['TRIP_ADVISOR_KEY']
API_BASE = "http://api.tripadvisor.com/api/partner/2.0/"
zcdb = ZipCodeDatabase()

# uses test data.
def main():
    cuisines = {
        'french': 100,
        'italian': 12,
        'german': 20,
        'american': 40,
    }
    avg_price = 3
    zipcodes = [13346]

    print getRestaurantJson(cuisines, avg_price, zipcodes)

'''
Takes a list of zipcodes and finds the most centralized point in longitude
and latitude
'''
def getCentralLocation(zip_codes):
    lon_sum = sum([zipToLongLat(zip_code)[0] for zip_code in zip_codes])
    lat_sum = sum([zipToLongLat(zip_code)[1] for zip_code in zip_codes])
    return (lon_sum/len(zip_codes), lat_sum/len(zip_codes))

'''
Returns JSON result from Tripadvisor containing nearby restaurants based on
a given longitude and latitude. Returns None with server error or request error.
'''
def getRestaurantJson(cuisines, price, zipcodes):
    params = {}
    lon, lat = getCentralLocation(zipcodes)
    populateParams(params, cuisines, price);  # modified in place.
    r = requests.get(API_BASE + "map/{lat},{lon}/restaurants".format(lon=lon, lat=lat), params=params)
    return r.json()

def populateParams(paramDict, cuisine_dict, avg_price):
    paramDict['key'] = api_key
    cuisines = [k for k in sorted(cuisine_dict, key=lambda k: cuisine_dict[k], reverse=True)][:3]  # Filter to top 3 cuisines
    paramDict['prices'] = [avg_price]
    paramDict['cuisines'] = cuisines

# zip is an integer.
def zipToLongLat(zip):
    zipcode = zcdb[zip]
    return (zipcode.longitude, zipcode.latitude)

if __name__ == '__main__':
    main()
