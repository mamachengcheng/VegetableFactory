# coding=utf-8
from rest_framework import serializers
from .models import MinuteStatistics, HourStatistics ,SittingHistory


class LineChartSerializers(serializers.ModelSerializer):
    updateTime = serializers.SerializerMethodField()

    class Meta:
        model = MinuteStatistics
        fields = ('temperature', 'humidity', 'illumination', 'capnography', 'updateTime')

    def get_updateTime(self, obj):
        return obj.updateTime.strftime("%Y-%m-%d")


class DataHistorySerializers(serializers.ModelSerializer):
    updateTime = serializers.SerializerMethodField()

    class Meta:
        model = HourStatistics
        fields = ('temperature', 'humidity', 'illumination', 'capnography', 'updateTime')

    def get_updateTime(self, obj):
        return obj.updateTime.strftime("%Y-%m-%d")


class SittingHistorySerializers(serializers.ModelSerializer):
    updateTime = serializers.SerializerMethodField()

    class Meta:
        model = SittingHistory
        fields = ('userName', 'sittingContent', 'deviceName', 'updateTime')

    def get_updateTime(self, obj):
        return obj.updateTime.strftime("%m-%d-%h")
