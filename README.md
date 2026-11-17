# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

Music recommendation systems predict which songs users might enjoy by analyzing their listening behavior and musical preferences. Collaborative filtering identifies patterns among users with similar listening habits, while content-based filtering recommends songs based on their musical attributes. My simulation will use content-based filtering to compare each song's genre, mood, energy, and tempo with a user's preferences. Each song will receive a weighted similarity score, and songs with the highest scores will be recommended first. I will prioritize genre and mood while using energy and tempo to identify songs with a similar musical vibe.

Each song recieves a score based on how closely its attributes match the user's preferences. Genre contributes up to 40 points, mood contributes up to 30 points, energy similarity contributes up to 20 points, and tempo similarity contributes up to 10 points. The songs are then ranked from highest to lowest score, and the best matches are recommended first.

Because genre contributes more points than mood or energy, the system may over-prioritize genre and overlook songs from other genres that match the user's desired vibe. The recommender also depends on a limited dataset and cannot account for individual listening history, changing preferences, or musical characteristics not included in the CSV. Increasing the diversity of songs and adjusting feature weights could improve recommendations.

You can include a simple diagram or bullet list if helpful.

Song Features
genre : the song's musical category
mood : the emotional feeling of the song
energy : the song's intensity or activity level
tempo_bpm : the song's speed in beats per minute

UserProfile Features
preferred_genre : the user's favorite musical genre
preferred_mood : the user's desired musical mood
preferred_energy : the user's preferred energy level
preferred_tempo : the user's preferred tempo in BPM

user_profile = {
  "favorite_genre": "pop",
  "favorite_mood": "calm",
  "target_energy": 0.3,
}

The system calculates a score for each song using the following rules:
genre match: +2.0 points if the song's genre matches the user's favorite genre
mood match: +1.0 point if the song's mood matches the user's favorite mood
energy similarity: 1 - abs(song_energy - target_energy)
The maximum possible score is 4.0 points. After calculating the scores for all songs, the system sorts them from highest to lowest and returns the top 3 recommendations.

1 Input: read the user's preferred genre, mood, and energy
2 Process: read each song from songs.csv and calculate its similarity score
3 Ranking: sort songs by their total scores
4 Output: display the top 3 highest-scoring songs

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

________________________________________________________________________________________________________

                          EXPLAINABLE MUSIC RECOMMENDER WITH RELIABILITY EVALUATION
________________________________________________________________________________________________________

## 1. Project Summary
This project is a Python-based music recommendation system that generates personalized song suggestions based on users' preferred genres, moods, and energy levels. Each recommendation includes a compatibility score and an explanation of how the song matches the user's preferences.

The project extends a basic music recommendation algorithm with integrated input validation, automated testing, application logging, and recommendation quality evaluation. These improvements make the system more transparent, testable, and reliable.

The goal is to demonstrate how recommendation systems can be designed not only to generate relevant results but also to evaluate and explain those results.

## 2. Original Project: Music Recommender Simulation (Modules 1-3)
My original project, Music Recommender Simulation, was developed during Modules 1–3 of CodePath AI110. Its goal was to simulate personalized music recommendations by comparing users' genre, mood, and energy preferences against a dataset of songs.

The original system used a weighted scoring algorithm to rank songs and generate explanations for each recommendation. It demonstrated how structured data and predefined scoring rules could be used to simulate personalized recommendations without requiring a trained machine-learning model.

Original Repository: https://github.com/earthtonaila/ai110-module3show-musicrecommendersimulation-starter

## 3. System Architecture
The system follows a modular workflow that separates user input validation, recommendation generation, reliability evaluation, and output presentation.

  1. User Preferences: The system receives the user's preferred genre, mood, and energy level.
  2. Input Validation: The validation module checks whether the preferences are correctly formatted and within acceptable ranges.
  3. Recommendation Engine: The recommender loads song information from a CSV dataset, calculates compatibility scores, and ranks songs.
  4. Reliability Evaluation: The evaluation module checks the recommendation output and calculates genre match rate, mood match rate, and average energy difference.
  5. Output and Logging: The application displays the highest-ranked songs, explanations, and evaluation metrics while recording relevant activity and errors.
  6. Testing and Human Review: Automated unit tests verify the reliability functions, while developers can inspect recommendation results and evaluation metrics to identify potential weaknesses.

The system architecture is documented in diagrams/architecture.mmd.

## 5. Setup Instructions
Prerequisites
  - Python 3 installed
  - Git installed
  - A terminal or code editor such as Visual Studio Code

  1. Clone the Repository
  git clone https://github.com/earthtonaila/applied-ai-system-final.git
  cd applied-ai-system-final

  2. Create a Virtual Environment (Optional)
  python3 -m venv .venv
  source .venv/bin/activate

  3. Run the Music Recommender
  python -m src.main
  The application loads the song dataset, validates the user preferences, generates recommendations, and displays evaluation metrics.

  4. Customize User Preferences
  Open src/main.py and locate the user_prefs dictionary:
  user_prefs = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.8
  }
  Modify the values to explore different music preferences, then rerun the application.
  Energy values must be betwenn 0 and 1.

  5. Run Automated Tests
  python -m unittest discover -s tests -v
  The command executes the discoverable automated tests and reports whether they pass or fail.

  6. View Evaluation Evidence
  See tests/evaluation_results.md for recorded test results and recommendation quality evaluations.

## Sample Interactions

### Example 1: High-Energy Pop
**Input:**
```python
user_prefs = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.9
}
```

**Output:**
============================================================
                Music Recommender Simulation                
============================================================
Loading songs from data/songs.csv...

Songs loaded: 10

User preferences
------------------------------------------------------------
  Favorite genre : pop
  Favorite mood  : happy
  Target energy  : 0.90

Top 3 recommendations
------------------------------------------------------------

1. Sunrise City by Neon Echo
   Score: 3.92
   Reasons:
     - genre match (+2.0)
     - mood match (+1.0)
     - energy similarity (+0.9)

2. Gym Hero by Max Pulse
   Score: 2.97
   Reasons:
     - genre match (+2.0)
     - energy similarity (+1.0)

3. Rooftop Lights by Indigo Parade
   Score: 1.86
   Reasons:
     - mood match (+1.0)
     - energy similarity (+0.9)


Recommendation Quality Evaluation
------------------------------------------------------------
Genre match rate: 66.7%
Mood match rate: 66.7%
Average energy difference: 0.083
Quality check passed: True

### Example 2: Chill Lofi
**Input:**
```python
user_prefs = {
    "genre": "lofi",
    "mood": "calm",
    "energy": 0.2
}
```

**Output:**
============================================================
                Music Recommender Simulation                
============================================================
Loading songs from data/songs.csv...

Songs loaded: 10

User preferences
------------------------------------------------------------
  Favorite genre : pop
  Favorite mood  : happy
  Target energy  : 0.80

Top 3 recommendations
------------------------------------------------------------

1. Sunrise City by Neon Echo
   Score: 3.98
   Reasons:
     - genre match (+2.0)
     - mood match (+1.0)
     - energy similarity (+1.0)

2. Gym Hero by Max Pulse
   Score: 2.87
   Reasons:
     - genre match (+2.0)
     - energy similarity (+0.9)

3. Rooftop Lights by Indigo Parade
   Score: 1.96
   Reasons:
     - mood match (+1.0)
     - energy similarity (+1.0)


Recommendation Quality Evaluation
------------------------------------------------------------
Genre match rate: 66.7%
Mood match rate: 66.7%
Average energy difference: 0.063
Quality check passed: True

### Example 3: Intense Rock
**Input:**
```python
user_prefs = {
    "genre": "rock",
    "mood": "intense",
    "energy": 0.95
}
```

**Output:**
============================================================
                Music Recommender Simulation                
============================================================
Loading songs from data/songs.csv...

Songs loaded: 10

User preferences
------------------------------------------------------------
  Favorite genre : rock
  Favorite mood  : intense
  Target energy  : 0.95

Top 3 recommendations
------------------------------------------------------------

1. Storm Runner by Voltline
   Score: 3.96
   Reasons:
     - genre match (+2.0)
     - mood match (+1.0)
     - energy similarity (+1.0)

2. Gym Hero by Max Pulse
   Score: 1.98
   Reasons:
     - mood match (+1.0)
     - energy similarity (+1.0)

3. Sunrise City by Neon Echo
   Score: 0.87
   Reasons:
     - energy similarity (+0.9)


Recommendation Quality Evaluation
------------------------------------------------------------
Genre match rate: 33.3%
Mood match rate: 66.7%
Average energy difference: 0.063
Quality check passed: True

## 6. Design Decisions and Trade-offs
I chose to extend my original rule-based recommendation system rather than replace it with a more complex machine-learning model. This allowed me to focus on improving reliability, transparency, and evaluation while preserving the original project's functionality.

**Weighted Scoring Algorithm:** I assigned greater weight to genre matches than mood matches, while using energy similarity to provide additional personalization. This approach makes recommendation decisions easy to understand and explain. However, manually selected weights may not accurately reflect every user's musical preferences.

**Modular Architecture:** I separated recommendation logic, input validation, and reliability evaluation into individual Python modules. This makes the code easier to maintain, test, and expand. The trade-off is a slightly more complex project structure.

**Integrated Reliability Evaluation:** Instead of relying exclusively on standalone tests, I incorporated evaluation into the application's normal execution workflow. This allows the system to check recommendation structure and report quality metrics each time it runs.

**Rule-Based Explanations:** Each recommendation includes an explanation derived directly from the scoring algorithm. This provides transparency without requiring an additional language model, although the explanations are less flexible than natural-language explanations generated by an LLM.

## 7. Testing Summary
I evaluated the system using automated unit tests and recommendation quality metrics.

**Automated Testing**
Four reliability tests passed successfully, verifying that the system:
  1. Accepts valid user preferences.
  2. Rejects energy values outside the allowed range.
  3. Correctly calculates genre and mood match rates for the tested examples.
  4. Detects an incorrect number of recommendations.
The observed test run completed with four passing tests and no reported failures.

**Recommendation Quality Evaluation**
The system measures recommendation quality using genre match rate, mood match rate, and average energy difference.
Three user preference profiles were selected for additional evaluation: high-energy pop, chill lofi, and intense rock.
Detailed results and terminal outputs are documented in tests/evaluation_results.md.

**Challenges and Limitations**
One challenge was ensuring that the new reliability features worked with the existing recommendation algorithm without disrupting its original functionality.
The system also has limitations. Its recommendations depend on the available dataset, and the scoring algorithm uses manually selected weights rather than learning from user behavior.
Although the reliability tests passed, they do not measure whether users genuinely enjoy the recommended songs. Future testing could include user feedback and a broader range of listening preferences.

## 8. Project Reflection
Developing this project helped me understand that building a functional recommendation system is only one part of creating reliable software. By integrating validation, automated testing, and evaluation metrics, I learned how to assess the behavior of a system rather than assuming that producing an output means it is working correctly.

The project also strengthened my understanding of modular software design, explainability, and the trade-offs between simple algorithms and more complex AI approaches. Most importantly, it showed me how reliability and transparency can be incorporated into the development process from the beginning.