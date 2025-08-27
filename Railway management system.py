import json
from datetime import datetime
import os

class Train:
    def __init__(self, train_id, name, total_seats, routes):
        self.train_id = train_id
        self.name = name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.routes = routes  # List of stations
    
    def to_dict(self):
        return {
            'train_id': self.train_id,
            'name': self.name,
            'total_seats': self.total_seats,
            'available_seats': self.available_seats,
            'routes': self.routes
        }
    
    @classmethod
    def from_dict(cls, data):
        train = cls(data['train_id'], data['name'], data['total_seats'], data['routes'])
        train.available_seats = data['available_seats']
        return train

class Schedule:
    def __init__(self, schedule_id, train_id, departure_time, arrival_time, departure_station, arrival_station):
        self.schedule_id = schedule_id
        self.train_id = train_id
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.departure_station = departure_station
        self.arrival_station = arrival_station
    
    def to_dict(self):
        return {
            'schedule_id': self.schedule_id,
            'train_id': self.train_id,
            'departure_time': self.departure_time,
            'arrival_time': self.arrival_time,
            'departure_station': self.departure_station,
            'arrival_station': self.arrival_station
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['schedule_id'], data['train_id'], data['departure_time'], 
                   data['arrival_time'], data['departure_station'], data['arrival_station'])

class Passenger:
    def __init__(self, passenger_id, name, age, gender):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.gender = gender
    
    def to_dict(self):
        return {
            'passenger_id': self.passenger_id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['passenger_id'], data['name'], data['age'], data['gender'])

class Booking:
    def __init__(self, booking_id, passenger_id, train_id, schedule_id, seat_number, booking_date):
        self.booking_id = booking_id
        self.passenger_id = passenger_id
        self.train_id = train_id
        self.schedule_id = schedule_id
        self.seat_number = seat_number
        self.booking_date = booking_date
    
    def to_dict(self):
        return {
            'booking_id': self.booking_id,
            'passenger_id': self.passenger_id,
            'train_id': self.train_id,
            'schedule_id': self.schedule_id,
            'seat_number': self.seat_number,
            'booking_date': self.booking_date
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['booking_id'], data['passenger_id'], data['train_id'], 
                   data['schedule_id'], data['seat_number'], data['booking_date'])

class RailwayManagementSystem:
    def __init__(self):
        self.trains = {}
        self.schedules = {}
        self.passengers = {}
        self.bookings = {}
        self.load_data()
    
    def load_data(self):
        if os.path.exists('trains.json'):
            with open('trains.json', 'r') as f:
                trains_data = json.load(f)
                self.trains = {tid: Train.from_dict(data) for tid, data in trains_data.items()}
        
        if os.path.exists('schedules.json'):
            with open('schedules.json', 'r') as f:
                schedules_data = json.load(f)
                self.schedules = {sid: Schedule.from_dict(data) for sid, data in schedules_data.items()}
        
        if os.path.exists('passengers.json'):
            with open('passengers.json', 'r') as f:
                passengers_data = json.load(f)
                self.passengers = {pid: Passenger.from_dict(data) for pid, data in passengers_data.items()}
        
        if os.path.exists('bookings.json'):
            with open('bookings.json', 'r') as f:
                bookings_data = json.load(f)
                self.bookings = {bid: Booking.from_dict(data) for bid, data in bookings_data.items()}
    
    def save_data(self):
        with open('trains.json', 'w') as f:
            json.dump({tid: train.to_dict() for tid, train in self.trains.items()}, f)
        
        with open('schedules.json', 'w') as f:
            json.dump({sid: schedule.to_dict() for sid, schedule in self.schedules.items()}, f)
        
        with open('passengers.json', 'w') as f:
            json.dump({pid: passenger.to_dict() for pid, passenger in self.passengers.items()}, f)
        
        with open('bookings.json', 'w') as f:
            json.dump({bid: booking.to_dict() for bid, booking in self.bookings.items()}, f)
    
    def add_train(self, train_id, name, total_seats, routes):
        if train_id in self.trains:
            print("Train ID already exists!")
            return False
        self.trains[train_id] = Train(train_id, name, total_seats, routes)
        self.save_data()
        return True
    
    def add_schedule(self, schedule_id, train_id, departure_time, arrival_time, departure_station, arrival_station):
        if schedule_id in self.schedules:
            print("Schedule ID already exists!")
            return False
        if train_id not in self.trains:
            print("Train does not exist!")
            return False
        self.schedules[schedule_id] = Schedule(schedule_id, train_id, departure_time, arrival_time, departure_station, arrival_station)
        self.save_data()
        return True
    
    def add_passenger(self, passenger_id, name, age, gender):
        if passenger_id in self.passengers:
            print("Passenger ID already exists!")
            return False
        self.passengers[passenger_id] = Passenger(passenger_id, name, age, gender)
        self.save_data()
        return True
    
    def book_ticket(self, booking_id, passenger_id, train_id, schedule_id):
        if booking_id in self.bookings:
            print("Booking ID already exists!")
            return False
        if passenger_id not in self.passengers:
            print("Passenger does not exist!")
            return False
        if train_id not in self.trains:
            print("Train does not exist!")
            return False
        if schedule_id not in self.schedules:
            print("Schedule does not exist!")
            return False
        
        train = self.trains[train_id]
        if train.available_seats <= 0:
            print("No seats available on this train!")
            return False
        
        seat_number = train.total_seats - train.available_seats + 1
        booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.bookings[booking_id] = Booking(booking_id, passenger_id, train_id, schedule_id, seat_number, booking_date)
        train.available_seats -= 1
        self.save_data()
        return True
    
    def display_train_info(self, train_id):
        if train_id not in self.trains:
            print("Train not found!")
            return
        train = self.trains[train_id]
        print(f"\nTrain ID: {train.train_id}")
        print(f"Name: {train.name}")
        print(f"Total Seats: {train.total_seats}")
        print(f"Available Seats: {train.available_seats}")
        print(f"Routes: {' -> '.join(train.routes)}")
    
    def display_schedule_info(self, schedule_id):
        if schedule_id not in self.schedules:
            print("Schedule not found!")
            return
        schedule = self.schedules[schedule_id]
        print(f"\nSchedule ID: {schedule.schedule_id}")
        print(f"Train ID: {schedule.train_id}")
        print(f"Departure: {schedule.departure_station} at {schedule.departure_time}")
        print(f"Arrival: {schedule.arrival_station} at {schedule.arrival_time}")
    
    def display_passenger_info(self, passenger_id):
        if passenger_id not in self.passengers:
            print("Passenger not found!")
            return
        passenger = self.passengers[passenger_id]
        print(f"\nPassenger ID: {passenger.passenger_id}")
        print(f"Name: {passenger.name}")
        print(f"Age: {passenger.age}")
        print(f"Gender: {passenger.gender}")
    
    def display_booking_info(self, booking_id):
        if booking_id not in self.bookings:
            print("Booking not found!")
            return
        booking = self.bookings[booking_id]
        print(f"\nBooking ID: {booking.booking_id}")
        print(f"Passenger ID: {booking.passenger_id}")
        print(f"Train ID: {booking.train_id}")
        print(f"Schedule ID: {booking.schedule_id}")
        print(f"Seat Number: {booking.seat_number}")
        print(f"Booking Date: {booking.booking_date}")

def main():
    rms = RailwayManagementSystem()
    
    while True:
        print("\nRailway Management System")
        print("1. Add Train")
        print("2. Add Schedule")
        print("3. Add Passenger")
        print("4. Book Ticket")
        print("5. Display Train Info")
        print("6. Display Schedule Info")
        print("7. Display Passenger Info")
        print("8. Display Booking Info")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            train_id = input("Enter Train ID: ")
            name = input("Enter Train Name: ")
            total_seats = int(input("Enter Total Seats: "))
            routes = input("Enter Routes (comma separated): ").split(',')
            rms.add_train(train_id, name, total_seats, routes)
        
        elif choice == '2':
            schedule_id = input("Enter Schedule ID: ")
            train_id = input("Enter Train ID: ")
            departure_time = input("Enter Departure Time (YYYY-MM-DD HH:MM): ")
            arrival_time = input("Enter Arrival Time (YYYY-MM-DD HH:MM): ")
            departure_station = input("Enter Departure Station: ")
            arrival_station = input("Enter Arrival Station: ")
            rms.add_schedule(schedule_id, train_id, departure_time, arrival_time, departure_station, arrival_station)
        
        elif choice == '3':
            passenger_id = input("Enter Passenger ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender (M/F/O): ")
            rms.add_passenger(passenger_id, name, age, gender)
        
        elif choice == '4':
            booking_id = input("Enter Booking ID: ")
            passenger_id = input("Enter Passenger ID: ")
            train_id = input("Enter Train ID: ")
            schedule_id = input("Enter Schedule ID: ")
            rms.book_ticket(booking_id, passenger_id, train_id, schedule_id)
        
        elif choice == '5':
            train_id = input("Enter Train ID: ")
            rms.display_train_info(train_id)
        
        elif choice == '6':
            schedule_id = input("Enter Schedule ID: ")
            rms.display_schedule_info(schedule_id)
        
        elif choice == '7':
            passenger_id = input("Enter Passenger ID: ")
            rms.display_passenger_info(passenger_id)
        
        elif choice == '8':
            booking_id = input("Enter Booking ID: ")
            rms.display_booking_info(booking_id)
        
        elif choice == '9':
            print("Exiting Railway Management System...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
