import streamlit as st
from PIL import Image
import time

def main():
    # Set page title
    st.set_page_config(page_title="Unit Converter", page_icon="🔄")
    
    # Layout for image and introduction
    col1, col2 = st.columns([1, 2])
    
    with col1:
        image = Image.open("images/unit.png")  # Ensure you have an image in your working directory
        st.image(image, caption="Unit Converter", width=200)
    
    with col2:
        intro_placeholder = st.empty()
        for opacity in range(0, 11):
            intro_placeholder.markdown(f"""
            <h1 style='color: #ff5733; text-align: left; opacity: {opacity /12};'>Welcome to the Unit Converter! 🌟</h2>
            Easily convert between different units of measurement with just a few clicks.<br>
            Select a category and enter the values to get instant results.
            """, unsafe_allow_html=True)
            time.sleep(0.1)
    
    # Heading with animation effect
    title_placeholder = st.empty()
    for opacity in range(0, 11):
        title_placeholder.markdown(f"""
        <h1 style='text-align: center; color: blue; font-size: 36px; opacity: {opacity / 10};'>🔄 Unit Converter 🔄</h1>
        """, unsafe_allow_html=True)
        time.sleep(0.1)
    
    # Unit Conversion Options
    conversion_type = st.selectbox("Select a conversion category", [
        "Length",
        "Weight",
        "Temperature",
        "Speed"
    ], format_func=lambda x: f"{x}", key="conversion", help="Choose a category to convert values.")
    
    # Input value
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    
    if conversion_type == "Length":
        units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Inches": 39.37, "Feet": 3.281}
    elif conversion_type == "Weight":
        units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.205, "Ounces": 35.274}
    elif conversion_type == "Temperature":
        units = {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15}
    elif conversion_type == "Speed":
        units = {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.237}
    
    from_unit = st.selectbox("From", list(units.keys()))
    to_unit = st.selectbox("To", list(units.keys()))
    
    if st.button("Convert"):
        if conversion_type == "Temperature":
            result = units[to_unit](units[from_unit](value))
        else:
            result = (value / units[from_unit]) * units[to_unit]
        
        result_placeholder = st.empty()
        for opacity in range(0, 11):
            result_placeholder.markdown(f"""
            <h3 style='text-align: center; color: #ff33a1; font-size: 24px; opacity: {opacity / 10};'>✅ {value} {from_unit} is equal to <b>{result:.2f} {to_unit}</b></h3>
            """, unsafe_allow_html=True)
            time.sleep(0.1)

if __name__ == "__main__":
    main()
