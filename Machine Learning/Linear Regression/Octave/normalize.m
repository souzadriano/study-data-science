function [X_norm, mu, sigma] = normalize(X)

X_norm = X;
mu = zeros(1, size(X, 2));
sigma = zeros(1, size(X, 2));

num_iters = size(X, 2);

for iter = 1:num_iters

  mu_i = mean(X(:, iter));
  sigma_i = std(X(:, iter));
  
  X_norm(:, iter) = (X(:, iter) - mu_i) / sigma_i;
  mu(:, iter) = mu_i;
  sigma(:, iter) = sigma_i;

end

end
