import os
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.icon_definitions import md_icons
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivymd.uix.screen import Screen
from kivy.clock import Clock
from datetime import datetime
import time
from kivy.resources import resource_find
import pandas as pd
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.utils import platform
from kivymd.uix.menu import MDDropdownMenu
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # Pyinstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(os.path.abspath("."), relative_path)

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     if hasattr(sys, '_MEIPASS'):
#         return os.path.join(sys._MEIPASS, relative_path)
#     return os.path.join(os.path.abspath("."), relative_path)



if platform in ('win', 'linux', 'macosx'):
    Window.size = (1280, 720)

class Pg1(Screen):
    def __init__(self, **kwargs):
        super(Pg1, self).__init__(**kwargs)
        Window.set_icon(resource_path("PSM (Phone).jpg"))

        bg_image = Image(source=resource_path("Photo 1.png"),allow_stretch=True,keep_ratio=False)
        self.add_widget(bg_image)

        frame = Image(source=resource_path("frame.png"), size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(frame)

        self.label = Label(text="PEEYESYEM HYUNDAI", color="#00FF00",
                           font_size="25dp", bold=True, pos_hint={'center_x': .5, 'center_y': .65})
        self.add_widget(self.label)

        self.label = Label(text="Enter Mobile Number", color="black",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .61})
        self.add_widget(self.label)

        self.mobile_input = TextInput(size_hint_x=.2, size_hint_y=.05,
                                      multiline=False, pos_hint={'center_x': .5, 'center_y': .56})
        self.add_widget(self.mobile_input)

        self.label = Label(text="Enter Password", color="black",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .51})
        self.add_widget(self.label)

        self.password_input = TextInput(password=True, size_hint_x=.2, size_hint_y=.05,
                                        multiline=False, pos_hint={'center_x': .5, 'center_y': .46})
        self.add_widget(self.password_input)

        self.Login_button = Button(text="Login", font_size="20dp", size_hint_x=.08, size_hint_y=.05,
                                   background_normal="", background_color="red", bold=True, color="white",
                                   pos_hint={'center_x': .4, 'center_y': .38})
        self.Login_button.bind(on_release=self.verify)
        self.add_widget(self.Login_button)

        self.Register_button = Button(text="Register", font_size="20dp", size_hint_x=.1, size_hint_y=.05,
                                      background_normal="", background_color="red",bold=True,
                                      color="white", pos_hint={'center_x': .61, 'center_y': .73})
        self.Register_button.bind(on_release=self.go_to_pg2)
        self.add_widget(self.Register_button)

        self.Exit_button = Button(text="Exit", font_size="20dp", size_hint_x=.08, size_hint_y=.05,
                                  background_normal="", background_color="red",
                                  bold=True, color="white", pos_hint={'center_x': .6, 'center_y': .38},
                                  on_press=App.get_running_app().stop)
        self.Exit_button.bind(on_release=App.get_running_app().stop)
        self.add_widget(self.Exit_button)

        self.Reset_button = Button(text="Reset", font_size="20dp", size_hint_x=.08, size_hint_y=.05,
                                   background_normal="", background_color="red", bold=True, color="white",
                                   pos_hint={'center_x': .5, 'center_y': .38})
        self.Reset_button.bind(on_release=self.reset)
        self.add_widget(self.Reset_button)

        Window.bind(on_key_down=self.on_key_down)

        self.show_password = False
        self.headlight_image = Image(source=resource_path("headlight_off.png"), size_hint=(None, None), size=(100, 100),
                                     pos_hint={'center_x': .61, 'center_y': .47})
        self.headlight_image.bind(on_touch_down=self.on_image_touch)
        self.add_widget(self.headlight_image)

        self.label = Label(text="Page 1", color="black",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .28})
        self.add_widget(self.label)

        self.Register_button = Button(text="Go Page 2", font_size="20dp", size_hint_x=.1, size_hint_y=.05, bold=True,
                                      color="white", pos_hint={'center_x': .59, 'center_y': .28})
        self.Register_button.bind(on_release=self.go_to_pg2)
        self.add_widget(self.Register_button)


    def toggle_password_visibility(self):
        self.show_password = not self.show_password
        self.password_input.password = not self.show_password
        self.headlight_image.source = resource_path("headlight_on.png") if self.show_password else resource_path("headlight_off.png")

    def on_image_touch(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.toggle_password_visibility()
            return True
        return False

    def reset(self, instance):
        self.mobile_input.text = ''
        self.password_input.text = ''

    def verify(self, instance):
        mobile = self.mobile_input.text.strip()
        password = self.password_input.text.strip()
        if not mobile or not password:
            self.show_popup("PSM_Hyundai", "Please fill all field")
            return
        try:
            with open("PSM.txt", "r") as f:
                info = f.readlines()
        except FileNotFoundError:
            self.show_popup("PSM_Hyundai", "User data file not found")
            return

        for line in info:
            parts = line.strip().split(',')
            if len(parts) != 2:
                continue
            u, p = parts
            if u == mobile and p == password:
                if mobile == "9840002856":
                    self.show_popup("Welcome", "Welcome Admin")
                    self.manager.current = "pg7"  # Admin page
                else:
                    self.show_popup("Welcome", f"Welcome {mobile}")
                    self.manager.current = "pg4"  # Regular user page
                return
        self.show_popup("PSM_Hyundai", "Invalid Login")

        self.mobile_input.text = ""
        self.password_input.text = ""

    def on_key_down(self, instance, key, *args):
        if key == 9:
            self.input_fields = [self.mobile_input, self.password_input]
            text_inputs = [i for i in self.input_fields if isinstance(i, TextInput)]
            focused = next((i for i, inp in enumerate(text_inputs) if inp.focus), None)
            if focused is not None:
                next_index = (focused + 1) % len(text_inputs)
                text_inputs[next_index].focus = True
                return True

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, size_hint=(1, 0.7))
        close_button = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(close_button)
        popup = Popup(title=title, content=layout, size_hint=(0.3, 0.3), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def go_to_pg2(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg2()
class Pg2(Screen):
    def __init__(self, **kwargs):
        super(Pg2, self).__init__(**kwargs)

        self.bg = Image(source=resource_path("Photo 2.png"), allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg)

        self.bg = Image(source=resource_path("frame.png"), size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.bg)

        self.label = Label(text="PEEYESYEM HYUNDAI", color="#00FF00", font_size="25dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .65})
        self.add_widget(self.label)

        self.label = Label(text="Register your Mobile Number", color="black", font_size="15dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .6})
        self.add_widget(self.label)

        self.label = Label(text="Enter Mobile Number", color="black", font_size="15dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .55})
        self.add_widget(self.label)

        self.mobile_input = TextInput(size_hint_x=.2, size_hint_y=.05,
                                      multiline=False, pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.mobile_input)

        self.label = Label(text="Enter Your Name", color="black", font_size="15dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .45})
        self.add_widget(self.label)
        self.Name_input = TextInput(size_hint_x=.2, size_hint_y=.05, multiline=False,
                                    pos_hint={'center_x': .5, 'center_y': .41})
        self.add_widget(self.Name_input)

        self.button = Button(text="Register", font_size="20dp", size_hint_x=.1, size_hint_y=.05,
                             background_normal="", background_color="red", bold=True, color="white",
                             pos_hint={'center_x': .5, 'center_y': .35}, on_press=self.verify)
        self.add_widget(self.button)

        self.button = Button(text="Exit", font_size="20dp", size_hint_x=.08, size_hint_y=.05,
                             background_normal="", background_color="red", bold=True, color="white",
                             pos_hint={'center_x': .6, 'center_y': .35}, on_press=App.get_running_app().stop)
        self.add_widget(self.button)

        self.button = Button(text="Reset", font_size="20dp", size_hint_x=.08, size_hint_y=.05, background_normal="",
                             background_color="red", bold=True, color="white",
                             pos_hint={'center_x': .4, 'center_y': .35}, on_press=self.reset)
        self.add_widget(self.button)

        Window.bind(on_key_down=self.on_key_down)

        self.label = Label(text="Page 2", color="white",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .25})
        self.add_widget(self.label)

        self.Register_button = Button(text="Go Page 3", font_size="20dp", size_hint_x=.1, size_hint_y=.05, bold=True,
                                      color="white", pos_hint={'center_x': .59, 'center_y': .28})
        self.Register_button.bind(on_release=self.go_to_pg3)
        self.add_widget(self.Register_button)

    def reset(self, instance):
        self.mobile_input.text = ''
        self.Name_input.text = ''

    def verify(self, instance):
        name = self.Name_input.text.strip().capitalize()
        mobile_number = self.mobile_input.text.strip()

        if not name or not mobile_number:
            self.show_popup("PSM_Hyundai", "Please fill all field")
            return

        # Check if already registered
        try:
            with open("Register.txt", "r") as f:
                lines = f.readlines()
                registered_numbers = [line.strip().split(",")[1] for line in lines if "," in line]
        except FileNotFoundError:
            registered_numbers = []

        if mobile_number in registered_numbers:
            self.show_popup("PSM_Hyundai", "This Number Already Registered")
            self.manager.current = "pg1"
            return

        allowed_numbers = ["9940265365", "9840662434", "9840002856"]
        if mobile_number in allowed_numbers:
            with open("Register.txt", "a") as f:
                f.write(f"{name},{mobile_number}\n")
            self.show_popup("PSM_Hyundai", "Successfully Registered")
            self.manager.current = "pg3"
        else:
            self.show_popup("PSM_Hyundai", "Number Not Allowed")

    def on_key_down(self, instance, key, *args):
        if key == 9:
            self.input_fields = [self.mobile_input, self.Name_input]
            text_inputs = [i for i in self.input_fields if isinstance(i, TextInput)]
            focused = next((i for i, inp in enumerate(text_inputs) if inp.focus), None)
            if focused is not None:
                next_index = (focused + 1) % len(text_inputs)
                text_inputs[next_index].focus = True
                return True

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, size_hint=(1, 0.7))
        close_button = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(close_button)
        popup = Popup(title=title, content=layout, size_hint=(0.3, 0.3), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def go_to_pg3(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg3()

class Pg3(Screen):
    def __init__(self, **kwargs):
        super(Pg3, self).__init__(**kwargs)

        self.bg = Image(source=resource_path("Photo 3.jpg"), allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg)

        self.bg = Image(source=resource_path("frame.png"), size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.bg)

        self.label = Label(text="PEEYESYEM HYUNDAI", color="#00FF00", font_size="25dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .65})
        self.add_widget(self.label)

        self.label = Label(text="Enter Mobile Number", color="black", font_size="15dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .62})
        self.add_widget(self.label)

        self.mobile_input = TextInput(size_hint_x=.2, size_hint_y=.05, multiline=False,
                                      pos_hint={'center_x': .5, 'center_y': .58})
        self.add_widget(self.mobile_input)

        self.label = Label(text="Enter Password", color="black", font_size="15dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .54})
        self.add_widget(self.label)

        self.password_input = TextInput(size_hint_x=.2, size_hint_y=.05, multiline=False,
                                        pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.password_input)

        self.label = Label(text="Conform Password", color="black", font_size="15dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .46})
        self.add_widget(self.label)

        self.confirm_password_input = TextInput(
            size_hint_x=.2, size_hint_y=.05, multiline=False, pos_hint={'center_x': .5, 'center_y': .42})
        self.add_widget(self.confirm_password_input)

        self.button = Button(text="Submit", font_size="20dp", size_hint_x=.1, size_hint_y=.05, background_normal="",
                             background_color="red", bold=True, color="white",
                             pos_hint={'center_x': .50, 'center_y': .35}, on_press=self.verify)
        self.add_widget(self.button)

        Window.bind(on_key_down=self.on_key_down)

        self.label = Label(text="Page 3", color="black",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .25})
        self.add_widget(self.label)

        self.Register_button = Button(text="Go Page 4", font_size="20dp", size_hint_x=.1, size_hint_y=.05, bold=True,
                                      color="white", pos_hint={'center_x': .59, 'center_y': .28})
        self.Register_button.bind(on_release=self.go_to_pg4)
        self.add_widget(self.Register_button)

    def verify(self, instance):
        mobile = self.mobile_input.text.strip()
        password = self.password_input.text.strip()
        confirm_password = self.confirm_password_input.text.strip()

        if not mobile or not password or not confirm_password:
            self.show_popup("PSM_Hyundai", "Please fill all fields")
            return

        found = False
        try:
            with open("Register.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if "," in line:
                        parts = line.strip().split(",")
                        if len(parts) >= 2 and parts[1] == mobile:
                            found = True
                            break

            if found:
                if password == confirm_password:
                    with open("PSM.txt", "a") as f:
                        f.write(f"{mobile},{password}\n")
                    self.show_popup("PSM_Hyundai", "Successfully Registered")
                    self.manager.current = "pg1"
                else:
                    self.show_popup("PSM_Hyundai", "Passwords do not match")
            else:
                self.show_popup("PSM_Hyundai", "Mobile number not found.")
        except Exception as e:
            self.show_popup("PSM_Hyundai", f"Error: {str(e)}")

    def on_key_down(self, instance, key, *args):
        if key == 9:
            self.input_fields = [self.mobile_input, self.password_input, self.confirm_password_input]
            text_inputs = [i for i in self.input_fields if isinstance(i, TextInput)]
            focused = next((i for i, inp in enumerate(text_inputs) if inp.focus), None)
            if focused is not None:
                next_index = (focused + 1) % len(text_inputs)
                text_inputs[next_index].focus = True
                return True


    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, size_hint=(1, 0.7))
        close_button = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(close_button)
        popup = Popup(title=title, content=layout, size_hint=(0.3, 0.3), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def go_to_pg4(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg4()

class Pg4(Screen):
    def __init__(self, **kwargs):
        super(Pg4, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.records = []

        self.bg = Image(source=resource_path("KLK.jpg"), allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg)

        self.bg = Image(source=resource_path("frame.png"), size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.bg)

        self.label = Label(
            text="PEEYESYEM HYUNDAI", color="#00FF00", font_size="25dp",
            bold=True, pos_hint={'center_x': .5, 'center_y': .65})
        self.add_widget(self.label)

        self.label = Label(text="S.C Name", color="black", font_size="15dp", bold=True,
                           pos_hint={'center_x': .5, 'center_y': .6})
        self.add_widget(self.label)

        self.scname_input = TextInput(
            size_hint_x=.2, size_hint_y=.05, multiline=False, pos_hint={'center_x': .5, 'center_y': .55})
        self.add_widget(self.scname_input)

        self.testdrive = Button(text="Test Drive", font_size="20dp", size_hint_x=.15, size_hint_y=.05, bold=True,
                                color="white",background_normal ="", background_color="red",
                                pos_hint={'center_x': .5, 'center_y': .47}, on_press=self.verify)
        self.add_widget(self.testdrive)

        self.Exit = Button(text="Exit", font_size="20dp", size_hint_x=.1, size_hint_y=.05, background_normal="",
                           background_color="red", bold=True, color="white",
                           pos_hint={'center_x': .5, 'center_y': .4}, on_press=App.get_running_app().stop)
        self.add_widget(self.Exit)

        self.label = Label(text="Page 4", color="white",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .25})
        self.add_widget(self.label)

        self.Register_button = Button(text="Go Page 5", font_size="20dp", size_hint_x=.1, size_hint_y=.05, bold=True,
                                      color="white", pos_hint={'center_x': .59, 'center_y': .28})
        self.Register_button.bind(on_release=self.go_to_pg5)
        self.add_widget(self.Register_button)

    def verify(self, instance):
        scname_input = self.scname_input.text.strip()
        name = self.scname_input.text.strip().capitalize()

        if not scname_input:
            self.show_popup("PSM_Hyundai", "Please fill S.C. Name")
            self.scname_input.text = ""  # Clear input
            return
        try:
            with open("records.txt", "r") as f:
                lines = f.readlines()
                for line in reversed(lines):
                    data = line.strip().split(',')
                    if len(data) >= 13:
                        last_scname = data[12].strip()
                        Closing_km = data[9].strip()
                        Time_in = data[10].strip()
                        Usedkm_input = data[11].strip()

                        if scname_input.lower() == last_scname.lower():
                            app = MDApp.get_running_app()
                            app.matched_record = data
                            self.scname_input.text = ""  # Clear input
                            if not Closing_km or not Time_in or not Usedkm_input:
                                app.root.current = 'pg6'
                                self.show_popup("PSM_Hyundai Reminder", "Please complete your previous trip.")
                                return
                            else:
                                break
            with open("Register.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if "," in line:
                        parts = line.strip().split(",")
                        if len(parts) >= 2 and parts[0].strip().lower() == name.lower():
                            MDApp.get_running_app().root.current = 'pg5'
                            self.show_popup("PSM_Hyundai Welcome", "New trip.")
                            self.scname_input.text = ""
                            return
            self.show_popup("PSM_Hyundai", "S.C. Name not Registered")
            self.scname_input.text = ""  # Clear input

        except FileNotFoundError:
            self.show_popup("Error", "File 'records.txt' or 'Register.txt' not found")
            self.scname_input.text = ""  # Clear input

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, size_hint=(1, 0.7))
        close_button = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(close_button)
        popup = Popup(title=title, content=layout, size_hint=(0.3, 0.3), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)

        popup.open()

    def go_to_pg5(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg5()

class Pg5(Screen):
    def __init__(self, **kwargs):
        super(Pg5, self).__init__(**kwargs)
        self.records = []

        with self.canvas.before:
            Color(.06, .65, .65, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        self.label = Label(text="PEEYESYEM HYUNDAI", color="blue", font_size="25dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .13})
        self.add_widget(self.label)

        frame = Image(source=resource_path("Photo-4.png"), size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .35})
        self.add_widget(frame)

        self.layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(self.layout)

        self.table = MDDataTable(size_hint=(1, None),
                                height=dp(210),
                                rows_num=5,
                                check=True,
                                column_data=[
                                    ("S.No", dp(25)),
                                    ("Date", dp(20)),
                                    ("Model", dp(25)),
                                    ("Variant", dp(20)),
                                    ("Reg.No.", dp(25)),
                                    ("Start km", dp(20)),
                                    ("Time out", dp(20)),
                                    ("From", dp(20)),
                                    ("To", dp(25)),
                                    ("S.C Name", dp(25)),
                                    ("Cust Name", dp(25)),
                                    ("Contact No.", dp(25)),
                                    ("Driver", dp(20)),
                                    ("GDMS No.", dp(20)),
                                    ("Gate Pass No.", dp(25))
                                ],
                                row_data=[],
                                )
        scroll = ScrollView(size_hint=(1, 0.6))
        scroll.add_widget(self.table)
        self.layout.add_widget(scroll)

        self.table.bind(on_row_press=self.on_row_press)

        self.date_input = TextInput(hint_text="Date", readonly=True, size_hint_x=.2, size_hint_y=.05,
                                    pos_hint={'center_x': .12, 'center_y': .48})
        self.add_widget(self.date_input)

        self.model_reg_map = {"Ioniq-5": "TN06AD3951",
                              "Tucson": "TN06AH2109",
                              "Alcazar-D": "TN06AH3134",
                              "Verna": "TN06AH6511",
                              "Creta Nline": "TN06AF4383",
                              "Creta IVT": "TN06AF1071",
                              "Creta EV": "TN06AH7576",
                              "Venue Nline": "TN06AF1038",
                              "Venue MT": "TN06AE8192",
                              "i20 Nline": "TN06AE5301",
                              "i20 Amt": "TN06AJ1921",
                              "i20 MT": "TN06AE5361",
                              "Exter Amt": "TN06AE1274",
                              "Exter MT": "TN06AH6544",
                              "Nios Amt": "TN06AF8701",
                              "Aura Amt": "TN06AF8741"}
        self.Model_spinner = Spinner(text="Select Vehicle", values=tuple(self.model_reg_map.keys()),
                                     size_hint_x=.2, size_hint_y=.05, pos_hint={'center_x': .12, 'center_y': .40})
        self.Model_spinner.bind(text=self.update_reg_no_spinner)
        self.add_widget(self.Model_spinner)

        self.Varient_input = TextInput(hint_text="Varient", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                       pos_hint={'center_x': .12, 'center_y': .32})
        self.add_widget(self.Varient_input)

        self.RegNo_input = TextInput(hint_text="Reg. Number", readonly=True, size_hint_x=.2, size_hint_y=.05,
                                     pos_hint={'center_x': .12, 'center_y': .24})
        self.add_widget(self.RegNo_input)

        self.Startkm_input = TextInput(hint_text="Start km", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                       pos_hint={'center_x': .12, 'center_y': .16})
        self.add_widget(self.Startkm_input)

        self.TimeOut_input = TextInput(hint_text="Time Out", readonly=True, size_hint_x=.2, size_hint_y=.05,
                                       pos_hint={'center_x': .12, 'center_y': .08})
        self.add_widget(self.TimeOut_input)

        self.From_input = TextInput(hint_text="From", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                    pos_hint={'center_x': .4, 'center_y': .48})
        self.add_widget(self.From_input)

        self.To_input = TextInput(hint_text="To", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                  pos_hint={'center_x': .63, 'center_y': .48})
        self.add_widget(self.To_input)

        self.scname_input = TextInput(hint_text="S.C Name", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                      pos_hint={'center_x': .87, 'center_y': .48})
        self.add_widget(self.scname_input)

        self.CustName_input = TextInput(hint_text="Cust Name", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                        pos_hint={'center_x': .87, 'center_y': .40})
        self.add_widget(self.CustName_input)

        self.ContactNo_input = TextInput(hint_text="Contact No.", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                         pos_hint={'center_x': .87, 'center_y': .32})
        self.add_widget(self.ContactNo_input)

        self.Driver_input = TextInput(hint_text="Driver", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                      pos_hint={'center_x': .87, 'center_y': .24})
        self.add_widget(self.Driver_input)

        self.GDMSNo_input = TextInput(hint_text="GDMS No", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                      pos_hint={'center_x': .87, 'center_y': .16})
        self.add_widget(self.GDMSNo_input)

        self.GatePassNo_input = TextInput(hint_text="Gate Pass No", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                          pos_hint={'center_x': .87, 'center_y': .08})
        self.add_widget(self.GatePassNo_input)

        self.AddRecord_button = Button(text="Add Record", font_size="20dp", size_hint_x=.15, size_hint_y=.05,
                                       background_normal="", background_color="red", bold=True,
                                       color="white", pos_hint={'center_x': .62, 'center_y': .08})
        self.AddRecord_button.bind(on_release=self.add_record)
        self.add_widget(self.AddRecord_button)

        self.Exit_button = Button(text="Exit", font_size="20dp", size_hint_x=.15, size_hint_y=.05,
                                  background_normal = "" ,background_color= "red", bold=True,
                                  color="white", pos_hint={'center_x': .4, 'center_y': .08})
        self.Exit_button.bind(on_release=App.get_running_app().stop)
        self.add_widget(self.Exit_button)

        Clock.schedule_once(self.set_current_datetime)
        Window.bind(on_key_down=self.on_key_down)

        self.label = Label(text="Page 5", color="white",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .25})
        self.add_widget(self.label)

        self.Register_button = Button(text="Go Page 6", font_size="20dp", size_hint_x=.1, size_hint_y=.05, bold=True,
                                      color="white", pos_hint={'center_x': .59, 'center_y': .28})
        self.Register_button.bind(on_release=self.go_to_pg6)
        self.add_widget(self.Register_button)

    def add_record(self, instance):
        date = self.date_input.text.strip()
        Model = self.Model_spinner.text.strip()
        Varient = self.Varient_input.text.strip()
        RegNo = self.RegNo_input.text.strip()
        Startkm = self.Startkm_input.text.strip()
        TimeOut = self.TimeOut_input.text.strip()
        From = self.From_input.text.strip()
        To = self.To_input.text.strip()
        scname = self.scname_input.text.strip()
        CustName = self.CustName_input.text.strip()
        ContactNo = self.ContactNo_input.text.strip()
        Driver = self.Driver_input.text.strip()
        GDMSNo = self.GDMSNo_input.text.strip()
        GatePassNo = self.GatePassNo_input.text.strip()

        sno = 1
        if os.path.exists("records.txt"):
            with open("records.txt", "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    if last_line:
                        last_sno = last_line.split(",")[0].strip()
                        if last_sno.isdigit():
                            sno = int(last_sno) + 1
                        else:
                            sno = 1
                    else:
                        sno = 1
                else:
                    sno = 1

        if not all(
                [date, Model, Varient, RegNo, Startkm, TimeOut, From, To, scname, CustName, ContactNo, Driver, GDMSNo,
                 GatePassNo]):
            self.show_popup("PSM_Hyundai", "Please Fill all Field")
            return

        with open("records.txt", "a") as f:
            data = [sno, date, Model, Varient, RegNo, Startkm, TimeOut,
                    From, To, "", "", "", scname, CustName,ContactNo, Driver, GDMSNo, GatePassNo]
            f.write(",".join(map(str, data)) + "\n")

        self.records.append((str(sno), date, Model, Varient, RegNo, Startkm, TimeOut, From, To, scname, CustName,
                             ContactNo, Driver, GDMSNo, GatePassNo))
        self.table.row_data.append((str(sno), date, Model, Varient, RegNo, Startkm, TimeOut, From, To, scname, CustName,
                                    ContactNo, Driver, GDMSNo, GatePassNo))
        self.table.update_row_data(self.table, self.records)
        self.show_popup("PSM_Hyundai", "Record Added Successfully")
        self.clear_inputs()
    def clear_inputs(self):
        self.Varient_input.text = ""
        self.RegNo_input.text = ""
        self.Startkm_input.text = ""
        self.From_input.text = ""
        self.To_input.text = ""
        self.scname_input.text = ""
        self.CustName_input.text = ""
        self.ContactNo_input.text = ""
        self.Driver_input.text = ""
        self.GDMSNo_input.text = ""
        self.GatePassNo_input.text = ""

    def update_reg_no_spinner(self, spinner, selected_model):
        reg_no = self.model_reg_map.get(selected_model)
        if reg_no:
            self.RegNo_input.text = reg_no

    def set_current_datetime(self, *args):
        self.date_input.text = datetime.now().strftime('%d/%m/%Y')
        current_time = time.strftime("%I:%M %p")
        self.TimeOut_input.text = current_time

    def on_row_press(self, instance_table, instance_row):
        self.selected_row_data = instance_table.row_data[instance_row.index]

    def on_model_selected(self, spinner, text):
        self.RegNo_input.text = self.model_reg_map.get(text, "")

    def on_key_down(self, instance, key, *args):
        if key == 9:  # Tab key
            self.input_fields = [self.Varient_input, self.Startkm_input, self.From_input,
                                 self.To_input, self.scname_input,
                                 self.CustName_input, self.ContactNo_input, self.Driver_input,
                                 self.GDMSNo_input, self.GatePassNo_input]
            text_inputs = [i for i in self.input_fields if isinstance(i, TextInput)]
            focused = next((i for i, inp in enumerate(text_inputs) if inp.focus), None)
            if focused is not None:
                next_index = (focused + 1) % len(text_inputs)
                text_inputs[next_index].focus = True
                return True

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, size_hint=(1, 0.7))
        close_button = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(close_button)
        popup = Popup(title=title, content=layout, size_hint=(0.3, 0.3), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def go_to_pg6(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg6()

class Pg6(Screen):
    def __init__(self, **kwargs):
        super(Pg6, self).__init__(**kwargs)
        self.records = []

        with self.canvas.before:
            Color(.06, .65, .65, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        frame = Image(source=resource_path("Photo-4.png"), size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .25})
        self.add_widget(frame)

        self.layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(self.layout)

        self.table = MDDataTable(
            size_hint=(1, None),
            height=dp(210),
            rows_num=5,
            check=True,
            column_data=[
                ("S.No", dp(25)),
                ("Date", dp(20)),
                ("Model", dp(25)),
                ("Variant", dp(20)),
                ("Reg.No.", dp(25)),
                ("Start km", dp(20)),
                ("Time out", dp(20)),
                ("From", dp(20)),
                ("To", dp(25)),
                ("Closing km", dp(20)),
                ("Time in", dp(16)),
                ("Used km", dp(20)),
                ("S.C Name", dp(25)),
                ("Cust Name", dp(25)),
                ("Contact No.", dp(25)),
                ("Driver", dp(20)),
                ("GDMS No.", dp(20)),
                ("Gate Pass No.", dp(25))
            ],
            row_data=[],
        )
        table_container = AnchorLayout(anchor_x='left', anchor_y='top')
        table_container.add_widget(self.table)
        self.layout.add_widget(table_container)

        self.table.bind(on_row_press=self.on_row_press)

        self.date_input = TextInput(hint_text="Date", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                    pos_hint={'center_x': .12, 'center_y': .48})
        self.add_widget(self.date_input)

        self.Model_input = TextInput(hint_text="Model", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                     pos_hint={'center_x': .12, 'center_y': .40})
        self.add_widget(self.Model_input)

        self.Varient_input = TextInput(hint_text="Varient", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                       pos_hint={'center_x': .12, 'center_y': .32})
        self.add_widget(self.Varient_input)

        self.RegNo_input = TextInput(hint_text="Reg. Number", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                     pos_hint={'center_x': .12, 'center_y': .24})
        self.add_widget(self.RegNo_input)

        self.Startkm_input = TextInput(hint_text="Start km", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                       pos_hint={'center_x': .12, 'center_y': .16})
        self.add_widget(self.Startkm_input)

        self.TimeOut_input = TextInput(hint_text="Time Out", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                       pos_hint={'center_x': .12, 'center_y': .08})
        self.add_widget(self.TimeOut_input)

        self.From_input = TextInput(hint_text="From", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                    pos_hint={'center_x': .4, 'center_y': .48})
        self.add_widget(self.From_input)

        self.To_input = TextInput(hint_text="To", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                  pos_hint={'center_x': .63, 'center_y': .48})
        self.add_widget(self.To_input)

        self.Closingkm_input = TextInput(hint_text="Closing km", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                         pos_hint={'center_x': .4, 'center_y': .40})
        self.add_widget(self.Closingkm_input)

        self.Timein_input = TextInput(hint_text="Time in", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                      pos_hint={'center_x': .63, 'center_y': .40})
        self.add_widget(self.Timein_input)

        self.Usedkm_input = TextInput(hint_text="Used km", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                      pos_hint={'center_x': .52, 'center_y': .32})
        self.add_widget(self.Usedkm_input)

        self.scname_input = TextInput(hint_text="S.C Name", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                      pos_hint={'center_x': .87, 'center_y': .48})
        self.add_widget(self.scname_input)

        self.CustName_input = TextInput(hint_text="Cust Name", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                        pos_hint={'center_x': .87, 'center_y': .40})
        self.add_widget(self.CustName_input)

        self.ContactNo_input = TextInput(hint_text="Contact No.", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                         pos_hint={'center_x': .87, 'center_y': .32})
        self.add_widget(self.ContactNo_input)

        self.Driver_input = TextInput(hint_text="Driver", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                      pos_hint={'center_x': .87, 'center_y': .24})
        self.add_widget(self.Driver_input)

        self.GDMSNo_input = TextInput(hint_text="GDMS No", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                      pos_hint={'center_x': .87, 'center_y': .16})
        self.add_widget(self.GDMSNo_input)

        self.GatePassNo_input = TextInput(hint_text="Gate Pass No", readonly=False, size_hint_x=.2, size_hint_y=.05,
                                          pos_hint={'center_x': .87, 'center_y': .08})
        self.add_widget(self.GatePassNo_input)


        self.SelectRecord_button = Button(text="Select Record", font_size="20dp", size_hint_x=.18, size_hint_y=.05,background_normal = "" ,background_color= "red",
                                          bold=True, color="white", pos_hint={'center_x': .48, 'center_y': .08})
        self.SelectRecord_button.bind(on_release=self.select_record)
        self.add_widget(self.SelectRecord_button)

        self.UpdateRecord_button = Button(text="Update Record", font_size="20dp", size_hint_x=.18, size_hint_y=.05,background_normal = "" ,background_color= "red",
                                          bold=True, color="white", pos_hint={'center_x': .67, 'center_y': .08})
        self.UpdateRecord_button.bind(on_release=self.update_record)
        self.add_widget(self.UpdateRecord_button)

        self.Exit_button = Button(text="Exit", font_size="20dp", size_hint_x=.15, size_hint_y=.05, bold=True,background_normal = "" ,background_color= "red",
                                  color="white", pos_hint={'center_x': .3, 'center_y': .08})
        self.Exit_button.bind(on_release=App.get_running_app().stop)
        self.add_widget(self.Exit_button)

        self.label = Label(text="Page 6", color="white",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .25})
        self.add_widget(self.label)

        self.Register_button = Button(text="Go Page 7", font_size="20dp", size_hint_x=.1, size_hint_y=.05, bold=True,
                                      color="white", pos_hint={'center_x': .59, 'center_y': .28})
        self.Register_button.bind(on_release=self.go_to_pg7)
        self.add_widget(self.Register_button)

        Window.bind(on_key_down=self.on_key_down)
    def on_row_press(self, instance_table, instance_row):
        self.selected_row_data = instance_table.row_data[instance_row.index]

    def on_pre_enter(self, *args):
        app = MDApp.get_running_app()

        if not hasattr(app, 'matched_record'):
            print("No matched_record found. Going back to Pg6.")
            self.manager.current = 'pg6'
            return
        data = app.matched_record

        sno = data[0]
        date = data[1]
        Model = data[2]
        Varient = data[3]
        RegNo = data[4]
        Startkm = data[5]
        TimeOut = data[6]
        From = data[7]
        To = data[8]
        Closingkm = data[9]
        Timein = data[10]
        Usedkm = data[11]
        scname = data[12]
        CustName = data[13]
        ContactNo = data[14]
        Driver = data[15]
        GDMSNo = data[16]
        GatePassNo = data[17]

        self.records.append((sno, date, Model, Varient, RegNo, Startkm, TimeOut, From, To, Closingkm, Timein,
                             Usedkm, scname, CustName, ContactNo, Driver, GDMSNo, GatePassNo))
        self.table.row_data.append((sno, date, Model, Varient, RegNo, Startkm, TimeOut, From, To, Closingkm, Timein,
                            Usedkm, scname, CustName, ContactNo, Driver, GDMSNo, GatePassNo))
        self.table.update_row_data(self.table, self.records)

    def clear_inputs(self):
        self.date_input.text = ""
        self.Model_input.text = ""
        self.Varient_input.text = ""
        self.RegNo_input.text = ""
        self.Startkm_input.text = ""
        self.TimeOut_input.text = ""
        self.From_input.text = ""
        self.To_input.text = ""
        self.Closingkm_input.text = ""
        self.Timein_input.text = ""
        self.Usedkm_input = ""
        self.scname_input.text = ""
        self.CustName_input.text = ""
        self.ContactNo_input.text = ""
        self.Driver_input.text = ""
        self.GDMSNo_input.text = ""
        self.GatePassNo_input.text = ""


    def select_record(self, instance):
        if hasattr(self, 'selected_row_data'):
            selected_row = self.selected_row_data

            (sno, date, model, varient, regno, startkm, timeout, from_place, to_place, closingkm, timein,
             usedkm, scname, custname, contactno, driver, gdmsno, gatepassno) = selected_row

            self.date_input.text = date
            self.Model_input.text = model
            self.Varient_input.text = varient
            self.RegNo_input.text = regno
            self.Startkm_input.text = startkm
            self.TimeOut_input.text = timeout
            self.From_input.text = from_place
            self.To_input.text = to_place
            self.Closingkm_input.text = closingkm
            self.Timein_input.text = timein
            self.Usedkm_input.text = usedkm
            self.scname_input.text = scname
            self.CustName_input.text = custname
            self.ContactNo_input.text = contactno
            self.Driver_input.text = driver
            self.GDMSNo_input.text = gdmsno
            self.GatePassNo_input.text = gatepassno
        else:
            self.show_popup("PSM_Hyundai", "No record selected.")

    def on_enter(self):
        self.Startkm_input.bind(text=self.auto_calculate_used_km)
        self.Closingkm_input.bind(text=self.auto_calculate_used_km)
    def auto_calculate_used_km(self, instance, value):
        try:
            start_km = int(self.Startkm_input.text.strip())
            closing_km = int(self.Closingkm_input.text.strip())
            if closing_km >= start_km:
                self.Usedkm_input.text = str(closing_km - start_km)
            else:
                self.Usedkm_input.text = ""
        except ValueError:
            self.Usedkm_input.text = ""

    def update_record(self, instance):
        if hasattr(self, 'selected_row_data'):
            selected_row = self.selected_row_data
            try:
                selected_index = self.records.index(selected_row)
            except ValueError:
                self.show_popup("PSM_Hyundai", "Selected record not found in records list.")
                return

            try:
                start_km = int(self.Startkm_input.text.strip())
                closing_km = int(self.Closingkm_input.text.strip())
            except ValueError:
                self.show_popup("PSM_Hyundai", "Start Km and Closing Km must be valid whole numbers.")
                return

            if closing_km < start_km:
                self.show_popup("PSM_Hyundai", "Closing Km must be greater than or equal to Start Km.")
                return
            Used_km = closing_km - start_km
            self.Usedkm_input.text = str(Used_km)

            updated_record = (
                selected_row[0],
                self.date_input.text,
                self.Model_input.text,
                self.Varient_input.text,
                self.RegNo_input.text,
                str(start_km),
                self.TimeOut_input.text,
                self.From_input.text,
                self.To_input.text,
                str(closing_km),
                self.Timein_input.text,
                str(Used_km),
                self.scname_input.text,
                self.CustName_input.text,
                self.ContactNo_input.text,
                self.Driver_input.text,
                self.GDMSNo_input.text,
                self.GatePassNo_input.text
            )
            self.records[selected_index] = updated_record
            self.table.row_data = self.records.copy()
            self.table.update_row_data(self.table, self.records)

            try:
                with open("records.txt", "w") as f:
                    for rec in self.records:
                        f.write(",".join(rec) + "\n")

                self.show_popup("PSM_Hyundai", "Record updated successfully.")
                self.clear_inputs()
                self.Closingkm_input.text = ""
                self.Timein_input.text = ""

            except Exception as e:
                self.show_popup("PSM_Hyundai", f"Error while updating file: {str(e)}")


    def on_key_down(self, instance, key, *args):
        if key == 9:
            self.input_fields = [self.date_input, self.Model_input, self.Varient_input, self.RegNo_input,
                                 self.Startkm_input,
                                 self.TimeOut_input, self.From_input, self.To_input, self.Closingkm_input,
                                 self.Timein_input, self.Usedkm_input, self.scname_input, self.CustName_input,
                                 self.ContactNo_input, self.Driver_input, self.GDMSNo_input, self.GatePassNo_input]
            text_inputs = [i for i in self.input_fields if isinstance(i, TextInput)]
            focused = next((i for i, inp in enumerate(text_inputs) if inp.focus), None)
            if focused is not None:
                next_index = (focused + 1) % len(text_inputs)
                text_inputs[next_index].focus = True
                return True

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, size_hint=(1, 0.7))
        close_button = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(close_button)
        popup = Popup(title=title, content=layout, size_hint=(0.4, 0.4), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()
    def go_to_pg7(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg7()

class Pg7(Screen):
    def __init__(self, **kwargs):
        super(Pg7, self).__init__(**kwargs)

        self.bg = Image(source=resource_path("Delivery.jpg"), allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg)

        self.bg = Image(source=resource_path("frame.png"), size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.bg)

        self.label = Label(text="PEEYESYEM HYUNDAI", color="#00FF00", font_size="25dp", bold=True,
                           pos_hint={'center_x': .5, 'center_y': .65})
        self.add_widget(self.label)

        self.IncompleateRecord = Button(text="In complete Demo", font_size="20dp", size_hint_x=.25, size_hint_y=.05,background_normal = "" ,background_color= "red",
                            bold=True, color="white", pos_hint={'center_x': .5, 'center_y': .58}, on_press=self.verify)
        self.add_widget(self.IncompleateRecord)
        self.CompleateRecord = Button(text="Complete Demo", font_size="20dp", size_hint_x=.25, size_hint_y=.05,background_normal = "" ,background_color= "red",
                        bold=True, color="white", pos_hint={'center_x': .5, 'center_y': .51}, on_press=self.verify)
        self.add_widget(self.CompleateRecord)

        self.Exit = Button(text="Exit", font_size="20dp", size_hint_x=.1, size_hint_y=.05, bold=True, color="white",background_normal = "" ,background_color= "red",
                           pos_hint={'center_x': .5, 'center_y': .37}, on_press=App.get_running_app().stop)
        self.add_widget(self.Exit)

        self.Resetpassword = Button(text="Reset Password", font_size="20dp", size_hint_x=.2, size_hint_y=.05, bold=True, color="white",
                           background_normal="", background_color="red",
                           pos_hint={'center_x': .5, 'center_y': .44},on_release=self.go_to_pg10)
        self.add_widget(self.Resetpassword)

        self.label = Label(text="Page 7", color="white",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .25})
        self.add_widget(self.label)

        self.Register_button = Button(text="Go Page 8", font_size="20dp", size_hint_x=.1, size_hint_y=.05, bold=True,
                                      color="white", pos_hint={'center_x': .59, 'center_y': .28})
        self.Register_button.bind(on_release=self.go_to_pg8)
        self.add_widget(self.Register_button)

    def verify(self, instance):
        try:
            with open("records.txt", "r") as f:
                lines = f.readlines()
            incomplete_records = []
            complete_records = []

            for line in lines:
                data = line.strip().split(',')
                if len(data) >= 13:
                    closing_km = data[9].strip()
                    time_in = data[10].strip()
                    using_km = data[11].strip()
                    if not closing_km or not time_in or not using_km:
                        incomplete_records.append(data)
                    else:
                        complete_records.append(data)
            app = App.get_running_app()
            if instance == self.IncompleateRecord:
                if incomplete_records:
                    app.incomplete_data = incomplete_records
                    app.root.current = 'pg8'
                else:
                    self.show_popup("Peeyesyem Hyundai", "No incomplete records found.")
            elif instance == self.CompleateRecord:
                if complete_records:
                    app.complete_data = complete_records
                    app.root.current = 'pg9'
                else:
                    self.show_popup("Peeyesyem Hyundai", "No complete records found.")
        except FileNotFoundError:
            self.show_popup("Error", "File 'records.txt' not found")

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, size_hint=(1, 0.7))
        close_button = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(close_button)
        popup = Popup(title=title, content=layout, size_hint=(0.3, 0.3), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()


    def go_to_pg8(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg8()
    def go_to_pg10(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg10()

class Pg8(Screen):
    def __init__(self, **kwargs):
        super(Pg8, self).__init__(**kwargs)

        with self.canvas.before:
            Color(.06, .65, .65, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        self.label = Label(text="PEEYESYEM HYUNDAI", color="blue", font_size="40dp", bold=True,
                           pos_hint={'center_x': .5, 'center_y': .60})
        self.add_widget(self.label)

        frame = Image(source=resource_path("Photo-4.png"), size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .35})
        self.add_widget(frame)

        self.bg = Image(source=resource_path("001.png"), size_hint=(.4, .4), pos_hint={'center_x': .15, 'center_y': .3})
        self.add_widget(self.bg)
        self.bg = Image(source=resource_path("002.png"), size_hint=(.4, .4), pos_hint={'center_x': .85, 'center_y': .32})
        self.add_widget(self.bg)

        self.layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(self.layout)

        self.table = MDDataTable(
            size_hint=(1, None),
            height=dp(210),
            rows_num=10,
            check=True,
            column_data=[
                ("S.No", dp(25)),
                ("Date", dp(20)),
                ("Model", dp(25)),
                ("Variant", dp(20)),
                ("Reg.No.", dp(25)),
                ("Start km", dp(20)),
                ("Time out", dp(20)),
                ("From", dp(20)),
                ("To", dp(25)),
                ("Closing km", dp(20)),
                ("Time in", dp(16)),
                ("Used km", dp(20)),
                ("S.C Name", dp(25)),
                ("Cust Name", dp(25)),
                ("Contact No.", dp(25)),
                ("Driver", dp(20)),
                ("GDMS No.", dp(20)),
                ("Gate Pass No.", dp(25))
            ],
            row_data=[],
        )
        table_container = AnchorLayout(anchor_x='left', anchor_y='top')
        table_container.add_widget(self.table)
        self.layout.add_widget(table_container)

        self.Exit = Button(text="Exit", font_size="20dp", size_hint_x=.15, size_hint_y=.05,background_normal = "" ,background_color= "red",
                           bold=True, color="white", pos_hint={'center_x': .3, 'center_y': .15},
                           on_release=App.get_running_app().stop)
        self.add_widget(self.Exit)

        self.Delete_button = Button(text="Delete", font_size="20dp", size_hint_x=.18, size_hint_y=.05,background_normal = "" ,background_color= "red",
                                    bold=True, color="white", pos_hint={'center_x': .48, 'center_y': .15})
        self.Delete_button.bind(on_release=self.delete_record)
        self.add_widget(self.Delete_button)

        self.Export_button = Button(text="Export", font_size="20dp", size_hint_x=.18, size_hint_y=.05,background_normal = "" ,background_color= "red",
                                    bold=True, color="white", pos_hint={'center_x': .67, 'center_y': .15},
                                    on_release=self.export_to_excel)
        self.Export_button.bind(on_release=self.export_to_excel)
        self.add_widget(self.Export_button)

        self.Back = Button(text="Back", font_size="20dp", size_hint_x=.15, size_hint_y=.05,background_normal = "" ,background_color= "red",
                           bold=True, color="white", pos_hint={'center_x': .48, 'center_y': .09},
                           on_release=self.go_to_pg7)
        self.add_widget(self.Back)

        self.label = Label(text="Page 8", color="white",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .25})
        self.add_widget(self.label)

        self.Register_button = Button(text="Go Page 9", font_size="20dp", size_hint_x=.1, size_hint_y=.05, bold=True,
                                      color="white", pos_hint={'center_x': .59, 'center_y': .28})
        self.Register_button.bind(on_release=self.go_to_pg9)
        self.add_widget(self.Register_button)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def on_enter(self):
        """Load data when Pg8 screen is shown"""
        self.load_data(App.get_running_app().incomplete_data)

    def load_data(self, data):
        self.table.row_data = [tuple(row[:18]) for row in data]

    def delete_record(self, instance):
        selected = self.table.get_row_checks()
        if not selected:
            self.show_popup("PSM_Hyundai", "Please select a record to delete.")
            return

        self.selected_row_to_delete = selected[0]
        selected_sno = self.selected_row_to_delete[0]

        self.dialog = MDDialog(
            title="Confirm Delete",
            text=f"Are you sure you want to delete record with S.No {selected_sno}?",
            buttons=[
                MDRaisedButton(text="Cancel", on_release=self.close_dialog),
                MDRaisedButton(text="Delete", on_release=self.confirm_delete),
            ],
        )
        self.dialog.open()

    def close_dialog(self, instance):
        self.dialog.dismiss()

    def confirm_delete(self, instance):
        self.dialog.dismiss()

        selected_row = self.selected_row_to_delete
        selected_sno = selected_row[0]

        try:
            app = App.get_running_app()
            app.incomplete_data = [row for row in app.incomplete_data if row[0] != selected_sno]

            updated_records = []
            with open("records.txt", "r") as f:
                for line in f:
                    fields = line.strip().split(",")
                    if fields[0] != selected_sno:
                        updated_records.append(line)

            with open("records.txt", "w") as f:
                f.writelines(updated_records)

            self.load_data(app.incomplete_data)
            self.show_popup("Success", f"Record S.No {selected_sno} deleted successfully.")
        except Exception as e:
            self.show_popup("PSM_Hyundai", f"Failed to delete: {str(e)}")
    def export_to_excel(self, instance):
        try:
            import os
            from datetime import datetime
            import pandas as pd
            app = App.get_running_app()
            data = app.incomplete_data
            df = pd.DataFrame(data, columns=[
                "S.No", "Date", "Model", "Variant", "Reg.No.", "Start km", "Time out", "From", "To", "Closing km",
                "Time in", "Used km", "S.C Name", "Cust Name", "Contact No.", "Driver", "GDMS No", "Gate Pass No"
            ])
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")

            if not os.path.exists(desktop):
                self.show_popup("PSM_Hyundai", "Desktop path not found. Saving to project directory instead.")
                desktop = os.getcwd()  # fallback

            filename = os.path.join(desktop, f"incomplete_records_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
            df.to_excel(filename, index=False)
            self.show_popup("Exported", f"Data exported to Desktop:\n{filename}")
        except Exception as e:
            self.show_popup("PSM_Hyundai", f"Export failed: {str(e)}")

    def exit_screen(self, instance):
        self.manager.current = 'pg7'

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, size_hint=(1, 0.7))
        close_button = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(close_button)
        popup = Popup(title=title, content=layout, size_hint=(0.4, 0.3), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def go_to_pg7(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg7()

    def go_to_pg9(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg9()

class Pg9(Screen):
    def __init__(self, **kwargs):
        super(Pg9, self).__init__(**kwargs)

        with self.canvas.before:
            Color(.06, .65, .65, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self.update_rect, pos=self.update_rect)

        self.label = Label(text="PEEYESYEM HYUNDAI", color="blue", font_size="40dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .60})
        self.add_widget(self.label)

        frame = Image(source=resource_path("Photo-4.png"), size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .35})
        self.add_widget(frame)

        self.bg = Image(source=resource_path("003.png"), size_hint=(.4, .4), pos_hint={'center_x': .15, 'center_y': .3})
        self.add_widget(self.bg)
        self.bg = Image(source=resource_path("004.png"), size_hint=(.4, .4), pos_hint={'center_x': .85, 'center_y': .33})
        self.add_widget(self.bg)

        self.layout = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(self.layout)

        self.table = MDDataTable(
            size_hint=(1, None),
            height=dp(210),
            rows_num=10,
            check=True,
            column_data=[
                ("S.No", dp(25)),
                ("Date", dp(20)),
                ("Model", dp(25)),
                ("Variant", dp(20)),
                ("Reg.No.", dp(25)),
                ("Start km", dp(20)),
                ("Time out", dp(20)),
                ("From", dp(20)),
                ("To", dp(25)),
                ("Closing km", dp(20)),
                ("Time in", dp(16)),
                ("Used km", dp(20)),
                ("S.C Name", dp(25)),
                ("Cust Name", dp(25)),
                ("Contact No.", dp(25)),
                ("Driver", dp(20)),
                ("GDMS No.", dp(20)),
                ("Gate Pass No.", dp(25))
            ],
            row_data=[],
        )
        table_container = AnchorLayout(anchor_x='left', anchor_y='top')
        table_container.add_widget(self.table)
        self.layout.add_widget(table_container)

        self.Exit = Button(text="Exit", font_size="20dp", size_hint_x=.15, size_hint_y=.05, bold=True, color="white",background_normal = "" ,background_color= "red",
                           pos_hint={'center_x': .3, 'center_y': .15}, on_release=App.get_running_app().stop)
        self.add_widget(self.Exit)

        self.Delete_button = Button(text="Delete", font_size="20dp", size_hint_x=.18, size_hint_y=.05,background_normal = "" ,background_color= "red",
                                    bold=True, color="white", pos_hint={'center_x': .48, 'center_y': .15})
        self.Delete_button.bind(on_release=self.delete_record)
        self.add_widget(self.Delete_button)

        self.Export_button = Button(text="Export", font_size="20dp", size_hint_x=.18, size_hint_y=.05, bold=True,background_normal = "" ,background_color= "red",
                                    color="white", pos_hint={'center_x': .67, 'center_y': .15})
        self.Export_button.bind(on_release=self.export_to_excel)
        self.add_widget(self.Export_button)

        self.Back = Button(text="Back", font_size="20dp", size_hint_x=.15, size_hint_y=.05, bold=True, color="white",background_normal = "" ,background_color= "red",
                           pos_hint={'center_x': .48, 'center_y': .09}, on_release=self.go_to_pg7)
        self.add_widget(self.Back)

        self.label = Label(text="Page 9", color="white",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .25})
        self.add_widget(self.label)

        self.Register_button = Button(text="Go Page 10", font_size="20dp", size_hint_x=.1, size_hint_y=.05, bold=True,
                                      color="white", pos_hint={'center_x': .59, 'center_y': .28})
        self.Register_button.bind(on_release=self.go_to_pg10)
        self.add_widget(self.Register_button)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def on_enter(self):
        """Load data when Pg9 screen is shown"""
        self.load_data(App.get_running_app().complete_data)
    def load_data(self, data):
        self.table.row_data = [tuple(row[:18]) for row in data]  # Show first 18 fields

    def delete_record(self, instance):
        selected = self.table.get_row_checks()
        if not selected:
            self.show_popup("PSM_Hyundai", "Please select a record to delete.")
            return

        self.selected_row_to_delete = selected[0]  # Store temporarily
        selected_sno = self.selected_row_to_delete[0]

        self.dialog = MDDialog(
            title="Confirm Delete",
            text=f"Are you sure you want to delete record with S.No {selected_sno}?",
            buttons=[
                MDRaisedButton(text="Cancel", on_release=self.close_dialog),
                MDRaisedButton(text="Delete", on_release=self.confirm_delete),
            ],
        )
        self.dialog.open()

    def close_dialog(self, instance):
        self.dialog.dismiss()

    def confirm_delete(self, instance):
        self.dialog.dismiss()

        selected_row = self.selected_row_to_delete
        selected_sno = selected_row[0]

        try:
            app = App.get_running_app()
            app.complete_data = [row for row in app.complete_data if row[0] != selected_sno]

            updated_records = []
            with open("records.txt", "r") as f:
                for line in f:
                    fields = line.strip().split(",")
                    if fields[0] != selected_sno:
                        updated_records.append(line)

            with open("records.txt", "w") as f:
                f.writelines(updated_records)

            self.load_data(app.complete_data)
            self.show_popup("Success", f"Record S.No {selected_sno} deleted successfully.")
        except Exception as e:
            self.show_popup("PSM_Hyundai", f"Failed to delete: {str(e)}")
    def export_to_excel(self, instance):
        try:
            import os
            app = App.get_running_app()
            data = app.complete_data
            df = pd.DataFrame(data, columns=[
                "S.No", "Date", "Model", "Variant", "Reg.No.", "Start km", "Time out", "From", "To", "Closing km",
                "Time in", "Used km", "S.C Name", "Cust Name", "Contact No.", "Driver", "GDMS No", "Gate Pass No"
            ])
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            filename = os.path.join(desktop, f"complete_records_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx")
            df.to_excel(filename, index=False)
            self.show_popup("Exported", f"Data exported to Desktop:\n{filename}")
        except Exception as e:
            self.show_popup("PSM_Hyundai", f"Export failed: {str(e)}")

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, size_hint=(1, 0.7))
        close_button = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(close_button)
        popup = Popup(title=title, content=layout, size_hint=(0.4, 0.3), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def go_to_pg7(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg7()

    def go_to_pg10(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg10()

class Pg10(Screen):
    def __init__(self, **kwargs):
        super(Pg10, self).__init__(**kwargs)

        self.bg = Image(source=resource_path("Show.jpg"), allow_stretch=True, keep_ratio=False)
        self.add_widget(self.bg)

        self.bg = Image(source=resource_path("frame.png"), size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.bg)

        self.label = Label(text="PEEYESYEM HYUNDAI", color="#00FF00", font_size="25dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .65})
        self.add_widget(self.label)

        self.label = Label(text="Enter Mobile Number", color="black", font_size="15dp",
                           bold=True, pos_hint={'center_x': .5, 'center_y': .60})
        self.add_widget(self.label)

        self.mobile_input = TextInput(size_hint_x=.2, size_hint_y=.05,
                                      multiline=False, pos_hint={'center_x': .5, 'center_y': .53})
        self.add_widget(self.mobile_input)

        self.delete_button = Button(text="Delete Password",font_size="15dp", size_hint_x=.2, size_hint_y=.05,
                                    background_normal="", background_color="red", bold=True,
                                    color="white", pos_hint={'center_x': .5, 'center_y': .45})
        self.delete_button.bind(on_press=self.delete_password)
        self.add_widget(self.delete_button)

        self.Exit = Button(text="Exit", font_size="20dp", size_hint_x=.1, size_hint_y=.05, bold=True, color="white",
                           background_normal="", background_color="red",
                           pos_hint={'center_x': .5, 'center_y': .37}, on_press=App.get_running_app().stop)
        self.add_widget(self.Exit)

        self.label = Label(text="Page 10", color="white",
                           font_size="15dp", bold=True, pos_hint={'center_x': .5, 'center_y': .25})
        self.add_widget(self.label)


    def delete_password(self, instance):
        mobile = self.mobile_input.text.strip()

        if not mobile:
            self.show_popup("PSM_Hyundai", "Please enter a mobile number.")
            return

        deleted_psm = self.delete_line_in_file("PSM.txt", mobile + ",")
        deleted_reg = self.delete_line_in_file("Register.txt", "," + mobile)

        if deleted_psm or deleted_reg:
            self.show_popup("Success", f"Deleted data for mobile {mobile}.")
        else:
            self.show_popup("PSM_Hyundai", f"No record found for mobile {mobile}.")
        self.mobile_input.text = ""
    def delete_line_in_file(self, filename, match_substring):
        if not os.path.exists(filename):
            return False

        found = False
        updated_lines = []

        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                if match_substring in line.strip():
                    found = True
                    continue  # Skip the line to delete it
                updated_lines.append(line)
        if found:
            with open(filename, "w") as f:
                f.writelines(updated_lines)
        return found
    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=message, size_hint=(1, 0.7))
        close_button = Button(text="OK", size_hint=(1, 0.3))
        layout.add_widget(label)
        layout.add_widget(close_button)
        popup = Popup(title=title, content=layout, size_hint=(0.3, 0.3), auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def go_to_pg1(self, instance):
        PSM_HyundaiApp.get_running_app().go_to_pg1()


class PSM_HyundaiApp(MDApp):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Pg1(name='pg1'))
        self.sm.add_widget(Pg2(name='pg2'))
        self.sm.add_widget(Pg3(name='pg3'))
        self.sm.add_widget(Pg4(name='pg4'))
        self.sm.add_widget(Pg5(name='pg5'))
        self.sm.add_widget(Pg6(name='pg6'))
        self.sm.add_widget(Pg7(name='pg7'))
        self.sm.add_widget(Pg8(name='pg8'))
        self.sm.add_widget(Pg9(name='pg9'))
        self.sm.add_widget(Pg10(name='pg10'))
        return self.sm

    def go_to_pg2(self):
        self.sm.current = 'pg2'

    def go_to_pg3(self):
        self.sm.current = 'pg3'

    def go_to_pg4(self):
        self.sm.current = 'pg4'

    def go_to_pg5(self):
        self.sm.current = 'pg5'

    def go_to_pg6(self):
        self.sm.current = 'pg6'

    def go_to_pg7(self):
        self.sm.current = 'pg7'

    def go_to_pg8(self):
        self.sm.current = 'pg8'

    def go_to_pg9(self):
        self.sm.current = 'pg9'

    def go_to_pg10(self):
        self.sm.current = 'pg10'

if __name__ == '__main__':
    PSM_HyundaiApp().run()