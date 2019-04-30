def Sports(what, climbplace, swimmplace):
    if what == "swimm":
        print("I swimm in the {}.".format(swimmplace))
    if what == "climb":
        print("I swimm in the {}.".format(climbplace))

k = {"swimmplace": "Umag", 'climbplace': 'Punat'}
Sports("swimm", **k)