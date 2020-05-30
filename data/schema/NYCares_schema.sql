CREATE TABLE "CovidIncident"
(
    "county" varchar NOT NULL,
    "state" char(2) NOT NULL,
    "date" date NOT NULL,
    "population" bigint NOT NULL,
    "deaths" int NOT NULL,
    "pctOfPopulation" decimal NOT NULL,
    "pctOfDeaths" decimal NOT NULL,
    "pctOfCases" decimal NOT NULL,
    "created" date NOT NULL,
    "createdBy" varchar NOT NULL,
    CONSTRAINT "pk_CovidIncident" PRIMARY KEY (
        "county"
     )
);

CREATE TABLE "DJI"
(
    "date" date NOT NULL,
    "open" int NOT NULL,
    "high" int NOT NULL,
    "low" int NOT NULL,
    "close" int NOT NULL,
    "adjClose" int NOT NULL,
    "volume" bigint NOT NULL,
    "created" date NOT NULL,
    "createdBy" varchar NOT NULL
);

CREATE TABLE "LunchProgram"
(
    "region" varchar NOT NULL,
    "baseYear" int NOT NULL,
    "baseYearNumber" int NOT NULL,
    "baseYearPct" decimal NOT NULL,
    "currentYear" int NOT NULL,
    "currentYearNumber" int NOT NULL,
    "currentYearPct" decimal NOT NULL,
    "number" bigint NOT NULL,
    "pct" decimal NOT NULL,
    "created" date NOT NULL,
    "createdBy" varchar NOT NULL,
    CONSTRAINT "pk_LunchProgram" PRIMARY KEY (
        "region"
     )
);

CREATE TABLE "UnemploymentBenefit"
(
    "county" varchar NOT NULL,
    "region" varchar NOT NULL,
    "beneficiaryMonth" int NOT NULL,
    "beneficiaryYear" int NOT NULL,
    "totReceivingAidInBenficiaryMonth" bigint NOT NULL,
    "ytdTotReceivingAid" bigint NOT NULL,
    "totPaidInBeneficiaryMonth" bigint NOT NULL,
    "ytdBenefitsPaid" bigint NOT NULL,
    "created" date NOT NULL,
    "createdBy" varchar NOT NULL,
    CONSTRAINT "pk_UnemploymentBenefit" PRIMARY KEY (
        "county"
     )
);

ALTER TABLE "CovidIncident" ADD CONSTRAINT "fk_CovidIncident_county" FOREIGN KEY("county")
REFERENCES "MedianIncome" ("county");

ALTER TABLE "MedianIncome" ADD CONSTRAINT "fk_MedianIncome_county" FOREIGN KEY("county")
REFERENCES "LunchProgram" ("region");

ALTER TABLE "LunchProgram" ADD CONSTRAINT "fk_LunchProgram_region" FOREIGN KEY("region")
REFERENCES "UnemploymentBenefit" ("county");

--DROP TABLE median_income_asian;
create table median_income_asian
(
    id varchar(250) NOT NULL,
    county varchar(250),
    asian bigint,
    TableReferenceId varchar(250),
    CensusNotes varchar(250)
);

--DROP TABLE median_income_pacific_islander;
create table median_income_pacific_islander
(
    id varchar(250) NOT NULL,
    county varchar(250),
    pacific_islander bigint,
    TableReferenceId varchar(250),
    CensusNotes varchar(250)
);

--DROP TABLE median_income_black;
create table median_income_black
(
    id varchar(250) NOT NULL,
    county varchar(250),
    black bigint,
    TableReferenceId varchar(250),
    CensusNotes varchar(250)
);

--DROP TABLE median_income_white;
create table median_income_white
(
    id varchar(250) NOT NULL,
    county varchar(250),
    white bigint,
    TableReferenceId varchar(250),
    CensusNotes varchar(250)
);

--DROP TABLE median_income_native_amer;
create table median_income_native_amer
(
    id varchar(250) NOT NULL,
    county varchar(250),
    native_american bigint,
    TableReferenceId varchar(250),
    CensusNotes varchar(250)
);


--DROP TABLE median_income_white_non_hisp;
create table median_income_white_non_hisp
(
    id varchar(250) NOT NULL,
    county varchar(250),
    white_non_hisp bigint,
    TableReferenceId varchar(250),
    CensusNotes varchar(250)
);

--DROP TABLE median_income_hisp_latino;
create table median_income_hisp_latino
(
    id varchar(250) NOT NULL,
    county varchar(250),
    hisp_latino bigint,
    TableReferenceId varchar(250),
    CensusNotes varchar(250)
);

--DROP TABLE median_income_mixed_race;
create table median_income_mixed_race
(
    id varchar(250) NOT NULL,
    county varchar(250),
    mixed_race bigint,
    TableReferenceId varchar(250),
    CensusNotes varchar(250)
);

--DROP TABLE median_income_other;
create table median_income_other
(
    id varchar(250) NOT NULL,
    county varchar(250),
    other bigint,
    TableReferenceId varchar(250),
    CensusNotes varchar(250)
);

--DROP TABLE median_income;
create table median_income
(
    id varchar(250) NOT NULL PRIMARY KEY,
    county varchar(250),
    asian bigint,
    black bigint,
    hispanic_latino bigint,
    mixed_race bigint,
    native_american bigint,
    other bigint,
    pacific_islander bigint,
    white bigint,
    white_non_hispanic bigint,
    TableReferenceId varchar(250),
    CensusNotes varchar(250)
);