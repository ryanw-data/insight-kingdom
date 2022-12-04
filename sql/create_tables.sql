create database development;

\connect development;

CREATE SCHEMA IF NOT EXISTS ons_raw;

CREATE TABLE IF NOT EXISTS ons_raw._datasets_metadata ( 
dataset_id varchar, 
dataset_collection_id varchar, 
dataset_title varchar, 
dataset_description varchar, 
dataset_state varchar, 
dataset_release_date varchar, 
dataset_next_release varchar, 
dataset_release_frequency varchar, 
dataset_national_stastic varchar, 
dataset_type varchar, 
dataset_editions_link varchar, 
dataset_latest_version_link varchar, 
dataset_latest_version_id varchar, 
dataset_download_url varchar, 
dataset_self_link varchar, 
dataset_taxonomy_link varchar, 
dataset_quality_methodology_information_link varchar, 
dataset_publications varchar, 
dataset_unit_of_measure varchar, 
dataset_licence varchar, 
dataset_usage_notes varchar);
