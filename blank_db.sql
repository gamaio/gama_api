-- Schema Version 1

CREATE TABLE api_owners (
	id serial PRIMARY KEY,
	name varchar (512) NOT NULL,
	email varchar (256) NOT NULL,
	user_id int NOT NULL
);

CREATE TABLE api_apps (
	id serial PRIMARY KEY,
	owner_id int NOT NULL,
	apikey varchar (256) NOT NULL,
	name varchar (512) NOT NULL,
	description varchar (2048),
	website varchar (3000),
	callback_uri varchar (3000),
	settings text
);

CREATE TABLE api_heartbeat (
	id serial PRIMARY KEY,
	api_id int NOT NULL,
	time_sent bigint NOT NULL,
	time_rcvd bigint NOT NULL,
	latency numeric (6, 2) NOT NULL,
	data text
);