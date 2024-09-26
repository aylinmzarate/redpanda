from geopy.geocoders import Nominatim

# Crear un geocodificador con un user_agent único
geolocator = Nominatim(user_agent="my_app")

# Geocodificar una dirección
location = geolocator.geocode("1600 Pennsylvania Ave NW, Washington, DC 20500")

# Mostrar la latitud y longitud
if location:
    print((location.latitude, location.longitude))
else:
    print("Ubicación no encontrada")
