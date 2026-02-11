# DTMF Home Automation Simulator
# Run this in VS Code to see how phone tones turn into commands

def dtmf_decoder_sim(key):
    # DTMF Frequency Table (Low, High) in Hz
    dtmf_table = {
        '1': (697, 1209, "0001"), '2': (697, 1336, "0010"), '3': (697, 1477, "0011"),
        '4': (770, 1209, "0100"), '5': (770, 1336, "0101"), '6': (770, 1477, "0110"),
        '7': (852, 1209, "0111"), '8': (852, 1336, "1000"), '9': (852, 1477, "1001"),
        '0': (941, 1336, "1010"), '*': (941, 1209, "1011"), '#': (941, 1477, "1100")
    }

    if key in dtmf_table:
        low, high, binary = dtmf_table[key]
        print(f"\n--- DTMF SIGNAL DETECTED: KEY {key} ---")
        print(f"Frequencies: {low}Hz (Low) + {high}Hz (High)")
        print(f"Binary Output (to Arduino): {binary}")
        
        # Simulation of Home Automation Action
        if key == '1':
            print("ACTION: Light 1 is now ON")
        elif key == '2':
            print("ACTION: Fan is now ON")
        elif key == '0':
            print("ACTION: ALL APPLIANCES OFF")
        else:
            print(f"ACTION: Command '{key}' received (No specific action assigned)")
    else:
        print("Invalid Key! Press 0-9, * or #")

# Main Loop
print("--- DTMF HOME AUTOMATION VIRTUAL TERMINAL ---")
while True:
    user_input = input("\nEnter phone key pressed (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    dtmf_decoder_sim(user_input)