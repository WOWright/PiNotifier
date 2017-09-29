# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:40:42 2017

@author: Josh
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MahApp(App):

    def build_settings(self, settings):
        with open("testConfig.json", "r") as settings_json:
            settings.add_json_panel('My Custom Settings', self.config, data = settings_json.read())

    def build_config(self, config):
        config.setdefaults('section1',{
                'Comms':'Twitter'
                })

    def build(self):
        btn = Button(text='Random Button')
        return btn

if __name__ == '__main__':
    MahApp().run()