def cube_times(times):
    
    times = sorted(times)
    
    min_value = min(times)
    
    retTimes = times[1:-1]
    
    avg_value = format((sum(retTimes)/len(retTimes)),'.2f')
    tup = (float(avg_value), min_value)
    
    return tup