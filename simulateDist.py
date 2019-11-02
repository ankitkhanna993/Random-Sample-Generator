"""
Assignment 4 CSE-5301 Fall 2019
@author Ankit Khanna
UTA ID: 1001553616
"""

import math
import random
import statistics
import sys


# Seeding the random number generator with value 25
random.seed(25)

num = int(sys.argv[1])
distribution = sys.argv[2].lower()
param = sys.argv[3:len(sys.argv)]


def bernoulli(number, v):
    sample = []
    if len(v) != 1 or len(v) > 1:
        print("Insufficient/Incorrect arguments passed")
        sys.exit()
    p = float(v[0])
    if p > 1.0 or p < 0.0:
        print('Error! Probability of Success should be btw 0.0 and 1.0')
        sys.exit()
    else:
        for i in range(number):
            if random.random() >= p:
                sample.append(0)
            else:
                sample.append(1)
    return sample


def binomial(number, v):
    sample = []
    if len(v) != 2 or len(v) > 2:
        print("Insufficient/Incorrect arguments passed")
        sys.exit()
    n = int(v[0])
    p = float(v[1])
    if p > 1.0 or p < 0.0:
        print('Error! Probability of Success should be btw 0.0 and 1.0')
        sys.exit()
    else:
        for i in range(number):
            count = 0
            for j in range(n):
                if random.random() < p:
                    count += 1
            sample.append(count)
    return sample


def geometric(number, v):
    sample = []
    if len(v) != 1 or len(v) > 1:
        print("Insufficient/Incorrect arguments passed")
        sys.exit()
    p = float(v[0])
    if p > 1.0 or p < 0.0:
        print('Error! Probability of Success should be btw 0.0 and 1.0')
        sys.exit()
    else:
        for i in range(number):
            count = 1
            while random.random() > p:
                count += 1
            sample.append(count)
    return sample


def negbinomial(number, v):
    sample = []
    if len(v) != 2 or len(v) > 2:
        print("Insufficient/Incorrect arguments passed")
        sys.exit()
    k = int(v[0])
    p = v[1:len(v)]
    for i in range(number):
        sample.append(sum(geometric(k, p)))
    return sample


def poisson(number, v):
    sample = []
    if len(v) != 1 or len(v) > 1:
        print("Insufficient/Incorrect arguments passed")
        sys.exit()
    val_lambda = float(v[0])
    for i in range(number):
        count = 0
        r = random.random()
        exp_lambda = math.exp(-val_lambda)
        while r >= exp_lambda:
            count += 1
            r *= random.random()
        sample.append(count)
    return sample


def arbdiscrete(number, v):
    sample = []
    p = []
    func = []
    for i in v:
        p.append(float(i))
    # Formulate cdf
    for i in range(len(p)):
        func.append(sum(p[0:i + 1]))
    if func[-1] != 1:
        print("Probability of p elements should equal 1")
        sys.exit()
    else:
        for i in range(number):
            count = 0
            r = random.random()
            while func[count] <= r:
                count += 1
            sample.append(count)
    return sample


def uniform(number, v):
    sample = []
    if len(v) != 2 or len(v) > 2:
        print("Insufficient/Incorrect parameters passed")
        sys.exit()
    a = float(v[0])
    b = float(v[1])
    # Swap the bounds if a > b
    if a > b:
        c = a
        a = b
        b = c
    for i in range(number):
        sample.append(a+((b-a)*random.random()))
    return sample


def exponential(number, v):
    sample = []
    if len(v) != 1 or len(v) > 1:
        print("Insufficient/Incorrect parameters passed")
        sys.exit()
    val_lambda = float(v[0])
    for i in range(number):
        sample.append((-(1/val_lambda))*math.log(1-random.random()))
    return sample


def gamma(number, v):
    sample = []
    if len(v) != 2 or len(v) > 2:
        print("Insufficient/Incorrect parameters passed")
        sys.exit()
    val_alpha = int(v[0])
    val_lambda = v[1:len(v)]
    for i in range(number):
        sample.append(sum(exponential(val_alpha, val_lambda)))
    return sample


def normal(number, v):
    sample = []
    if len(v) != 2 or len(v) > 2:
        print("Insufficient/Incorrect arguments passed")
        sys.exit()
    mu = float(v[0])
    sigma = float(v[1])
    u = int(math.ceil(float(number)/2))
    for i in range(u):
        u1 = random.random()
        u2 = random.random()
        z1 = math.sqrt((-2)*math.log(u1))*math.cos(2*math.pi*u2)
        z2 = math.sqrt((-2)*math.log(u1))*math.sin(2*math.pi*u2)
        sample.append(z1*sigma + mu)
        sample.append(z2*sigma + mu)
    if number % 2 == 0:
        return sample
    else:
        return sample[0:len(sample)-1]


if distribution == "bernoulli":
    outcome = bernoulli(num, param)

elif distribution == "binomial":
    outcome = binomial(num, param)

elif distribution == "geometric":
    outcome = geometric(num, param)

elif distribution == "negbinomial":
    outcome = negbinomial(num, param)

elif distribution == "poisson":
    outcome = poisson(num, param)

elif distribution == "arbdiscrete":
    outcome = arbdiscrete(num, param)

elif distribution == "uniform":
    outcome = uniform(num, param)

elif distribution == "exponential":
    outcome = exponential(num, param)

elif distribution == "gamma":
    outcome = gamma(num, param)

elif distribution == "normal":
    outcome = normal(num, param)

else:
    sys.exit("Invalid Distribution Name: " + distribution)

print("Randomly Generated Samples are: ", str(outcome))

sample_mean = sum(outcome)/num
print("Sample Mean: ", sample_mean)

sample_variance = statistics.variance(outcome, sample_mean)
print("Sample Variance: ", sample_variance)

pop_mean = statistics.mean(outcome)
print("Population Mean: ", pop_mean)

pop_variance = statistics.pvariance(outcome, pop_mean)
print("Population Variance: ", pop_variance)
