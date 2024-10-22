from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class LoginScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Logo di tengah
        self.logo = Image(source='logo.png', size_hint=(None, None), size=(150, 150),
                          pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.add_widget(self.logo)

        # Layout vertikal untuk username, password, dan tombol
        self.form_layout = BoxLayout(orientation='vertical', size_hint=(0.8, 0.4),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.3})

        # Input Username
        self.username_label = Label(text="Username", size_hint_y=None, height=40)
        self.form_layout.add_widget(self.username_label)
        self.username_input = TextInput(hint_text='Masukkan username', multiline=False)
        self.form_layout.add_widget(self.username_input)

        # Input Password
        self.password_label = Label(text="Password", size_hint_y=None, height=40)
        self.form_layout.add_widget(self.password_label)
        self.password_input = TextInput(hint_text='Masukkan password', password=True, multiline=False)
        self.form_layout.add_widget(self.password_input)

        # Tombol Login
        self.login_button = Button(text='Login', size_hint_y=None, height=50)
        self.form_layout.add_widget(self.login_button)

        # Tambahkan form layout ke FloatLayout
        self.add_widget(self.form_layout)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
