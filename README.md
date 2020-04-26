# Reddit Flair Detector

A Reddit Flair Detector web application to detect flairs of r/india subreddit posts using Machine Learning algorithms. The application can be found live at [Reddit Flair Predictor](https://flair-predictor-riya.herokuapp.com/).

### Codebase Structure

The directory is a ***Django*** web application set-up for hosting on *Heroku* servers.

  1. [manage.py] - The file used to start Django server.
  2. [requirements.txt] - Contains all Python dependencies of the project needed to reproduce the development environment.
  3. [nltk.txt]-  Containing all NLTK library needed dependencies.
  4. [Procfile] - Needed to setup Heroku.
  5. [website/flairPredictor] - Django application root directory.
  8. [csv_data] - Folder containing dataset in CSV format.
  9. [model] - Folder containing the saved model.
  10. [Notebooks]- Folder containing Jupyter Notebooks to collect Reddit India data and train Machine Learning models. 
  
### Codebase

The entire code has been developed in Python. The web inerface is handled using Django and DjangoRestFramework.

### Project Execution

  1. Open the `Terminal`.
  2. Clone this repository.
  3. Ensure that `Python3` and `pip` is installed on the system.
  4. Create a `virtualenv` by executing the following command: `virtualenv -p python3 env`.
  5. Activate the `env` virtual environment by executing: `source env/bin/activate`.
  6. cd into the cloned repository directory and run `pip install -r requirements.txt` to download project dependencies.
  7. Enter `python` shell and `import nltk`. Execute `nltk.download('stopwords')` and exit the shell.
  8. Now, execute the following command: `python manage.py runserver` and it will point to the `localhost` with the port. Access the url in browser aplication.

  
### Dependencies

The following dependencies can be found in [requirements.txt]:

  1. [praw](https://praw.readthedocs.io/en/latest/)
  2. [scikit-learn](https://scikit-learn.org/)
  3. [nltk](https://www.nltk.org/)
  4. [Django](https://www.djangoproject.com/)
  5. [bs4](https://pypi.org/project/bs4/)
  6. [pandas](https://pandas.pydata.org/)
  7. [numpy](http://www.numpy.org/)
  
### Approach

The approach taken for the task is as follows:

  1. Collect 100 r/india posts for each of the 12 flairs using `praw` module.
  2. The data includes *title, comments, body, url, author, score, id, time-created* and *number of comments*.
  3. For **comments**, only top level comments are considered in dataset and no sub-comments are present.
  4. The ***title, comments*** and ***body*** are cleaned by removing bad symbols and stopwords using `nltk`.
  5. Following types of features are considered for the the given task:
    
    a) Title
    b) Comments
    c) Urls
    d) Body
    e)Combinations of Title, comments and Body in pairs.
    f) Combining Title, Comments and Body as one feature.

  6. The dataset is split into **90% train** and **10% test** data using `train-test-split` of `scikit-learn`.
  7. Then, the following ML algorithms (using `scikit-learn` libraries) are applied on the dataset:
    
    a) Naive-Bayes
    b) Linear Support Vector Machine
    c) Logistic Regression
    d) Random Forest
    e) MLP

   8. Training and Testing on the dataset showed the **Logistic Regression** showed the best testing accuracy of **76%** when trained on the combination of **Title + Comments + Body** feature.
   9. The best model is saved and is used for prediction of the flair from the URL of the post.
    
### Results

#### Title as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Random Forest              | 0.583333333334    |
| Logistic Regression        | 0.5666666666667   |
| Linear SVM                 | 0.575             |
| MLP                        | 0.5333333333333   |

#### Body as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Random Forest              | 0.3               |
| Logistic Regression        | 0.3               |
| Linear SVM                 | 0.3               |
| MLP                        | 0.275             |

#### Comments as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Logistic Regression        | 0.6416666666666667|
| Linear SVM                 | 0.5916666666666667|
| MLP                        | 0.525             |


#### Title and Comments combined as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Random Forest              | 0.633333333333333 |
| Logistic Regression        | **0.733333333333**|
| Linear SVM                 | 0.6916666666666667|
| MLP                        | 0.6              |

#### Title and Comments and Body combined as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Random Forest              | 0.65              |
| Logistic Regression        | **0.7666666666**  |
| Linear SVM                 | 0.725             |
| MLP                        | 0.6583333333333   |






### References

1. [Scraping Reddit Data](https://towardsdatascience.com/scraping-reddit-data-1c0af3040768)
2. [Praw Documentation](https://praw.readthedocs.io/en/latest/)
3. [Multi-Class Text Classification Model Comparison and Selection](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568)
