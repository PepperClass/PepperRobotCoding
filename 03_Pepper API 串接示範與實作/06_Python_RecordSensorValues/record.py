


#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Record some sensors values and write them into a file."""

import qi
import argparse
import sys
import os
import time


# MEMORY_VALUE_NAMES is the list of ALMemory values names you want to save.
ALMEMORY_KEY_NAMES = ["Device/SubDeviceList/HeadYaw/Position/Sensor/Value",
                      "Device/SubDeviceList/HeadYaw/Position/Actuator/Value"]

def recordData(memory_service):
    """ Record the data from ALMemory.
    Returns a matrix of values

    """
    print "Recording data ..."
    data = list()
    for range_counter in range (1, 100):
        line = list()
        for key in ALMEMORY_KEY_NAMES:
            value = memory_service.getData(key)
            line.append(value)
        data.append(line)
        time.sleep(0.05)
    return data

def main(session):
    """ Parse command line arguments, run recordData
    and write the results into a csv file.
    """
    # Get the services ALMemory and ALMotion.

    memory_service = session.service("ALMemory")
    motion_service = session.service("ALMotion")

    # Set stiffness on for Head motors
    motion_service.setStiffnesses("Head", 1.0)
    # Will go to 1.0 then 0 radian  in two seconds
    motion_service.angleInterpolation(
        ["HeadYaw"],
        [1.0, 0.0],
        [1  , 2],
        False,
        _async=True
    )
    data = recordData(memory_service)
    # Gently set stiff off for Head motors
    motion_service.setStiffnesses("Head", 0.0)

    output = os.path.abspath("record.csv")

    with open(output, "w") as fp:
        for line in data:
            fp.write("; ".join(str(x) for x in line))
            fp.write("\n")

    print "Results written to", output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
	
	