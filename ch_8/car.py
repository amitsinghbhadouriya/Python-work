def make_car(manufacturer, model, **kwargs):
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    car_info.update(kwargs)
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
