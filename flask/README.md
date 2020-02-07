# GlimpseK12
 Maximizing student outcomes through predictive analytics. 

# Introduction
Glimpse K12 is a company that provides return on investment (ROI) analyses for schools that want to be more efficient with spending. Historically, Glimpse has provided ROI analyses in two ways. 
- One, by identifying tools and resources that are purchased and go unused by the students. 
- Two, by identifying correlations between educational spending and student test outcomes. 

As part of product discovery, Glimpse wanted to learn how well we could predict student testing outcomes using a subset (~ 292,419 observations) of a larger database. Math and reading outcomes were chosen for this pass at product discovery. 

# Navigation section. 
Bulleted list with links to other sections of the README doc. 

# Tools and technologies used. 
- Languages: Python, PostgreSQL, HTML/CSS
- Tools: Pandas, Scikit-learn, NumPy, Matplotlib, Seaborn, Flask, AWS

## Work flow 
(1) Flat files obtained from company. 
(2) Pre-processed using Python language and tools Pandas, NumPy
(3) Exploratory Data Analysis using Python language and tools Pandas, NumPy, Matplotlib, and Seaborn
(4) Baseline modeling and analyses using Python language and tools Pandas, Scikit-learn, Matplotlib
	- Regression models developed to predict testing scores
	- Classification models developed to predict academic proficiency (binary - proficient or not)
(5) Feature extraction through consultation with Glimpse domain experts. 
(6) Dimensionality reduction (PCA) using Python langauge and tools Pandas and Scikit-learn
(7) Re-test baseline models on modified dataset
(8) Researched competing regression and classification models using Python language and tools Pandas, Matplotlib, Scikit-learn, and NumPy; Validated using holdout validation datasets. 
(9) Final models selected
(10) Demonstrated how these models could be used to generate insight
	- Used models and data to predict academic outcomes for the grade each student would enter next
	- Predictions stored in PostgreSQL database
	- Webapp developed using Python, HTML, and CSS
	- Webapp deployed using Flask with AWS (www.behavioralpredictions.xyz)

This project is licensed under GNU General Public License v3.0.
