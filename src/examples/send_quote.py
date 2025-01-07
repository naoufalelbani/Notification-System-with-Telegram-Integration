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
        "type": "quote",
        "content": {
            "text": "The only limit to our realization of tomorrow is our doubts of today.",
            "author": "Franklin D. Roosevelt"
    }
}

    # Send the message
    socket.send_json(alert_message)
    print("Alert message sent.")

if __name__ == "__main__":
    send_alert_message()