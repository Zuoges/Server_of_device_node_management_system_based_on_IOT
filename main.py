import gui
import mqtt
import threading
import db


def main():
    print("this is main")
    db.connect()
    # gui_task = threading.Thread(target=gui.gui_set)
    mqtt_task = threading.Thread(target=mqtt.MQTT_init)
    tick_task = threading.Thread(target=gui.gui_event)
    # gui_task.setDaemon(True)
    # gui_task.start()
    mqtt_task.start()
    tick_task.start()
    db.select_all()
    gui.gui_set()


if __name__ == '__main__':
    main()
