#!/bin/bash
#
# This is a simple scipt that helps to initialise confinout database
URL=https://confinoutapi.herokuapp.com

echo "Ready to initialize datas"
echo "by @$(hostname) on $(date)"

# 1- Initializing types of event
echo "Start initilizing types of event"

TYPES="Lectures Spectacles Théatres Sports Balades Salons Restaurants Bars Jardins"  
for TYPENAME in $TYPES
do 
    echo ""
    curl ${URL}/addtype/${TYPENAME}
done

echo "Types of event initialized"

# 2- Initializing events 
echo "Start initilizing events"

add_event(){
    echo "adding new event at $1"
    curl --data "place=$1&address=$2&price=$3&date=$4&description=$5&typeid=$6&$7" ${URL}/addevent
    echo ""
}

#1
PLACE="Comedie de Lille"
ADDRESS="204 Rue Solférino, Lille"
PRICE="0"
DATE="2020-06-29 20:00:00"
DESCRIPTION="Le théâtre la Comédie de Lille n'a qu'une envie : vous faire rire !"
TYPEID="4"
NEXT="number=0320535494"

add_event "${PLACE}" "${ADDRESS}" "${PRICE}" "${DATE}" "${DESCRIPTION}" "${TYPEID}" "${NEXT}"

#2
PLACE="BAEconf 2020 Challenges"
ADDRESS="60 Boulevard Vauban, Lille"
PRICE=0
DATE="2020-06-30 20:00:00"
DESCRIPTION=""
TYPEID=2
NEXT="link=sciencesconf.org"

add_event "${PLACE}" "${ADDRESS}" "${PRICE}" "${DATE}" "${DESCRIPTION}" "${TYPEID}" "${NEXT}"

#3
PLACE="Le Comptoir de Cana"
ADDRESS="38 Rue des Bouchers, Lille"
PRICE=19.99
DATE="2020-06-30 08:00:00"
DESCRIPTION="Un petit‑déjeuner pour créer des liens"
TYPEID=8
NEXT=""

add_event "${PLACE}" "${ADDRESS}" "${PRICE}" "${DATE}" "${DESCRIPTION}" "${TYPEID}" "${NEXT}"

#4
PLACE="Théâtre du Nord"
ADDRESS="4 Place Charles de Gaulle, 59800 Lille"
PRICE=9
DATE="2020-06-30 13:45:00"
DESCRIPTION="Autour de la Grand'Place"
TYPEID=4
NEXT=""

add_event "${PLACE}" "${ADDRESS}" "${PRICE}" "${DATE}" "${DESCRIPTION}" "${TYPEID}" "${NEXT}"

#5
PLACE="Le Monde d'Uranie"
ADDRESS="24 Avenue du Président John F. Kennedy, 59000 Lille"
PRICE=10
DATE="2020-06-30 14:00:00"
DESCRIPTION="Atelier AstroTarot en FEMININ SACRE"
TYPEID=2
NEXT="link=libr-aire.fr"

add_event "${PLACE}" "${ADDRESS}" "${PRICE}" "${DATE}" "${DESCRIPTION}" "${TYPEID}" "${NEXT}"

#6
PLACE="EuraTechnologies"
ADDRESS="165 Avenue de Bretagne, Lille"
PRICE=0
DATE="2020-06-30 10:30:00"
DESCRIPTION="Open Innovation Day"
TYPEID=7
NEXT=""

add_event "${PLACE}" "${ADDRESS}" "${PRICE}" "${DATE}" "${DESCRIPTION}" "${TYPEID}" "${NEXT}"


#6
PLACE="Musée d'histoire naturelle de Lille"
ADDRESS="19 Rue de Bruxelles, Lille"
PRICE=0
DATE="2020-07-01 14:30:00"
DESCRIPTION="Atelier de dessin naturaliste (inratable !) / pour enfants"
TYPEID=2
NEXT=""

add_event "${PLACE}" "${ADDRESS}" "${PRICE}" "${DATE}" "${DESCRIPTION}" "${TYPEID}" "${NEXT}"

#7
PLACE="Cabinet paramédical"
ADDRESS="142 Rue de Lannoy, Villeneuve-d'Ascq"
PRICE=30
DATE="2020-07-01 17:00:00"
DESCRIPTION="Bilan coaching diététique digitopuncture 1ère séance"
TYPEID=7
NEXT=""

add_event "${PLACE}" "${ADDRESS}" "${PRICE}" "${DATE}" "${DESCRIPTION}" "${TYPEID}" "${NEXT}"

#8
PLACE="Centre Ekilibre"
ADDRESS="2 Rue Anne Josèph du Bourg, Villeneuve-d'Ascq"
PRICE=9
DATE="2020-06-29 16:00:00"
DESCRIPTION="Séance collective Mouvement Eveil Corporel"
TYPEID=5
NEXT=""

add_event "${PLACE}" "${ADDRESS}" "${PRICE}" "${DATE}" "${DESCRIPTION}" "${TYPEID}" "${NEXT}"

#9
PLACE="Atelier 47"
ADDRESS="47 Avenue du Lieutenant Colpin, 59650 Villeneuve-d'Ascq"
PRICE=14.99
DATE="2020-07-06 15:00:00"
DESCRIPTION="Stage Raku à l'Atelier 47"
TYPEID=5
NEXT=""

add_event "${PLACE}" "${ADDRESS}" "${PRICE}" "${DATE}" "${DESCRIPTION}" "${TYPEID}" "${NEXT}"

#10
PLACE="Musée du Terroir"
ADDRESS="12 Carrière Delporte, Villeneuve-d'Ascq"
PRICE=9
DATE="2020-07-05 14:00:00"
DESCRIPTION="Bêtes et utiles au musée du Terroir"
TYPEID=5
NEXT=""

add_event "${PLACE}" "${ADDRESS}" "${PRICE}" "${DATE}" "${DESCRIPTION}" "${TYPEID}" "${NEXT}"

