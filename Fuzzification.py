# Step 1: Define fuzzy sets for room temperature and humidity
def fuzzify_room_temperature(value):
    if value < 20:
        return "cold"
    elif 20 <= value < 25:
        return "warm"
    else:
        return "hot"

def fuzzify_humidity(value):
    if value < 40:
        return "low"
    elif 40 <= value < 70:
        return "moderate"
    else:
        return "high"

# Step 2: Define fuzzy rules for AC temperature setting
def fuzzy_rules(room_temp, humidity):
    if room_temp == "cold" and humidity == "low":
        return 22  # 22°C
    elif room_temp == "cold" and humidity == "moderate":
        return 22  # 22°C
    elif room_temp == "cold" and humidity == "high":
        return 22  # 22°C
    
    elif room_temp == "warm" and humidity == "low":
        return 20  # 20°C
    elif room_temp == "warm" and humidity == "moderate":
        return 22  # 22°C
    elif room_temp == "warm" and humidity == "high":
        return 24  # 24°C
    
    elif room_temp == "hot" and humidity == "low":
        return 22  # 22°C
    elif room_temp == "hot" and humidity == "moderate":
        return 24  # 24°C
    elif room_temp == "hot" and humidity == "high":
        return 26  # 26°C

# Step 3: Main function to calculate the AC temperature setting
def calculate_ac_temperature(room_temp_input, humidity_input):
    # Fuzzify the inputs
    room_temp = fuzzify_room_temperature(room_temp_input)
    humidity = fuzzify_humidity(humidity_input)

    # Apply the fuzzy rules
    ac_temp_setting = fuzzy_rules(room_temp, humidity)
    
    return ac_temp_setting

# Example: Calculate the AC temperature setting based on inputs
room_temp_input = 28  # Room temperature in Celsius
humidity_input = 65   # Current humidity percentage

ac_temp = calculate_ac_temperature(room_temp_input, humidity_input)
print(f"Recommended AC Temperature Setting: {ac_temp}°C")
