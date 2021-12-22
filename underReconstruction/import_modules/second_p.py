import first_p as cs

permanent_notes = f"{cs.today}" """     last day confirmed        """ f"{cs.total_confirmed} \n "
others_countries_notes = f"{cs.today}  \n{cs.country}      |  population           |  {cs.population} \n               last day confirmed       {cs.total_confirmed} \n"

if cs.country == "Ukraine":

    file = open("Projects\Project_1\API_covid_statistics\src\statistics_Ukraine.txt", "a")
    file.write(permanent_notes)
    file.close()

elif cs.country == "Poland":

    file = open("Projects\Project_1\API_covid_statistics\src\statistics_Poland.txt", "w")
    file.write(permanent_notes)
    file.close()

else:

    file = open("Projects\Project_1\API_covid_statistics\src\statistics_others.txt", "a")
    file.write(others_countries_notes)
    file.close()
