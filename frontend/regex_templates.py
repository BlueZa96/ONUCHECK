import re

ONU_DATA_LINE_REGEX = re.compile(
    r"(?P<IntfName>GPON0/\d+:\d+)\s+"
    r"(?P<VendorID>\S+)\s+"
    r"(?P<ModelID>\S+)\s+"
    r"(?P<SN>\S+:\S+)\s+"
    r"(?P<LOID>\S+)\s+"
    r"(?P<Status>\S+)\s+"
    r"(?P<ConfigStatus>\S+)\s+"
    r"(?P<ActiveTime>(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}|N/A)?)"
)

ONU_STATS_LINE_REGEX = re.compile(
    r"(?P<IntfName>gpon0/\d+:\s*\d+)\s+"
    r"(?P<Temp>--|\d+\.\d+)\s+"
    r"(?P<Volt>--|\d+\.\d+)\s+"
    r"(?P<Bias>--|\d+\.\d+)\s+"
    r"(?P<RxPow>--|-\d+\.\d+)\s+"
    r"(?P<TxPow>--|-?\d+\.\d+)\s*"
)