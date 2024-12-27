from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Label
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk
from pymavlink import mavutil
import cv2
import time
import datetime
import serial
from threading import Thread

# Paths for assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"") # Images file path should be added here


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Initialize main window
window = Tk()
window.geometry("1820x1024")
window.configure(bg="#000000")

# Canvas setup
canvas = Canvas(
    window,
    bg="#000000",
    height=1024,
    width=1820,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    910.0,
    512.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1359.0,
    526.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    455.0,
    752.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    228.0,
    300.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    681.0,
    300.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    764.0,
    550.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    764.0,
    550.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    142.0,
    550.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    455.0,
    45.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1362.0,
    13.0,
    image=image_image_10
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    126.0,
    44.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    348.0,
    44.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    349.0,
    550.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    557.0,
    550.0,
    image=image_image_15
)


# Graph data
time_values_height = []
height_values = []
time_values_velocity = []
velocity_values = []

# Graph setup for height
fig_height = Figure(figsize=(4, 4), facecolor="#66A0BB")
ax_height = fig_height.add_subplot()
canvas_height = FigureCanvasTkAgg(figure=fig_height, master=window)
canvas_height.draw()
canvas_height.get_tk_widget().place(x=40, y=580)

# Graph setup for velocity
fig_velocity = Figure(figsize=(4, 4), facecolor="#66A0BB")
ax_velocity = fig_velocity.add_subplot()
canvas_velocity = FigureCanvasTkAgg(figure=fig_velocity, master=window)
canvas_velocity.draw()
canvas_velocity.get_tk_widget().place(x=460, y=580)


def update_graphs(height, velocity):
    """Update the height and velocity graphs."""
    time_step = 1
    max_data_points = 10

    while True:
        # Update height graph
        time_values_height.append(time_step)
        height_values.append(height)

        if len(height_values) > max_data_points:
            time_values_height.pop(0)
            height_values.pop(0)

        ax_height.clear()
        ax_height.set_facecolor("#66A0BB")
        ax_height.plot(time_values_height, height_values, marker='o', linestyle='-', color='#eeff00', linewidth=2)
        ax_height.set_xlabel("Time (s)", fontsize=10, fontweight='bold')
        ax_height.set_ylabel("Height (m)", fontsize=10, fontweight='bold')
        ax_height.set_title("Height (m)", fontsize=12, fontweight='bold')
        ax_height.grid(True)

        # Update velocity graph
        time_values_velocity.append(time_step)
        velocity_values.append(velocity)

        if len(velocity_values) > max_data_points:
            time_values_velocity.pop(0)
            velocity_values.pop(0)

        ax_velocity.clear()
        ax_velocity.set_facecolor("#66A0BB")
        ax_velocity.plot(time_values_velocity, velocity_values, marker='o', linestyle='-', color='#00f7f3', linewidth=2)
        ax_velocity.set_xlabel("Time (s)", fontsize=10, fontweight='bold')
        ax_velocity.set_ylabel("Velocity (m/s)", fontsize=10, fontweight='bold')
        ax_velocity.set_title("Velocity (m/s)", fontsize=12, fontweight='bold')
        ax_velocity.grid(True)

        canvas_height.draw()
        canvas_velocity.draw()

        time_step += 1
        time.sleep(1)


# Table setup
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#66A0BB", foreground="black", rowheight=25, fieldbackground="#66A0BB")
style.configure("Treeview.Heading", font=('Lucida Grande', 20, 'bold'))
style.map('Treeview', background=[('selected', '#347083')])


def create_table(parent):
    """Create a table widget."""
    table = ttk.Treeview(parent, columns=("Time", "Latitude", "Longitude"), show="headings")
    table.heading("Time", text="Time")
    table.heading("Latitude", text="Latitude")
    table.heading("Longitude", text="Longitude")
    return table


# Initialize table
data_table = create_table(window)
data_table.place(x=40, y=580, width=810, height=380)


def fetch_uav_data(table, connection, serial_port):
    """Fetch data from UAV and update the table."""
    gps_data = connection.recv_match(type="GPS_RAW_INT", blocking=True).to_dict()
    attitude_data = connection.recv_match(type="ATTITUDE", blocking=True).to_dict()
    system_status = connection.recv_match(type="SYS_STATUS", blocking=True).to_dict()

    latitude = gps_data["lat"] / 1e7
    longitude = gps_data["lon"] / 1e7
    altitude = gps_data["alt"] / 1e3

    log_entry = f"{datetime.datetime.now()}, {latitude}, {longitude}, {altitude}, {gps_data['vel']}, {attitude_data['roll']}, {attitude_data['pitch']}, {attitude_data['yaw']}, {system_status['voltage_battery']}, {system_status['current_battery']}"
    print(log_entry)

    with open("logs.txt", "a") as log_file:
        log_file.write(log_entry + "\n")

    table.insert('', 0, values=(datetime.datetime.now().strftime("%H:%M:%S"), latitude, longitude))
    window.after(1000, lambda: fetch_uav_data(table, connection, serial_port))


# Camera setup
def show_camera_frame():
    """Display the camera feed."""
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (370, 350))
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    camera_label.imgtk = imgtk
    camera_label.configure(image=imgtk)
    camera_label.after(10, show_camera_frame)


camera = cv2.VideoCapture(0)
camera_label = Label(window)
camera_label.place(x=30, y=120)
show_camera_frame()


def connect_to_uav():
    """Establish connection to the UAV."""
    serial_port = serial.Serial("COM1")
    connection = mavutil.mavlink_connection(device="COM3", baud=57600)
    connection.wait_heartbeat()
    print("Connected to UAV")

    fetch_uav_data(data_table, connection, serial_port)

    graph_thread = Thread(target=update_graphs, args=(100, 50), daemon=True)
    graph_thread.start()


def disconnect_from_uav():
    """Disconnect from the UAV."""
    print("Disconnected from UAV")
    camera.release()


# Buttons
connect_button = Button(window, text="Connect", command=connect_to_uav)
connect_button.place(x=10, y=10)

disconnect_button = Button(window, text="Disconnect", command=disconnect_from_uav)
disconnect_button.place(x=100, y=10)

# Finalize window
window.resizable(False, False)
window.mainloop()
