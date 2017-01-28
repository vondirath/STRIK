-- remove for final --
DROP DATABASE IF EXISTS strik_database;
-- --
CREATE DATABASE strik_database;

\c strik_database

-- Create Table todo: add all options for posts --
CREATE TABLE posts 
( 
id serial PRIMARY KEY,
title varchar(100) NOT NULL,
)
