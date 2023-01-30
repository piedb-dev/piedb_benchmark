# piedb_benchmark
Use tests with realistic datasets/queries to quantitatively benchmark PIEDB.
This repository contains the code of the PIEDB benchmark.

It includes:
- [TPS](./src/tps):  
- [QPS](./src/qps):  
- [RT](./src/rt):  

## Workload Generator


## Performance Tests

### Stability Tests

multi-thread / multi-process mode (6 by default)

1. 24-hour write stress test
2. 24-hour query stress test, including random time window, random column tests

### Performance

1. write QPS: write 10 million+ data into database, when varying # of threads (1,2,3,8,16,32)
2. read QPS: query 1-10 million+ data when varying # of threads
3. mixed QPS: read while writing

### Compression Ratio

1. compare ratio of raw data to DB size, when varying compression algorithms



## Functional Tests

### DDL Tests

1. create / remove database
2. create / drop table 
3. table index
4. create / drop views
5. add / remove columns in tables

### DML Tests

1. insert
2. update
3. delete

### DQL Tests

1. select from where
2. table join
3. limit
4. groupby

### Streaming Tests

1. streaming clause
2. time window: minute, hour, day
3. math functions: count, sum, max, min, avg, etc
