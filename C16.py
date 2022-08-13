# %%
class Event:
    def __init__(self, timestamp=0, event_type='', session_id=''):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict):
        self.timestamp = event_dict.get("timestamp")
        self.type = event_dict.get("type")
        self.session_id = event_dict.get("session_id")
    
events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", 
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", 
    },
]


for event in events:
    event_obj = Event(timestamp=event.get("timestamp"),
	              event_type=event.get("type"),
		      session_id=event.get("session_id"))
    print(event_obj.timestamp)

for event in events:
    event_obj = Event()
    event_obj.init_from_dict(event)
    print(event_obj.timestamp)
# %%
class Room1:
   def get_room(self):
       print('room1')
 
class Room2:
   def get_room(self):
       print('room2')
 
   def get_room2(self):
       print('room2 for flat')
 
class Kitchen:
   def get_kitchen(self):
       print('kitchen')
 
class Flat(Kitchen,Room1,Room2):
   ...
 
f=Flat()
f.get_kitchen()
f.get_room()
f.get_room2()
# %%
class Room:
   def get_room(self):
       print('room')
 
class Room1(Room):
   def get_room(self):
       print('room1')
 
class Room2(Room):
   def get_room(self):
       print('room2')
 
 
 
class Flat(Room1,Room2):
   ...
 
print(Flat.mro()) #  метод класса, который показывает порядок наследования
 
f=Flat()
f.get_room()
# %%
