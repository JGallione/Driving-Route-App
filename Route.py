import googlemaps
import folium
import polyline

# API key for accessing the Google Maps API
api_key = '' #API KEY HERE

# Initialize the Google Maps API client
gmaps = googlemaps.Client(api_key)

# List of addresses
addresses = ['Address 1', 'Address 2', 'Address 3', 'Address 4']

# Function to get the optimized driving route between two addresses
def get_driving_route(gmaps, origin, destination):
    route = gmaps.directions(origin, destination, mode="driving")[0]['overview_polyline']['points']
    return polyline.decode(route)

# Get the optimized route as a list of latitudes and longitudes
route_coords = []
for i in range(len(addresses) - 1):
    origin = addresses[i]
    destination = addresses[i + 1]
    route_coords += get_driving_route(gmaps, origin, destination)

# Create the Folium map object
route_map = folium.Map(location=route_coords[0], zoom_start=12)

# Add the optimized route to the map
route = folium.PolyLine(route_coords, color='red', weight=5).add_to(route_map)

# Add the addresses as blue dots to the map
for address in addresses:
    result = gmaps.geocode(address)
    lat = result[0]['geometry']['location']['lat']
    lng = result[0]['geometry']['location']['lng']
    folium.CircleMarker(location=[lat, lng], radius=5, color='blue').add_to(route_map)

# Print the addresses in order
print("Addresses in order:")
for address in addresses:
    print(address)

# Show the map
route_map.save('route_map.html')
