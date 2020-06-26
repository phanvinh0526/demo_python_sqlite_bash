-- ** since SQLite doesnt support variable, need a workaround solution, so I keep static table names atm **

-- SET @tbl_src_name='ticket_activities' 
-- SET @tbl_dest_name='ticket_status'

DROP TABLE IF EXISTS ticket_status;

CREATE TABLE ticket_status
AS
SELECT
  ticket_id
  ,ABS(RANDOM() % 2000) as time_spent_open
  ,ABS(RANDOM() % 2000) as time_spent_waiting_on_customer
  ,ABS(RANDOM() % 2000) as time_spent_waiting_for_response
  ,ABS(RANDOM() % 2000) as time_till_resolution
  ,ABS(RANDOM() % 2000) as time_to_first_response
FROM
  ticket_activities;