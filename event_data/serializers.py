from rest_framework import serializers

from event_data.models import EventDetails


class EventDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDetails
        fields = (
            "event_id",
            "adapter",
            "status",
            "data",
            "result",
            "error",
        )
