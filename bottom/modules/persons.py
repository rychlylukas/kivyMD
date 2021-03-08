from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, TwoLineAvatarListItem, ImageLeftWidget
import json
import os


class MyItem(TwoLineAvatarListItem):
    def __init__(self, name, pohlavi, povolani, obrazek, vek, ockovani, *args, **kwargs):
        super(MyItem, self).__init__(*args)
        self.text = f"{name},  {pohlavi}, {vek}, {povolani}"
        self.secondary_text = ockovani
        self._no_ripple_effect = True
        self.obrazek = ImageLeftWidget(source=obrazek)
        self.add_widget(self.obrazek)


class Persons(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Persons, self).__init__(orientation="horizontal")
        scrollview = ScrollView()
        list = MDList()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '/' + 'persons.json', encoding="utf-8") as json_file:
            data = json.load(json_file)
            for p in data['people']:
                list.add_widget(MyItem(name=p['jmeno'], pohlavi=p['pohlavi'], obrazek=p['obrazek'], povolani=p['povolani'], vek=p['vek'], ockovani=p['ockovani']))
        scrollview.add_widget(list)
        self.add_widget(scrollview)
