☕ Coffee Shop Locator Web Application
A simple yet powerful web application that helps users discover coffee shops ideal for working remotely.
The app displays coffee shop details such as amenities, seating capacity, coffee prices, and more—while also plotting their locations on an interactive map.
✨ Features
Comprehensive Coffee Shop Details
Location
Number of washrooms
Availability of charging ports
Availability of Wi-Fi
Whether calls can be taken
Seating capacity
Coffee prices
Images of the coffee shop
Interactive Map Integration
Plots all coffee shop locations using Folium
Zoom and navigate to find the perfect spot
Add, view, and update coffee shop records
Data persistence with SQLAlchemy
User-Friendly Interface
Simple and clean design for easy navigation
🛠️ Technologies Used
Flask – Python web framework
SQLAlchemy – ORM for database interaction
Folium – Interactive maps
Geopy – Geocoding and location services
⚙️ How It Works
Home Page
Displays all coffee shops from the database
Interactive map with location markers
Add Coffee Shops
Fill out a form with details like name, location, amenities, and images
Location is geocoded and displayed on the map
Manage Coffee Shops
Update existing coffee shop details
Delete records when needed
Database Operations
CRUD operations implemented via Flask + SQLAlchemy
🚀 Installation
Clone the repository
git clone https://github.com/mohamedalisaifudeen/Laptrix.git
cd Laptrix
Create & activate a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
Install dependencies
pip install -r requirements.txt
Run the application
flask run
Open in browser
Visit http://localhost:5000
