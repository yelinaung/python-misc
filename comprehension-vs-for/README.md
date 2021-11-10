Trying out between for-loop and list comprehension with different Python versions.

Install [pyperf](https://github.com/psf/pyperf) to measure and analyze the benchmark
```bash
pip install pyperf

# run the benchmark
python3 -m pyperf timeit -s 'from filter_list import for_loop' 'for_loop()' -o for_loop_bench.json

# analyze
python3 -m pyperf stats for_loop_bench.json
```

### Python 3.10.0

#### For Loop

```
Total duration: 15.7 sec
Start date: 2021-11-10 21:19:15
End date: 2021-11-10 21:19:32
Raw value minimum: 165 ms
Raw value maximum: 211 ms

Number of calibration run: 1
Number of run with values: 20
Total number of run: 21

Number of warmup per run: 1
Number of value per run: 3
Loop iterations per value: 4
Total number of values: 60

Minimum:         41.2 ms
Median +- MAD:   42.5 ms +- 0.7 ms
Mean +- std dev: 44.0 ms +- 3.1 ms
Maximum:         52.8 ms

  0th percentile: 41.2 ms (-6% of the mean) -- minimum
  5th percentile: 41.6 ms (-6% of the mean)
 25th percentile: 42.1 ms (-4% of the mean) -- Q1
 50th percentile: 42.5 ms (-3% of the mean) -- median
 75th percentile: 45.5 ms (+3% of the mean) -- Q3
 95th percentile: 51.3 ms (+17% of the mean)
100th percentile: 52.8 ms (+20% of the mean) -- maximum

Number of outlier (out of 37.1 ms..50.5 ms): 5
```

#### List Comprehension Loop

```
Total duration: 10.7 sec
Start date: 2021-11-10 21:20:20
End date: 2021-11-10 21:20:33
Raw value minimum: 106 ms
Raw value maximum: 148 ms

Number of calibration run: 1
Number of run with values: 20
Total number of run: 21

Number of warmup per run: 1
Number of value per run: 3
Loop iterations per value: 4
Total number of values: 60

Minimum:         26.6 ms
Median +- MAD:   28.6 ms +- 1.2 ms
Mean +- std dev: 29.0 ms +- 2.4 ms
Maximum:         37.1 ms

  0th percentile: 26.6 ms (-8% of the mean) -- minimum
  5th percentile: 27.0 ms (-7% of the mean)
 25th percentile: 27.3 ms (-6% of the mean) -- Q1
 50th percentile: 28.6 ms (-1% of the mean) -- median
 75th percentile: 29.7 ms (+2% of the mean) -- Q3
 95th percentile: 34.5 ms (+19% of the mean)
100th percentile: 37.1 ms (+28% of the mean) -- maximum

Number of outlier (out of 23.8 ms..33.2 ms): 5
```
