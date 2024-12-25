from flask import Flask, render_template

app = Flask(__name__)

# Örnek araba verileri
cars = [
    {
        'id': 1,
        'name': 'Rolls-Royce Phantom',
        'year': 2024,
        'price': '₺42.750.000',
        'image': 'https://images.unsplash.com/photo-1631295868223-63265b40d9e4',
        'details': '6.75L V12 Motor, 571 HP, 0-100 km/s: 5.3 saniye',
        'color': 'Arctic White',
        'transmission': '8 İleri ZF Otomatik',
        'engine': {
            'type': 'V12 Twin-Turbo',
            'displacement': '6.75L',
            'horsepower': 571,
            'torque': '900 Nm',
            'cylinders': 12
        },
        'performance': {
            'acceleration': 5.3,
            'top_speed': 250,
            'fuel_consumption': '15.7L/100km',
            'emission': '365 g/km'
        },
        'dimensions': {
            'length': '5.762 mm',
            'width': '2.018 mm',
            'height': '1.646 mm',
            'wheelbase': '3.552 mm',
            'weight': '2.560 kg'
        },
        'features': [
            'Starlight Tavan Döşemesi',
            'Bespoke Ses Sistemi',
            'Arka Koltuk Tiyatro Konfigürasyonu',
            'Şampanya Soğutucusu',
            'Özel Deri Döşeme',
            'Planar Süspansiyon Sistemi'
        ]
    },
    {
        'id': 2,
        'name': 'Bentley Continental GT Speed',
        'year': 2024,
        'price': '₺32.950.000',
        'image': 'https://images.unsplash.com/photo-1621136624827-a5fa8bf2b533',
        'details': '6.0L W12 Motor, 650 HP, 0-100 km/s: 3.6 saniye',
        'color': 'Havana Metalik',
        'transmission': '8 İleri Çift Kavrama',
        'engine': {
            'type': 'W12 Twin-Turbo',
            'displacement': '6.0L',
            'horsepower': 650,
            'torque': '900 Nm',
            'cylinders': 12
        },
        'performance': {
            'acceleration': 3.6,
            'top_speed': 335,
            'fuel_consumption': '14.8L/100km',
            'emission': '338 g/km'
        },
        'dimensions': {
            'length': '4.850 mm',
            'width': '1.966 mm',
            'height': '1.405 mm',
            'wheelbase': '2.851 mm',
            'weight': '2.273 kg'
        },
        'features': [
            'Naim for Bentley Ses Sistemi',
            'Döner Gösterge Paneli',
            'Dinamik Ride Sistemi',
            'Karbon Seramik Frenler',
            'Mulliner Sürüş Paketi',
            'City & Touring Specification'
        ]
    },
    {
        'id': 3,
        'name': 'Bugatti Chiron Super Sport',
        'year': 2024,
        'price': '₺185.500.000',
        'image': 'https://images.unsplash.com/photo-1627454819213-0e8d8c7817f6',
        'details': '8.0L W16 Motor, 1600 HP, 0-100 km/s: 2.4 saniye',
        'color': 'Nocturne Siyah',
        'transmission': '7 İleri DSG',
        'engine': {
            'type': 'W16 Quad-Turbo',
            'displacement': '8.0L',
            'horsepower': 1600,
            'torque': '1600 Nm',
            'cylinders': 16
        },
        'performance': {
            'acceleration': 2.4,
            'top_speed': 440,
            'fuel_consumption': '25.2L/100km',
            'emission': '516 g/km'
        },
        'dimensions': {
            'length': '4.544 mm',
            'width': '2.038 mm',
            'height': '1.212 mm',
            'wheelbase': '2.711 mm',
            'weight': '1.975 kg'
        },
        'features': [
            'Karbon Fiber Monokok Şasi',
            'Aktif Aerodinamik Sistem',
            'Özel Michelin Lastikler',
            'Telemetri Sistemi',
            'Sky View Cam Tavan',
            'Burmester 3D Ses Sistemi'
        ]
    },
    {
        'id': 4,
        'name': 'Mercedes AMG GT',
        'year': 2024,
        'price': '₺12.500.000',
        'image': 'https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8',
        'details': 'V8 Biturbo Motor, 585 HP, 0-100 km/s: 3.2 saniye',
        'color': 'Metalik Gri',
        'transmission': 'Otomatik',
        'engine': {
            'type': 'V8 Biturbo',
            'displacement': '4.0L',
            'horsepower': 585,
            'torque': '700 Nm',
            'cylinders': 8
        },
        'performance': {
            'acceleration': 3.2,
            'top_speed': 318,
            'fuel_consumption': '12.5L/100km',
            'emission': '284 g/km'
        },
        'dimensions': {
            'length': '4.544 mm',
            'width': '1.939 mm',
            'height': '1.288 mm',
            'wheelbase': '2.700 mm',
            'weight': '1.645 kg'
        },
        'features': [
            'AMG RIDE CONTROL süspansiyon',
            'AMG DYNAMIC SELECT sürüş modları',
            'Burmester® surround ses sistemi',
            'MBUX multimedya sistemi',
            'AMG Performance koltuklar',
            'LED MULTIBEAM farlar'
        ]
    },
    {
        'id': 5,
        'name': 'Aston Martin DBS Superleggera',
        'year': 2024,
        'price': '₺28.950.000',
        'image': 'https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a',
        'details': '5.2L V12 Twin-Turbo, 725 HP, 0-100 km/s: 3.4 saniye',
        'color': 'British Racing Green',
        'transmission': '8 İleri Otomatik',
        'engine': {
            'type': 'V12 Twin-Turbo',
            'displacement': '5.2L',
            'horsepower': 725,
            'torque': '900 Nm',
            'cylinders': 12
        },
        'performance': {
            'acceleration': 3.4,
            'top_speed': 340,
            'fuel_consumption': '14.4L/100km',
            'emission': '285 g/km'
        },
        'dimensions': {
            'length': '4.712 mm',
            'width': '1.968 mm',
            'height': '1.280 mm',
            'wheelbase': '2.805 mm',
            'weight': '1.693 kg'
        },
        'features': [
            'Bang & Olufsen BeoSound Ses Sistemi',
            'Karbon Fiber Gövde Panelleri',
            'Adaptif Süspansiyon',
            'Ventilli Karbon Seramik Frenler',
            'Bridge of Weir Deri Döşeme',
            '360° Kamera Sistemi'
        ]
    },
    {
        'id': 6,
        'name': 'BMW M4 Competition',
        'year': 2023,
        'price': '₺8.950.000',
        'image': 'https://images.unsplash.com/photo-1617531653332-bd46c24f2068',
        'details': '3.0L Çift Turbo Motor, 510 HP, 0-100 km/s: 3.5 saniye, Maksimum Hız: 290 km/s',
        'color': 'Yarış Mavisi',
        'transmission': 'Otomatik',
        'engine': {
            'type': 'Sıralı 6 Çift Turbo',
            'displacement': '3.0L',
            'horsepower': 510,
            'torque': '650 Nm',
            'cylinders': 6
        },
        'performance': {
            'acceleration': 3.5,
            'top_speed': 290,
            'fuel_consumption': '10.2L/100km',
            'emission': '234 g/km'
        },
        'dimensions': {
            'length': '4.794 mm',
            'width': '1.887 mm',
            'height': '1.393 mm',
            'wheelbase': '2.857 mm',
            'weight': '1.725 kg'
        },
        'features': [
            'M xDrive dört tekerlekten çekiş',
            'Adaptif M süspansiyon',
            'M Servotronic direksiyon',
            'Harman Kardon ses sistemi',
            'BMW Live Cockpit Professional',
            'Lazer LED farlar'
        ]
    },
    {
        'id': 7,
        'name': 'Porsche 911 GT3',
        'year': 2023,
        'price': '₺14.750.000',
        'image': 'https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e',
        'details': '4.0L Boxer Motor, 510 HP, 0-100 km/s: 3.4 saniye, Maksimum Hız: 320 km/s',
        'color': 'Racing Sarı',
        'transmission': 'PDK',
        'engine': {
            'type': 'Naturally Aspirated Boxer',
            'displacement': '4.0L',
            'horsepower': 510,
            'torque': '470 Nm',
            'cylinders': 6
        },
        'performance': {
            'acceleration': 3.4,
            'top_speed': 320,
            'fuel_consumption': '12.4L/100km',
            'emission': '283 g/km'
        },
        'dimensions': {
            'length': '4.573 mm',
            'width': '1.852 mm',
            'height': '1.279 mm',
            'wheelbase': '2.457 mm',
            'weight': '1.435 kg'
        },
        'features': [
            'Porsche Active Suspension Management',
            'Sport Chrono Package',
            'Porsche Ceramic Composite Brake',
            'Porsche Communication Management',
            'GT Sport direksiyon',
            'Dinamik motor takozları'
        ]
    },
    {
        'id': 8,
        'name': 'Audi RS e-tron GT',
        'year': 2023,
        'price': '₺11.250.000',
        'image': 'https://images.unsplash.com/photo-1614200187524-dc4b892acf16',
        'details': 'Çift Elektrik Motoru, 646 HP, 0-100 km/s: 3.3 saniye, Menzil: 472 km',
        'color': 'Metalik Siyah',
        'transmission': 'Otomatik',
        'engine': {
            'type': 'Çift Elektrik Motoru',
            'power': '646 HP',
            'torque': '830 Nm',
            'battery': '93.4 kWh',
            'range': '472 km'
        },
        'performance': {
            'acceleration': 3.3,
            'top_speed': 250,
            'charging_time': '22.5 dakika (5-80%)',
            'energy_consumption': '20.2 kWh/100km'
        },
        'dimensions': {
            'length': '4.989 mm',
            'width': '1.964 mm',
            'height': '1.396 mm',
            'wheelbase': '2.900 mm',
            'weight': '2.347 kg'
        },
        'features': [
            'Adaptif hava süspansiyonu',
            'Dört tekerlekten yönlendirme',
            'Matrix LED farlar',
            'Bang & Olufsen 3D ses sistemi',
            'Audi virtual cockpit plus',
            'e-quattro dört tekerlekten çekiş'
        ]
    },
    {
        'id': 9,
        'name': 'Ferrari F8 Tributo',
        'year': 2023,
        'price': '₺19.850.000',
        'image': 'https://images.unsplash.com/photo-1592198084033-aade902d1aae',
        'details': 'V8 Turbo Motor, 720 HP, 0-100 km/s: 2.9 saniye, Maksimum Hız: 340 km/s',
        'color': 'Rosso Corsa',
        'transmission': 'F1 DCT',
        'engine': {
            'type': 'V8 Twin Turbo',
            'displacement': '3.9L',
            'horsepower': 720,
            'torque': '770 Nm',
            'cylinders': 8
        },
        'performance': {
            'acceleration': 2.9,
            'top_speed': 340,
            'fuel_consumption': '12.9L/100km',
            'emission': '292 g/km'
        },
        'dimensions': {
            'length': '4.611 mm',
            'width': '1.979 mm',
            'height': '1.206 mm',
            'wheelbase': '2.650 mm',
            'weight': '1.435 kg'
        },
        'features': [
            'Ferrari Dynamic Enhancer+',
            'SSC 6.1 yeni nesil kontrol sistemi',
            'Ferrari Peak Performance (FPP)',
            'Karbon fiber yarış koltukları',
            'JBL Professional ses sistemi',
            'Karbon seramik frenler'
        ]
    },
    {
        'id': 10,
        'name': 'Lamborghini Huracán EVO',
        'year': 2023,
        'price': '₺18.950.000',
        'image': 'https://images.unsplash.com/photo-1566473965997-3de9c817e938',
        'details': 'V10 Motor, 640 HP, 0-100 km/s: 2.9 saniye, Maksimum Hız: 325 km/s',
        'color': 'Verde Mantis',
        'transmission': 'LDF',
        'engine': {
            'type': 'V10 Naturally Aspirated',
            'displacement': '5.2L',
            'horsepower': 640,
            'torque': '600 Nm',
            'cylinders': 10
        },
        'performance': {
            'acceleration': 2.9,
            'top_speed': 325,
            'fuel_consumption': '13.7L/100km',
            'emission': '332 g/km'
        },
        'dimensions': {
            'length': '4.520 mm',
            'width': '1.933 mm',
            'height': '1.165 mm',
            'wheelbase': '2.620 mm',
            'weight': '1.422 kg'
        },
        'features': [
            'LDVI (Lamborghini Dinamica Veicolo Integrata)',
            'Magneto-reolojik süspansiyon',
            'Dinamik direksiyon sistemi',
            'Sensonum ses sistemi',
            'Karbon seramik frenler',
            'ALA 2.0 aktif aerodinamik sistem'
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html', cars=cars)

@app.route('/car/<int:car_id>')
def car_detail(car_id):
    car = next((car for car in cars if car['id'] == car_id), None)
    if car:
        return render_template('car_detail.html', car=car)
    return 'Araba bulunamadı', 404

if __name__ == '__main__':
    app.run(debug=True) 