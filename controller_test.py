from controller import *


class test:
    def setup_method(self):
        self.tv = Controller()

    def teardown_method(self):
        del self.tv

    # testing on and off as well as initializing the class

    def test_init(self):
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tv.power()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"
        self.tv.power()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

    # testing channels

    def test_channel_up(self):
        self.tv.channel_up()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 1, Volume = 0"

        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        self.tv.channel_down()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 3, Volume = 0"

        self.tv.channel_down()
        self.tv.channel_down()
        self.tv.channel_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"

    # testing volume

    def test_volume_up(self):
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"

        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        self.tv.volume_down()
        assert self.tv.__str__() == "TV status: Is on = False, Channel = 0, Volume = 0"

        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 0"

        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == "TV status: Is on = True, Channel = 0, Volume = 1"


