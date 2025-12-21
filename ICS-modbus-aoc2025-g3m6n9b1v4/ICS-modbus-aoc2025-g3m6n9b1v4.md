![ICS/Modbus - Claus for Concern Banner](https://tryhackme-images.s3.eu-west-1.amazonaws.com/room-icons/63c131e50a24c3005eb34678-1763819753983)

<p align="center">
   <img src="https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ICS-modbus-aoc2025-g3m6n9b1v4/ICS-Modbus_-_Claus_for_Concern_Cover.png" alt="ICS/Modbus - Claus for Concern Logo">
</p>

# <img src="https://tryhackme-images.s3.amazonaws.com/room-icons/63c131e50a24c3005eb34678-1764070538293" alt="image" style="vertical-align: middle;height: 50px;" /> ICS/Modbus - Claus for Concern | Advent of Cyber 2025 - Day 19

This guide contains the answer and steps necessary to get to them for the [ICS/Modbus - Claus for Concern](https://tryhackme.com/room/ICS-modbus-aoc2025-g3m6n9b1v4) room.

## Table of contents

- [SCADA (Supervisory Control and Data Acquisition)](#scada-supervisory-control-and-data-acquisition)
- [Practical](#practical)

### SCADA (Supervisory Control and Data Acquisition)

1.  What port is commonly used by Modbus TCP?

    The answer to this question can be found in the text.

    ><details><summary>Click for answer</summary>502</details>

### Practical

1.  What's the flag?

    Create the first script that is provided using `nano`.

    ```cmd
    nano reconnaissance.py
    ```

    ```python
    #!/usr/bin/env python3
    from pymodbus.client import ModbusTcpClient

    PLC_IP = "10.82.170.49"
    PORT = 502
    UNIT_ID = 1

    # Connect to PLC
    client = ModbusTcpClient(PLC_IP, port=PORT)

    if not client.connect():
        print("Failed to connect to PLC")
        exit(1)

    print("=" * 60)
    print("TBFC Drone System - Reconnaissance Report")
    print("=" * 60)
    print()

    # Read holding registers
    print("HOLDING REGISTERS:")
    print("-" * 60)

    registers = client.read_holding_registers(address=0, count=5, slave=UNIT_ID)
    if not registers.isError():
        hr0, hr1, hr2, hr3, hr4 = registers.registers
        
        print(f"HR0 (Package Type): {hr0}")
        print(f"  0=Christmas, 1=Eggs, 2=Baskets")
        print()
        
        print(f"HR1 (Delivery Zone): {hr1}")
        print(f"  1-9=Normal zones, 10=Ocean dump")
        print()
        
        print(f"HR4 (System Signature): {hr4}")
        if hr4 == 666:
            print(f"  WARNING: Eggsploit signature detected")
        print()

    # Read coils
    print("COILS (Boolean Flags):")
    print("-" * 60)

    coils = client.read_coils(address=10, count=6, slave=UNIT_ID)
    if not coils.isError():
        c10, c11, c12, c13, c14, c15 = coils.bits[:6]
        
        print(f"C10 (Inventory Verification): {c10}")
        print(f"  Should be True")
        print()
        
        print(f"C11 (Protection/Override): {c11}")
        if c11:
            print(f"  ACTIVE - System monitoring for changes")
        print()
        
        print(f"C12 (Emergency Dump): {c12}")
        if c12:
            print(f"  CRITICAL: Dump protocol active")
        print()
        
        print(f"C13 (Audit Logging): {c13}")
        print(f"  Should be True")
        print()
        
        print(f"C14 (Christmas Restored): {c14}")
        print(f"  Auto-set when system is fixed")
        print()
        
        print(f"C15 (Self-Destruct Armed): {c15}")
        if c15:
            print(f"  DANGER: Countdown active")
        print()

    print("=" * 60)
    print("THREAT ASSESSMENT:")
    print("=" * 60)

    if hr4 == 666:
        print("Eggsploit framework detected")
    if c11:
        print("Protection mechanism active - trap is set")
    if hr0 == 1:
        print("Package type forced to eggs")
    if not c10:
        print("Inventory verification disabled")
    if not c13:
        print("Audit logging disabled")

    print()
    print("REMEDIATION REQUIRED")
    print("=" * 60)

    client.close()
    ```

    ```cmd
    python3 reconnaissance.py
    ```

    ![Script1](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ICS-modbus-aoc2025-g3m6n9b1v4/ICS-Modbus_-_Claus_for_Concern_Script1.png)

    We can now see what the status is of the system and on the CCTV we can see that eggs er loaded onto the drones.

    Lets create the restore script and run it.

    ```cmd
    nano restore_christmas.py
    ```

    ```python
    #!/usr/bin/env python3
    from pymodbus.client import ModbusTcpClient
    import time

    PLC_IP = "10.82.170.49"
    PORT = 502
    UNIT_ID = 1

    def read_coil(client, address):
        result = client.read_coils(address=address, count=1, slave=UNIT_ID)
        if not result.isError():
            return result.bits[0]
        return None

    def read_register(client, address):
        result = client.read_holding_registers(address=address, count=1, slave=UNIT_ID)
        if not result.isError():
            return result.registers[0]
        return None

    # Connect to PLC
    client = ModbusTcpClient(PLC_IP, port=PORT)

    if not client.connect():
        print("Failed to connect to PLC")
        exit(1)

    print("=" * 60)
    print("TBFC Drone System - Christmas Restoration")
    print("=" * 60)
    print()

    # Step 1: Check current state
    print("Step 1: Verifying current system state...")
    time.sleep(1)

    package_type = read_register(client, 0)
    protection = read_coil(client, 11)
    armed = read_coil(client, 15)

    print(f"  Package Type: {package_type} (1 = Eggs)")
    print(f"  Protection Active: {protection}")
    print(f"  Self-Destruct Armed: {armed}")
    print()

    # Step 2: Disable protection
    print("Step 2: Disabling protection mechanism...")
    time.sleep(1)

    result = client.write_coil(11, False, slave=UNIT_ID)
    if not result.isError():
        print("  Protection DISABLED")
        print("  Safe to proceed with changes")
    else:
        print("  FAILED to disable protection")
        client.close()
        exit(1)

    print()
    time.sleep(1)

    # Step 3: Change package type to Christmas
    print("Step 3: Setting package type to Christmas presents...")
    time.sleep(1)

    result = client.write_register(0, 0, slave=UNIT_ID)
    if not result.isError():
        print("  Package type changed to: Christmas Presents")
    else:
        print("  FAILED to change package type")

    print()
    time.sleep(1)

    # Step 4: Enable inventory verification
    print("Step 4: Enabling inventory verification...")
    time.sleep(1)

    result = client.write_coil(10, True, slave=UNIT_ID)
    if not result.isError():
        print("  Inventory verification ENABLED")
    else:
        print("  FAILED to enable verification")

    print()
    time.sleep(1)

    # Step 5: Enable audit logging
    print("Step 5: Enabling audit logging...")
    time.sleep(1)

    result = client.write_coil(13, True, slave=UNIT_ID)
    if not result.isError():
        print("  Audit logging ENABLED")
        print("  Future changes will be logged")
    else:
        print("  FAILED to enable logging")

    print()
    time.sleep(2)

    # Step 6: Verify restoration
    print("Step 6: Verifying system restoration...")
    time.sleep(1)

    christmas_restored = read_coil(client, 14)
    new_package_type = read_register(client, 0)
    emergency_dump = read_coil(client, 12)
    self_destruct = read_coil(client, 15)

    print(f"  Package Type: {new_package_type} (0 = Christmas)")
    print(f"  Christmas Restored: {christmas_restored}")
    print(f"  Emergency Dump: {emergency_dump}")
    print(f"  Self-Destruct Armed: {self_destruct}")
    print()

    if christmas_restored and new_package_type == 0 and not emergency_dump and not self_destruct:
        print("=" * 60)
        print("SUCCESS - CHRISTMAS IS SAVED")
        print("=" * 60)
        print()
        print("Christmas deliveries have been restored")
        print("The drones will now deliver presents, not eggs")
        print("Check the CCTV feed to see the results")
        print()
        
        # Read the flag from registers
        flag_result = client.read_holding_registers(address=20, count=12, slave=UNIT_ID)
        if not flag_result.isError():
            flag_bytes = []
            for reg in flag_result.registers:
                flag_bytes.append(reg >> 8)
                flag_bytes.append(reg & 0xFF)
            flag = ''.join(chr(b) for b in flag_bytes if b != 0)
            print(f"Flag: {flag}")
        
        print()
        print("=" * 60)
    else:
        print("Restoration incomplete - check system state")

    client.close()
    print()
    print("Disconnected from PLC")
    ```

    ```cmd
    python3 restore_christmas.py 
    ```

    ![Flag](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ICS-modbus-aoc2025-g3m6n9b1v4/ICS-Modbus_-_Claus_for_Concern_Flag.png)

    We can see that the script has finished and the CCTV shows us that the we have defeated Malhare!

    ><details><summary>Click for answer</summary>THM{eGgMas0V3r}</details>

2.  If you enjoyed today's room, feel free to check out our OT challenge: [Industrial Intrusion](https://tryhackme.com/jr/industrial-intrusion)

    Lets quickly see what would have happened if we were to trigger the trap set. 

    We can slightly modify the restore script to re-enable the protections and then make a change to HR0. This should trigger the trap.

    ![Script2](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ICS-modbus-aoc2025-g3m6n9b1v4/ICS-Modbus_-_Claus_for_Concern_Script2.png)

    ![Destruction](https://github.com/Kevinovitz/TryHackMe_Writeups/raw/main/ICS-modbus-aoc2025-g3m6n9b1v4/ICS-Modbus_-_Claus_for_Concern_Destruction.png)