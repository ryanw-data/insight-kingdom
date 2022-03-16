CREATE TABLE IF NOT EXISTS uk_crime.crime_street_raw
(
    crime_id character varying(128) COLLATE pg_catalog."default",
    month character varying(12) COLLATE pg_catalog."default",
    reported_by character varying(128) COLLATE pg_catalog."default",
    falls_within character varying(128) COLLATE pg_catalog."default",
    longitude character varying(15) COLLATE pg_catalog."default",
    latitude character varying(15) COLLATE pg_catalog."default",
    location character varying(128) COLLATE pg_catalog."default",
    lsoa_code character varying(9) COLLATE pg_catalog."default",
    lsoa_name character varying(100) COLLATE pg_catalog."default",
    crime_type character varying(128) COLLATE pg_catalog."default",
    last_outcome_category character varying(128) COLLATE pg_catalog."default" DEFAULT NULL::character varying,
    context character varying(128) COLLATE pg_catalog."default" DEFAULT NULL::character varying
);

CREATE TABLE IF NOT EXISTS uk_crime.crime_street_src
(
    crime_id character varying(64) COLLATE pg_catalog."default",
    crime_month date,
    reporting_police_force character varying(50) COLLATE pg_catalog."default",
    location_police_force character varying(50) COLLATE pg_catalog."default",
    crime_longitude numeric(8,6),
    crime_latitude numeric(8,6),
    crime_location character varying(100) COLLATE pg_catalog."default",
    lsoa_code character varying(10) COLLATE pg_catalog."default",
    lsoa_name character varying(50) COLLATE pg_catalog."default",
    crime_type character varying(50) COLLATE pg_catalog."default",
    crime_last_outcome_category character varying(100) COLLATE pg_catalog."default",
    crime_context character varying(100) COLLATE pg_catalog."default"
);