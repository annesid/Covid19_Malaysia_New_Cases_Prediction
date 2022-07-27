# Covid19 New_Cases_Prediction (Malaysia)

## Covid19

The year 2020 was a catastrophic year for humanity. Pneumonia of unknown aetiology was first reported in December 2019. Since then, COVID-19 spread to the whole world and became a global pandemic. More than 200 countries were affected due to pandemic and many countries were trying to save precious lives of their people by imposing travel restrictions, quarantines, social distances, event postponements and lockdowns to prevent the spread of the virus.
 
 ## AI assisted automated tracking

The scientists believed that the absence of AI assisted automated tracking and predicting system is the cause of the wide spread of COVID-19 pandemic. Hence, the scientist proposed the usage of deep learning model to predict the daily COVID cases to determine if travel bans should be imposed or rescinded

### Time-series, RNN-LSTM, Deep Learning
This project will predict new cases for Covid19 in Malaysia using deep learning RNN - LSTM Model using past 30 days windows frame. 

3 hidden layers were used in this LSTM model

![model](https://user-images.githubusercontent.com/106498393/181194159-900beb59-6d99-4849-9316-a02cf02e98fb.png)

### 0.16% MAPE

Below is the actual vs prediction graph. with 0.16% MAPE (Mean Absolute Percentage Error).


<img width="358" alt="Covid19_PredictionGraph" src="https://user-images.githubusercontent.com/106498393/181194191-21a4a1a8-bd98-48f8-8f37-5549be39935f.png">


<img width="264" alt="MAPE_Prediction" src="https://user-images.githubusercontent.com/106498393/181194270-162a1f58-fe9b-452c-bc34-8d20d9add5b7.png">


### Tensorboard


<img width="997" alt="Covid19_tensorboard" src="https://user-images.githubusercontent.com/106498393/181194199-55739fe7-799e-466b-81b8-d78d791720bc.png">

### Data Source

    `Malaysian MOH Data
[Data](https://github.com/MoH-Malaysia/covid19-public) by MOH is readily available on ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


## Execution
There are 2 .py file included in this repo:
* covid19_prediction
* covid19_classes

To test the model, ![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252) link has been added in file : 
      
      `covid19_prediction

You can just execute using ![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252). covid19_classes has been pre-install on ![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)

## Contributing

:heart: Firstly, thank you for taking the time to contribute to this project! :heart:

Steps to contribute:
* Make your awesome changes
* Submit pull request; if you add a new entry, please give a very brief explanation why you think it should be added.

![Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
