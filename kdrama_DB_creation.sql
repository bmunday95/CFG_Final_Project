CREATE database K_Drama;

USE k_drama;

CREATE TABLE Completed_shows  (
	show_title VARCHAR(50) NOT NULL,
    show_release VARCHAR(15) NOT NULL,
    show_overview TEXT NOT NULL
    );

CREATE TABLE Watch_list (
	show_title VARCHAR(50) NOT NULL,
    show_release VARCHAR(15) NOT NULL,
    show_overview TEXT NOT NULL
);