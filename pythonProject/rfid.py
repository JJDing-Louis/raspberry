from LCD.lcd_display import lcd
from mfrc522 import MFRC522
from tkinter import *
from threading import Timer
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class App:
    def __init__(self, window):
        self.uid = []
        self.preUid = []
        self.MIFAREReader = MFRC522()
        self.rfidHandler()
        self.lcd = lcd()

        #initialFireStore
        cred = credentials.Certificate('/home/pi/Documents/certificate/raspberryfirebase-firebase-adminsdk-y4f0x-65514e121f.json')
        firebase_admin.initialize_app(cred)
        self.doors_ref = firestore.client()

    def rfidHandler(self): #0.1秒執行一次
        reqStatus, tagType = self.MIFAREReader.MFRC522_Request(MFRC522.PICC_REQIDL)
        if reqStatus == MFRC522.MI_OK:
            scanStatus, self.uid = self.MIFAREReader.MFRC522_Anticoll()
            if scanStatus == MFRC522.MI_OK:
                if self.uid != self.preUid:
                    self.preUid = self.uid
                    #在lcd上顯示
                    self.displayInLcd()

        Timer(0.1, self.rfidHandler).start()

    def displayInLcd(self):
        document_ref = self.doors_ref.collection(u'Doors').document()
        uidString = ''
        for index, uid in enumerate(self.uid):
           uidString += str(uid)
           uidString += ' '

        self.lcd.clear()
        self.lcd.display_string(uidString, 0)
        document_ref.set({'uid': self.uid})






if __name__ == "__main__":
    window = Tk()
    window.title("RFID")
    window.option_add("*font", ("Helvetica", 18))
    app = App(window)
    window.mainloop()

