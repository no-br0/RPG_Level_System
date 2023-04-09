from typing import Any, Iterable


class EventChain():
    def __init__(self, name:str, next_event:str, next_options:list[str]):
        self.event_name = name
        self.next_event = next_event
        self.next_options = next_options
        
    def __str__(self):
        return f"Current Event: {self.event_name}\nNext Event: {self.next_event}\nNext Options: {self.next_options}\n"
    
    def __repr__(self):
        return f"[{self.event_name} -> {self.next_event}]"



event_list = {}

event_list['wolf_encounter'] = EventChain("wolf_encounter", "wolf_fight", ['wolf_fight', 'run'])
event_list['wolf_fight'] = EventChain("wolf_fight", "death", ['death', 'run'])
event_list['run'] = EventChain('run', 'escape', ['escape', 'death'])


#l = {'wolf_encounter': event_list['wolf_encounter'].__dict__}
#a = l[0]
#b = l[1]
#print(l)
#print(event_list)
#print(event_list["wolf_encounter"].__dict__)

#print(eventChain)


event = event_list['wolf_encounter']

print(event_list[event.next_options[1]])

#print(event_list.keys())
#print(list(event_list.values()))
#print(list(event_list))
#print({k: v.__dict__ for k,v in event_list.items()})