from hyperspy._signals.signal1d import Signal1D
from hyperspy._signals.eels import EELSSpectrum

class MySignal(Signal1D):
    _signal_type = "MySignal"
    _signal_dimension = 1

    def create_model(self, dictionary=None):
        from hspy_ext.model import MyModel
        return MyModel(self, dictionary=dictionary)
 
class MyEELSSpectrum(EELSSpectrum):
    _signal_type = "MyEELSSignal"
    _signal_dimension = 1

    def create_model(self, dictionary=None):
        from hspy_ext.model import MyModel
        return MyModel(self, dictionary=dictionary)
