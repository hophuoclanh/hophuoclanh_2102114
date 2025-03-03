# San Francisco Crime Data Visualization

## Overview
This project visualizes crime incidents in San Francisco using Folium, a Python library for interactive maps. The dataset contains crime reports from the San Francisco Police Department for the year 2016. The primary objective is to display crime locations on a map, helping to identify crime hotspots and patterns in the city.

## Dataset
The dataset (`Police_Department_Incidents_Previous_Year_2016.csv`) includes:
- `Category`: The type of crime (e.g., Assault, Theft, Robbery).
- `Descript`: A detailed description of the crime.
- `Address`: The location where the incident occurred.
- `X`: Longitude coordinate.
- `Y`: Latitude coordinate.

## Features
- **Data Sampling:** To improve performance, a random sample of 5000 records is selected.
- **Interactive Map:** Crimes are displayed using markers on a Folium map.
- **Popups & Tooltips:** Clicking on a marker reveals details about the crime (category, description, and location).
- **HTML Map Export:** The final map is saved as an HTML file (`crime_map.html`).

## Libraries Used
- `pandas` for data manipulation.
- `folium` for creating interactive maps.

## Code Execution
Upload the code and dataset to your Google Colab environment and execute the script.

## Learning Outcome
This project provides insights into:
- Using **Folium** to visualize geographic data interactively.
- Handling large datasets efficiently by **sampling**.
- Enhancing data visualization with **popups and tooltips** for better user interaction.