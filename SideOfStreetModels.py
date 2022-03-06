# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 16:54:29 2022

@author: lewis
"""

""" ----------------------------------------------------------------------------------------------------------

- The beginning of the 'front' of first house on the street is the at the beginning of the street
- The end of the 'front' of last house on the street is the at the end of the street 
- The deliver point of the house (entrance of the property so drive/door etc) is considered to be at the 'end' of the house
  o- The entrance location was considered to have no/little effect
  o- If the house has a drive the walking up and down the drive is constant and should not determine the shortest route
- Lamp posts' are used to represent 'cart lock up points'. This doesn't just need to be lamp posts. 


First model below 'StreetSide A' looks something like.....
:: = door (entrance)
 * = lamp post (lock up point)

               _____________________________________________________________________________________________________________
houseNo....   |    0    |    1     |    2     |    3     |    4     |    5     |    6     |    7     |    8     |    9     |
letters....   |    5    |    5     |    5     |    5     |    5     |    5     |    5     |    5     |    5     |    5     | 
              |        ::         ::         ::         ::         ::         ::         ::         ::         ::         ::
              --------------------------------------------------------------------------------------------------------------
lamp posts..  *                               *                                *                                *

distance      0       10          20         30         40         50         60         70          80        90         100

"""
#  StreetSide A - nice spread all houses
StreetSide_A_LampPosts      =         [0,       30,         60,         90    ]
StreetSide_A_HouseFronts    =         [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_A_HouseLetters   =         [  5,  5,  5,  5,  5,  5,  5,  5,  5,  5]
StreetSide_A_MaxSackLetters = 15

# StreetSide B - some no delieveries
StreetSide_B_LampPosts      =         [ 0,      30,         60,         90    ]
StreetSide_B_HouseFronts    =         [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_B_HouseLetters   =         [  5,  0,  0,  5,  5,  0,  0,  0,  0,  5]
StreetSide_B_MaxSackLetters = 15

# StreetSide C - first & last house only
StreetSide_C_LampPosts      =         [ 0,      30,         60,         90    ]
StreetSide_C_HouseFronts    =         [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_C_HouseLetters   =         [  5,  0,  0,  0,  0,  0,  0,  0,  0,  5]
StreetSide_C_MaxSackLetters = 15

# StreetSide D - last house only
StreetSide_D_LampPosts      =         [ 0,      30,         60,         90    ]
StreetSide_D_HouseFronts    =         [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_D_HouseLetters   =         [  0,  0,  0,  0,  0,  0,  0,  0,  0,  5]
StreetSide_D_MaxSackLetters = 15

# StreetSide E - first house only
StreetSide_E_LampPosts      =         [ 0,      30,         60,         90    ]
StreetSide_E_HouseFronts    =         [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_E_HouseLetters   =         [  5,  0,  0,  0,  0,  0,  0,  0,  0,  0]
StreetSide_E_MaxSackLetters = 15

# StreetSide F one post
StreetSide_F_LampPosts      =         [                     60,               ]
StreetSide_F_HouseFronts    =         [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_F_HouseLetters   =         [  5,  0,  5,  0,  5,  0,  5,  0,  5,  0]
StreetSide_F_MaxSackLetters = 15

#  StreetSide G 
StreetSide_G_LampPosts      =         [0,       30,         60,         90    ]
StreetSide_G_HouseFronts    =         [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_G_HouseLetters   =         [ 10, 10,  6,  4, 10, 10, 10, 10, 10, 10]
StreetSide_G_MaxSackLetters = 15

#  StreetSide H 
StreetSide_H_LampPosts      =         [0,                 60,                 ]
StreetSide_H_HouseFronts    =         [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
StreetSide_H_HouseLetters   =         [ 10, 10,  6,  4, 10, 10, 10, 10, 10, 10]
StreetSide_H_MaxSackLetters = 15

#   Street M mixed spread
StreetSide_Z_LampPosts      =  [0,30,60,90,150,180]
StreetSide_Z_HouseFronts    =  [ 8,  8,  8,   8,  8,  8,  8,  8,  8,  8, 10, 10, 10, 10, 10, 10, 10, 10, 50, 50]
StreetSide_Z_HouseLetters   =  [ 2,  5,  4,  47,  0,  0,  0,  0,  0,  0,  4,  8,  9, 12, 45,  6,  4,  7,  6,  60]
StreetSide_Z_MaxSackLetters = 60
