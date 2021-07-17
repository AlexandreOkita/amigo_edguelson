from events.onMessage import on_message
def configureEvents(client):

    events_list = [
        on_message
    ]
	
    for event in events_list:
        client.event(event)
    return client