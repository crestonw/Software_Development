"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#

acp_brevets = {'200' : (15, 34), '300' : (15, 32), '400' : (15, 32), '600' : (15, 30), '1000' : (11.428, 28)} 

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    if control_dist_km > brevet_dist_km:
    	control_dist_km = brevet_dist_km

    max_speed = acp_brevets['{}'.format(brevet_dist_km)][1]
    open_t = control_dist_km / max_speed
    mn = round((open_t % 1) * 60)	
    hrs = (open_t // 1) - 4
    time = brevet_start_time.shift(hours=hrs, minutes=mn)			
    return time.isoformat()

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    min_speed = acp_brevets['{}'.format(brevet_dist_km)][0]
    
    if control_dist_km > brevet_dist_km:
    	control_dist_km = brevet_dist_km

    open_t = control_dist_km / min_speed
    
    if control_dist_km == 200 and brevet_dist_km == 200:
    	mn = round((open_t % 1) * 60) + 10

    else:	
    	mn = round((open_t % 1) * 60)	

    if control_dist_km == 0:
    	hrs = -3
    else:
    	hrs = (open_t // 1) - 4

    time = brevet_start_time.shift(hours=hrs, minutes=mn)			
    return time.isoformat()


