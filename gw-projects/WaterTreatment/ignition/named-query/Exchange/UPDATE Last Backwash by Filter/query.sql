UPDATE backwash 
SET end_time = :end_time, duration = TIMEDIFF(:end_time,backwash.start_time)/60.0, flow_after = :flow_after, level_after = :level_after, loh_after = :loh_after, turb_after = :turb_after
WHERE filter = :filter AND end_time IS NULL