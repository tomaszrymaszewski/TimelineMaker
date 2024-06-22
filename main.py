import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsLineItem, \
    QGraphicsTextItem
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPen, QColor
import json


def get_json_info(json_file):
    try:
        info = json.loads(json_file)  # Parse the JSON string
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return [], [], [], 0  # Return 4 values in case of error

    dates = []
    descriptions = []
    no_of_events = 0

    for item in info:
        dates.append(int(item['date']))  # Access the 'date' key within each dictionary
        descriptions.append(item['description'])  # Access the 'description' key
        no_of_events += 1

    return info, dates, descriptions, no_of_events

json_file = input("Enter a paste your json: ")
json_file = json_file.replace('\\n', '')
print(json_file)
info, dates, descriptions, no_of_events = get_json_info(json_file)

print(f"THE JSON IS: {info}")

for i in range(no_of_events):
    print(f"{i + 1}. {descriptions[i]} (in {dates[i]})")

timeline_initial_length = (dates[len(dates) - 1] - dates[0])

scale_factor = 1000 / timeline_initial_length

timeline_length = scale_factor * timeline_initial_length + 100
min_distance_between_events = 50  # Based on size of text (visibility)


class Timeline(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Timeline Example")

        # Set the window geometry (x, y, width, height)
        self.setGeometry(100, 100, 1200, 600)

        # Create a QGraphicsScene to hold the items
        self.scene = QGraphicsScene()

        # Create a QGraphicsView to visualize the scene
        self.view = QGraphicsView(self.scene, self)

        # Set the QGraphicsView as the central widget of the window
        self.setCentralWidget(self.view)

        # Draw the timeline on the scene
        self.draw_timeline()

    def draw_timeline(self):
        # Create a pen to draw the main line of the timeline
        pen = QPen(QColor(0, 0, 0), 2, Qt.DashLine)

        # Draw the main horizontal line of the timeline
        self.scene.addLine(0, 100, timeline_length, 100, pen)

        # Add each event to the timeline
        for i in range(no_of_events - 1):
            self.add_event(
                scale_factor * (dates[i] - dates[0]) + 50,
                descriptions[i],
                str(dates[i])
            )

    def add_event(self, time, label, date_string):
        # Create a pen to draw the vertical line for the event
        pen = QPen(QColor(255, 0, 0), 2)

        # Draw the vertical line at the specified time
        self.scene.addLine(time, 90, time, 110, pen)

        # Create a text item for the event label
        description_item = QGraphicsTextItem(label)
        date_item = QGraphicsTextItem(date_string)

        # Position the text item slightly below the timeline

        description_item.setRotation(90)
        description_item.setPos(QPointF(time + 10, 120))
        date_item.setRotation(90)
        date_item.setPos(QPointF(time + 10, 50))

        # Add the text item to the scene

        self.scene.addItem(description_item)
        self.scene.addItem(date_item)


if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the main window instance
    window = Timeline()

    # Show the main window
    window.show()

    # Execute the application
    sys.exit(app.exec_())
