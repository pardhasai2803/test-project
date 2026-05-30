# Travel Clustering Project
## Overview
The Travel Clustering Project is a data analysis tool designed to cluster travel data using K-means and Agglomerative Hierarchical Clustering algorithms. The project utilizes various libraries, including NumPy, Pandas, and Scipy, to perform data analysis and clustering.

## Features
* **K-means Clustering**: The project implements the K-means clustering algorithm using the `k_means` function, which takes the number of clusters and a Pandas DataFrame as input.
* **Agglomerative Hierarchical Clustering**: The project also implements the Agglomerative Hierarchical Clustering algorithm using the `agglomerative_clustering` function, which takes the number of clusters and a Pandas DataFrame as input.
* **Silhouette Coefficient Calculation**: The project calculates the Silhouette Coefficient for each cluster using the `silhouette_coefficient` function.
* **Jaccard Similarity Calculation**: The project calculates the Jaccard similarity between clusters using the `jaccard_coefficients` function.

## Installation
To install the project, follow these steps:
1. Clone the repository to your local machine.
2. Install the required libraries by running `pip install numpy pandas scipy`.
3. Ensure that the `travel.csv` file is in the same directory as the project code.

## Usage
To use the project, follow these steps:
1. Run the `THRC.py` script using Python (e.g., `python THRC.py`).
2. The script will perform K-means clustering and Agglomerative Hierarchical Clustering on the travel data.
3. The script will calculate the Silhouette Coefficient for each cluster and print the results.
4. The script will also calculate the Jaccard similarity between clusters and print the results.

## Functions/API
The project provides the following functions:
* `k_means(n_clusters, df)`: Performs K-means clustering on the input DataFrame.
* `agglomerative_clustering(n_clusters, df)`: Performs Agglomerative Hierarchical Clustering on the input DataFrame.
* `silhouette_coefficient(n_clusters, final_clusters, df)`: Calculates the Silhouette Coefficient for each cluster.
* `jaccard_coefficients(file1, file2, n_clusters)`: Calculates the Jaccard similarity between clusters.
* `kmeans_to_file(n_clusters, final_clusters, filename)`: Writes the K-means clustering results to a file.
* `agglomerative_to_file(n_clusters, clusters, filename)`: Writes the Agglomerative Hierarchical Clustering results to a file.

## Requirements
* Python 3.x
* NumPy
* Pandas
* Scipy
* `travel.csv` file (provided with the project)