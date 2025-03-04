import Optimierung
import cProfile
import pstats


with cProfile.Profile() as profile:
    test = Optimierung.optimieren([1, 0, 0, 0, 1, 0, 0, 0, 1, "x"], 2, 30, 0.2, 15)
    print(test[:3])
    print(test[3:6])
    print(test[6:9])
    print(test[9])

results = pstats.Stats(profile)
results.sort_stats(pstats.SortKey.TIME)
results.print_stats()
results.dump_stats("results.prof")
