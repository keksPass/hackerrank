select sum(city.population) from country
join city on country.code = city.CountryCode
where continent = 'Asia';
