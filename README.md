# piedb_benchmark
Use tests with realistic datasets/queries to quantitatively benchmark PIEDB.

## Workload Generator


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
