import streamlit as st

cities = ["Helsinki", "London", "Lagos", "Paris", "Tokyo", "Buenos Aires", 
          "Seattle", "Moscow", "Canberra", "Szczecin", "Berlin", 
          "Manchester", "Delhi", "Istanbul", "Mexico City", 
          "Cairo", "Miami", "Auckland", "Shanghai", "Rio de Janeiro"]

distances = {
    "Helsinki": 5700, "London": 4300, "Lagos": 6000, "Paris": 4400,
    "Tokyo": 7600, "Buenos Aires": 4900, "Seattle": 3100, "Moscow": 5500,
    "Canberra": 8500, "Szczecin": 4800, "Berlin": 4600, "Manchester": 4300,
    "Delhi": 8200, "Istanbul": 6000, "Mexico City": 2200, "Cairo": 6200,
    "Miami": 200, "Auckland": 8000, "Shanghai": 7900,
    "Rio de Janeiro": 4600,
}

st.title("Distance from Tampa International Airport")

# Ask if the user wants to see distances
see_distances = st.radio(
    "Would you like to know the distance of cities from Tampa International Airport?",
    ("Yes", "No")
)

def get_distance(city_name):
    for city in distances:
        if city.lower() == city_name.lower():
            return f"The distance from Tampa International Airport to {city} is approximately {distances[city]} miles."
    return f"Sorry, {city_name} is not in the list."

if see_distances == "Yes":
    # Number of cities
    num_cities = st.number_input("How many cities would you like to know the distance of? (1-20)", min_value=1, max_value=20, value=1)
    
    # Select cities
    selected_cities = st.multiselect(
        "Select the cities (hold Ctrl or Cmd to select multiple):",
        cities,
        max_selections=num_cities
    )
    
    if st.button("Show Distances"):
        for city_choice in selected_cities:
            st.write(get_distance(city_choice))
else:
    st.write("Okay, have a great day!")