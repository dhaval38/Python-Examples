import pytz
import time
from datetime import datetime, timedelta
import tzlocal

# Get local time and timezone
_time = time.strftime("%Y-%m-%d-%H-%M-%S")
_std_time = datetime.strptime(_time, "%Y-%m-%d-%H-%M-%S")
local_timezone = tzlocal.get_localzone()
local_dt = local_timezone.localize(_std_time, is_dst=None)
india_offset = local_timezone.utcoffset(_std_time)
offset_days = india_offset.days
print "india offset : %s, offset_days : %s" %(india_offset, offset_days)
print "Offset : %s" %local_timezone.utcoffset(_std_time)

# Get UTC time based on local time and timezone
utc_dt = local_dt.astimezone(pytz.utc)
print "_time : %s, _std_time : %s, local_timezone : %s" %(_time, _std_time, local_timezone)
print "local_dt = %s" %local_dt
print "utc_dt : %s" %utc_dt

america = pytz.timezone("US/Eastern")
loc_ame = america.localize(datetime(2016,07,28,0,0,0))
offset = america.utcoffset(_std_time)
days = offset.days
if days < 0:
    offset_hours = 24 - (offset.seconds/3600)
print "days : %s, offset_hours : %s" %(days, offset_hours)
print "america offset : %s %s %s %s" %(offset, type(offset), offset.days, (offset.seconds/3600))
