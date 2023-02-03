
select_table_pointget = [
    'select * from t where id = {};',
    'select * from t where uid = {};',
    'select * from t where v1 = {};',
]
select_table_scan = [
    'select * from t where id < {} and id > {};',
    'select * from t where uid < {} and uid > {};',
    'select * from t where v1 < {} and v1 > {};',
]

select_source_pointget = [
    'select * from s1 where id = {};',
    'select * from s1 where uid = {};',
    'select * from s1 where v1 = {};',
]

select_source_scan = [
    'select * from s1 where id < {} and id > {};',
    'select * from s1 where uid < {} and uid > {};',
    'select * from s1 where v1 < {} and v1 > {};',
]




