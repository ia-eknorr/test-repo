SELECT COUNT(filter) FROM backwash WHERE filter = :filter AND backwash.start_time IS NOT NULL AND backwash.end_time IS NULL