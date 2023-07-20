--check bin log status, should be 'ON' for bin log replication
SELECT variable_value as bin_log_status
FROM performance_schema.global_variables
WHERE variable_name='log_bin';

-- check the format of bin log replication; should be to ROW 
SELECT variable_value as bin_log_format
FROM performance_schema.global_variables
WHERE variable_name='binlog_format';

--grant user permissioins to change binlog_format
GRANT SYSTEM_VARIABLES_ADMIN ON *.* TO admin;

-- change the binlog for to ROW
SET GLOBAL binlog_format = 'ROW';
