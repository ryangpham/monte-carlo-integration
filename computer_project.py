import numpy as np

# 1
def monte_carlo_integration(func, a, b, samples=10**6):
    x = np.random.uniform(a, b, samples)
    y = func(x)
    return (b - a) * np.mean(y)

def f1(x):
    return np.sin(1/x)

result_a = monte_carlo_integration(f1, 0, 1)
print(f"Monte Carlo estimation (a): {result_a}")

def f2(x):
    return np.exp(-x**2)

result_b = monte_carlo_integration(f2, -2, 2)
print(f"Monte Carlo estimation (b): {result_b}")

# 2
def virus_simulation(num_computers = 20, spread_prob = 0.1, removal_rate = 5, trials = 1000):
    total_days = []
    all_infected_prob = []
    total_infected = []

    for _ in range(trials):
        infected = set([np.random.randint(0, num_computers)])
        check_infected = set(infected)
        days = 0

        while infected:
            days += 1

            new_infected = set()
            for computer in infected:
                for other_computer in range(num_computers):
                    if other_computer not in infected and np.random.rand() < spread_prob:
                        new_infected.add(other_computer)
            infected.update(new_infected)
            check_infected.update(new_infected)

            removal_count = min(removal_rate, len(infected))
            removed = set(np.random.choice(list(infected), removal_count, replace=False))
            infected -= removed

        total_days.append(days)
        all_infected_prob.append(len(check_infected) == num_computers)
        total_infected.append(len(check_infected))

    expected_days = np.mean(total_days)
    all_infected_prob = np.mean(all_infected_prob)
    expected_infected = np.mean(total_infected)

    return expected_days, all_infected_prob, expected_infected

expected_days, all_infected_prob, expected_infected = virus_simulation()
print(f"(a) Expected time it takes to remove the virus from the whole network: {expected_days} days")
print(f"(b) Probability that each computer gets infected at least once: {all_infected_prob}")
print(f"(c) Expected number of computers that get infected: {expected_infected}")