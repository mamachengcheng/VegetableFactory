from .models import MinuteStatistics
import send
# from .send import control

TemperatureCode = "01 03 00 34 00 10"
HumidityCode = "01 03 00 36 00 10"
IlluminationCode = "01 03 00 39 00 10"
CapnographyCode = "01 03 00 3C 00 10"


def minuteDataStatistics():
    temperature = send.control(TemperatureCode, "Temperature")
    humidity = send.control(HumidityCode, "Humidity")
    illumination = send.control(IlluminationCode, "illumination")
    capnography = send.control(CapnographyCode, "capnography")
    dayData = MinuteStatistics(temperature=temperature, humidity=humidity, illumination=illumination, capnography=capnography)
    dayData.save()