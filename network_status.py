import psutil
import time

def get_network_usage(interval=1):
    while True:
        net_info = psutil.net_io_counters(pernic=True)
        for interface, stats in net_info.items():
            print(f"Interface: {interface}")
            print(f"  İndirilen Veri: {convert_bytes(stats.bytes_recv)}")
            print(f"  Gönderilen Veri: {convert_bytes(stats.bytes_sent)}")
            print()
        time.sleep(interval)

def convert_bytes(bytes):
    if bytes < 1024:
        return f"{bytes} B"
    elif bytes < 1024**2:
        return f"{bytes / 1024:.2f} KB"
    elif bytes < 1024**3:
        return f"{bytes / (1024**2):.2f} MB"
    else:
        return f"{bytes / (1024**3):.2f} GB"

if __name__ == "__main__":
    get_network_usage()
