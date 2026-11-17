# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibeFinder 1.0 — A Content-Based Music Recommender

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

VibeFinder recommends songs based on a user's favorite genre, preferred mood, and desired energy level. It compares these preferences with the available songs and recommends the closest matches.

VibeFinder is intended for educational purposes and exploring how recommendation systems work. It can suggest songs based on basic musical preferences. It is not designed to predict a person's exact musical taste or replace recommendation sysems used by major streaming platforms.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

This music recommendation system uses content-based filtering to identify songs that match a user's musical preferences. Each song is evaluated based on its genre, mood, and energy level.

The algorithm awards 2.0 points for a genre match, 1.0 point for a mood match, and up to 1.0 point for energy similarity. The energy score is calculated using the absolute difference between the song's energy and the user's preferred energy level.

After scoring all songs, the system sorts them from highest to lowest score and returns the top recommendations. Each recommendation includes an explanation of the factors that contributed to its score.

This approach is simple and interpretable, but it may favor genre matches over songs with similar moods or energy levels. It also does not learn from a user's listening history or account for preferences that change over time.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The system uses a CSV dataset containing 18 songs. Each song has attributes such as title, artist, genre, mood, and energy. The dataset includes several musical styles but is limited in size. Some genres and moods may have fewer songs than others.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system awards 2 points when a song matches the user's favorite genre and 1 point when it matches their preferred mood. It also awards up to 1 point based on how close the song's energy is to the user's desired energy. Songs are ranked by their total scores, and the highest-scoring songs are recommended first.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users 

One limitation of my recommendation system is that it places more importance on genre than on mood or energy. This can cause songs from a user's favorite genre to rank higher than songs from other genres that better match their desired musical vibe. The system also relies on a small song dataset, which limits the variety of recommendations available. These limitations may create a filter bubble by repeatedly recommending similar songs instead of introducing users to different styles. Adjusting the feature weights and expanding the dataset could improve the system's diversity.

The system tends to prioritize songs from the user's favorite genre because genre has the highest weight. This may cause it to overlook songs from other genres that have similar moods or energy levels. The small dataset also limits the variety of recommendations.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I evaluated my music recommendation system using three different user profiles:

1 High-Energy Pop: prefers pop music, happy moods, and energy of 0.9
2 Chill Lofi: prefers lofi music, calm moods, and energy of 0.2
3 Deep intense Rock: prefers rock music, intense moods, and energy of 0.95

Each profile was tested against the same song dataset, and the top five recommendations were recorded

I tested the sensitivity of my algorithm by reducing the genre match weight from 2.0 to 1.0 and increasing the energy similarity weight from 1.0 to 2.0. The mood weight remained unchanged at 1.0.

I tested the system using three profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock. I compared the top five recommendations for each profile and examined whether the results matched the user's preferences. I also tested how changing the genre and energy weights affected the rankings.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes

1 Exapnd the dataset to include more songs and genres
2 Add features such as danceability, tempo, and acousticness
3 Incorporate user feedback, such as likes and skips, to improve recommendations over time

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

My biggest learning moment was realizing that a recommendation system can be build using a simple scoring algorithm. Before this project, I assumed music recommendations required advanced machine learning. I learned that comparing a few musical features can already produce meaningful results.

AI coding tools helped me understand how to structure my Python functions, implement scoring rules, and troubleshoot errors. However, I also learned the importance of checking AI-generated code instead of assuming it would work correctly. Testing the program helped me understand how each function contributed to the final recommendations.

What suprised me most was how a relatively simple scoring algorithm could still produce results that felt personalized. Small changes to the scoring weights could significantly influence which songs appeared first. This showed me that recommendation systems reflect the priorities and assumptions built into their algorithms.

If I continued developing VibeFinder, I would expand the dataset and incorporate user feedback. I would also experiment with additional musical features to make the recommendations more diverse and responsive to individual preferences.
__________________________________________________________________________
    
                                FINAL PROJECT
__________________________________________________________________________

## 1. System Description

This project is a rule-based music recommendation system that ranks songs according to user preferences for genre, mood, and energy.

The original Music Recommender Simulation was extended with input validation, reliability evaluation, automated testing, and logging.

## 2. Intended Use

The system is intended for educational purposes and demonstrates how recommendation algorithms can generate personalized, explainable results.

It is not intended to predict individual listening preferences with high accuracy or replace commercial recommendation systems.

## 3. AI Collaboration During Development

Throughout the development of my Music Recommender Simulation, I used Claude Anthropic's AI Agent as a coding assistant to help extend my original project into a more reliable and explainable recommendation system. AI assistance was particularly useful for understanding how to integrate input validation, automated testing, evaluation metrics, and application logging into my existing Python code.

Rather than replacing my original recommendation algorithm, I used AI-generated suggestions to build upon its existing functionality. I reviewed the proposed changes, organized the new components into separate Python modules, and ran automated tests to verify their behavior. I also used ChatGPT to help structure my system architecture diagram and project documentation.

This collaboration helped me better understand the importance of evaluating software beyond whether it produces an output. I learned how to incorporate reliability checks into an application's workflow, measure recommendation quality, and document limitations. The experience reinforced that AI-generated code should be reviewed and tested rather than assumed to be correct.

## 4. Reliability and Testing

To improve the reliability of my Music Recommender Simulation, I integrated input validation, recommendation evaluation, and application logging into the existing system. Input validation checks that users provide valid genre and mood preferences and an energy value between 0 and 1. The evaluation module verifies the structure and number of recommendations before calculating three quality metrics: genre match rate, mood match rate, and average energy difference.

I implemented four automated unit tests to verify these components. All four tests passed successfully, confirming that the system accepts valid preferences, rejects invalid energy values, calculates genre and mood match rates correctly for the tested examples, and detects incorrect recommendation counts.

Beyond automated testing, I designed three evaluation scenarios representing different listening preferences: high-energy pop, chill lofi, and intense rock. These scenarios allow me to compare recommendation quality across different genres, moods, and energy levels. The results can help identify potential weaknesses in the recommendation algorithm, particularly when the available dataset does not closely match a user's preferences.

Although the automated tests passed, I recognize that technical reliability does not necessarily guarantee recommendation quality. My evaluation metrics measure how closely recommendations align with stated preferences, but they cannot determine whether users actually enjoy the songs. Future improvements could include collecting voluntary user feedback, expanding the dataset, and evaluating alternative scoring weights.

## 5. Potential Biases

The system's recommendations may reflect limitations in the song dataset, including unequal representation of genres, artists, and musical styles.

Its scoring algorithm also prioritizes genre matches more heavily than mood matches, which may not reflect every listener's preferences.

## 6. Ethical Considerations

A recommendation system should avoid presenting subjective musical preferences as objective judgements of quality.

The system uses explicit preference inputs and provides explanations of its scoring, decisions, supporting transparency.

The current implementation does not require collecting personal listening histories.

## 7. Limitations
    - The system does not learn from feedback
    - Recommendation quality depends on the dataset
    - The scoring weights are manually selected
    - The evaluation does not measure actual user satisfaction
    - The reliability tests do not cover every possible input

## 8. Future Improvements

Potential improvements include allowing interactive preference entry, gathering voluntary user feedback, expanding genre representation, and testing alternative scoring weights.