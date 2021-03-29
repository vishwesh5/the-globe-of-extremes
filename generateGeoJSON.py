from geojson import Point, Feature, FeatureCollection, dump

features = []

# Charleston, USA
point = Point((-81.633294,38.349497))
fact = "BR: "
country = "USA"
name = "Charleston"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Tuscaloosa, USA
point = Point((33.2098407,-87.56917349999999))
fact = "BR: 294,296,167"
country = "USA"
name = "Tuscaloosa"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Aguascalientes, Mexico
point = Point((22.0375,-102.351))
fact = "BR: 177,247"
country = "Mexico"
name = "Aguascalientes"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Iracemapolis, Brazil
point = Point((-22.583719,-47.523414))
fact = "BRxx"
country = "Brazil"
name = "Iracemápolis"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Buenos Aires, Argentina
point = Point((-34.603722,-58.381592))
fact = "BRxx"
country = "Argentina"
name = "Buenos Aires"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Esipovo, Russia
point = Point((57.630273,32.855286))
fact = "BR: 167"
country = "Russia"
name = "Esipovo"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Beijing, China
point = Point((39.904211,116.407395))
fact = "BR: 177,247,206,254,214,243,293,294,295"
country = "China"
name = "Beijing"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Fuzhou, China
point = Point((26.074508,119.296494))
fact = "BRxx"
country = "China"
name = "Fuzhou"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Pune, India
point = Point((18.5204303,73.85674369999992))
fact = "BRxx"
country = "India"
name = "Pune"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# East London, South Africa
point = Point((-32.983333,27.866667000000007))
fact = "BR: 206"
country = "South Africa"
name = "East London"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Graz, Austria
point = Point((47.070714,15.439503999999943))
fact = "BR:"
country = "Austria"
name = "Graz"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Kecskemet, Hungary
point = Point((46.8963711,19.689686100000017))
fact = "BR: 177,118,206,254"
country = "Hungary"
name = "Kecskemét"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Kecskemet, Hungary
point = Point((61.462532,23.736301))
fact = "BR: 177,253"
country = "Finland"
name = "Valment"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Bremen, Germany
point = Point((53.079296,8.801694))
fact = "BR: 206,236,254,239,293,295,232"
country = "Germany"
name = "Bremen"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Dusseldorf, Germany
point = Point((51.2277411,6.773455600000034))
fact = "BRxx"
country = "Germany"
name = "Düsseldorf"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Hambach, Germany
point = Point((50.398318,7.980559))
fact = "BRxx"
country = "Germany"
name = "Hambach"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Rastatt, Germany
point = Point((48.8591174,8.2059096))
fact = "BR: 177,247,243"
country = "Germany"
name = "Rastatt"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Sindelfingen, Germany
point = Point((48.707456,9.004405))
fact = "BR: 257,214,223,297,192,290"
country = "Germany"
name = "Sindelfingen"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

# Ludwigsfelde, Germany
point = Point((52.301144,13.261627))
fact = "BR: "
country = "Germany"
name = "Ludwigsfelde"

features.append(Feature(geometry=point, properties={"facts": fact,
    "name": name,
    "location": country}))

feature_collection = FeatureCollection(features)

with open('myfile.geojson', 'w') as f:
   dump(feature_collection, f)
