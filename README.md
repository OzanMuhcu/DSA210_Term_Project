# Chess Data Analysis - DSA210 Project

## **Project Overview**
In this project, I will explore chess games and player profiles using data from Lichess. My goal is to examine statistical trends related to player nationality, rating, game type, and opening choices. I aim to uncover patterns such as which openings are most effective at different rating levels, how player profiles influence their game types, and which counterplay strategies are most successful against specific openings.

This project brings together my love for chess and data analysis. Instead of relying on complicated chess engines to figure out winning probabilities, I’m keeping it simple. I’ll focus on basic stats and correlations to spot interesting trends without getting bogged down in unnecessary details.

---

## **Objectives**

1. **Opening Effectiveness by Rating**
   - Determine which openings perform best for different Elo
   - Identify the most common openings and their win rates 

2. **Player Profile and Game Type Correlation**
   - Analyze player profiles (e.g., country, rating) and their influence on game type (e.g., Blitz, Bullet, Classical).
   - Which specific rating groups prefer different time controls or openings

3. **Counterplay Effectiveness**
   - Study which openings work best at some rating levels
   - Find correlations between openings and their most successful responses 

4. **Applying Data Science Skills**
   - Use data collection, preprocessing, visualization, and statistical analysis

---

## **Dataset**

In order to conduct this analysis, I will be collecting two kinds of data from the Lichess databases:

### **1. Game Data**
Each game record will include:
- **Game ID**: Unique identifier for each match
- **Player Ratings**: Ratings of both players 
- **Game Type**: Blitz, Bullet, Classical, Rapid ...
- **Opening Name**: Opening used in the game 
- **Game Result**: Win, loss, or draw
- **Moves Played**: Move sequence (may be)
- **Time Control**: Game duration and increment

### **2. Player Profile Data**
Each player's profile will include:
- **Username**: Identifier for players
- **Country**: The player's country
- **Peak Rating**: Highest rating player got in each time control
- **Game Preferences**: Most played game type (e.g., Blitz vs. Bullet)
- **Account Type**: Titled player or a casual player
- **Total win/lose/draw**: Number of previous recorded win/lose/draw 

---

## **Data Collection Plan**

1. **Extracting Data from Lichess API**
   - Use Lichess API to download game and player [data](https://database.lichess.org/)
   - Filter some of the data to keep it simple (time period, rating, country ...)

2. **Ensuring Data Quality**
   - Handle missing values (missing country data, ...)
   - Normalize data formats (convert game times to a common format, ...)

## **Analysis Plan**

1. **Data Preprocessing**
   - Convert lichess data into structured [Data Frames](https://github.com/OzanMuhcu/DSA210_Term_Project/tree/main/data)
   - Handle missing or inconsistent values
   - [Enriched game data](https://github.com/OzanMuhcu/DSA210_Term_Project/tree/main/enriched_data) with player metadata from Lichess for deeper analysis. 

2. **Exploratory Data Analysis [(EDA)](https://github.com/OzanMuhcu/DSA210_Term_Project/tree/main/EDA_on_data)**
   - **Opening Popularity by Elo**: Identify which openings are most common in different rating
   - **Win Rate by Opening**: Determine which openings perform best
   - **Player Profile Trends**: Find correlations between player country, rating, and preferred game type.

---

## Hypothesis Testing

### Research Question 1: A45 - Queen's pawn game - Opening

To go beyond descriptive analysis, a formal hypothesis test was conducted to investigate whether Black wins more frequently when using the A45 opening compared to all other openings **for high elo.**

#### Hypotheses

- **Null Hypothesis (H₀):**  
  The proportion of Black wins with the A45 opening is less than or equal to the proportion of Black wins in all other openings.

- **Alternative Hypothesis (H₁):**  
  The proportion of Black wins with the A45 opening is greater than in other openings.

#### Test Method

A one-sided two-proportion Z-test was used to compare the Black win rates between:

- **Group 1:** Games using the A45 opening  
- **Group 2:** All other games (non-A45)

---

### Research Question 2: C20 - King's pawn game - Opening

Similarly, a hypothesis test was conducted to determine whether the C20 opening results in more White wins compared to all other openings **for low elo.**

#### Hypotheses

- **Null Hypothesis (H₀):**  
  The proportion of White wins with the C20 opening is less than or equal to the proportion of White wins across all other openings.

- **Alternative Hypothesis (H₁):**  
  The proportion of White wins with the C20 opening is greater than in other openings.

#### Test Method

A one-sided two-proportion Z-test was used to compare the White win rates between:

- **Group 1:** Games using the C20 opening  
- **Group 2:** Games using any opening except C20

---

### Research Question 3: C41  - Philidor Defense - Opening

To explore whether the C41 opening leads to more draws than expected compared to other openings **for mid elo.**

#### Hypotheses

- **Null Hypothesis (H₀):**  
  The proportion of draws with the C41 opening is less than or equal to the proportion of draws in all other openings.

- **Alternative Hypothesis (H₁):**  
  The proportion of draws with the C41 opening is greater than in other openings.

#### Test Method

A one-sided two-proportion Z-test was used to compare the draw rates between:

- **Group 1:** Games using the C41 opening (Philidor Defense)  
- **Group 2:** Games using any other opening except C41

## **Expected Findings**

By the end of this project, I expect to answer questions such as:
- What openings tend to be most effective at various Elo levels?  
- What are some common counter strategies for popular openings?  
- Do players from specific countries show a preference for particular openings or styles of play?  
- How do the opening choices of Blitz and Bullet (or other gametypes) players differ from one another?  

These insights could be truly valuable for me and my other players who are looking to improve their game strategies. 

---

## **Conclusion**
This project aims to uncover meaningful insights from chess games and player profiles by analyzing opening trends, player behaviors, and win probabilities across different rating levels. Through data visualization and statistical testing, I hope to identify useful strategies that can help chess players improve their game while also applying my data analysis skills to a subject I’m passionate about.

By exploring chess through the data science, I’ll not only deepen my understanding of game patterns but also strengthen my skills in data collection, processing, and statistical evaluation.

---

I’m excited to see what the data reveals and to deepen my chess knowledge through this analysis.

