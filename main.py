def participant_cost(attendees, food_per_person, transport_per_person):
    return (attendees * food_per_person) + (attendees * transport_per_person)

def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    return participant_cost(attendees, food_per_person, transport_per_person) + venue_cost


def budget_status(budget, total):
    if total <= budget:
        return "Within Budget"
    else:
        return "Over Budget"

def event_summary(event_name, total, status):
    return f"{event_name}: total {total} naira. {status}."


event_name = "Study Day"
attendees = 10
food_per_person = 800
transport_per_person = 200
venue_cost = 5000
budget = 16000


people = participant_cost(attendees, food_per_person, transport_per_person)
total = event_total(attendees, food_per_person, transport_per_person, venue_cost)
status = budget_status(budget, total)
summary = event_summary(event_name, total, status)

print(people)
print(total)
print(status)
print(summary)