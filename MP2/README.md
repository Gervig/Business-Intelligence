# Wine Quality Analysis (MP2)

This project performs a comprehensive exploratory data analysis on red and white wine datasets to understand the relationships between various chemical properties and wine quality.

## Project Overview

The analysis combines two wine quality datasets (red and white wines) to explore patterns, correlations, and distributions of various chemical properties that influence wine quality. The project includes data cleaning, preprocessing, normalization, and extensive statistical analysis with visualizations.


## Key Features

### 1. Data Preprocessing
- **Data Integration**: Combines red and white wine datasets with type encoding
- **Data Cleaning**: 
  - Removes 1,177 duplicate entries
  - Checks for missing values (none found)
  - Validates data integrity (no negative values or invalid pH ranges)
- **Outlier Detection**: Identifies values outside expected ranges for different wine types
- **Encoding**: Converts categorical wine type to numerical (Red=0, White=1)
- **Normalization**: Applies MinMax scaling to all numerical features

### 2. Statistical Analysis
- **Descriptive Statistics**: Comprehensive summary statistics for all features
- **Correlation Analysis**: Pearson correlation matrices for different wine types
- **Distribution Analysis**: Examines normality and skewness of key variables

### 3. Data Visualization
- **Correlation Heatmaps**: Visual correlation matrices for all wines, red wines, and white wines
- **Histograms**: Distribution analysis with normal curve overlays
- **Scatter Plots**: Relationship exploration between key variables
- **Box Plots**: Comparative analysis between wine types
- **Binning Analysis**: pH distribution categorization

## Key Findings

### Wine Type Differences
- **White wines** have higher average quality, alcohol content, and residual sugar
- **Red wines** show stronger correlations between fixed acidity and pH
- **Residual sugar** has much higher variance in white wines, creating stronger density correlations

### Correlation Insights
- **Red wines**: Strong negative correlation between fixed acidity and pH (-0.68)
- **White wines**: Strong positive correlation between residual sugar and density (0.84)
- **Alcohol-density relationship**: More pronounced in white wines due to better normal distribution

### Chemical Property Analysis
- **Fixed acidity** is the primary determinant of pH in wines
- **Volatile acidity** shows minimal correlation with pH due to low concentrations
- **Citric acid** correlation falls between volatile and fixed acidity as expected

## Technical Requirements

### Dependencies
```python
pandas
matplotlib
seaborn
numpy
sklearn
scipy
```

### File Structure
```
wine-data/
├── winequality-red.xlsx
└── winequality-white.xlsx
MP2.ipynb
README.md
```

## Usage

1. Place the wine data files in a `wine-data` folder
2. Run the Jupyter notebook `MP2.ipynb` cell by cell
3. The analysis will automatically:
   - Load and combine the datasets
   - Clean and preprocess the data
   - Generate all statistical analyses and visualizations

## Analysis Sections

1. **Data Ingestion**: Loading and combining datasets
2. **Data Cleaning**: Removing duplicates and validating data quality
3. **Outlier Analysis**: Identifying values outside expected ranges
4. **Encoding & Normalization**: Preparing data for analysis
5. **Exploratory Analysis**: Statistical exploration with visualizations
6. **Correlation Analysis**: Understanding relationships between variables
7. **Distribution Analysis**: Examining data normality and patterns

## Key Visualizations

- Correlation heatmaps for different wine types
- pH distribution histograms with normal curves
- Scatter plot matrices showing variable relationships
- Comparative box plots between wine types
- Residual sugar distribution analysis
- Alcohol vs. quality relationship plots

## Results Summary

The analysis reveals significant differences between red and white wines in terms of chemical composition and quality relationships. White wines demonstrate higher quality ratings on average and show different correlation patterns, particularly regarding residual sugar's impact on density. The study provides insights into which chemical properties most strongly influence wine quality for each wine type.

## Future Work

12. Explore the features for outliers? Which feature contains outliers? Which of the observations of this feature is outlier? Remove those observations. 
13. Remove the attributes, which aren’t correlated with the wine quality, as well as the attributes that are highly correlated with another independent attribute. 
14. Apply data transformation as preparation for further analysis: 
a. scaling, normalization and standartisation of the numeric variables 
b. dimensionality reduction by PCA (Principle Component Analysis). 
 
Create and Deploy Interactive Application 
15. Use Streamlit to build an application, which allows interactive data loading, analysis, and visualization of the outcomes. Apply various 2D and 3D data visualization techniques. 
16. Extend your application with useful information, extracted from the alternative public sources, collected in p.4 above. Apply AI techniques for operating with text and visuals. 