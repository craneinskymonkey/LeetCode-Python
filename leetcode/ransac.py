#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time: 2024/3/6 下午10:32
# @Author: houhaiyang
# @Project: LeetCode-Python
# @File：ransac.py
# @Description: 随机采样一致性算法
# @company：


import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA


def ransac_3d(data, n, k, t, d):
    """
    RANSAC-3D algorithm for plane fitting
    :param data: 3D point cloud data
    :param n: the minimum number of points to fit a plane
    :param k: the maximum number of iterations
    :param t: the inlier distance threshold
    :param d: the number of inliers required to accept the result
    :return: the best fit plane model and the corresponding inliers
    """
    best_model = None
    best_inliers = None
    for i in range(k):
        # Randomly select n points
        indices = np.random.choice(data.shape[0], n, replace=False)
        sample = data[indices, :]

        # Fit a plane to the sample points
        pca = PCA(n_components=3)
        pca.fit(sample)
        normal = pca.components_[2, :]
        point = np.mean(sample, axis=0)
        plane = np.append(normal, -np.dot(normal, point))

        # Compute the distance between each point and the plane
        distances = np.abs(np.dot(data, plane[:-1]) + plane[-1])
        inliers = np.where(distances < t)[0]

        # Check if we have enough inliers to accept the result
        if len(inliers) >= d:
            # Refit the plane to all inliers
            sample = data[inliers, :]
            pca = PCA(n_components=3)
            pca.fit(sample)
            normal = pca.components_[2, :]
            point = np.mean(sample, axis=0)
            plane = np.append(normal, -np.dot(normal, point))

            # Save the model if it is better than the current best
            if best_inliers is None or len(inliers) > len(best_inliers):
                best_model = plane
                best_inliers = inliers

    return best_model, best_inliers

if __name__ == '__main__':
    pass


