from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    playerClass = serializers.CharField(required=True, max_length=128)

    def validate(self, data):
        values = ['Druid', 'Hunter', 'Mage', 'Paladin', 'Priest',
                  'Rogue', 'Shaman', 'Warlock', 'Warrior', 'Neutral']

        if data['playerClass'] not in values:
            raise serializers.ValidationError({
                "error": "Invalid input. Input must be a string containing one of the following: Druid, Hunter, Mage, Paladin, Priest, Rogue, Shaman, Warlock, Warrior, Neutral"})
        return data
