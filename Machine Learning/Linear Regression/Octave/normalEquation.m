function [theta] = normalEquation(X, y)

theta = ((X' * X) ^ -1) * X' * y;

end
