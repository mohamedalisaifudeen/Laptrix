# cafe website
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import folium
from geopy.geocoders import  Nominatim



asd=r'C:\Users\User\Desktop\Web Development1\cafe\cafes .db'

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



@app.route('/')
def home_page():
    data=cafe.query.all()
    m=folium.Map(location=[51.5072,0.1276])


    geolocator=Nominatim(user_agent='Cafe Shops')

    for item in data:
        location=geolocator.geocode(item.location)
        folium.Marker(location=[location.latitude, location.longitude], popup=item.name, icon=folium.Icon(color='blue')).add_to(m)

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

        dt=cafe(name=name,map_url='none',img_url=image,has_sockets=socket,has_toilet=toilet,has_wifi=wifi,can_take_calls=calls,seats=seats,coffee_price=price,location=place)
        db.session.add(dt)
        db.session.commit()
        return redirect(url_for('home_page'))
    else:
        return render_template('addmore.html')


app.run(debug=True)