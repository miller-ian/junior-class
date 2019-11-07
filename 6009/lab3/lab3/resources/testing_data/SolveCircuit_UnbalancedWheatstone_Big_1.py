junctions = {'0-1', '0-2', '0-3', '0-4', '0-5', '0-6', '0-7', '0-8', '0-9', '1-1', '1-2', '1-3', '1-4', '1-5', '1-6', '1-7', '1-8', '1-9', '10-1', '10-2', '10-3', '10-4', '10-5', '10-6', '10-7', '10-8', '10-9', '11-1', '11-2', '11-3', '11-4', '11-5', '11-6', '11-7', '11-8', '11-9', '12-1', '12-2', '12-3', '12-4', '12-5', '12-6', '12-7', '12-8', '12-9', '13-1', '13-2', '13-3', '13-4', '13-5', '13-6', '13-7', '13-8', '13-9', '14-1', '14-2', '14-3', '14-4', '14-5', '14-6', '14-7', '14-8', '14-9', '2-1', '2-2', '2-3', '2-4', '2-5', '2-6', '2-7', '2-8', '2-9', '3-1', '3-2', '3-3', '3-4', '3-5', '3-6', '3-7', '3-8', '3-9', '4-1', '4-2', '4-3', '4-4', '4-5', '4-6', '4-7', '4-8', '4-9', '5-1', '5-2', '5-3', '5-4', '5-5', '5-6', '5-7', '5-8', '5-9', '6-1', '6-2', '6-3', '6-4', '6-5', '6-6', '6-7', '6-8', '6-9', '7-1', '7-2', '7-3', '7-4', '7-5', '7-6', '7-7', '7-8', '7-9', '8-1', '8-2', '8-3', '8-4', '8-5', '8-6', '8-7', '8-8', '8-9', '9-1', '9-2', '9-3', '9-4', '9-5', '9-6', '9-7', '9-8', '9-9', 'A', 'B'}

wires = {'battery': ('B', 'A'), ('0-1', '0-2'): ('0-1', '0-2'), ('0-1', '1-1'): ('0-1', '1-1'), ('0-2', '0-3'): ('0-2', '0-3'), ('0-2', '1-2'): ('0-2', '1-2'), ('0-3', '0-4'): ('0-3', '0-4'), ('0-3', '1-3'): ('0-3', '1-3'), ('0-4', '0-5'): ('0-4', '0-5'), ('0-4', '1-4'): ('0-4', '1-4'), ('0-5', '0-6'): ('0-5', '0-6'), ('0-5', '1-5'): ('0-5', '1-5'), ('0-6', '0-7'): ('0-6', '0-7'), ('0-6', '1-6'): ('0-6', '1-6'), ('0-7', '0-8'): ('0-7', '0-8'), ('0-7', '1-7'): ('0-7', '1-7'), ('0-8', '0-9'): ('0-8', '0-9'), ('0-8', '1-8'): ('0-8', '1-8'), ('0-9', '1-9'): ('0-9', '1-9'), ('0-9', 'B'): ('0-9', 'B'), ('1-1', '1-2'): ('1-1', '1-2'), ('1-1', '2-1'): ('1-1', '2-1'), ('1-2', '1-3'): ('1-2', '1-3'), ('1-2', '2-2'): ('1-2', '2-2'), ('1-3', '1-4'): ('1-3', '1-4'), ('1-3', '2-3'): ('1-3', '2-3'), ('1-4', '1-5'): ('1-4', '1-5'), ('1-4', '2-4'): ('1-4', '2-4'), ('1-5', '1-6'): ('1-5', '1-6'), ('1-5', '2-5'): ('1-5', '2-5'), ('1-6', '1-7'): ('1-6', '1-7'), ('1-6', '2-6'): ('1-6', '2-6'), ('1-7', '1-8'): ('1-7', '1-8'), ('1-7', '2-7'): ('1-7', '2-7'), ('1-8', '1-9'): ('1-8', '1-9'), ('1-8', '2-8'): ('1-8', '2-8'), ('1-9', '2-9'): ('1-9', '2-9'), ('1-9', 'B'): ('1-9', 'B'), ('10-1', '10-2'): ('10-1', '10-2'), ('10-1', '11-1'): ('10-1', '11-1'), ('10-2', '10-3'): ('10-2', '10-3'), ('10-2', '11-2'): ('10-2', '11-2'), ('10-3', '10-4'): ('10-3', '10-4'), ('10-3', '11-3'): ('10-3', '11-3'), ('10-4', '10-5'): ('10-4', '10-5'), ('10-4', '11-4'): ('10-4', '11-4'), ('10-5', '10-6'): ('10-5', '10-6'), ('10-5', '11-5'): ('10-5', '11-5'), ('10-6', '10-7'): ('10-6', '10-7'), ('10-6', '11-6'): ('10-6', '11-6'), ('10-7', '10-8'): ('10-7', '10-8'), ('10-7', '11-7'): ('10-7', '11-7'), ('10-8', '10-9'): ('10-8', '10-9'), ('10-8', '11-8'): ('10-8', '11-8'), ('10-9', '11-9'): ('10-9', '11-9'), ('10-9', 'B'): ('10-9', 'B'), ('11-1', '11-2'): ('11-1', '11-2'), ('11-1', '12-1'): ('11-1', '12-1'), ('11-2', '11-3'): ('11-2', '11-3'), ('11-2', '12-2'): ('11-2', '12-2'), ('11-3', '11-4'): ('11-3', '11-4'), ('11-3', '12-3'): ('11-3', '12-3'), ('11-4', '11-5'): ('11-4', '11-5'), ('11-4', '12-4'): ('11-4', '12-4'), ('11-5', '11-6'): ('11-5', '11-6'), ('11-5', '12-5'): ('11-5', '12-5'), ('11-6', '11-7'): ('11-6', '11-7'), ('11-6', '12-6'): ('11-6', '12-6'), ('11-7', '11-8'): ('11-7', '11-8'), ('11-7', '12-7'): ('11-7', '12-7'), ('11-8', '11-9'): ('11-8', '11-9'), ('11-8', '12-8'): ('11-8', '12-8'), ('11-9', '12-9'): ('11-9', '12-9'), ('11-9', 'B'): ('11-9', 'B'), ('12-1', '12-2'): ('12-1', '12-2'), ('12-1', '13-1'): ('12-1', '13-1'), ('12-2', '12-3'): ('12-2', '12-3'), ('12-2', '13-2'): ('12-2', '13-2'), ('12-3', '12-4'): ('12-3', '12-4'), ('12-3', '13-3'): ('12-3', '13-3'), ('12-4', '12-5'): ('12-4', '12-5'), ('12-4', '13-4'): ('12-4', '13-4'), ('12-5', '12-6'): ('12-5', '12-6'), ('12-5', '13-5'): ('12-5', '13-5'), ('12-6', '12-7'): ('12-6', '12-7'), ('12-6', '13-6'): ('12-6', '13-6'), ('12-7', '12-8'): ('12-7', '12-8'), ('12-7', '13-7'): ('12-7', '13-7'), ('12-8', '12-9'): ('12-8', '12-9'), ('12-8', '13-8'): ('12-8', '13-8'), ('12-9', '13-9'): ('12-9', '13-9'), ('12-9', 'B'): ('12-9', 'B'), ('13-1', '13-2'): ('13-1', '13-2'), ('13-1', '14-1'): ('13-1', '14-1'), ('13-2', '13-3'): ('13-2', '13-3'), ('13-2', '14-2'): ('13-2', '14-2'), ('13-3', '13-4'): ('13-3', '13-4'), ('13-3', '14-3'): ('13-3', '14-3'), ('13-4', '13-5'): ('13-4', '13-5'), ('13-4', '14-4'): ('13-4', '14-4'), ('13-5', '13-6'): ('13-5', '13-6'), ('13-5', '14-5'): ('13-5', '14-5'), ('13-6', '13-7'): ('13-6', '13-7'), ('13-6', '14-6'): ('13-6', '14-6'), ('13-7', '13-8'): ('13-7', '13-8'), ('13-7', '14-7'): ('13-7', '14-7'), ('13-8', '13-9'): ('13-8', '13-9'), ('13-8', '14-8'): ('13-8', '14-8'), ('13-9', '14-9'): ('13-9', '14-9'), ('13-9', 'B'): ('13-9', 'B'), ('14-1', '14-2'): ('14-1', '14-2'), ('14-2', '14-3'): ('14-2', '14-3'), ('14-3', '14-4'): ('14-3', '14-4'), ('14-4', '14-5'): ('14-4', '14-5'), ('14-5', '14-6'): ('14-5', '14-6'), ('14-6', '14-7'): ('14-6', '14-7'), ('14-7', '14-8'): ('14-7', '14-8'), ('14-8', '14-9'): ('14-8', '14-9'), ('14-9', 'B'): ('14-9', 'B'), ('2-1', '2-2'): ('2-1', '2-2'), ('2-1', '3-1'): ('2-1', '3-1'), ('2-2', '2-3'): ('2-2', '2-3'), ('2-2', '3-2'): ('2-2', '3-2'), ('2-3', '2-4'): ('2-3', '2-4'), ('2-3', '3-3'): ('2-3', '3-3'), ('2-4', '2-5'): ('2-4', '2-5'), ('2-4', '3-4'): ('2-4', '3-4'), ('2-5', '2-6'): ('2-5', '2-6'), ('2-5', '3-5'): ('2-5', '3-5'), ('2-6', '2-7'): ('2-6', '2-7'), ('2-6', '3-6'): ('2-6', '3-6'), ('2-7', '2-8'): ('2-7', '2-8'), ('2-7', '3-7'): ('2-7', '3-7'), ('2-8', '2-9'): ('2-8', '2-9'), ('2-8', '3-8'): ('2-8', '3-8'), ('2-9', '3-9'): ('2-9', '3-9'), ('2-9', 'B'): ('2-9', 'B'), ('3-1', '3-2'): ('3-1', '3-2'), ('3-1', '4-1'): ('3-1', '4-1'), ('3-2', '3-3'): ('3-2', '3-3'), ('3-2', '4-2'): ('3-2', '4-2'), ('3-3', '3-4'): ('3-3', '3-4'), ('3-3', '4-3'): ('3-3', '4-3'), ('3-4', '3-5'): ('3-4', '3-5'), ('3-4', '4-4'): ('3-4', '4-4'), ('3-5', '3-6'): ('3-5', '3-6'), ('3-5', '4-5'): ('3-5', '4-5'), ('3-6', '3-7'): ('3-6', '3-7'), ('3-6', '4-6'): ('3-6', '4-6'), ('3-7', '3-8'): ('3-7', '3-8'), ('3-7', '4-7'): ('3-7', '4-7'), ('3-8', '3-9'): ('3-8', '3-9'), ('3-8', '4-8'): ('3-8', '4-8'), ('3-9', '4-9'): ('3-9', '4-9'), ('3-9', 'B'): ('3-9', 'B'), ('4-1', '4-2'): ('4-1', '4-2'), ('4-1', '5-1'): ('4-1', '5-1'), ('4-2', '4-3'): ('4-2', '4-3'), ('4-2', '5-2'): ('4-2', '5-2'), ('4-3', '4-4'): ('4-3', '4-4'), ('4-3', '5-3'): ('4-3', '5-3'), ('4-4', '4-5'): ('4-4', '4-5'), ('4-4', '5-4'): ('4-4', '5-4'), ('4-5', '4-6'): ('4-5', '4-6'), ('4-5', '5-5'): ('4-5', '5-5'), ('4-6', '4-7'): ('4-6', '4-7'), ('4-6', '5-6'): ('4-6', '5-6'), ('4-7', '4-8'): ('4-7', '4-8'), ('4-7', '5-7'): ('4-7', '5-7'), ('4-8', '4-9'): ('4-8', '4-9'), ('4-8', '5-8'): ('4-8', '5-8'), ('4-9', '5-9'): ('4-9', '5-9'), ('4-9', 'B'): ('4-9', 'B'), ('5-1', '5-2'): ('5-1', '5-2'), ('5-1', '6-1'): ('5-1', '6-1'), ('5-2', '5-3'): ('5-2', '5-3'), ('5-2', '6-2'): ('5-2', '6-2'), ('5-3', '5-4'): ('5-3', '5-4'), ('5-3', '6-3'): ('5-3', '6-3'), ('5-4', '5-5'): ('5-4', '5-5'), ('5-4', '6-4'): ('5-4', '6-4'), ('5-5', '5-6'): ('5-5', '5-6'), ('5-5', '6-5'): ('5-5', '6-5'), ('5-6', '5-7'): ('5-6', '5-7'), ('5-6', '6-6'): ('5-6', '6-6'), ('5-7', '5-8'): ('5-7', '5-8'), ('5-7', '6-7'): ('5-7', '6-7'), ('5-8', '5-9'): ('5-8', '5-9'), ('5-8', '6-8'): ('5-8', '6-8'), ('5-9', '6-9'): ('5-9', '6-9'), ('5-9', 'B'): ('5-9', 'B'), ('6-1', '6-2'): ('6-1', '6-2'), ('6-1', '7-1'): ('6-1', '7-1'), ('6-2', '6-3'): ('6-2', '6-3'), ('6-2', '7-2'): ('6-2', '7-2'), ('6-3', '6-4'): ('6-3', '6-4'), ('6-3', '7-3'): ('6-3', '7-3'), ('6-4', '6-5'): ('6-4', '6-5'), ('6-4', '7-4'): ('6-4', '7-4'), ('6-5', '6-6'): ('6-5', '6-6'), ('6-5', '7-5'): ('6-5', '7-5'), ('6-6', '6-7'): ('6-6', '6-7'), ('6-6', '7-6'): ('6-6', '7-6'), ('6-7', '6-8'): ('6-7', '6-8'), ('6-7', '7-7'): ('6-7', '7-7'), ('6-8', '6-9'): ('6-8', '6-9'), ('6-8', '7-8'): ('6-8', '7-8'), ('6-9', '7-9'): ('6-9', '7-9'), ('6-9', 'B'): ('6-9', 'B'), ('7-1', '7-2'): ('7-1', '7-2'), ('7-1', '8-1'): ('7-1', '8-1'), ('7-2', '7-3'): ('7-2', '7-3'), ('7-2', '8-2'): ('7-2', '8-2'), ('7-3', '7-4'): ('7-3', '7-4'), ('7-3', '8-3'): ('7-3', '8-3'), ('7-4', '7-5'): ('7-4', '7-5'), ('7-4', '8-4'): ('7-4', '8-4'), ('7-5', '7-6'): ('7-5', '7-6'), ('7-5', '8-5'): ('7-5', '8-5'), ('7-6', '7-7'): ('7-6', '7-7'), ('7-6', '8-6'): ('7-6', '8-6'), ('7-7', '7-8'): ('7-7', '7-8'), ('7-7', '8-7'): ('7-7', '8-7'), ('7-8', '7-9'): ('7-8', '7-9'), ('7-8', '8-8'): ('7-8', '8-8'), ('7-9', '8-9'): ('7-9', '8-9'), ('7-9', 'B'): ('7-9', 'B'), ('8-1', '8-2'): ('8-1', '8-2'), ('8-1', '9-1'): ('8-1', '9-1'), ('8-2', '8-3'): ('8-2', '8-3'), ('8-2', '9-2'): ('8-2', '9-2'), ('8-3', '8-4'): ('8-3', '8-4'), ('8-3', '9-3'): ('8-3', '9-3'), ('8-4', '8-5'): ('8-4', '8-5'), ('8-4', '9-4'): ('8-4', '9-4'), ('8-5', '8-6'): ('8-5', '8-6'), ('8-5', '9-5'): ('8-5', '9-5'), ('8-6', '8-7'): ('8-6', '8-7'), ('8-6', '9-6'): ('8-6', '9-6'), ('8-7', '8-8'): ('8-7', '8-8'), ('8-7', '9-7'): ('8-7', '9-7'), ('8-8', '8-9'): ('8-8', '8-9'), ('8-8', '9-8'): ('8-8', '9-8'), ('8-9', '9-9'): ('8-9', '9-9'), ('8-9', 'B'): ('8-9', 'B'), ('9-1', '10-1'): ('9-1', '10-1'), ('9-1', '9-2'): ('9-1', '9-2'), ('9-2', '10-2'): ('9-2', '10-2'), ('9-2', '9-3'): ('9-2', '9-3'), ('9-3', '10-3'): ('9-3', '10-3'), ('9-3', '9-4'): ('9-3', '9-4'), ('9-4', '10-4'): ('9-4', '10-4'), ('9-4', '9-5'): ('9-4', '9-5'), ('9-5', '10-5'): ('9-5', '10-5'), ('9-5', '9-6'): ('9-5', '9-6'), ('9-6', '10-6'): ('9-6', '10-6'), ('9-6', '9-7'): ('9-6', '9-7'), ('9-7', '10-7'): ('9-7', '10-7'), ('9-7', '9-8'): ('9-7', '9-8'), ('9-8', '10-8'): ('9-8', '10-8'), ('9-8', '9-9'): ('9-8', '9-9'), ('9-9', '10-9'): ('9-9', '10-9'), ('9-9', 'B'): ('9-9', 'B'), ('A', '0-1'): ('A', '0-1'), ('A', '1-1'): ('A', '1-1'), ('A', '10-1'): ('A', '10-1'), ('A', '11-1'): ('A', '11-1'), ('A', '12-1'): ('A', '12-1'), ('A', '13-1'): ('A', '13-1'), ('A', '14-1'): ('A', '14-1'), ('A', '2-1'): ('A', '2-1'), ('A', '3-1'): ('A', '3-1'), ('A', '4-1'): ('A', '4-1'), ('A', '5-1'): ('A', '5-1'), ('A', '6-1'): ('A', '6-1'), ('A', '7-1'): ('A', '7-1'), ('A', '8-1'): ('A', '8-1'), ('A', '9-1'): ('A', '9-1')}

resistances = {'battery': 0, ('0-1', '0-2'): 86, ('0-1', '1-1'): 78, ('0-2', '0-3'): 100, ('0-2', '1-2'): 80, ('0-3', '0-4'): 69, ('0-3', '1-3'): 53, ('0-4', '0-5'): 50, ('0-4', '1-4'): 92, ('0-5', '0-6'): 74, ('0-5', '1-5'): 63, ('0-6', '0-7'): 81, ('0-6', '1-6'): 95, ('0-7', '0-8'): 66, ('0-7', '1-7'): 84, ('0-8', '0-9'): 71, ('0-8', '1-8'): 79, ('0-9', '1-9'): 80, ('0-9', 'B'): 72, ('1-1', '1-2'): 71, ('1-1', '2-1'): 60, ('1-2', '1-3'): 91, ('1-2', '2-2'): 62, ('1-3', '1-4'): 58, ('1-3', '2-3'): 89, ('1-4', '1-5'): 61, ('1-4', '2-4'): 98, ('1-5', '1-6'): 97, ('1-5', '2-5'): 59, ('1-6', '1-7'): 63, ('1-6', '2-6'): 69, ('1-7', '1-8'): 62, ('1-7', '2-7'): 87, ('1-8', '1-9'): 72, ('1-8', '2-8'): 81, ('1-9', '2-9'): 65, ('1-9', 'B'): 51, ('10-1', '10-2'): 55, ('10-1', '11-1'): 96, ('10-2', '10-3'): 90, ('10-2', '11-2'): 85, ('10-3', '10-4'): 89, ('10-3', '11-3'): 92, ('10-4', '10-5'): 85, ('10-4', '11-4'): 69, ('10-5', '10-6'): 65, ('10-5', '11-5'): 63, ('10-6', '10-7'): 57, ('10-6', '11-6'): 69, ('10-7', '10-8'): 97, ('10-7', '11-7'): 71, ('10-8', '10-9'): 83, ('10-8', '11-8'): 55, ('10-9', '11-9'): 87, ('10-9', 'B'): 54, ('11-1', '11-2'): 51, ('11-1', '12-1'): 96, ('11-2', '11-3'): 81, ('11-2', '12-2'): 58, ('11-3', '11-4'): 82, ('11-3', '12-3'): 50, ('11-4', '11-5'): 68, ('11-4', '12-4'): 93, ('11-5', '11-6'): 59, ('11-5', '12-5'): 59, ('11-6', '11-7'): 78, ('11-6', '12-6'): 91, ('11-7', '11-8'): 54, ('11-7', '12-7'): 54, ('11-8', '11-9'): 69, ('11-8', '12-8'): 56, ('11-9', '12-9'): 64, ('11-9', 'B'): 53, ('12-1', '12-2'): 73, ('12-1', '13-1'): 50, ('12-2', '12-3'): 79, ('12-2', '13-2'): 60, ('12-3', '12-4'): 69, ('12-3', '13-3'): 93, ('12-4', '12-5'): 58, ('12-4', '13-4'): 60, ('12-5', '12-6'): 90, ('12-5', '13-5'): 90, ('12-6', '12-7'): 71, ('12-6', '13-6'): 85, ('12-7', '12-8'): 94, ('12-7', '13-7'): 82, ('12-8', '12-9'): 59, ('12-8', '13-8'): 71, ('12-9', '13-9'): 95, ('12-9', 'B'): 74, ('13-1', '13-2'): 67, ('13-1', '14-1'): 90, ('13-2', '13-3'): 64, ('13-2', '14-2'): 54, ('13-3', '13-4'): 54, ('13-3', '14-3'): 84, ('13-4', '13-5'): 60, ('13-4', '14-4'): 96, ('13-5', '13-6'): 95, ('13-5', '14-5'): 71, ('13-6', '13-7'): 51, ('13-6', '14-6'): 82, ('13-7', '13-8'): 59, ('13-7', '14-7'): 55, ('13-8', '13-9'): 57, ('13-8', '14-8'): 55, ('13-9', '14-9'): 87, ('13-9', 'B'): 80, ('14-1', '14-2'): 96, ('14-2', '14-3'): 70, ('14-3', '14-4'): 91, ('14-4', '14-5'): 79, ('14-5', '14-6'): 87, ('14-6', '14-7'): 93, ('14-7', '14-8'): 62, ('14-8', '14-9'): 53, ('14-9', 'B'): 76, ('2-1', '2-2'): 78, ('2-1', '3-1'): 83, ('2-2', '2-3'): 92, ('2-2', '3-2'): 89, ('2-3', '2-4'): 79, ('2-3', '3-3'): 50, ('2-4', '2-5'): 75, ('2-4', '3-4'): 99, ('2-5', '2-6'): 99, ('2-5', '3-5'): 52, ('2-6', '2-7'): 54, ('2-6', '3-6'): 87, ('2-7', '2-8'): 60, ('2-7', '3-7'): 88, ('2-8', '2-9'): 92, ('2-8', '3-8'): 51, ('2-9', '3-9'): 71, ('2-9', 'B'): 85, ('3-1', '3-2'): 96, ('3-1', '4-1'): 77, ('3-2', '3-3'): 56, ('3-2', '4-2'): 86, ('3-3', '3-4'): 82, ('3-3', '4-3'): 51, ('3-4', '3-5'): 61, ('3-4', '4-4'): 88, ('3-5', '3-6'): 57, ('3-5', '4-5'): 75, ('3-6', '3-7'): 78, ('3-6', '4-6'): 64, ('3-7', '3-8'): 69, ('3-7', '4-7'): 92, ('3-8', '3-9'): 84, ('3-8', '4-8'): 73, ('3-9', '4-9'): 58, ('3-9', 'B'): 56, ('4-1', '4-2'): 96, ('4-1', '5-1'): 99, ('4-2', '4-3'): 72, ('4-2', '5-2'): 51, ('4-3', '4-4'): 72, ('4-3', '5-3'): 72, ('4-4', '4-5'): 59, ('4-4', '5-4'): 98, ('4-5', '4-6'): 66, ('4-5', '5-5'): 59, ('4-6', '4-7'): 63, ('4-6', '5-6'): 75, ('4-7', '4-8'): 71, ('4-7', '5-7'): 53, ('4-8', '4-9'): 51, ('4-8', '5-8'): 77, ('4-9', '5-9'): 86, ('4-9', 'B'): 57, ('5-1', '5-2'): 56, ('5-1', '6-1'): 86, ('5-2', '5-3'): 56, ('5-2', '6-2'): 88, ('5-3', '5-4'): 85, ('5-3', '6-3'): 58, ('5-4', '5-5'): 79, ('5-4', '6-4'): 75, ('5-5', '5-6'): 91, ('5-5', '6-5'): 93, ('5-6', '5-7'): 75, ('5-6', '6-6'): 59, ('5-7', '5-8'): 90, ('5-7', '6-7'): 61, ('5-8', '5-9'): 57, ('5-8', '6-8'): 74, ('5-9', '6-9'): 91, ('5-9', 'B'): 88, ('6-1', '6-2'): 78, ('6-1', '7-1'): 87, ('6-2', '6-3'): 62, ('6-2', '7-2'): 65, ('6-3', '6-4'): 87, ('6-3', '7-3'): 70, ('6-4', '6-5'): 56, ('6-4', '7-4'): 59, ('6-5', '6-6'): 66, ('6-5', '7-5'): 65, ('6-6', '6-7'): 99, ('6-6', '7-6'): 82, ('6-7', '6-8'): 96, ('6-7', '7-7'): 95, ('6-8', '6-9'): 87, ('6-8', '7-8'): 71, ('6-9', '7-9'): 88, ('6-9', 'B'): 78, ('7-1', '7-2'): 87, ('7-1', '8-1'): 86, ('7-2', '7-3'): 86, ('7-2', '8-2'): 52, ('7-3', '7-4'): 98, ('7-3', '8-3'): 77, ('7-4', '7-5'): 70, ('7-4', '8-4'): 96, ('7-5', '7-6'): 92, ('7-5', '8-5'): 64, ('7-6', '7-7'): 54, ('7-6', '8-6'): 51, ('7-7', '7-8'): 80, ('7-7', '8-7'): 63, ('7-8', '7-9'): 60, ('7-8', '8-8'): 85, ('7-9', '8-9'): 100, ('7-9', 'B'): 60, ('8-1', '8-2'): 85, ('8-1', '9-1'): 67, ('8-2', '8-3'): 87, ('8-2', '9-2'): 59, ('8-3', '8-4'): 72, ('8-3', '9-3'): 85, ('8-4', '8-5'): 81, ('8-4', '9-4'): 88, ('8-5', '8-6'): 70, ('8-5', '9-5'): 79, ('8-6', '8-7'): 53, ('8-6', '9-6'): 79, ('8-7', '8-8'): 96, ('8-7', '9-7'): 89, ('8-8', '8-9'): 60, ('8-8', '9-8'): 62, ('8-9', '9-9'): 51, ('8-9', 'B'): 64, ('9-1', '10-1'): 74, ('9-1', '9-2'): 100, ('9-2', '10-2'): 53, ('9-2', '9-3'): 95, ('9-3', '10-3'): 67, ('9-3', '9-4'): 71, ('9-4', '10-4'): 96, ('9-4', '9-5'): 62, ('9-5', '10-5'): 62, ('9-5', '9-6'): 63, ('9-6', '10-6'): 75, ('9-6', '9-7'): 55, ('9-7', '10-7'): 72, ('9-7', '9-8'): 80, ('9-8', '10-8'): 89, ('9-8', '9-9'): 68, ('9-9', '10-9'): 50, ('9-9', 'B'): 86, ('A', '0-1'): 21, ('A', '1-1'): 28, ('A', '10-1'): 28, ('A', '11-1'): 7, ('A', '12-1'): 35, ('A', '13-1'): 7, ('A', '14-1'): 7, ('A', '2-1'): 14, ('A', '3-1'): 56, ('A', '4-1'): 70, ('A', '5-1'): 42, ('A', '6-1'): 63, ('A', '7-1'): 56, ('A', '8-1'): 42, ('A', '9-1'): 21}

voltages = {'battery': 2, ('0-1', '0-2'): 0, ('0-1', '1-1'): 0, ('0-2', '0-3'): 0, ('0-2', '1-2'): 0, ('0-3', '0-4'): 0, ('0-3', '1-3'): 0, ('0-4', '0-5'): 0, ('0-4', '1-4'): 0, ('0-5', '0-6'): 0, ('0-5', '1-5'): 0, ('0-6', '0-7'): 0, ('0-6', '1-6'): 0, ('0-7', '0-8'): 0, ('0-7', '1-7'): 0, ('0-8', '0-9'): 0, ('0-8', '1-8'): 0, ('0-9', '1-9'): 0, ('0-9', 'B'): 0, ('1-1', '1-2'): 0, ('1-1', '2-1'): 0, ('1-2', '1-3'): 0, ('1-2', '2-2'): 0, ('1-3', '1-4'): 0, ('1-3', '2-3'): 0, ('1-4', '1-5'): 0, ('1-4', '2-4'): 0, ('1-5', '1-6'): 0, ('1-5', '2-5'): 0, ('1-6', '1-7'): 0, ('1-6', '2-6'): 0, ('1-7', '1-8'): 0, ('1-7', '2-7'): 0, ('1-8', '1-9'): 0, ('1-8', '2-8'): 0, ('1-9', '2-9'): 0, ('1-9', 'B'): 0, ('10-1', '10-2'): 0, ('10-1', '11-1'): 0, ('10-2', '10-3'): 0, ('10-2', '11-2'): 0, ('10-3', '10-4'): 0, ('10-3', '11-3'): 0, ('10-4', '10-5'): 0, ('10-4', '11-4'): 0, ('10-5', '10-6'): 0, ('10-5', '11-5'): 0, ('10-6', '10-7'): 0, ('10-6', '11-6'): 0, ('10-7', '10-8'): 0, ('10-7', '11-7'): 0, ('10-8', '10-9'): 0, ('10-8', '11-8'): 0, ('10-9', '11-9'): 0, ('10-9', 'B'): 0, ('11-1', '11-2'): 0, ('11-1', '12-1'): 0, ('11-2', '11-3'): 0, ('11-2', '12-2'): 0, ('11-3', '11-4'): 0, ('11-3', '12-3'): 0, ('11-4', '11-5'): 0, ('11-4', '12-4'): 0, ('11-5', '11-6'): 0, ('11-5', '12-5'): 0, ('11-6', '11-7'): 0, ('11-6', '12-6'): 0, ('11-7', '11-8'): 0, ('11-7', '12-7'): 0, ('11-8', '11-9'): 0, ('11-8', '12-8'): 0, ('11-9', '12-9'): 0, ('11-9', 'B'): 0, ('12-1', '12-2'): 0, ('12-1', '13-1'): 0, ('12-2', '12-3'): 0, ('12-2', '13-2'): 0, ('12-3', '12-4'): 0, ('12-3', '13-3'): 0, ('12-4', '12-5'): 0, ('12-4', '13-4'): 0, ('12-5', '12-6'): 0, ('12-5', '13-5'): 0, ('12-6', '12-7'): 0, ('12-6', '13-6'): 0, ('12-7', '12-8'): 0, ('12-7', '13-7'): 0, ('12-8', '12-9'): 0, ('12-8', '13-8'): 0, ('12-9', '13-9'): 0, ('12-9', 'B'): 0, ('13-1', '13-2'): 0, ('13-1', '14-1'): 0, ('13-2', '13-3'): 0, ('13-2', '14-2'): 0, ('13-3', '13-4'): 0, ('13-3', '14-3'): 0, ('13-4', '13-5'): 0, ('13-4', '14-4'): 0, ('13-5', '13-6'): 0, ('13-5', '14-5'): 0, ('13-6', '13-7'): 0, ('13-6', '14-6'): 0, ('13-7', '13-8'): 0, ('13-7', '14-7'): 0, ('13-8', '13-9'): 0, ('13-8', '14-8'): 0, ('13-9', '14-9'): 0, ('13-9', 'B'): 0, ('14-1', '14-2'): 0, ('14-2', '14-3'): 0, ('14-3', '14-4'): 0, ('14-4', '14-5'): 0, ('14-5', '14-6'): 0, ('14-6', '14-7'): 0, ('14-7', '14-8'): 0, ('14-8', '14-9'): 0, ('14-9', 'B'): 0, ('2-1', '2-2'): 0, ('2-1', '3-1'): 0, ('2-2', '2-3'): 0, ('2-2', '3-2'): 0, ('2-3', '2-4'): 0, ('2-3', '3-3'): 0, ('2-4', '2-5'): 0, ('2-4', '3-4'): 0, ('2-5', '2-6'): 0, ('2-5', '3-5'): 0, ('2-6', '2-7'): 0, ('2-6', '3-6'): 0, ('2-7', '2-8'): 0, ('2-7', '3-7'): 0, ('2-8', '2-9'): 0, ('2-8', '3-8'): 0, ('2-9', '3-9'): 0, ('2-9', 'B'): 0, ('3-1', '3-2'): 0, ('3-1', '4-1'): 0, ('3-2', '3-3'): 0, ('3-2', '4-2'): 0, ('3-3', '3-4'): 0, ('3-3', '4-3'): 0, ('3-4', '3-5'): 0, ('3-4', '4-4'): 0, ('3-5', '3-6'): 0, ('3-5', '4-5'): 0, ('3-6', '3-7'): 0, ('3-6', '4-6'): 0, ('3-7', '3-8'): 0, ('3-7', '4-7'): 0, ('3-8', '3-9'): 0, ('3-8', '4-8'): 0, ('3-9', '4-9'): 0, ('3-9', 'B'): 0, ('4-1', '4-2'): 0, ('4-1', '5-1'): 0, ('4-2', '4-3'): 0, ('4-2', '5-2'): 0, ('4-3', '4-4'): 0, ('4-3', '5-3'): 0, ('4-4', '4-5'): 0, ('4-4', '5-4'): 0, ('4-5', '4-6'): 0, ('4-5', '5-5'): 0, ('4-6', '4-7'): 0, ('4-6', '5-6'): 0, ('4-7', '4-8'): 0, ('4-7', '5-7'): 0, ('4-8', '4-9'): 0, ('4-8', '5-8'): 0, ('4-9', '5-9'): 0, ('4-9', 'B'): 0, ('5-1', '5-2'): 0, ('5-1', '6-1'): 0, ('5-2', '5-3'): 0, ('5-2', '6-2'): 0, ('5-3', '5-4'): 0, ('5-3', '6-3'): 0, ('5-4', '5-5'): 0, ('5-4', '6-4'): 0, ('5-5', '5-6'): 0, ('5-5', '6-5'): 0, ('5-6', '5-7'): 0, ('5-6', '6-6'): 0, ('5-7', '5-8'): 0, ('5-7', '6-7'): 0, ('5-8', '5-9'): 0, ('5-8', '6-8'): 0, ('5-9', '6-9'): 0, ('5-9', 'B'): 0, ('6-1', '6-2'): 0, ('6-1', '7-1'): 0, ('6-2', '6-3'): 0, ('6-2', '7-2'): 0, ('6-3', '6-4'): 0, ('6-3', '7-3'): 0, ('6-4', '6-5'): 0, ('6-4', '7-4'): 0, ('6-5', '6-6'): 0, ('6-5', '7-5'): 0, ('6-6', '6-7'): 0, ('6-6', '7-6'): 0, ('6-7', '6-8'): 0, ('6-7', '7-7'): 0, ('6-8', '6-9'): 0, ('6-8', '7-8'): 0, ('6-9', '7-9'): 0, ('6-9', 'B'): 0, ('7-1', '7-2'): 0, ('7-1', '8-1'): 0, ('7-2', '7-3'): 0, ('7-2', '8-2'): 0, ('7-3', '7-4'): 0, ('7-3', '8-3'): 0, ('7-4', '7-5'): 0, ('7-4', '8-4'): 0, ('7-5', '7-6'): 0, ('7-5', '8-5'): 0, ('7-6', '7-7'): 0, ('7-6', '8-6'): 0, ('7-7', '7-8'): 0, ('7-7', '8-7'): 0, ('7-8', '7-9'): 0, ('7-8', '8-8'): 0, ('7-9', '8-9'): 0, ('7-9', 'B'): 0, ('8-1', '8-2'): 0, ('8-1', '9-1'): 0, ('8-2', '8-3'): 0, ('8-2', '9-2'): 0, ('8-3', '8-4'): 0, ('8-3', '9-3'): 0, ('8-4', '8-5'): 0, ('8-4', '9-4'): 0, ('8-5', '8-6'): 0, ('8-5', '9-5'): 0, ('8-6', '8-7'): 0, ('8-6', '9-6'): 0, ('8-7', '8-8'): 0, ('8-7', '9-7'): 0, ('8-8', '8-9'): 0, ('8-8', '9-8'): 0, ('8-9', '9-9'): 0, ('8-9', 'B'): 0, ('9-1', '10-1'): 0, ('9-1', '9-2'): 0, ('9-2', '10-2'): 0, ('9-2', '9-3'): 0, ('9-3', '10-3'): 0, ('9-3', '9-4'): 0, ('9-4', '10-4'): 0, ('9-4', '9-5'): 0, ('9-5', '10-5'): 0, ('9-5', '9-6'): 0, ('9-6', '10-6'): 0, ('9-6', '9-7'): 0, ('9-7', '10-7'): 0, ('9-7', '9-8'): 0, ('9-8', '10-8'): 0, ('9-8', '9-9'): 0, ('9-9', '10-9'): 0, ('9-9', 'B'): 0, ('A', '0-1'): 0, ('A', '1-1'): 0, ('A', '10-1'): 0, ('A', '11-1'): 0, ('A', '12-1'): 0, ('A', '13-1'): 0, ('A', '14-1'): 0, ('A', '2-1'): 0, ('A', '3-1'): 0, ('A', '4-1'): 0, ('A', '5-1'): 0, ('A', '6-1'): 0, ('A', '7-1'): 0, ('A', '8-1'): 0, ('A', '9-1'): 0}

soln = {'battery': 0.04427758527737697, ('0-1', '0-2'): 0.0028184275923485154, ('0-1', '1-1'): 0.00017730940158868945, ('0-2', '0-3'): 0.0028321103521488705, ('0-2', '1-2'): -1.3682759800318967e-05, ('0-3', '0-4'): 0.0029306028247211595, ('0-3', '1-3'): -9.849247257228881e-05, ('0-4', '0-5'): 0.003158777193039297, ('0-4', '1-4'): -0.00022817436831813753, ('0-5', '0-6'): 0.0031391422615703857, ('0-5', '1-5'): 1.9634931468911262e-05, ('0-6', '0-7'): 0.0027938131901783926, ('0-6', '1-6'): 0.00034532907139199313, ('0-7', '0-8'): 0.002858421883898063, ('0-7', '1-7'): -6.46086937196706e-05, ('0-8', '0-9'): 0.0029259267703041865, ('0-8', '1-8'): -6.750488640612313e-05, ('0-9', '1-9'): 0.0001988264977596299, ('0-9', 'B'): 0.0027271002725445356, ('1-1', '1-2'): 0.0032036622370989996, ('1-1', '2-1'): -0.0002856167570603423, ('1-2', '1-3'): 0.0030668742302481455, ('1-2', '2-2'): 0.00012310524705053458, ('1-3', '1-4'): 0.0032144767942555606, ('1-3', '2-3'): -0.00024609503657969917, ('1-4', '1-5'): 0.002953572167537288, ('1-4', '2-4'): 3.273025840013415e-05, ('1-5', '1-6'): 0.002720265860370173, ('1-5', '2-5'): 0.000252941238636028, ('1-6', '1-7'): 0.0029851662912660126, ('1-6', '2-6'): 8.042864049616289e-05, ('1-7', '1-8'): 0.0030443562674780707, ('1-7', '2-7'): -0.00012379866993173332, ('1-8', '1-9'): 0.003180275090811825, ('1-8', '2-8'): -0.00020342370973987274, ('1-9', '2-9'): -0.00015903762324100443, ('1-9', 'B'): 0.003538139211812476, ('10-1', '10-2'): 0.003361098202557999, ('10-1', '11-1'): -0.00045169517266522983, ('10-2', '10-3'): 0.002911795222328989, ('10-2', '11-2'): -0.00027437019399441056, ('10-3', '10-4'): 0.0026512585275484312, ('10-3', '11-3'): -0.00020601048158085022, ('10-4', '10-5'): 0.0026181618547716254, ('10-4', '11-4'): -0.00012380057666727513, ('10-5', '10-6'): 0.00297936376113128, ('10-5', '11-5'): -0.00032491176345253843, ('10-6', '10-7'): 0.0031086453152459116, ('10-6', '11-6'): -0.00020530901709438603, ('10-7', '10-8'): 0.002554883974256094, ('10-7', '11-7'): 0.0005522417061884523, ('10-8', '10-9'): 0.002681922969154877, ('10-8', '11-8'): -0.00015175063554677076, ('10-9', '11-9'): -0.00010355001670163703, ('10-9', 'B'): 0.003268729606340415, ('11-1', '11-2'): 0.004017679827980924, ('11-1', '12-1'): 0.000305388933469843, ('11-2', '11-3'): 0.003289260150539453, ('11-2', '12-2'): 0.00045404948344705977, ('11-3', '11-4'): 0.0030045455300878854, ('11-3', '12-3'): 7.870413887071381e-05, ('11-4', '11-5'): 0.003097302299237062, ('11-4', '12-4'): -0.00021655734581645507, ('11-5', '11-6'): 0.0033891824303649235, ('11-5', '12-5'): -0.0006167918945803963, ('11-6', '11-7'): 0.0029560034139475603, ('11-6', '12-6'): 0.00022786999932297074, ('11-7', '11-8'): 0.0037086722112664562, ('11-7', '12-7'): -0.00020042709113043543, ('11-8', '11-9'): 0.00321647883973746, ('11-8', '12-8'): 0.00034044273598224373, ('11-9', '12-9'): -0.00038745325612313947, ('11-9', 'B'): 0.0035003820791589613, ('12-1', '12-2'): 0.0027660164884089266, ('12-1', '13-1'): -0.0006680365505985992, ('12-2', '12-3'): 0.0030889925202190116, ('12-2', '13-2'): 0.00013107345163697524, ('12-3', '12-4'): 0.0032217057009092842, ('12-3', '13-3'): -5.400904181955531e-05, ('12-4', '12-5'): 0.0033511322022208127, ('12-4', '13-4'): -0.0003459838471279823, ('12-5', '12-6'): 0.0028565406123351577, ('12-5', '13-5'): -0.0001222003046947405, ('12-6', '12-7'): 0.0028029441327954347, ('12-6', '13-6'): 0.00028146647886269344, ('12-7', '12-8'): 0.0024484697398344446, ('12-7', '13-7'): 0.0001540473018305646, ('12-8', '12-9'): 0.003018224378559283, ('12-8', '13-8'): -0.00022931190274259473, ('12-9', '13-9'): -0.00021135399360852538, ('12-9', 'B'): 0.002842125116044671, ('13-1', '13-2'): 0.0036296334071940317, ('13-1', '14-1'): -0.0001064045832230699, ('13-2', '13-3'): 0.003611611892341637, ('13-2', '14-2'): 0.00014909496648936953, ('13-3', '13-4'): 0.0038252130263755615, ('13-3', '14-3'): -0.0002676101758534784, ('13-4', '13-5'): 0.0034021111855659907, ('13-4', '14-4'): 7.711799368159168e-05, ('13-5', '13-6'): 0.003073803507747577, ('13-5', '14-5'): 0.00020610737312367434, ('13-6', '13-7'): 0.0036807110093186905, ('13-6', '14-6'): -0.00032544102270841186, ('13-7', '13-8'): 0.0034109005372814794, ('13-7', '14-7'): 0.00042385777386776976, ('13-8', '13-9'): 0.003057504456787938, ('13-8', '14-8'): 0.0001240841777509403, ('13-9', '14-9'): -3.379813657204737e-05, ('13-9', 'B'): 0.0028799485997514475, ('14-1', '14-2'): 0.0027168018641927317, ('14-2', '14-3'): 0.0028658968306821014, ('14-3', '14-4'): 0.0025982866548286297, ('14-4', '14-5'): 0.0026754046485102214, ('14-5', '14-6'): 0.0028815120216338958, ('14-6', '14-7'): 0.002556070998925486, ('14-7', '14-8'): 0.0029799287727932558, ('14-8', '14-9'): 0.003104012950544201, ('14-9', 'B'): 0.0030702148139721535, ('2-1', '2-2'): 0.0032337121740356753, ('2-1', '3-1'): 0.0007380714098310226, ('2-2', '2-3'): 0.0027125062106505967, ('2-2', '3-2'): 0.0006443112104356127, ('2-3', '2-4'): 0.002677844020830745, ('2-3', '3-3'): -0.00021143284675984587, ('2-4', '2-5'): 0.0025584515996811613, ('2-4', '3-4'): 0.00015212267954971593, ('2-5', '2-6'): 0.0025706245613193574, ('2-5', '3-5'): 0.00024076827699783725, ('2-6', '2-7'): 0.003180470664286347, ('2-6', '3-6'): -0.0005294174624708325, ('2-7', '2-8'): 0.003050720872979525, ('2-7', '3-7'): 5.951121375088262e-06, ('2-8', '2-9'): 0.0025556487121382154, ('2-8', '3-8'): 0.00029164845110143126, ('2-9', '3-9'): 0.00015211055580189854, ('2-9', 'B'): 0.0022445005330953127, ('3-1', '3-2'): 0.00258659708632893, ('3-1', '4-1'): 0.0003097516768762624, ('3-2', '3-3'): 0.0032434862734480904, ('3-2', '4-2'): -1.2577976683547675e-05, ('3-3', '3-4'): 0.002892456893402964, ('3-3', '4-3'): 0.0001395965332852852, ('3-4', '3-5'): 0.003103994673845127, ('3-4', '4-4'): -5.9415100892445446e-05, ('3-5', '3-6'): 0.00343706249003099, ('3-5', '4-5'): -9.229953918802695e-05, ('3-6', '3-7'): 0.0027990824844542684, ('3-6', '4-6'): 0.00010856254310589661, ('3-7', '3-8'): 0.0028607771696222695, ('3-7', '4-7'): -5.5743563792912724e-05, ('3-8', '3-9'): 0.0027505411901485428, ('3-8', '4-8'): 0.00040188443057517065, ('3-9', '4-9'): -0.0003113249656775358, ('3-9', 'B'): 0.003213976711627976, ('4-1', '4-2'): 0.0023268826580554163, ('4-1', '5-1'): 5.021774608407021e-05, ('4-2', '4-3'): 0.0026366161181309417, ('4-2', '5-2'): -0.0003223114367590755, ('4-3', '4-4'): 0.003122687683096643, ('4-3', '5-3'): -0.0003464750316804187, ('4-4', '4-5'): 0.0031805040431184053, ('4-4', '5-4'): -0.00011723146091420302, ('4-5', '4-6'): 0.0031785307595400885, ('4-5', '5-5'): -9.032625560971727e-05, ('4-6', '4-7'): 0.003273841637455676, ('4-6', '5-6'): 1.325166519030733e-05, ('4-7', '4-8'): 0.003265628112744678, ('4-7', '5-7'): -4.7530039081921165e-05, ('4-8', '4-9'): 0.003601000951592021, ('4-8', '5-8'): 6.651159172783265e-05, ('4-9', '5-9'): -0.00018470197654977286, ('4-9', 'B'): 0.003474377962464276, ('5-1', '5-2'): 0.003606630268505074, ('5-1', '6-1'): 7.539091168250803e-06, ('5-2', '5-3'): 0.003238000741056259, ('5-2', '6-2'): 4.631809068973844e-05, ('5-3', '5-4'): 0.0028034239093453713, ('5-3', '6-3'): 8.810180003046707e-05, ('5-4', '5-5'): 0.0024532806662355, ('5-4', '6-4'): 0.00023291178219566537, ('5-5', '5-6'): 0.0023747929021966175, ('5-5', '6-5'): -1.1838491570840163e-05, ('5-6', '5-7'): 0.0027031874159879027, ('5-6', '6-6'): -0.00031514284860097375, ('5-7', '5-8'): 0.0026611120071028567, ('5-7', '6-7'): -5.454630196884114e-06, ('5-8', '5-9'): 0.002853426069909991, ('5-8', '6-8'): -0.00012580247107930087, ('5-9', '6-9'): 0.00023777052695402783, ('5-9', 'B'): 0.0024309535664061854, ('6-1', '6-2'): 0.00263331955354502, ('6-1', '7-1'): -0.00023952126219870356, ('6-2', '6-3'): 0.002941321837422913, ('6-2', '7-2'): -0.0002616841931881539, ('6-3', '6-4'): 0.0028810288684743028, ('6-3', '7-3'): 0.00014839476897907734, ('6-4', '6-5'): 0.0031292823080685977, ('6-4', '7-4'): -1.5341657398626287e-05, ('6-5', '6-6'): 0.0030092985719473164, ('6-5', '7-5'): 0.00010814524455044024, ('6-6', '6-7'): 0.0022323207255004066, ('6-6', '7-6'): 0.00046183499784592893, ('6-7', '6-8'): 0.002401285731472904, ('6-7', '7-7'): -0.00017441963616938202, ('6-8', '6-9'): 0.002225192951696026, ('6-8', '7-8'): 5.0290308697562603e-05, ('6-9', '7-9'): -2.2518532848983783e-06, ('6-9', 'B'): 0.00246521533193497, ('7-1', '7-2'): 0.0024049172693168825, ('7-1', '8-1'): -0.00033201032080253426, ('7-2', '7-3'): 0.002439058840767279, ('7-2', '8-2'): -0.000295825764638548, ('7-3', '7-4'): 0.002442415509614388, ('7-3', '8-3'): 0.00014503810013196793, ('7-4', '7-5'): 0.002616777256201986, ('7-4', '8-4'): -0.00018970340398622178, ('7-5', '7-6'): 0.0024940732030012003, ('7-5', '8-5'): 0.00023084929775122123, ('7-6', '7-7'): 0.0030844336400941254, ('7-6', '8-6'): -0.00012852543924699416, ('7-7', '7-8'): 0.0031332988446877126, ('7-7', '8-7'): -0.00022328484076295833, ('7-8', '7-9'): 0.003163716863182605, ('7-8', '8-8'): 1.987229020266699e-05, ('7-9', '8-9'): -4.661763976895328e-05, ('7-9', 'B'): 0.0032080826496666457, ('8-1', '8-2'): 0.0026164441206868497, ('8-1', '9-1'): -0.0005450474840866949, ('8-2', '8-3'): 0.0027162061353718627, ('8-2', '9-2'): -0.00039558777932356047, ('8-3', '8-4'): 0.0029163508256857106, ('8-3', '9-3'): -5.5106590181880354e-05, ('8-4', '8-5'): 0.0026686455527517835, ('8-4', '9-4'): 5.800186894769418e-05, ('8-5', '8-6'): 0.002973222603120508, ('8-5', '9-5'): -7.372775261750019e-05, ('8-6', '8-7'): 0.0030008918678983603, ('8-6', '9-6'): -0.00015619470402484525, ('8-7', '8-8'): 0.0027752083042740633, ('8-7', '9-7'): 2.398722861338739e-06, ('8-8', '8-9'): 0.003057868385780571, ('8-8', '9-8'): -0.00026278779130385307, ('8-9', '9-9'): -6.916680018985732e-05, ('8-9', 'B'): 0.003080417546201468, ('9-1', '10-1'): 0.00016704288294012878, ('9-1', '9-2'): 0.002355762527121007, ('9-2', '10-2'): -0.0007236731742234195, ('9-2', '9-3'): 0.002683847922020866, ('9-3', '10-3'): -0.0004665471763614101, ('9-3', '9-4'): 0.0030952885082003957, ('9-4', '10-4'): -0.00015689724944408534, ('9-4', '9-5'): 0.0033101876265921753, ('9-5', '10-5'): 3.629014290711421e-05, ('9-5', '9-6'): 0.0032001697310675447, ('9-6', '10-6'): -7.602746297974712e-05, ('9-6', '9-7'): 0.0031200024900224486, ('9-7', '10-7'): -1.5196348013711713e-06, ('9-7', '9-8'): 0.003123920847685155, ('9-8', '10-8'): -2.471164064797722e-05, ('9-8', '9-9'): 0.002885844697029271, ('9-9', '10-9'): 0.0004832566204838873, ('9-9', 'B'): 0.0023334212763555452, ('A', '0-1'): 0.002995736993937205, ('A', '1-1'): 0.0027407360784499684, ('A', '10-1'): 0.002742360146952643, ('A', '11-1'): 0.00477476393411599, ('A', '12-1'): 0.0017925910043404816, ('A', '13-1'): 0.004191265374569557, ('A', '14-1'): 0.0028232064474158014, ('A', '2-1'): 0.004257400340927041, ('A', '3-1'): 0.002158277353374169, ('A', '4-1'): 0.0020673487272632237, ('A', '5-1'): 0.0035639516135892524, ('A', '6-1'): 0.0023862592001780663, ('A', '7-1'): 0.002312428210713053, ('A', '8-1'): 0.002403406957402691, ('A', '9-1'): 0.0030678528941478315}

