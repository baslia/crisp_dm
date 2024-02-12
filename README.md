# CRISP-DM Methodology

The Cross-Industry Standard Process for Data Mining (CRISP-DM) is a robust and well-established data mining process model that provides a structured approach to planning a data mining project.
Here is a brief overview of the CRISP-DM process:

![CRISP-DM](images/CRISP-DM-data-mining-framework.png)

## 1. Business Understanding

This initial phase focuses on: Understanding the project objectives and requirements from a business perspective Converting the objectives and requirements into a data mining problem definition and a preliminary plan, both of which are designed to achieve the project objectives In simple terms, this phase focuses on:

Defining the business problem or categorizing the types of insights desired Defining the business decisions that the desired insights will inform and the types of actions that will be taken
## 2. Data Understanding

The data understanding phase (also called exploratory data analysis) starts with an initial data collection and assessment to identify key trends. Data exploration and visualization yield key insights about:

Data quality and missing variables Data coverage including whether additional data must be brought in, derived, or acquired to support business objectives Trends and relationships among key variables
## 3. Data Preparation

The data preparation phase covers all the activities needed to construct the modeling dataset or modeling universe. This data is subsequently fed into the modeling software.

This phase also includes outlier treatment, variable preparation, transformation, normalization, reduction, and imputation. Data preparation tasks are iterative and may need to be performed multiple times depending on the outcome of the modeling step (i.e. assessing whether the model “fits” the data).

Typically, the data required for a data mining project resides across multiple systems that do not talk to each other, is noisy, contains duplicate information, and/or requires significant massaging in order to support a modeling effort.

There is no perfect data. It is always noisy and full of hidden surprises. On average, data preparation and data understanding tasks account for more than 75% of the effort in a data mining project (Press, 2016).
## 4. Modeling

In this phase, various modeling techniques are selected and applied, and their parameters are calibrated to achieve optimal values. Depending on the modeling outcome (assessment of model fit), it may be necessary to return to the data preparation phase before continuing.

Typically, there are several techniques that can be applied to a data mining problem. Choosing an appropriate technique depends on such factors as:

Model performance Predictive or explanatory power requirements Data volume/speed One-off vs. repeatable processes Supervised vs. unsupervised learning
## 5. Evaluation

At this stage, the model (or models) that have been constructed should be of high quality from a data analysis perspective. Before proceeding to the final deployment, however, the model(s) must be evaluated to ensure they align with the project’s business objectives.

Conducting a sensitivity analysis across various scenarios is an essential part of this phase. A key objective is to determine if there are any important business issues that have not been sufficiently considered. At the end of this phase, a decision on the use of the analytical results should be reached.
## 6. Deployment

Proper model deployment is critical to ensure the successful adoption or integration of analytics into an organization’s business processes. Deployment can lead to such capabilities as scoring a database (e.g. evaluating a customer’s likelihood of responding to an offer or assessing a credit card holder’s risk), personalizing a web page in real time, or enabling a binary decision (such as whether or not to proceed with an acquisition).

In order to achieve a successful deployment, it is critical to work with customers or business process owners to make sure they are comfortable with the outcomes and fully understand how the data model works (that is, the model is not perceived simply as a “black box”).