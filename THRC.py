import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import fcluster, linkage
import os

# # Take data from a file
def get_data(filepath):
    return pd.read_csv(filepath)

# Calculating cosine similarity
def cosine_similarity(x, y):
    if np.linalg.norm(x) * np.linalg.norm(y) == 0:
        return 0.0
    return 1 - np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

# K-means Clustering
def k_means(n_clusters, df):
    k = n_clusters

    # Randomly initializing k points
    init_points = df.sample(n=k)
    means = init_points.values.tolist()

    # Running K-means 20 times
    final_clusters = [[] for _ in range(k)]
    for _ in range(20):
        clusters = [[] for _ in range(k)]
        for point in df.values:
            distances = [cosine_similarity(point[1:11], mean) for mean in means]
            nearest_mean_index = np.argmax(distances)
            clusters[nearest_mean_index].append(point)
        for j in range(k):
            if len(clusters[j]) > 0:
                means[j] = np.mean([point[1:11] for point in clusters[j]], axis=0)
    return final_clusters


# Calculation of Silhouette Coefficient for each sample
def silhouette_coefficient(n_clusters, final_clusters, df):
    s = 0
    for i in range(len(df)):
        cluster_index = None
        for j in range(n_clusters):
            if df.values[i] in final_clusters[j]:
                cluster_index = j
                break
        if cluster_index is not None and cluster_index != -1:
            # Calculating a
            a = 0
            dist_a = [cosine_similarity(df.values[i][1:11], other_pts[1:11]) for other_pts in final_clusters[cluster_index] if not np.array_equal(df.values[i], other_pts)]
            if len(dist_a) > 0:
                a = np.mean(dist_a)

            # Calculating b
            cluster_labels = fcluster(linkage(df.values[:, 1:11], method='ward'), n_clusters, criterion='maxclust')
            b = np.inf
            dist_b = []
            points_in_cluster = []
            for j in range(1, n_clusters+1):
                for point in final_clusters[cluster_labels == j]:
                    dist = cosine_similarity(df.values[i][1:11], point[1:11])
                    dist_b.append(dist)
                    points_in_cluster.append(point)
                    if len(dist_b) > 0:
                        if dist_mean(dist_b) < b:
                            b = dist_mean(dist_b)
                        if len(points_in_cluster) > len([p for p in points_in_cluster if np.array_equal(p, df.values[i]) == False]):
                            dist_b = []
                            b = np.inf
            if a != 0 and b != np.inf:
                s = (b - a) / max(a, b)

        silhouette_coeff += s / len(df.values)
    return silhouette_coeff


def kmeans_to_file(n_clusters, final_clusters, filename):
    f = open(filename, "w")
    for j in range(n_clusters):
        user_count = 0
        for point in final_clusters[j]:
            x = str(point[0])
            x = x[5:]
            if user_count == 0:
                f.write(x)
            else:
                f.write(", ")
                f.write(x)
            user_count += 1
        if j < n_clusters-1:
            f.write("\n")
    f.close()


def agglomerative_clustering(n_clusters, df):
    cosine_distances = squareform(pdist(df.values[:, 1:11], metric='cosine'))

    clusters = [[i] for i in range(len(df.values))]
    k = min(n_clusters, len(df.values))
    while len(clusters) > k:
        min_dist = np.inf
        merge_cluster_index1 = -1
        merge_cluster_index2 = -1
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                dist = np.min(cosine_distances[np.ix_(np.ravel(clusters[i]),np.ravel(clusters[j]))])
                if dist < min_dist:
                    min_dist = dist
                    merge_cluster_index1 = i
                    merge_cluster_index2 = j
        clusters[merge_cluster_index1].extend(clusters[merge_cluster_index2])
        del clusters[merge_cluster_index2]
    return clusters


def agglomerative_to_file(n_clusters, clusters, filename):
    f = open(filename, "w")
    for j in range(n_clusters):
        user_count = 0
        for point in clusters[j]:
            x = str(point) + "1"
            if user_count == 0:
                f.write(x)
            else:
                f.write(", ")
                f.write(x)
            user_count += 1
        if j < n_clusters-1:
            f.write("\n")
    f.close()


def jaccard_coefficients(file1, file2, n_clusters):
    os.system(f"mkdir -p results")

    try:
        os.remove(f"results/jaccard_similarities.txt")
    except OSError:
        pass

    result1 = []
    with open('results/kmeans.txt', "r") as f:
        lines = [line.strip().split(",") for line in f.readlines()]
    for line in lines:
        if line[0] == '':
            line[0] = '981'
        result1.append([int(x) for x in line])

    try:
        os.remove(file1)
    except OSError:
        pass
    kmeans_to_file(n_clusters,clusters[n_clusters],"kmeans.txt")


    result2 = []
    with open('results/agglomerative.txt', "r") as f:
        lines = [line.strip().split(",") for line in f.readlines()]
    for line in lines:
        if line[0] == '':
            line[0] = '981'
        result2.append([int(x) for x in line])

    try:
        os.remove(file2)
    except OSError:
        pass
    agglomerative_to_file(n_clusters,clusters[n_clusters],"agglomerative.txt")


    jaccard_list = []
    for i in range(n_clusters):
        jaccard_similarities = []
        A = set(result1[i])
        for j in range(n_clusters):
            B = set(result2[j])
            intersection = len(A.intersection(B))
            union = len(A.union(B))
            jaccard_similarity = intersection / union
            jaccard_similarities.append(jaccard_similarity)
        jaccard_list.append(jaccard_similarities)

    with open(f'results/jaccard_similarities.txt', "a+") as f:
        for i in range(n_clusters):
            avg = sum(jaccard_list[i])/len(jaccard_list[i])
            f.write(f'Jaccard Similarities for cluster {i}: {avg}\n')
    print('Jaccard Similarities were logged in results/jaccard_similarities.txt')
    return jaccard_list


if __name__ == "__main__":
    df = get_data('travel.csv')
    clusters = {}
    max_silhouette = -2
    optim_clusters = -1
    for i in range(3, 7):
        clusters[i] = k_means(n_clusters=i, df=df)
        silhouette_value = silhouette_coefficient(n_clusters=i, final_clusters=clusters[i], df=df)
        if silhouette_value > 0:
            print(f'k={i}')
            print(f'The Silhouette Coefficient is : {silhouette_value}')
            if silhouette_value > max_silhouette:
                max_silhouette = silhouette_value
                optim_clusters = i
    print(f'The optimal value is :\nk = {optim_clusters}')
    kmeans_to_file(optim_clusters,clusters[optim_clusters],"kmeans.txt")
    clusters[optim_clusters] = agglomerative_clustering(optim_clusters,df)
    agglomerative_to_file(optim_clusters,clusters[optim_clusters],"agglomerative.txt")
    jaccard_matrix = jaccard_coefficients("kmeans.txt", "agglomerative.txt", optim_clusters)
    for i in range(len(jaccard_matrix)):
        print(f'jaccard_similarities for cluster {i} : {jaccard_matrix[i]}')