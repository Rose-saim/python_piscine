import datetime
import time

# Convertir le timestamp en un objet datetime
timetmp = time.time()
timestamp = "{:,.4f}".format(timetmp)
date = datetime.datetime.utcfromtimestamp(timetmp)

# Formatage en notation scientifique
formatted_timestamp = f"{timetmp:.2e}"

# Formater la date
date_formattee = date.strftime("%b %d %Y")


print(f"Seconds since January 1, 1970: {timestamp} or {formatted_timestamp} in scientific notation\n")
# Afficher la date formattée
print(date_formattee)
