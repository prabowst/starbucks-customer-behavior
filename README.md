## Starbucks Customer Behavior - Study of Rewards App

This project is an edited version of another repository on Starbucks Capstone Project for Udacity Nanodegree. This repository is created specifically for my web portfolio.

### Table of Contents 

1. [Requirements](#requirements)
2. [Project Description](#description)
3. [Files](#files)
4. [Project Results](#results)
5. [Licensing and Acknowledgements](#licensing)

### Requirements<a name="requirements"></a>

The code runs using Python version 3. Below are the list of packages used within this project.

1. pandas
2. numpy 
3. math
4. json
5. re
6. datetime
7. matplotlib
8. seaborn
9. sklearn
10. xgboost

### Project Description<a name="description"></a>

The project aims to build a robust machine learning model in determining customers behavior of Starbucks rewards mobile app. The data sets provided are simulated version of the rewards mobile app data. The data sets are cleaned, explored, processed into one master DataFrame which is fed into various machine learning models. The machine learning model with ideal learning curve and high accuracy is determined to be the best fit for this project.

### Files<a name="files"></a>

The files are organized as follows. 

```
- data
|- portfolio.json
|- transcript.json
|- profile.json
|- processed_data.csv

- figures
|- channel_dist.svg
|- event_types.svg
|- heatmap_features.svg
|- learning_curve_adaboostclassifier.svg 
|- learning_curve_randomforestclassifier.svg
|- learning_curbe_xgbclassifier.svg
|- offer_id_gender_dist.svg
|- profile_age.svg
|- profile_income.svg
|- profile_membership.svg
|- tree.svg
|- XGB_feature_importance.svg

- starbucks_customer_behavior.ipynb
- starbucks_customer_behavior.html
- init_setup.py
- README.md
```

### Project Results<a name="results"></a>

The XGB Classifier is chosen as the best machine learning model for this classification problem. The accuracy of this model reaches up to 91.43%, also checked with confusion matrix to avoid class prediction bias. 

![conf_mat](https://github.com/prabowst/starbucks-customer-behavior/blob/master/figures/confusion_matrix.svg)

This model specifies the following as its top three features importance:

1. offer_duration
2. money_spent
3. channel_social

Offer duration might be significant since it specifies the number of days the duration of the offer lasts. The longer the offer lasts, the higher the chance for a particular customer to fulfill its requirement.

![feature_importance](https://github.com/prabowst/starbucks-customer-behavior/blob/master/figures/XGB_feature_importance.svg)

How about money spent? Unlike income, the money spent by a user typically reflects a closer lifestyle of that person. The more often you buy, the higher the chance that you will buy enough to meet the offer conditions. This is more informational than the income information, since it only gives an idea of how much money they make, not how much money they are willing to spend.

Finally, the social channel feature. The fact that this comes in the top three features signifies how social channel is the one that majority of people pay more attention to. This can be used as a reasoning for Starbucks to concentrate more on advertising or sending their offers through these social channels, instead of through web for example. One thing to note, from the previous findings the combination of both social channel and web channel seems to be the most effective. 

Since the model trains with these channels as separate features, it might portray the web channel to be inferior in comparison to the social channel (it is possible, but both still gives significant contribution).

The main project results can be found in this [blog post](https://medium.com/@prabowoas1002/starbucks-capstone-challenge-16f4234d447b).

### Licensing and Acknowledgements<a name="licensing"></a>

Credit to Udacity and Starbucks for the capstone project and data sets. 
