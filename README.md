# Chess Data Analysis - DSA210 Project

## **Project Overview**
In this project, I will analyze chess games and player profiles with using data collected from Lichess. My goal is to understand statistical trends related to player country, rating, game type, and opening choices. I aim to identify patterns such as which openings are more effective at different rating levels, how player profiles correlate with game types, and what counterplay strategies work best against certain openings.

This project combines my passion for chess and data analysis. Unlikee advanced chess engines which calculates probabilities for winning, I will keep the analysis simple by focusing on fundamental statistics and correlations.

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

To make this analysis, I will collect two types of data from Lichess databases:

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

---

## **Data Collection Plan**

1. **Extracting Data from Lichess API**
   - Use Lichess API to download game and player data
   - Filter some of the data to keep it simple (time period, rating, country ...)

2. **Ensuring Data Quality**
   - Handle missing values (missing country data, ...)
   - Normalize data formats (convert game times to a common format, ...)

## **Analysis Plan**

1. **Data Preprocessing**
   - Convert lichess data into structured Data Frames
   - Handle missing or inconsistent values

2. **Exploratory Data Analysis (EDA)**
   - **Opening Popularity by Elo**: Identify which openings are most common in different rating
   - **Win Rate by Opening**: Determine which openings perform best
   - **Player Profile Trends**: Find correlations between player country, rating, and preferred game type.

---

## **Expected Findings**

By the end of this project, I expect to answer questions such as:
- Which openings perform best at different Elo levels?
- What are the most common counterplays for popular openings?
- Do players from certain countries favor specific openings or game types?
- How do Blitz and Bullet (or any gametpe) players differ in their opening selections?

These insights can provide valuable information for me and players who looking to optimize their game strategies based on their rating and preferred game type or other perspectives I will study.

---

## **Conclusion**
This project aims to bring light to meaningful insights from chess games and player profiles via analyzing opening trends, player behaviors, and win probabilities across rating levels. With using data visualization and statistical testing, I hope to find and be able to provide useful strategies for chess players while applying my data analysis skills to a subject I am passionate about.

By using data science techniques, I will gain a better understanding of chess patterns while also developing skills in data collection, processing, and statistical evaluation.

---

I look forward to seeing what the data tells and improvine my chess knowledge through this analysis.

