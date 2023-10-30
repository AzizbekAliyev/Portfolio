car = {  
    "name":"Ferrari",
    "color":"red",
    "year":"2013"
}

info_car = input("Iltimos sizga kerakli malumotni nomini kiriting = ")
def search_car_info(info_car):
    if info_car in car:
        print(f"{info_car} malumotlar bazasida mavjud. ")
        print(car[info_car])
    else:
        print(f"{info_car} malumotlar bazasidan topilmadi. ")
        value_car = input(f"Iltimos {info_car} uchun malumot kiriting = ")
        car[info_car] = value_car
        print(f"\n{info_car} malumotlar bazasiga muvaffaqqiyatli qo'shildi.\n")
        print(car)
        
search_car_info(info_car)
        