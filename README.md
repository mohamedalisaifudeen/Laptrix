Coffee Shop Locator Web Application

This web application was created to collect and display the locations of coffee shops that are ideal for people who want to work remotely. The application allows users to see the amenities available at each coffee shop, such as the number of washrooms, charging ports, and other essential features. Additionally, the app provides an interactive map that plots the locations of these coffee shops.

Features

Displays a list of coffee shops along with their details such as:
Location
Number of washrooms
Availability of charging ports
Availability of Wi-Fi
Whether calls can be taken
Seating capacity
Coffee prices
Coffee shop images
Plots the locations of coffee shops on an interactive map using Folium.
Built using Flask and SQLAlchemy to implement CRUD (Create, Read, Update, Delete) operations and understand how databases interact with web applications.
Technologies Used

Flask (Python web framework)
SQLAlchemy (Database ORM)
Folium (For interactive maps)
Geopy (For geolocation)
How It Works

Home Page: The main page displays all coffee shops saved in the database along with their locations plotted on a map.
Adding Coffee Shops: Users can add new coffee shops through a form that collects relevant details such as name, location, amenities, and images.
Map Integration: The locations of the coffee shops are geocoded and displayed as markers on an interactive map.
CRUD Operations: The app performs basic CRUD operations (Create, Read, Update, Delete) on the coffee shops database to manage and display the data.
Installation

Clone the repository:
git clone https://github.com/mohamedalisaifudeen/Laptrix.git
