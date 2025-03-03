# Real-Time Weather Visualization

## Overview
This project visualizes real-time weather data for selected cities in Vietnam and Canada using Folium. It fetches temperature, humidity, and wind speed data from the WeatherAPI and updates the interactive map every 30 seconds. The project integrates **marker clusters**, **temperature-based icons**, **popups with trend charts**, and a **heatmap** to enhance weather analysis.

## Features
- **Real-Time Weather Updates**: Fetches weather data every 30 seconds.
- **Interactive Map**: Displays temperature, humidity, and wind speed for selected cities.
- **Marker Clustering**: Groups city markers for better visualization.
- **Temperature-Based Icons**: Uses red for high temperatures (>30°C) and blue for lower temperatures.
- **Weather Trend Charts**: Displays temperature trends for each city.
- **Heatmap**: Highlights temperature intensity across locations.

## Dataset & API
- Uses WeatherAPI (`http://api.weatherapi.com/v1/current.json`).
- Requires an API key for data retrieval.
- Cities included:
  - **Vietnam**: Hanoi, Ho Chi Minh, Hai Phong, Nha Trang, Can Tho, Hue, Vung Tau, Da Lat, Buon Ma Thuot, Thanh Hoa, Quy Nhon, Phan Thiet.
  - **Canada**: Toronto, Vancouver, Montreal, Calgary, Edmonton, Ottawa, Winnipeg, Halifax.

## Libraries Used
- `folium` for interactive maps.
- `requests` for API calls.
- `matplotlib` for generating trend charts.
- `base64` & `BytesIO` for embedding charts into popups.
- `IPython.display` for dynamically updating the map.

### Run the Script:
- Ensure you have a valid WeatherAPI key.
- Execute the script in a Jupyter Notebook or Google Colab.
- The map will update in real-time every 30 seconds.

## Learning Outcome
- Fetching and processing real-time data from an API.
- Implementing **dynamic updates** in Python visualizations.
- Enhancing **interactive maps** using marker clusters and heatmaps.
- Embedding **real-time charts** in map popups.