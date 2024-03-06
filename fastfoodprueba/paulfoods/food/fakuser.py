import csv
import random
from faker import Faker
from faker.providers import address, phone_number, date_time

fake = Faker('es_MX')
fake.add_provider(address)
fake.add_provider(phone_number)
fake.add_provider(date_time)

activity_types = ["terrestre", "acuático", "aéreo"]

activities = [
    "Buceo en cavernas acuático",
    "Rapel en cascadas terrestre",
    "Espeleología en grutas terrestre",
    "Tirolesa sobre cañones terrestre",
    "Escalada en roca terrestre",
    "Descenso en rápidos acuático",
    "Paracaidismo aéreo",
    "Windsurf en mar abierto acuático",
    "Barranquismo terrestre",
    "Salto en bungee aéreo",
    "Recorrido en ATV terrestre",
    "Parapente en montañas aéreo",
    "Surf de remo en ríos acuático",
    "Ala delta en acantilados aéreo",
    "Exploración en motocicleta terrestre",
    "Vuelo en globo aerostático aéreo"
]

locations = [
    "Los Cabos",
    "Cancún",
    "Puerto Vallarta",
    "Acapulco",
    "Tulum",
    "Riviera Maya",
    "Puerto Escondido",
    "Cozumel",
    "Sayulita",
    "Mazatlán",
    "Playa del Carmen",
    "Isla Holbox",
    "Puerto Morelos",
    "Mérida",
    "Zihuatanejo",
    "Manzanillo"
]

def generate_record():
    name = random.choice(activities)
    price_m = round(random.uniform(50, 200), 2)
    price_l = round(price_m * random.uniform(1.1, 1.5), 2)
    desc = fake.sentence(nb_words=6, variable_nb_words=True)
    address = fake.address()
    tel = fake.phone_number()
    estd = random.choice(locations)
    pimage = fake.image_url()
    datev = fake.date_this_year()
    lat = fake.latitude()
    lon = fake.longitude()
    catg = random.choice(activity_types)
    rating = round(random.uniform(1, 5), 1)
    puntos = random.randint(1, 10)
    
    record = {
        "Name": name,
        "PriceM": price_m,
        "PriceL": price_l,
        "Desc": desc,
        "Address": address,
        "Tel": tel,
        "Estd": estd,
        "PImage": pimage,
        "Datev": datev,
        "Lat": lat,
        "Lon": lon,
        "Catg": catg,
        "Rating": rating,
        "Puntos": puntos
    }
    return record

# Generar 100 registros aleatorios
data = [generate_record() for _ in range(100)]

# Escribir los datos en un archivo CSV
csv_file = "actividades_extremas_mexico.csv"
csv_columns = data[0].keys()

with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for record in data:
        writer.writerow(record)

print(f"Se han guardado los datos en {csv_file}.")
