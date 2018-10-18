

def get_attended_members():

    """
    Return a list of members
    """

    return [
        {'id': '892310584', 'name': 'Salomé Tournifier', 'native_languages': ['French'], 'speaking_languages': ['English']},
        {'id': '189195070', 'name': 'Gautier Elrih', 'native_languages': ['French'], 'speaking_languages': ['Spanish']},
        {'id': '244502335', 'name': 'Alexandre Blonchet', 'native_languages': ['English'], 'speaking_languages': ['French']},
        {'id': '549752805', 'name': 'Victor Possignini', 'native_languages': ['Spanish'], 'speaking_languages': ['French', 'Italian']},
    ]


def dispatching_members(members):

    """
    Return a list of member groups
    """

    # Your code in this function

    return []


if __name__ == "__main__":

    # Test your code
    # If it is green congratulations, you did it

    attended_members = get_attended_members()
    assert dispatching_members(attended_members) == [
        ['Gautier', 'Victor'],
        ['Salomé', 'Alexandre'],
    ]



