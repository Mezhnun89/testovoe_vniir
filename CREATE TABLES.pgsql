CREATE TABLE tnved1
(
    razdel integer PRIMARY KEY,
    naim varchar(128) NOT NULL,
    prim varchar(128),
    data date,
    data1 date
);

CREATE TABLE tnved2
(
   razdel integer PRIMARY KEY,
   gruppa integer NOT NULL,
   naim varchar(128) NOT NULL,
   prim varchar(128),
   data date,
   data1 date
);

CREATE TABLE tnved3
(
    gruppa integer PRIMARY KEY,
    tov_poz integer NOT NULL,
    naim varchar(128) NOT NULL,
    data date,
    data1 date
);

CREATE TABLE tnved4
(
    gruppa integer PRIMARY KEY,
    tov_poz integer NOT NULL,
    sub_poz integer NOT NULL,
    kr_naim varchar(128) NOT NULL,
    data date,
    data1 date
);