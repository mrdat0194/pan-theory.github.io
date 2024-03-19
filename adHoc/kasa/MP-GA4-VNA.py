from ga4mp import GtagMP
from ga4mp.store import DictStore
import json

# refund
with open("credentials/credentials.json", 'r') as json_file:
    client_config = json.load(json_file)
    measurement_id = client_config['MEASUREMENT_ID']
    api_secret = client_config['API_SECRET']
    client_id = client_config['CLIENT_ID']
    gtag_tracker = GtagMP(api_secret=api_secret, measurement_id=measurement_id, client_id=client_id)

    # Create a new event for purchase.
    purchase_event = gtag_tracker.create_new_event(name="refund")

    # Set transaction_id, value, and currency.
    purchase_event.set_event_param(name="transaction_id", value="t2003")
    purchase_event.set_event_param(name="currency", value="VND")
    purchase_event.set_event_param(name="value", value=30000)

    # Send the event to GA4 immediately.
    event_list = [purchase_event]
    gtag_tracker.send(events=event_list)