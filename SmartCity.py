class Room:
    def __init__(self, room_num=0, size='small', price=30000, no_beds=2):
        self.room_num = room_num
        self.size = size
        self.price = price
        self.no_beds = no_beds
        self.taken = False
        self.r_num = 0



    def set_room_num(self, room_num):
        self.room_num = room_num

    def set_size(self, size):
        self.size = size

    def set_price(self, price):
        self.price = price

    def set_no_beds(self, no_beds):
        self.no_beds = no_beds

    def set_taken(self, taken):
        self.taken = taken

    def display(self):
        print(f"{self.price} {self.room_num} {self.size} {self.no_beds}")


class Client:
    def __init__(self, no=0, name="", contact='', arrival_date="", departure_date="", room_type="", no_rooms=0):
        self.name = name
        self.client_no = no
        self.contact = contact
        self.arrival_date = arrival_date
        self.departure_date = departure_date
        self.room_type = room_type
        self.no_rooms = no_rooms
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

    def book(self, room):
        self.rooms = room
        self.no_rooms += 1
        room.taken = True

    def display(self):
        print(f"{self.client_no} {self.name} {self.no_rooms} {self.room_type} {self.client_no} {self.arrival_date}")


def create_a_room(num):
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

#
#room1 = create_a_room(1)
# client1 = create_a_client(1)
# room1.display()
# client1.display()
# client1.set_client_rooms(room1)
#
# client1.display()



hotel_structure = {
    "Rooms": {

    },
    "Clients": {

    }
}

for i in range(2):
    hotel_structure['Rooms'][f'room{i}'] = {
        "size": "wilfred",
        "price": "Large",
        "no_beds": "0",
        "taken": False,
    }

room = Room(hotel_structure['Rooms'][f'room{1}'])

print(room.r_num)


