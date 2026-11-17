
def validate_preferences(user_prefs: dict) -> bool:
    """
    Validate the user's music preferences.
    """

    if not isinstance(user_prefs, dict):
        raise ValueError("Preferences must be a dictionary.")

    genre = user_prefs.get("genre")
    mood = user_prefs.get("mood")
    energy = user_prefs.get("energy")

    if not isinstance(genre, str) or not genre.strip():
        raise ValueError("Genre must be a nonempty string.")

    if not isinstance(mood, str) or not mood.strip():
        raise ValueError("Mood must be a nonempty string.")

    if isinstance(energy, bool) or not isinstance(energy, (int, float)):
        raise ValueError("Energy must be numeric.")

    if not 0 <= energy <= 1:
        raise ValueError("Energy must be between 0 and 1.")

    return True
