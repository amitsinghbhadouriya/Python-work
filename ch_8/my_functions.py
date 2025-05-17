# my_functions.py

def make_car(manufacturer, model, **kwargs):
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    car_info.update(kwargs)
    return car_info

