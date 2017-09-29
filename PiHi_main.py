# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:52:23 2017

@author: Josh
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class PiHiScreen(Screen):

    def resetForm(self):
        self.person.text = ''
        self.contact.text = ''
        self.note.text = ''

    def recordCSV(self):
        pass

    def sendMsg(self):
        pass

class PiByeScreen(Screen):
    def callNext(self,dt):
        self.manager.current = 'submit_screen'

class PiHiApp(App):

    def build_settings(self, settings):
        with open("testConfig.json", "r") as settings_json:
            settings.add_json_panel('My Custom Settings', self.config, data = settings_json.read())

    def build_config(self, config):
        config.setdefaults('section1',{
                'Comms':'Twitter'
                })

    def build(self):
        manager = ScreenManager()

        manager.add_widget(PiHiScreen(name='submit_screen'))
        manager.add_widget(PiByeScreen(name='thanks_screen'))

        return manager

if __name__ == '__main__':
    PiHiApp().run()