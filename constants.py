TEMPLATE=(

# FRESHMAN
#########
'ID1',
'CSCI051',
'AREA1',
'MATH030',
##########
'CSCI052',
'CSCI055',
'MATH031',
'AREA2',

# SOPHOMORE
##########
'CSCI062',
'CSCI081',
'MATH060',
'AREA3',
##########
'CSCI105',
'CSCI140',
'AREA5',
'OTHER1',

# JUNIOR
##########
'CSCI131',
'ELEC1',
'AREA6',
'OTHER1',
##########
'ELEC2',
'OTHER1',
'OTHER2',
'OTHER3',

# SENIOR
##########
'CSCI190',
'ELEC3',
'OTHER1',
'OTHER2',
##########
'OTHER1',
'OTHER2',
'OTHER3',
'OTHER4'
)

###
# Schedule Modifiers:
###
CREDIT_CHOICES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
)

LANGUAGE_CHOICES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)

MATH_CHOICES = (
    #
    ('NONE', 'None'),
    ('MATH030', 'Calc1'),
    ('MATH031', 'Calc2'),
    ('MATH060', 'Linear')
)


# For pre-existing classes taken
## change to year which is just a number, and semester which is fall or spring
TERM_CHOICES = (
    ('FA13', 'Fall 2013'),
    ('SP14', 'Spring 2014'),
    ('FA14', 'Fall 2014'),
    ('SP15', 'Spring 2015'),
    ('FA15', 'Fall 2015'),
    ('SP16', 'Spring 2016'),
    ('FA16', 'Fall 2016'),
    ('SP17', 'Spring 2017'),
    ('FA17', 'Fall 2017'),
    ('SP18', 'Spring 2018'),
    ('FA18', 'Fall 2018'),
    ('SP19', 'Spring 2019'),
    ('FA19', 'Fall 2019'),
    ('SP20', 'Spring 2020'),
    ('FA20', 'Fall 2020'),
    ('SP21', 'Spring 2021'),
)
