# Mens-Sprint_Data-Analysis

## METADATA

- Ana Castanheira
	analuciacastanhei@gmail.com

- Eduardo Carvalho
	eduardo_martins_carvalho@hotmail.com

- Introduction to Programming.
	-- Lecturer: Dr. José Campos.

- FCUL - Faculdade de Ciências da Universidade de Lisboa.

DELIVERY STRUCTURE
---------------
- README.md
- main.py
- csv_files
    - athletes.csv
	- sport_events.csv
- images [if created]

INTRODUCTION
---------------

> This assignment was made by Eduardo Carvalho and Ana Castanheira for the Introduction to 
> Programming class - lectured by Dr. José Campos.
> Within, are 2 csv structured files representing Cycling Olympic Players and selected data of 
> their performance at the Men's Sprint events in one or many Olympic Editions.
> The PDF file contains a data analysis of the athlete statistics per edition.

REQUIREMENTS
---------------
None. As it's only a database as of now, a plain text editor or excel-type software will work.

> We recommend opening this readme.md file in a markdown editor/interface for proper displaying.

Recommended:
```sh 
Excel 2016 or later
Notepad++
```

Men's Sprint Rules
---------------
> *As defined by Union Cycliste Internationale (UCI) rules, the first round of competition used 
> to qualify for the sprint competition is the flying 200 m time trial. In this round each rider 
> completes two to three warm up laps and then completes the final 200 m, which is usually just 
> under a lap. The number of riders that qualify for the sprint rounds depends on the competition;
> in World Cup competitions, 16 riders will advance and in a world championship, 24 riders will advance. 
> The top riders are seeded in the following rounds, meaning the fastest qualifier will face the slowest 
> qualifier and so on. Knock-out rounds then proceed, initially on a one race basis and then on a best-of 
> three-race format from the quarter-final stage. Riders defeated in the earlier rounds may get a chance to 
> continue in the competition through the repechage races.*

### Olympic's Specific Rules
> *Matches are contested between two riders who cover three laps of the track. The first rider over the line 
> wins the race, best of three races wins the match. The top 16 riders qualify for the knockout stages with 
> a flying 200-metre time trial.*

ATHLETES.CSV STRUCTURE
---------------

|athete_id|name                         |date_of_birth|nation             |sex |
|---------|-----------------------------|-------------|-------------------|----|
|1        |Jason Kenny                  |23/03/1988   |Great Britain      |male|
|2        |Callum Skinner               |20/08/1992   |Great Britain      |male|
|3        |Matthew Glaetzer             |24/08/1992   |Australia          |male|
|4        |Denis Dmitriev               |23/03/1986   |Russia             |male|
|5        |Grégory Baugé                |31/01/1985   |France             |male|

Table Caption

- **athlete_id**: Identifier number of each individual athlete_id
	- **Type: Int**
    	- Positive values(1 till infinite)
- **name**: Athele's name
	- **Type - String**
- **date_of_birth**: day/month/year of birth of each athlete
	- **Type - String**
- **nation**: Country that each Athlete represented while sporting. May not reflect country of birth.
	- **Type - String**
- **sex**: Gender of each athlete
	- **Type - String** 
		- Two possible "values": **female** or **male**


ATHLETES.CSV STRUCTURE
---------------

|year|athete_id|race_id|round                    |heat|time   |avg_km_h|rank|result|record|host_country  |venue                   |
|----|---------|-------|-------------------------|----|-------|--------|----|------|------|--------------|------------------------|
|2016|1        |101    |qualifying               |1   |9,551  |75,384  |1   |Q     |OR    |Brazil        |Rio Olympic Velodrome   |
|2016|2        |103    |qualifying               |1   |9,703  |74,203  |2   |Q     |N     |Brazil        |Rio Olympic Velodrome   |
|2016|3        |72     |qualifying               |1   |9,704  |74,196  |3   |Q     |N     |Brazil        |Rio Olympic Velodrome   |
|2016|4        |143    |qualifying               |1   |9,774  |73,664  |4   |Q     |N     |Brazil        |Rio Olympic Velodrome   |
|2016|5        |94     |qualifying               |1   |9,807  |73,416  |5   |Q     |N     |Brazil        |Rio Olympic Velodrome   |

**Table Caption**

 - **year**: *Date of when the event happened* 
	 - **Type - Int** 
	 	 - Positive number with four digits;
		 - (Years considered: 2016, 2012, 2008, 2004, 2000, 1896)
 - **athlete_id**: *Identifier number of each individual athlete_id*
	 - **Type - Int**
	    - Positive number with possible values of 1 till infinite;
 - **race_id**: *Individual Identifier of an Athlete in a race (i.e. Shirt Numbering) - NA (Not Appliable) if no Personal Numbering was used*. 
	- **Type -  Int**
	    - Positive number with possible values of 1 till infinite;
- **round**: *Round of the event competition - i.e. Qualifyings - 1/16, 1/8, Quarter Finals... etc.*
	- **Type - String**
- **heat**: *Which race each round was, each round may have several heats.* ; **Type - Int**
	    - Positive number with possible values of 1 till infinite;
- **time**: *How long, in seconds, each competitor took to finish the race (less is better)*
	- **Type - Float**
	    - Positive values with 3 decimals; this variable can take no value due to athlete quiting (-)
- **avg_km_h**: *Average speed per Kilometer of each competitor (more is better)* 
	- **Type - Float**
    	- This variable can take no value due to athlete quiting (-)
- **rank**: *Place each competitor finished each race.* 
	- **Type - Int**
    	- Positive number with possible value in range 1 to infinite
- **result**: *What happened to each competitor after each round*
	- **Type - String**
    	- **Q** - *Qualified to next round*
    	- **N** - *Didn't Qualify to next round*
    	- **R** - *Repechaged - Didn't Automatically qualified but stille given a chance to win a spot in the following round*
    	- **TBD** - *To Be Decided, in case it's a best of 3/5 and more races between the same competitors are yet to take place.*
    	- **B** - *Qualified to the Bronze medal race.*
    	- **C** - *Qualified to a placement in the final table race excluding 1-4th. I.e. race to 9-12th placement, 5th-8th placement.*
    	- **Number** *(i.e. 1,2,3,4,5,6...) - Final athlete placement in the competition.*
    	- **DNS** - *Did Not Start, disqualified due to not starting the race*
- **record** - *If a record happened in each race, OR - Olympic Record, WR - World Record.*
	- **Type - String**
- **host_country**: *Where the competition took place, in this case, Olympic Games organizer.*
	- **Type - String**
- **venue**: *In what velodrome each race took place*.
	- **Type - String**

Data Limitations
---------------
> While data collecting we experienced some trouble finding some needed data.
Except for 2016, there wasn´t any personal identifier used (i.e. shirt numbering) 
which in 16 is equivalente to **race_id**. Also, some of the time difference 
(**time**) of the athletes that did not make the first place is missing as well. 
So we just replaced the data we did not have by "**NA**" - Not Applicable.

> Curiously, we added the information of the winner of the very first man´s cycling sprint event 
at the 1896 Olympic Games that took place in Greece, for future comparison for assignment 2.2, as baseline data.

Resources Consulted
---------------
https://www.olympedia.org/editions/59

**2016:**
https://en.wikipedia.org/wiki/Cycling_at_the_2016_Summer_Olympics_%E2%80%93_Men%27s_sprint
https://www.olympic.org/rio-2016/cycling-road
https://www.cyclingweekly.com/news/racing/olympics/rio-2016-olympic-games-cycling-medal-table-272364
www.assetrio2016.azureedge.net/_odf-documents
https://web.archive.org/web/20160806081759/https://www.rio2016.com/en/cycling-track-standings-ct-mens-sprint

**2012:**
https://en.wikipedia.org/wiki/Cycling_at_the_2012_Summer_Olympics_%E2%80%93_Men%27s_sprint

**2008:**
https://en.wikipedia.org/wiki/Cycling_at_the_2008_Summer_Olympics_%E2%80%93_Men%27s_sprint

**2004:**
https://en.wikipedia.org/wiki/Cycling_at_the_2004_Summer_Olympics_%E2%80%93_Men%27s_sprint

**1896:**
https://www.olympedia.org/results/153001

MANTAINERS
---------------

This program was coded and is maintained by:
> Ana Castanheira | analuciacastanhei@gmail.com | Master's in Biostatistics | FCUL
> Eduardo Carvalho | eduardo_martins_carvalho@hotmail.com | Master's in Informatics | FCUL
