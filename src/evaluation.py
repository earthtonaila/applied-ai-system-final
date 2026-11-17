
def evaluate_recommendations(
    recommendations: list,
    user_prefs: dict,
    expected_count: int = 3
) -> dict:
    """
    Evaluate recommendation quality and reliability.
    """

    if len(recommendations) != expected_count:
        raise ValueError(
            f"Expected {expected_count} recommendations, "
            f"but received {len(recommendations)}."
        )

    if not recommendations:
        raise ValueError("No recommendations returned.")

    genre_matches = 0
    mood_matches = 0
    energy_differences = []

    for song, score, explanation in recommendations:

        if not isinstance(song, dict):
            raise ValueError("Invalid song format.")

        if not isinstance(score, (int, float)):
            raise ValueError("Invalid recommendation score.")

        if not isinstance(explanation, str):
            raise ValueError("Invalid explanation format.")

        if song["genre"] == user_prefs["genre"]:
            genre_matches += 1

        if song["mood"] == user_prefs["mood"]:
            mood_matches += 1

        energy_difference = abs(
            song["energy"] - user_prefs["energy"]
        )

        energy_differences.append(energy_difference)

    count = len(recommendations)

    return {
        "genre_match_rate": genre_matches / count,
        "mood_match_rate": mood_matches / count,
        "average_energy_difference": (
            sum(energy_differences) / count
        ),
        "quality_check_passed": True
    }
