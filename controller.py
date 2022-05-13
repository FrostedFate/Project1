from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from view import Ui_remoteControl

class Controller(QMainWindow, Ui_remoteControl):

    #creates the limits

    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    """
            This method is used to initialize the TV object.
            :param TV_Channel: This is the initial TV channel.
            :param TV_Volume: This is the initial TV volume.
            :param TV_ISON: This is the initial TV status.
            :param IS_MUTE: This is the mute status
            """

    # creates the objects

    TV_Channel: int = MIN_CHANNEL
    TV_VOLUME: int = MIN_VOLUME
    TV_ISON: bool = False
    IS_MUTE = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.Power_Button.clicked.connect(lambda : self.turns())
        self.Vol_up.clicked.connect(lambda : self.turnVup())
        self.Vol_down.clicked.connect(lambda : self.turnVdown())
        self.Ch_up.clicked.connect(lambda : self.turnCup())
        self.Ch_down.clicked.connect(lambda : self.turnCdown())
        self.pushButton.clicked.connect(lambda : self.disableVolume())


    def turns(self):
        Controller.power(self)


    def turnVup(self):
        Controller.volume_up(self)


    def turnVdown(self):
        Controller.volume_down(self)


    def turnCup(self):
        Controller.channel_up(self)


    def turnCdown(self):
        Controller.channel_down(self)

    def disableVolume(self):
        Controller.Mute(self)

    # Old code from classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def power(self) -> None:
        """
        This turns the tv on and off
        also places the Black screen on and off
        :param TV_ISON: This is the TV status.
        """

        if Controller.TV_ISON == False:
            Controller.TV_ISON = True
            self.label_4.setGeometry(QtCore.QRect(10, 10, 0, 0))
        else:
            Controller.TV_ISON = False
            self.label_4.setGeometry(QtCore.QRect(10, 10, 451, 241))
        pass

    def screenChannel(self) -> None:

        # this logic allows for the proper display of channels

        if Controller.TV_Channel == 0:
            self.CN.setGeometry(QtCore.QRect(60, 0, 351, 241))
            self.Nick.setGeometry(QtCore.QRect(90, 20, 0, 0))
            self.History.setGeometry(QtCore.QRect(110, 10, 0, 0))
            self.Weather.setGeometry(QtCore.QRect(90, 10, 0, 0))
        elif Controller.TV_Channel == 1:
            self.CN.setGeometry(QtCore.QRect(60, 0, 0, 0))
            self.Nick.setGeometry(QtCore.QRect(90, 20, 291, 191))
            self.History.setGeometry(QtCore.QRect(110, 10, 0, 0))
            self.Weather.setGeometry(QtCore.QRect(90, 10, 0, 0))
        elif Controller.TV_Channel == 2:
            self.CN.setGeometry(QtCore.QRect(60, 0, 0, 0))
            self.Nick.setGeometry(QtCore.QRect(90, 20, 0, 0))
            self.History.setGeometry(QtCore.QRect(110, 10, 251, 221))
            self.Weather.setGeometry(QtCore.QRect(90, 10, 0, 0))
        elif Controller.TV_Channel == 3:
            self.CN.setGeometry(QtCore.QRect(60, 0, 0, 0))
            self.Nick.setGeometry(QtCore.QRect(90, 20, 0, 0))
            self.History.setGeometry(QtCore.QRect(110, 10, 0, 0))
            self.Weather.setGeometry(QtCore.QRect(90, 10, 291, 231))

    def Mute(self):
        if Controller.TV_ISON == True:
            if Controller.IS_MUTE == False:
                Controller.IS_MUTE = True
                self.volumeHorizontalSlider.setProperty("value", 0)
                self.Vol_up.setEnabled(False)
                self.Vol_down.setEnabled(False)
            else:
                self.Vol_up.setEnabled(True)
                self.Vol_down.setEnabled(True)
                self.volumeHorizontalSlider.setProperty("value", Controller.TV_VOLUME)
                Controller.IS_MUTE = False





    def channel_up(self) -> None:
        """
        This method should be used to adjust the TV channel by incrementing its value up.
        :param TV_Channel: This is the TV channel.
        :param TV_ISON: This is the TV status.
        :param MAX_CHANNEL: This is the maximum TV channel.
        :param MIN_CHANNEL: This is the minimum TV channel.
        """

        if Controller.TV_ISON == True:
            Controller.TV_Channel = Controller.TV_Channel + 1
            if Controller.TV_Channel > Controller.MAX_CHANNEL:
                Controller.TV_Channel = Controller.MIN_CHANNEL

        Controller.screenChannel(self)

        pass

    def channel_down(self) -> None:
        """
        This method should be used to adjust the TV channel by decrementing its value down.
        :param TV_Channel: This is the TV channel.
        :param TV_ISON: This is the TV status.
        :param MAX_CHANNEL: This is the maximum TV channel.
        :param MIN_CHANNEL: This is the minimum TV channel.
        """

        if Controller.TV_ISON == True:
            Controller.TV_Channel = Controller.TV_Channel - 1
            if Controller.TV_Channel < Controller.MIN_CHANNEL:
                Controller.TV_Channel = Controller.MAX_CHANNEL

        Controller.screenChannel(self)

        pass


    def volume_up(self) -> None:
        """
        This method should be used to adjust the TV volume by incrementing its value up.
        :param TV_Volume: This is the TV volume.
        :param TV_ISON: This is the TV status.
        :param MAX_VOLUME: This is the maximum TV volume.
        :param MIN_VOLUME: This is the minimum TV volume.
        """

        if Controller.TV_ISON == True:
            Controller.TV_VOLUME = Controller.TV_VOLUME + 1
            if Controller.TV_VOLUME > Controller.MAX_VOLUME:
                Controller.TV_VOLUME = Controller.MAX_VOLUME

        self.volumeHorizontalSlider.setProperty("value", Controller.TV_VOLUME)

        pass

    def volume_down(self) -> None:
        """
        This method should be used to adjust the TV volume by decrementing its value down.
        :param TV_Volume: This is the TV volume.
        :param TV_ISON: This is the TV status.
        :param MAX_VOLUME: This is the maximum TV volume.
        :param MIN_VOLUME: This is the minimum TV volume.
        """

        if Controller.TV_ISON == True:
            Controller.TV_VOLUME = Controller.TV_VOLUME - 1
            if Controller.TV_VOLUME < Controller.MIN_VOLUME:
                Controller.TV_VOLUME = Controller.MIN_VOLUME

        self.volumeHorizontalSlider.setProperty("value", Controller.TV_VOLUME)

        pass

    def str(self):
        """
        - This method should be used to return the TV status using this format: "TV is on = yes/no channel = X volume = Y"
        """
        Reader = "TV status: Is on = " + str(Controller.TV_ISON) + ", Channel = " + str(
            Controller.TV_Channel) + ", Volume = " + str(Controller.TV_VOLUME)
        return Reader

