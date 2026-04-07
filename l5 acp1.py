weather_temperature = float(input("What is the temperature outside?? : "))
if weather_temperature <= 18 :
    print("Weather is Chilling Cold ❄️☃️")
    print("You can wear the following :")
    print("""
            1. Sweatshirt
            2. Hoodie
            3. Overshirts """)
elif weather_temperature <= 24:
    print("Weather is pleasant 🌤️🌈")
    print("You can wear the following :")
    print("""
            1. Light T-Shirt
            2. Polo T-Shirt
            3. Thin Shirt """)
else:
    print("Weather is Hot ☀️🌡")
    print("You can wear the following :")
    print("""
            1. Linen Shirts
            2. Cargo Shorts
            3. Cotton T-Shirts """)