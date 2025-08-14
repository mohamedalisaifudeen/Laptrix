# cafe website
from flask import Flask,render_template,request,redirect,url_for
import folium
from flask_sqlalchemy import SQLAlchemy
from geopy.geocoders import  Nominatim
import ssl
import certifi

asd=r'/Users/mohamedali/Desktop/Folder/laptrix/Laptrix/cafes .db'

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+asd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)



class cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    map_url=db.Column(db.String(100),nullable=False)
    img_url=db.Column(db.String(100),nullable=False)
    location=db.Column(db.String(100),nullable=False)
    has_sockets=db.Column(db.String(100),nullable=False)
    has_toilet=db.Column(db.String(100),nullable=False)
    has_wifi=db.Column(db.String(100),nullable=False)
    can_take_calls=db.Column(db.String(100),nullable=False)
    seats=db.Column(db.String(100),nullable=False)
    coffee_price=db.Column(db.String(100),nullable=False)

location_cache = {}

@app.route('/')
def home_page():
    data=cafe.query.all()
    m=folium.Map(location=[51.5072,0.1276])


    ssl_context = ssl.create_default_context(cafile=certifi.where())
    geolocator = Nominatim(
        user_agent='Cafe Shops',ssl_context=ssl_context,timeout=10)


    for item in data:
        if item.location not in location_cache:
            loc = geolocator.geocode(item.location)
            if loc:
                location_cache[item.location] = (loc.latitude, loc.longitude)
        lat, lon = location_cache[item.location]
        folium.Marker(location=[lat, lon], popup=item.name, icon=folium.Icon(color='blue')).add_to(m)

    map = m.get_root()._repr_html_()
    return render_template('index.html',data=data,map=map)


@app.route("/Add",methods=('GET','POST'))
def adding():
    if(request.method=='POST'):
        name=request.form['name']
        place=request.form['place']
        price=request.form['price']
        seats=request.form['seats']
        socket=request.form['socket']
        toilet=request.form['toilet']
        wifi=request.form['wifi']
        calls=request.form['calls']
        image=request.form['image']
        if not all([name, place, price, image]):
            error_msg = "Please fill in all required fields!"
            return render_template('addmore.html', error=error_msg)
        dt=cafe(name=name,map_url='none',img_url=image,has_sockets=socket,has_toilet=toilet,has_wifi=wifi,can_take_calls=calls,seats=seats,coffee_price=price,location=place)
        db.session.add(dt)
        db.session.commit()
        return redirect(url_for('home_page'))
    else:
        return render_template('addmore.html')


app.run(debug=True)