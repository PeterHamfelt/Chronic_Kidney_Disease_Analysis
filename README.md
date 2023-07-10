# Chronic Kidney Disease Analysis
 An application that can be used across biomedical data science projects. The dataset used for the proof of concept can help physicians better understand chronic kidney disease (CKD) using numerous measurements and biomarkers that have been collected. 


## Description

This project is a display of what can be done with machine learning in order to make some analysis over data such as the Chronic Kidney Disease dataset.


## Getting Started

### Dependencies

* python 3.10


### Installing

* Clone the project
* Create a virtual environment

    ```bash
    # Linux
    python -m venv .venv

    # Windows
    py -m venv .venv
    ```

* Activate the virtual environment
  
    ```bash
    # Linux
    .venv/bin/activate

    # Windows (batch/cmd)
    .venv/Scripts/activate.bat

    # Windows (powershell)
    .venv/Scripts/Activate.ps1
    ```

* Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

* Download the chronic kidney disease dataset from [here](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease) and extract it so that the .arff files are directly in the data/ folder.

* Unit testing
This code has been partially programmed following the Test Driven Developement approach. Here is the command to launch the tests script.

    ```bash
    python -m unittest discover
    ```


### Executing program

#### CKD Prediction

* import dependencies

    ```python
    from src import ETL_tool as ETL
    from sklearn.model_selection import train_test_split
    from autogluon.tabular import TabularDataset, TabularPredictor
    from pandas import DataFrame, Series, merge
    from sklearn.cluster import KMeans
    import seaborn as sns
    from autogluon.features import AutoMLPipelineFeatureGenerator
    from matplotlib import pyplot as plt
    import lightgbm as lgm
    import numpy as np

    set_option('display.max_columns', None)
    ```

* Extract Data

    ```python
    df = ETL.load_data("data/chronic_kidney_disease_full.arff")
    ```

* Prepare Data

    ```python
    df_train, df_test = train_test_split(df, test_size=0.33, random_state=1)
    test_data = df_test.drop(['class'], axis=1)
    ```

* Train Models

    ```python
    predictor = TabularPredictor(label='class').fit(train_data=df_train, verbosity=2, presets='best_quality')
    ```

* Display Training statistics

    ```python
    predictor.fit_summary()
    predictor.leaderboard(df_train, silent=True)
    ```

* Model Prediction Test and evaluation

    ```python
    y_pred = predictor.predict(test_data)
    df_pred = DataFrame(y_pred, columns=['class'])
    predictor.evaluate(df_test)
    ```

* Use Pretrained Model

    ```python
    predictor = TabularPredictor.load("AutogluonModels/ag-20230702_213736/")
    y_pred = predictor.predict(test_data)
    ```

#### CKD factors

* Feature importance

    ```python
    predictor.feature_importance(data=df_train)
    ```

* HeatMap

    ```python
    auto_ml_pipeline_feature_generator = AutoMLPipelineFeatureGenerator()
    new_df = auto_ml_pipeline_feature_generator.fit_transform(X=df)

    X=new_df.drop(['class'],axis=1)
    y=new_df['class']

    #get correlations of each features in dataset
    corrmat = new_df.corr()
    top_corr_features = corrmat.index
    plt.figure(figsize=(20,20))

    #plot heat map
    g=sns.heatmap(new_df[top_corr_features].corr(),annot=True,cmap="RdYlGn")
    ```

#### CKD subtypes

* Contributions

    ```python
    auto_ml_pipeline_feature_generator = AutoMLPipelineFeatureGenerator()
    new_df = auto_ml_pipeline_feature_generator.fit_transform(X=df)
    #new_df = new_df.dropna()
    X=new_df.drop(['class'],axis=1)
    columns = list(X.columns)
    y=new_df['class']

    #we create a basic lightGBM model :
    X_train = lgm.Dataset(X, y)
    parameters = {
        "max_depth":3,
        "random_state": 43
    }

    #we train our model
    basic_model = lgm.train(parameters,train_set = X_train)

    #We create a contributions table
    contributions = basic_model.predict(X, pred_contrib = True)
    dataframe_contributions = DataFrame(contributions, columns = columns+["expected_value"]).drop(['expected_value'], axis = 1)
    ```

* Clusters

    ```python
    # We'll be creating 5 clusters. 
    kmeans = KMeans(n_clusters=5, random_state=0).fit(dataframe_contributions)

    # We'll then proceed to create the dataframe we'll be using in our analysis. 
    # I would like to use the original dataset for this (use feature values instead of contribution values ),
    # and add columsn for target, prediction and KMeans cluster group. 

    X["PREDICTION"] = basic_model.predict(X, predict_proba = True)
    X['TARGET'] = y
    X["KMEANS_CLUSTER"]= kmeans.predict(dataframe_contributions)
    X['DIFF'] = X['TARGET']-X['PREDICTION']

    num_values=X.groupby("KMEANS_CLUSTER").mean()
    categorical_values=X.drop(list(num_values.columns),axis=1)
    categorical_values=categorical_values.replace(np.nan, "NaN")
    categorical_values=categorical_values.groupby("KMEANS_CLUSTER").apply(lambda x: x.mode(dropna =False))
    Clusters =merge(num_values, categorical_values, left_index=True, right_index=True)
    ```

## Authors

David Urban


## License

This project is licensed under the MIT License - see the LICENSE.md file for details


## Acknowledgments

* [DomPizzie](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [GhostofGoes](https://gist.github.com/GhostofGoes/94580e76cd251972b15b4821c8a06f59)
* [nicolasdao](https://gist.github.com/nicolasdao/a7adda51f2f185e8d2700e1573d8a633#mit-license)
* [Rahil Shaikh](https://towardsdatascience.com/feature-selection-techniques-in-machine-learning-with-python-f24e7da3f36e)
* [Ana Preciado](https://towardsdatascience.com/applying-a-clustering-algorithm-to-feature-contribution-3c649ab0ca17)