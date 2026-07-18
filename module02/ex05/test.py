from TinyStatistician import TinyStatistician

tsat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(f'mean: {tsat.mean(a)}')
print(f'medain: {tsat.median(a)}')
print(f'quartile: {tsat.quartile(a)}')
print(f'variance: {tsat.var(a)}')
print(f'std: {tsat.std(a)}')
