def get_weather(district):
    district = district.lower()
    
    weather_data = {
        "chennai": {"temp": 33, "condition": "Sunny"},
        "coimbatore": {"temp": 28, "condition": "Cloudy"},
        "madurai": {"temp": 32, "condition": "Hot"},
        "trichy": {"temp": 31, "condition": "Sunny"},
        "salem": {"temp": 29, "condition": "Cloudy"},
        "tirunelveli": {"temp": 30, "condition": "Humid"},
        "vellore": {"temp": 32, "condition": "Sunny"},
        "thanjavur": {"temp": 31, "condition": "Hot"},
        "erode": {"temp": 28, "condition": "Cloudy"},
        "dindigul": {"temp": 30, "condition": "Humid"}
    }

    if district in weather_data:
        data = weather_data[district]
        print(f"\nDistrict: {district.title()}")
        print(f"Temperature: {data['temp']}°C")
        print(f"Condition: {data['condition']}\n")
    else:
        print(f"\nNo weather data available for '{district.title()}'\n")


if __name__ == "__main__":
    print("Welcome to Tamil Nadu District Weather App!")
    print("Type a district name to get the weather, or 'exit' to quit.\n")

    while True:
        district_name = input("Enter district name: ").strip()
        if district_name.lower() == "exit":
            print("Goodbye!")
            break
        elif district_name == "":
            print("Please enter a valid district name.\n")
        else:
            get_weather(district_name)
