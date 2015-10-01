def  _validate(lat, lng):
    if lat <= -90 or lat >= 90:
      raise ValueError('The latitude should be a number between -90 and 90.')
    if (lng <= -180 or lng >= 180):
      raise ValueError('The longitude should be a number between -180 and 180.')


def _format_values(n, precision):
    #Adjust the precision of the values
    # We want 6 digits after the decimal point
    after_comma = (precision - 6) / 2;
    formatter = "{0:.%sf}" % after_comma
    tmp = formatter.format(n)
    # Now zero pad the portion before the decimal point
    (a, b) = tmp.split(".")
    r = ".".join([a.zfill(3), b])
    return r


def encode(lat, lng, validate=False, precision=18):
    if validate:
        _validate(lat, lng)
    shifted_lat = lat + 90.0
    shifted_lng = lng + 180.0
    lat_r = _format_values(shifted_lat, precision)
    lng_r = _format_values(shifted_lng, precision)
    return int("".join(["%s%s" % x for x in zip(lat_r,lng_r)]).replace(".", ""))

def decode(geozip):
    s = str(geozip)
    if len(s) % 2 == 1:
        #even, so zero pad
        s = "0" + s
    # Add the decimal point
    lat = s[::2][:3] + "." + s[::2][3:]
    lng = s[1::2][:3] + "." + s[1::2][3:]
    # adjust the shifted values
    d = {'lat': float(lat) - 90, 'lng': float(lng) - 180}
    return d

