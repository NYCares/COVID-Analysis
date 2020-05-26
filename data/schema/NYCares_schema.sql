CREATE TABLE "CovidIncident" (
    "county" varchar   NOT NULL,
    "state" char(2)   NOT NULL,
    "date" date   NOT NULL,
    "population" bigint   NOT NULL,
    "deaths" int   NOT NULL,
    "pctOfPopulation" decimal   NOT NULL,
    "pctOfDeaths" decimal   NOT NULL,
    "pctOfCases" decimal   NOT NULL,
    "created" date   NOT NULL,
    "createdBy" varchar   NOT NULL,
    CONSTRAINT "pk_CovidIncident" PRIMARY KEY (
        "county"
     )
);

CREATE TABLE "MedianIncome" (
    "county" varchar   NOT NULL,
    "value" int   NOT NULL,
    "state" char(2)   NOT NULL,
    "created" date   NOT NULL,
    "createdBy" varchar   NOT NULL,
    CONSTRAINT "pk_MedianIncome" PRIMARY KEY (
        "county"
     )
);

CREATE TABLE "DJI" (
    "date" date   NOT NULL,
    "open" int   NOT NULL,
    "high" int   NOT NULL,
    "low" int   NOT NULL,
    "close" int   NOT NULL,
    "adjClose" int   NOT NULL,
    "volume" bigint   NOT NULL,
    "created" date   NOT NULL,
    "createdBy" varchar   NOT NULL
);

CREATE TABLE "LunchProgram" (
    "region" varchar   NOT NULL,
    "baseYear" int   NOT NULL,
    "baseYearNumber" int   NOT NULL,
    "baseYearPct" decimal   NOT NULL,
    "currentYear" int   NOT NULL,
    "currentYearNumber" int   NOT NULL,
    "currentYearPct" decimal   NOT NULL,
    "number" bigint   NOT NULL,
    "pct" decimal   NOT NULL,
    "created" date   NOT NULL,
    "createdBy" varchar   NOT NULL,
    CONSTRAINT "pk_LunchProgram" PRIMARY KEY (
        "region"
     )
);

CREATE TABLE "UnemploymentBenefit" (
    "county" varchar   NOT NULL,
    "region" varchar   NOT NULL,
    "beneficiaryMonth" int   NOT NULL,
    "beneficiaryYear" int   NOT NULL,
    "totReceivingAidInBenficiaryMonth" bigint   NOT NULL,
    "ytdTotReceivingAid" bigint   NOT NULL,
    "totPaidInBeneficiaryMonth" bigint   NOT NULL,
    "ytdBenefitsPaid" bigint   NOT NULL,
    "created" date   NOT NULL,
    "createdBy" varchar   NOT NULL,
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

