from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    """
    Checks that the json body from the user input is valid
    """
    playerClass = serializers.CharField(required=True, max_length=128)

    def validate(self, data):
        """
        Checks that the json body has a valid playerClass value.

        Parameters
        ----------
        arg1 : dict
            Request body received from user

        Returns
        -------
        dict
            the json body unchanged if valid, else an exception is raised

        """
        values = ['Druid', 'Hunter', 'Mage', 'Paladin', 'Priest',
                  'Rogue', 'Shaman', 'Warlock', 'Warrior', 'Neutral']

        if data['playerClass'] not in values:
            raise serializers.ValidationError({
                'errors': {
                    'playerClass': ['Input must be a string containing one of the following: Druid, Hunter, Mage, Paladin, Priest, Rogue, Shaman, Warlock, Warrior, Neutral.'],
                },
                'message': 'bad request'
            })
        return data
