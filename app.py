import streamlit as st
import requests
import time
from datetime import datetime



def getWeather(city_name):
    try:
        city = city_name
        api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=408f0c27e53acbc27a001767040fa797"
        json_data = requests.get(api).json()
        country_id = json_data['sys']['country']
        condition = json_data['weather'][0]['main']
        description = (json_data['weather'][0]['description']).title()
        temp = round(float(json_data['main']['temp'] - 273.15),1)
        min_temp = float(json_data['main']['temp_min'] - 273.15)
        max_temp = float(json_data['main']['temp_max'] - 273.15)
        feels_like = round(float(json_data['main']['feels_like'] - 273.15),1)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        visibility = float(int(json_data['visibility'])/1000)
        sunrise = time.strftime("%I:%M",time.gmtime(json_data['sys']['sunrise'] - 19800))	
        sunset = time.strftime("%I:%M",time.gmtime(json_data['sys']['sunset'] - 19800))

        
        st.header(city_name.title() + ', ' + country_id)
        
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        st.subheader('As of ' + current_time)

        

        st.write(condition)

        col1, col2, col3 = st.columns(3)
        col1.metric("🌡️ Temperature", str(temp) + ' °C')
        col2.metric("💨 Wind", str(wind) + ' m/s')
        col3.metric("♨️️Humidity", str(humidity) + '%')

        st.write('')
        st.write('Feels Like ' + str(feels_like) + '°C' + '.  ' + description + '.')
        st.write('')
        st.write('')

        col4, col5, col6 = st.columns(3)
        col4.metric("🌫️ Visibility", str(visibility) + ' km')
        col5.metric("📏 Pressure", str(pressure) + ' hPa')
        col6.metric(" ", " ")

        col7, col8, col9 = st.columns(3)
        col7.metric("🌅 Sunrise", sunrise + " AM")
        col8.metric("🌇 Sunset", sunset + " PM")
        col6.metric(" ", " ")



    except:
        pass
    
    

st.title('Weather Application')

st.caption('Enter a City')
city_name = st.text_input('')

getWeather(city_name)






