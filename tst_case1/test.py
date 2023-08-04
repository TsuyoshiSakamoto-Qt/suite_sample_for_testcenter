# -*- coding: utf-8 -*-

import names


def main():
    startApplication("testQML")
    test.compare(str(waitForObjectExists(names.hello_World_clicked_Text).text), "default text")
    
    mouseClick(waitForObject(names.hello_World_push_me_Button), Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.hello_World_clicked_Text).text), "clicked!")

    snooze(2)
