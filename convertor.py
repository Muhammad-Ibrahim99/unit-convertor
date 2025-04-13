import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
        margin-bottom: 10px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        color: black;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# title and description:
st.markdown("<h1>♾ Universal Unit Convertor</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# sidebar menu
conversion_type = st.sidebar.selectbox("Select the conversion type:", ["Length", "Weight", "Temperature"])
value  = st.number_input("Enter the value to convert:", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From Unit", ["Meters", "Centimeters", "Millimeters", "Micrometers", "Nanometers", "Feet", "Kilometers", "Miles", "Yards", "Inches"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Meters", "Centimeters", "Millimeters", "Micrometers", "Nanometers", "Feet", "Kilometers", "Miles", "Yards", "Inches"])  
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilograms", "Grams", "Milligrams", "Micrograms", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilograms", "Grams", "Milligrams", "Micrograms", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    
#converted function
def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Micrometers": 1e+6, "Nanometers": 1e+9, "Inches": 39.3701,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
    "Kilograms":1, "Grams":1000, "Milligrams":1e+6, "Micrograms":1e+9, "Pounds":2.20462, "Ounces":35.274,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]


def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 +32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 5/9 + 32 if to_unit == "Fahrenheit" else value
    return value

#button for conversion
if st.button("🤖Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'> {value} {from_unit} = {result: .4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'> Created with ♥ by Muhammad Ibrahim </div>", unsafe_allow_html=True)