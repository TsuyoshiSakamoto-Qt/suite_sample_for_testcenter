# -*- coding: utf-8 -*-

import names


def main():
    startApplication("testQML")
    mouseClick(waitForObject(names.hello_World_text_set_Button), 101, 20, Qt.LeftButton)
