import gpiod

def log_chip_info(chip_path):
    try:
        chip = gpiod.Chip(chip_path)
        print(f"\n📌 Chip: {chip_path}")
        for line in chip.get_all_lines():
            offset = line.offset()
            name = line.name() or "Unnamed"
            consumer = line.consumer() or "None"
            print(f"Offset {offset:>3} | Name: {name:<10} | Used by: {consumer}")
    except Exception as e:
        print(f"❌ Error accessing {chip_path}: {e}")

if __name__ == "__main__":
    log_chip_info("/dev/gpiochip0")
    log_chip_info("/dev/gpiochip1")
