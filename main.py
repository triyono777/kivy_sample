from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 50, 50, 50]  # Padding untuk seluruh layout
        self.spacing = 10  # Jarak antara elemen

        # Logo
        self.logo = Image(source='logo.png', size_hint=(None, None), size=(200, 200))  # Sesuaikan ukuran logo
        self.add_widget(self.logo)

        # Input Username
        self.username_label = Label(text="Username", size_hint_y=None, height=40)
        self.add_widget(self.username_label)
        self.username_input = TextInput(hint_text='Masukkan username', multiline=False)
        self.add_widget(self.username_input)

        # Input Password
        self.password_label = Label(text="Password", size_hint_y=None, height=40)
        self.add_widget(self.password_label)
        self.password_input = TextInput(hint_text='Masukkan password', password=True, multiline=False)
        self.add_widget(self.password_input)

        # Tombol Login
        self.login_button = Button(text='Login', size_hint_y=None, height=50)
        self.add_widget(self.login_button)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
