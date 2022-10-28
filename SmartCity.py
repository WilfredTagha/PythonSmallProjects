import json
import re


class Room:
    def __init__(self, room_num, size, price, no_beds):
        self.room_num = room_num
        self.size = size
        self.price = price
        self.no_beds = no_beds
        self.taken = False

    def display(self):
        print(f"{self.room_num}\t\t{self.size}\t{self.no_beds}\t\t{self.price}  ")


class Client:
    def __init__(self, no=0, name="", contact='', arrival_date="", departure_date="", room_type="", no_rooms=0):
        self.name = name
        self.client_no = no
        self.contact = contact
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.room_type = room_type
        self.no_rooms = no_rooms
        self.bill = 0
        self.rooms = []

    def set_client_num(self, client_num):
        self.client_no = client_num

    def set_client_name(self, name):
        self.name = name

    def set_client_contact(self, contact):
        self.contact = contact

    def set_client_arrival_date(self, arrival_date):
        self.arrival_date = arrival_date

    def set_client_departure_date(self, departure_date):
        self.departure_date = departure_date

    def book(self, room_name_id):
        for ids in room_name_id:
            self.rooms.append(ids)
            self.no_rooms += 1
            self.bill += hotel_structure['Rooms'][ids]['price']
            hotel_structure['Rooms'][ids]['taken'] = True
            print("You've successfully booked " + ids)
            print("You're bill is now " + str(self.bill))

    def display(self):
        print(f"{self.client_no} {self.name} {self.no_rooms} {self.room_type} {self.client_no} {self.arrival_date}")


class Admin:
    def __init__(self, name="Admin", password="1234"):
        self.name = name
        self.password = password

    def create_room(self):
        try:
            last_key = list(hotel_structure['Rooms'])[-1]
            last_key_int = int(re.search(r'\d+', last_key).group())
            created_room = create_a_room(last_key_int + 1).__dict__
            hotel_structure['Rooms'][f"room{last_key_int + 1}"] = created_room


        except IndexError:
            created_room = create_a_room(1).__dict__
            hotel_structure['Rooms'].update(room1=created_room)
            print(hotel_structure)


def create_a_room(num=1):
    size = input("please enter the size of the room")
    no_beds = int(input("please enter the number of beds of the room"))
    price = int(input("please enter the price of the room"))
    return Room(num, size, price, no_beds)


def create_a_client(num):
    name = input("Please enter your name")
    #  no_beds = int(input("please enter the number of beds of the room"))
    contact = input("Enter your contact")
    arrival_date = input("please enter the date of today")
    return Client(num, name, contact, arrival_date)


def create_a_new_client():
    try:
        last_key = list(hotel_structure['Clients'])[-1]
        last_key_int = int(re.search(r'\d+', last_key).group())
        created_client = create_a_client(last_key_int + 1)
        hotel_structure['Clients'][f"client{last_key_int + 1}"] = created_client.__dict__
        print(hotel_structure)
        return created_client


    except IndexError:
        created_client = create_a_client(1)
        hotel_structure['Clients'].update(client1=created_client.__dict__)
        print(hotel_structure)
        return created_client


def display_rooms():
    print("RoomID\tSize\tNo_beds\tPrice")
    for each_room in hotel_structure['Rooms']:
        p = hotel_structure['Rooms'][each_room]
        if p['taken'] is False:
            Room(p['room_num'], p['size'], p['price'], p['no_beds']).display()


run = True
while run:
    try:
        with open('hotel_structure.json', 'r') as openfile:
            hotel_structure = json.load(openfile)
    except FileNotFoundError:
        hotel_structure = {
            'Rooms': {},
            'Clients': {}
        }

    responds = int(input("\n\n\nENTER 1 TO ADD ROOMS\nENTER 2 TO VIEW ROOMS\nENTER 3 TO BOOK FOR A ROOM\nTO END ENTER "
                         "ANYOTHER NUMBER\n"))
    if responds not in (1, 2, 3):
        run = False
    if responds == 1:
        a = Admin()
        a.create_room()
    elif responds == 2:
        display_rooms()
    else:
        client = create_a_new_client()
        client_list = []
        c = int(input('how manay rooms do you want to book?'))
        for num in range(c):
            print(f"{c - num} rooms are left for you to book")
            client_list.append("room"+input('enter the id of the room your interested in'))

        client.book(client_list)

    j_hotel_structure = json.dumps(hotel_structure, indent=4)
    with open("hotel_structure.json", "w") as outfile:
        outfile.write(j_hotel_structure)
