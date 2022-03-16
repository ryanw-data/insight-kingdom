insert into uk_crime.stop_and_search_src
select 
type,
cast(event_date as timestamp),
cast(nullif(part_of_policing_operation_flag,'') as boolean),
policing_operation,
cast(nullif(latitude,'') as numeric(8,6)),
cast(nullif(longitude,'') as numeric(8,6)),
gender,
age_range,
self_defined_ethnicity,
officer_defined_ethnicity,
legislation,
object_of_search,
outcome,
cast(nullif(outcome_linked_to_object_of_search,'') as boolean),
cast(nullif(removal_of_more_than_clothing,'') as boolean)
from uk_crime.stop_and_search_raw
;