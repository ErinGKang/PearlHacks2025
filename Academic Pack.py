import csv
import mysql.connector
con = mysql.connector.connect(user='root', password='Tkswhgdk3308?', database = "data")

cur = con.cursor()

# cur.execute("CREATE DATABASE data;") 
# Social ENUM('Minimal interaction, focus is key', 'Some interaction, balance between studying and chatting', 'Lots of interaction, more of a group
# learning experience')
#cur.execute('DROP TABLE data;')
cur.execute('''CREATE TABLE IF NOT EXISTS data(
            Email varchar (100) NOT NULL,
            Name text, 
            Phone text, 
            Year ENUM('1st Year', '2nd Year', '3rd Year', '4th Year', '5th Year', 'Graduate Student'), 
            Major text, 
            Gender ENUM('Woman', 'Man', 'Nonbinary', 'Prefer not to answer'), 
            Residence ENUM('On-campus (North)', 'On-campus (South)', 'On-campus (Mid)', 'Off-campus'), 
            StudyStyle ENUM('Alone / With a partner', 'Group', 'Mix of both'), 
            Goals SET('Motivation to stay on track', 'Better understanding of the material', 'Practice and review', 'Accountability'),
            Social ENUM('Minimal interaction', 'Some interaction', 'Lots of interaction'),
            Meeting SET('In-person', 'Online'),
            Pref SET('Similar location', 'Same gender', 'Same year/grade', "Don't have any"),
            Duration ENUM('1-2 hours', '3-4 hours', 'All day', 'Depends / a little bit of everything'),
            UNIQUE(Email)
            );''')


insert_statement = """INSERT INTO data (Email, Name, Phone, Year, Major, Gender, Residence, StudyStyle, Goals, Social, Meeting, Pref, Duration)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

with open('StudyPact.csv') as csvfile:
    readData = csv.reader(csvfile)
    next(readData)
    for row in readData:
        print(row)
        replacedSocial = row[10].replace('Minimal interaction, focus is key', 'Minimal interaction').replace('Some interaction, balance between studying and chatting', 'Some interaction').replace('Lots of interaction, more of a group learning experience', 'Lots of interaction')
        print(replacedSocial)
        cur.execute(insert_statement, (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9].replace(', ', ','), replacedSocial, row[11].replace(', ', ','), row[12].replace(', ', ','), row[13]))
    con.commit()
    # Motivation to stay on track, Better understanding of the material
    # Motivation to stay on track,Better understanding of the material

    # for row in readData:
    #     print(len(row))
    #     print(row[1])
    #     print(row[2])
    #     print(row[3])
    #     print(row[4])
    #     print(row[5])
    #     print(row[6])
    #     print(row[7])
    #     print(row[8])
    #     print(row[9])
    #     print(row[10])
    #     print(row[11])
    #     print(row[12])
    #     print(row[13])
        # 0-13 columns: 14 in total
        # We are choosing the option from here.
        # Timestamp,Email Address,What is your first and last name?,What is your phone number?,Year in college?,Major?,Gender Identity:,Do you live on-campus or off-campus?,How do you prefer to study?,What are you hoping to achieve by studying with a buddy or a group?,How much social interaction do you like during study sessions?,Are you open to meeting in-person or would you prefer online study sessions?,Preferences for study buddy/group:,How long do you usually study for?




            
