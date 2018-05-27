clear ; close all; clc
data = rand(1000, 3) * 10000;
X = data(:, 1:2);
y = data(:, 3);
m = length(y);
X = [ones(m, 1) X];
theta = normalEquation(X, y)
resultNormEquation = theta' * [1;11000;5000]
[X mu sigma] = normalize(X(:, 2:3));
theta = zeros(3, 1);
X = [ones(m, 1) X];
theta = gradientDescent(X, y, theta, 1, 50)
resultGradientDescent = theta' * [1; (11000 - mu(1)) / sigma(1); (5000 - mu(2)) / sigma(2)]