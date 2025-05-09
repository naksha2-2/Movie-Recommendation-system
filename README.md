# Movie-Recommendation-system
Movie Recommendation System
This project implements a Movie Recommendation System using K-Nearest Neighbors (KNN) and Cosine Similarity. The system recommends movies similar to a given movie based on the ratings from the MovieLens dataset.

Table of Contents
Overview

Installation

Usage

Dependencies

License

Overview
This project uses the MovieLens 100K dataset to recommend movies based on a given movie's similarity. The similarity is calculated using cosine similarity between movie vectors, which are generated from users' ratings.

The system can provide top movie recommendations when a movie title is inputted. The model uses a user-movie rating matrix to calculate similarities.

Key Features:
Uses cosine similarity to calculate movie similarity.

Provides top 5 movie recommendations based on a given movie.

Built with Pandas and Scikit-Learn libraries.

Installation
To use the movie recommendation system, you will need to set up a Python environment and install the necessary dependencies.

Step 1: Clone this repository
bash
Copy
Edit
git clone https://github.com/your-username/movie-recommendation.git
Step 2: Install Dependencies
Create a virtual environment and install the required libraries.

bash
Copy
Edit
pip install -r requirements.txt
OR if you're not using requirements.txt:

bash
Copy
Edit
pip install pandas scikit-learn
Step 3: Download the MovieLens Dataset
Download the MovieLens 100K dataset from here and place the following files in the ml-100k/ directory:

u.data (user ratings)

u.item (movie titles)

Usage
Step 1: Run the Script
Run the script file.py using the Python interpreter:

bash
Copy
Edit
python file.py
Step 2: Get Recommendations
The script will output the top 5 recommended movies similar to "Star Wars (1977)" (or whichever movie title you choose to change in the script). To change the movie title, locate the following line in file.py:

python
Copy
Edit
print(recommend('Star Wars (1977)'))
Change 'Star Wars (1977)' to any other movie title from the dataset.

For example:

python
Copy
Edit
print(recommend('The Godfather (1972)'))
The script will then output the top 5 movies similar to "The Godfather (1972)".

Sample Output:
java
Copy
Edit
Top 5 recommendations similar to 'Star Wars (1977)':
Return of the Jedi (1983)    0.884476
Raiders of the Lost Ark (1981) 0.764885
Empire Strikes Back, The (1980) 0.749819
Toy Story (1995)               0.734572
Godfather, The (1972)          0.697332
Name: Star Wars (1977), dtype: float64
Dependencies
This project requires the following Python libraries:

pandas — for data manipulation and analysis

scikit-learn — for cosine similarity and machine learning algorithms

You can install the dependencies using pip:

bash
Copy
Edit
pip install pandas scikit-learn
License
This project is open source and available under the MIT License.

Feel free to adapt the details like repository URL, additional features, etc. based on your actual project setup. Let me know if you'd like me to add anything else!








