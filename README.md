![Review Scraper Project](Ceneo_Reviews_Sentiment_Analysis.png)
<br>
![Python](https://img.shields.io/badge/python-v3.11-blue.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
<a target="_blank" href="https://www.linkedin.com/in/tkacz-milosz-data-science/"><img height="20" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
<br>
This sentiment analysis project aims to analyze and classify the sentiment of customer reviews using natural language processing (NLP) techniques and machine learning models. The project is implemented in Python, leveraging popular libraries such as pandas, numpy, spacy, gensim, tensorflow, and scikit-learn.<br>
It is a second part of my Sentiment Analysis of Ceneo Reviews project. For the first part go to:<br>
https://github.com/LazyDart/Ceneo-Scrape

## Key Features
1. Data Cleaning Pipeline. (WIP)
2. Data Analysis of Ceneo Reviews. (WIP)
3. Polish Language Model Comparison: Comparing Default Spacy pl_core_news_lg word embedding with https://huggingface.co/clarin-pl/word2vec-kgr10 Clarin W2V word embedding. (WIP)
4. Sentiment Analysis Neural Network, Creating Model, Evaluating Model on different benchmarks. (WIP)

## Usage

Navigate to repo folder thru console and install the required dependencies:
```sh    
bash
pip install -r requirements.txt
```

After cloning the repository locally and installing dependencies data must be provided and put inside `./data folder`. It can be generated via Ceneo Scraper project. Follow instructions here(https://github.com/LazyDart/Ceneo-Scrape/blob/main/README.md)

## Additional Information
### Versions
    gensim==4.3.2
    huggingface_hub==0.20.1
    matplotlib==3.7.1
    numpy==1.23.5
    pandas==2.0.0
    scikit_learn==1.2.2
    seaborn==0.13.1
    spacy==3.7.2
    tensorflow==2.12.0

### WIP
Project is currently in HEAVY development stage. Alle the scripts and files change on day to day basis.

Feel free to reach out for any further clarifications or ideas.
