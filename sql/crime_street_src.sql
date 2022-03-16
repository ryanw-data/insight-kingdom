insert into uk_crime.crime_street_src
select 
crime_id,
cast(concat(month,'-01') as date), --crime_month
nullif(reported_by,''),
nullif(falls_within,''),
cast(nullif(longitude,'') as numeric),
cast(nullif(latitude,'') as numeric),
nullif(location,''),
nullif(lsoa_code,''),
nullif(lsoa_name,''),
nullif(crime_type,''),
nullif(last_outcome_category,''),
nullif(context,'')
from uk_crime.crime_street_raw 
;