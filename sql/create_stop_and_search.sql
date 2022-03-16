-- Creates the raw table which is populated by EL python script
CREATE TABLE IF NOT EXISTS uk_crime.stop_and_search_raw
(
	    type varchar(128),
	    event_date varchar(32),
	    part_of_policing_operation_flag varchar(1),
	    policing_operation varchar(128),
	    latitude numeric(8,6),	
	    longitude numeric(8,6),
	    gender varchar(12),
	    age_range varchar(12),
	 	self_defined_ethnicity varchar(256),
	 	office_defined_ethnicity varchar(256),
	    legislation varchar(128),
	    object_of_search varchar(128),
	    outcome varchar(128),
	    outcome_linked_to_object_of_search varchar(12),
	    removal_of_more_than_clothing varchar(12)
);

-- Creates the source table which ingests data from the raw table post-processing
CREATE TABLE IF NOT EXISTS uk_crime.stop_and_search_src 
(
		search_type varchar(26),
		search_date timestamp,
		part_of_policing_operation_flag boolean,
		policing_operation varchar(264),
		search_latitude numeric(8,6),
		search_longitude numeric(8,6),
		person_gender varchar(8),
		person_age_range varchar(10),
		person_defined_ethnicity varchar(100),
		officer_defined_ethnicity varchar(10),
		legislation varchar(100),
		object_of_search varchar(100),
		search_oucome varchar(100),
		outcome_linked_to_object_of_search_flag boolean,
		removal_of_more_than_clothing_flag boolean
);