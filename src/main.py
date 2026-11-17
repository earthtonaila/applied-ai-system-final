
"""
Music Recommender Simulation with Reliability Evaluation.

Run from the project root:
    python -m src.main
"""

import logging
from pathlib import Path

from src.recommender import load_songs, recommend_songs
from src.validation import validate_preferences
from src.evaluation import evaluate_recommendations

WIDTH = 60
TOP_K = 3

# Configure logging
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/recommender.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def print_header(title: str) -> None:
    print("=" * WIDTH)
    print(title.center(WIDTH))
    print("=" * WIDTH)


def print_preferences(user_prefs: dict) -> None:
    print("\nUser preferences")
    print("-" * WIDTH)
    print(f"  Favorite genre : {user_prefs['genre']}")
    print(f"  Favorite mood  : {user_prefs['mood']}")
    print(f"  Target energy  : {user_prefs['energy']:.2f}")


def print_recommendations(recommendations: list) -> None:
    print(f"\nTop {len(recommendations)} recommendations")
    print("-" * WIDTH)

    for rank, (song, score, explanation) in enumerate(
        recommendations, start=1
    ):
        reasons = explanation.split("; ") if explanation else []

        print(f"\n{rank}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")

        for reason in reasons:
            print(f"     - {reason}")

    print()


def print_evaluation(metrics: dict) -> None:
    print("\nRecommendation Quality Evaluation")
    print("-" * WIDTH)

    print(
        f"Genre match rate: "
        f"{metrics['genre_match_rate']:.1%}"
    )

    print(
        f"Mood match rate: "
        f"{metrics['mood_match_rate']:.1%}"
    )

    print(
        f"Average energy difference: "
        f"{metrics['average_energy_difference']:.3f}"
    )

    print(
        f"Quality check passed: "
        f"{metrics['quality_check_passed']}"
    )


def main() -> None:
    print_header("Music Recommender Simulation")

    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8
    }

    try:
        # Step 1: Validate user input
        validate_preferences(user_prefs)
        logging.info("User preferences validated")

        # Step 2: Load song dataset
        songs = load_songs("data/songs.csv")
        logging.info("Loaded %d songs", len(songs))

        # Step 3: Generate recommendations
        recommendations = recommend_songs(
            user_prefs, songs, k=TOP_K
        )

        logging.info(
            "Generated %d recommendations",
            len(recommendations)
        )

        # Step 4: Evaluate results before displaying
        metrics = evaluate_recommendations(
            recommendations,
            user_prefs,
            expected_count=min(TOP_K, len(songs))
        )

        logging.info("Evaluation metrics: %s", metrics)

        # Step 5: Display validated recommendations
        print(f"\nSongs loaded: {len(songs)}")
        print_preferences(user_prefs)
        print_recommendations(recommendations)
        print_evaluation(metrics)

    except (ValueError, OSError, KeyError, TypeError) as error:
        logging.error("Application error: %s", error)
        print(f"\nUnable to generate recommendations: {error}")


if __name__ == "__main__":
    main()
