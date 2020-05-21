select COUNTRY.Continent,  floor (avg(CITY.Population)) from country
join 
city on CITY.CountryCode = COUNTRY.Code
group  by  COUNTRY.Continent;
