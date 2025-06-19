import gpiod
import sys
import glob

def log(msg: str):
    """Log message to stdout with flush (so Home Assistant captures it)."""
    print(msg, flush=True)

# Glob all gpiochip devices
chip_devices = sorted(glob.glob("/dev/gpiochip*"))
if not chip_devices:
    log("Geen GPIO-chips gevonden op dit systeem.")
    sys.exit(0)

for chip_path in chip_devices:
    try:
        chip = gpiod.Chip(chip_path)
    except Exception as e:
        log(f"Kon {chip_path} niet openen: {e}")
        continue

    chip_info = chip.get_info()
    # Log chip header: e.g. gpiochip0 [label] (X lines)
    log(f"{chip_info.name} [{chip_info.label}] ({chip_info.num_lines} lines):")

    # Iterate over all lines of the chip
    for offset in range(chip_info.num_lines):
        try:
            line_info = chip.get_line_info(offset)
        except Exception as e:
            log(f"  line {offset:>3}: (Fout bij uitlezen: {e})")
            continue

        # Line name and consumer
        line_name = line_info.name or ""
        consumer = line_info.consumer or ""
        used = consumer != ""

        # Determine status strings
        consumer_str = f"\"{consumer}\"" if used else "unused"
        direction_str = "output" if hasattr(line_info, "direction") and str(line_info.direction).endswith("OUTPUT") else "input"
        active_str = "active-low" if getattr(line_info, "active_low", False) else "active-high"

        # Format line output similar to gpioinfo
        # Example: line   0: "LINE_NAME"       unused   input  active-high [used]
        line_output = f"  line {offset:>3}: \"{line_name}\"".ljust(20)
        line_output += f"{consumer_str}".ljust(12)
        line_output += f"{direction_str}".ljust(7)
        line_output += f"{active_str}"
        if used:
            line_output += " [used]"
        log(line_output)
    # Close the chip when done
    chip.close()
