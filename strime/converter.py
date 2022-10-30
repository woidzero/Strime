# converter.py
# A simple string (time+unit) to seconds converter.
# https://github.com/woidzero/Strime.git


def converter(value, unit):
    match unit:
        case "ms":
            return value * 1000
        case "s":
            return value
        case "m":
            return value * 60
        case "h":
            return value * 3600
        case "d":
            return value * 86400
        case "w":
            return value * 604800
        case "mn":
            return value * 2628000
        case "y":
            return value * 60 * 60 * 24 * 365
        case "c":
            return value * 60 * 60 * 24 * 365 * 100