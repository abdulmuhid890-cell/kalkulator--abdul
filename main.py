from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class KalkulatorAbdulApp(App):
    def build(self):
        # Layout utama vertikal
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 1. Layar Teks
        self.layar = TextInput(
            multiline=False, 
            readonly=True, 
            halign="right", 
            font_size=40,
            size_hint=(1, 0.2)
        )
        main_layout.add_widget(self.layar)
        
        # 2. Susunan Tombol
        tombol_tombol = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        
        grid_tombol = GridLayout(cols=4, spacing=10)
        for baris in tombol_tombol:
            for teks in baris:
                btn = Button(text=teks, font_size=30)
                btn.bind(on_press=self.ketika_tombol_ditekan)
                grid_tombol.add_widget(btn)
                
        main_layout.add_widget(grid_tombol)
        
        # 3. Tombol "="
        btn_hasil = Button(text="=", font_size=34, size_hint=(1, 0.15), background_color=(0, 0.6, 0.8, 1))
        btn_hasil.bind(on_press=self.hitung_hasil)
        main_layout.add_widget(btn_hasil)
        
        return main_layout

    def ketika_tombol_ditekan(self, instance):
        teks_tombol = instance.text
        if teks_tombol == "C":
            self.layar.text = ""
        else:
            self.layar.text += teks_tombol

    def hitung_hasil(self, instance):
        teks_saat_ini = self.layar.text
        if teks_saat_ini:
            try:
                self.layar.text = str(eval(teks_saat_ini))
            except Exception:
                self.layar.text = "Eror"

if __name__ == "__main__":
    KalkulatorAbdulApp().run()
