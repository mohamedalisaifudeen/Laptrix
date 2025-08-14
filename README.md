# ☕ Coffee Shop Locator Web Application

A simple yet powerful web application that helps users discover coffee shops ideal for working remotely.  
The app displays coffee shop details such as amenities, seating capacity, coffee prices, and more—while also plotting their locations on an interactive map.

---

## ✨ Features

### Comprehensive Coffee Shop Details
- Location  
- Number of washrooms  
- Availability of charging ports  
- Availability of Wi-Fi  
- Whether calls can be taken  
- Seating capacity  
- Coffee prices  
- Images of the coffee shop  

### Interactive Map Integration
- Plots all coffee shop locations using **Folium**  
- Zoom and navigate to find the perfect spot  

### Data Management
- Add, view, and update coffee shop records  
- Data persistence with **SQLAlchemy**  

### User-Friendly Interface
- Simple and clean design for easy navigation  

---

## 🛠️ Technologies Used
- **Flask** – Python web framework  
- **SQLAlchemy** – ORM for database interaction  
- **Folium** – Interactive maps  
- **Geopy** – Geocoding and location services  

---

## ⚙️ How It Works

1. **Home Page**  
   - Displays all coffee shops from the database  
   - Interactive map with location markers  

2. **Add Coffee Shops**  
   - Fill out a form with details like name, location, amenities, and images  
   - Location is geocoded and displayed on the map  

3. **Manage Coffee Shops**  
   - Update existing coffee shop details  
   - Delete records when needed  

4. **Database Operations**  
   - CRUD operations implemented via Flask + SQLAlchemy  

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/mohamedalisaifudeen/Laptrix.git
cd Laptrix
```

### 2. Create & activate a virtual environment
```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
flask run
```

### 5. Open in browser  
Visit: [http://localhost:5000](http://localhost:5000)

---
