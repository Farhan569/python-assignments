import streamlit as st 

st.title("Unit Converter")

category = st.selectbox("Select Conversion Type", ["Lenght", "Weight", "Temperature"])

if category == "Lenght":
    units = ["Meter", "Kilometer", "Mile", "Foot"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value", min_value=0.0)

    conversion_factors = {
        "Meter": 1,
        "Kilometer": 1000,
        "Mile": 1609.34,
        "Foot": 0.3048
    }

    result = value * conversion_factors[from_unit] / conversion_factors[to_unit]
    st.write(f"Result: {result: .4f} {to_unit}")

elif category == "Weight":
    units = ["Gram", "Kilogram", "Pound"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value", min_value=0.0)

    conversion_factors = {
        "Gram": 1,
        "Kilogram": 1000,
        "Pound": 453.592
    }

    result = value * conversion_factors[from_unit] / conversion_factors[to_unit]
    st.write(f"Resukt: {result: .4f} {to_unit}")

elif category == "Temperature" :
    units = ["Celcius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value")

    def convert_temp(v, from_u, to_u):
        if from_u == to_u:
            return v
        if from_u == "Ferenhiet":
            v = (v - 32) * 5/9
        elif from_u == "Kelvin":
            return v + 273.15
        else :
            return v
        
    result = convert_temp(value, from_unit, to_unit)
    st.write(f"Result: {result: .4f} {to_unit}")
