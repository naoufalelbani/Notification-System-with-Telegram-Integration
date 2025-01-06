# src/main.py
import zmq
import json

def send_alert_message():
    """
    Send an alert message to the ZeroMQ listener.
    """
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://localhost:5555")

    # Define the alert message
    alert_message = {
        "type": "alert",
        "content": {
            "message": "This is an alert message.",
            "type": "FIRE",
            "alert_label": "Alert"
        }
    }

    # Send the message
    socket.send_json(alert_message)
    print("Alert message sent.")

if __name__ == "__main__":
    send_alert_message()