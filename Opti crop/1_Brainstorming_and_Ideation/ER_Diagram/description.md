# Entity Relationship Diagram Documentation

## Project Title

OptiCrop – Smart Agricultural Production Optimization System

## Introduction

The Entity Relationship (ER) Diagram represents the database structure of the OptiCrop system. It illustrates the entities, attributes, relationships, primary keys, and foreign keys required to manage agricultural data and crop prediction processes.

## Entities

### 1. User

Attributes:

* user_id (Primary Key)
* name
* email
* password
* phone_number

### 2. SoilData

Attributes:

* soil_id (Primary Key)
* user_id (Foreign Key)
* nitrogen
* phosphorus
* potassium
* temperature
* humidity
* ph
* rainfall

### 3. Crop

Attributes:

* crop_id (Primary Key)
* crop_name
* crop_type
* description

### 4. Dataset

Attributes:

* dataset_id (Primary Key)
* dataset_name
* source
* upload_date

### 5. MLModel

Attributes:

* model_id (Primary Key)
* dataset_id (Foreign Key)
* model_name
* algorithm
* accuracy

### 6. Prediction

Attributes:

* prediction_id (Primary Key)
* soil_id (Foreign Key)
* crop_id (Foreign Key)
* model_id (Foreign Key)
* prediction_date
* confidence_score

### 7. Report

Attributes:

* report_id (Primary Key)
* prediction_id (Foreign Key)
* report_date
* recommendation
* summary

## Relationships

### User → SoilData

Relationship Type: One-to-Many (1:M)

A single user can submit multiple soil data records.

### SoilData → Prediction

Relationship Type: One-to-One (1:1)

Each soil data record generates one crop prediction.

### Crop → Prediction

Relationship Type: One-to-Many (1:M)

One crop can appear in multiple prediction results.

### Dataset → MLModel

Relationship Type: One-to-Many (1:M)

One dataset can train multiple machine learning models.

### MLModel → Prediction

Relationship Type: One-to-Many (1:M)

One machine learning model can generate multiple prediction records.

### Prediction → Report

Relationship Type: One-to-Many (1:M)

One prediction can generate multiple agricultural reports.

## Primary Keys

* User: user_id
* SoilData: soil_id
* Crop: crop_id
* Dataset: dataset_id
* MLModel: model_id
* Prediction: prediction_id
* Report: report_id

## Foreign Keys

* SoilData.user_id references User.user_id
* Prediction.soil_id references SoilData.soil_id
* Prediction.crop_id references Crop.crop_id
* Prediction.model_id references MLModel.model_id
* Report.prediction_id references Prediction.prediction_id

## Conclusion

The ER Diagram provides a structured database design for the OptiCrop system. It supports efficient storage and management of user information, soil parameters, crop recommendations, machine learning models, prediction records, and agricultural reports, enabling data-driven decision-making in smart agriculture.
