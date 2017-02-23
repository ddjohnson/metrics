#!/usr/bin/env python
"""
Parse input.json and print the individual timestamp information.
Instructions: Ensure input.json is present in local directory.
Usage: ./json.parser.py
"""
from collections import OrderedDict
from decimal import Decimal
import json
import syslog


def json_egress():
    """Parse json and emit formatted single metrics."""
    with open("input.json") as json_data:
        jsonStr = json_data.read(100*2**20)  # 100MB file limit for safety or more/would probs just tail file/yield to func
    # We can close the file now.
    metric_data = json.loads(jsonStr, parse_float=Decimal, object_pairs_hook=OrderedDict)  # Preserve loading order/ordered dict/nosort required now!
    for epoch, metriclist in metric_data.items():
        for metric in metriclist:
            sample = metric.get("sample_ms")  # Safety, either gets the data or NoneType.
            source = metric.get("source")
            target = metric.get("target")
            tag = {"source": source, "target": target}
            #print "Timestamp: {0}, sample_ms: {1}, tag: {2}".format(epoch, sample, tag) # debug/not for prod/will cause perf prob


if __name__ == "__main__":
    json_egress()
