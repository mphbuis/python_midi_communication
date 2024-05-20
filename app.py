import mido
import rtmidi

print('Current backend:', mido.backend)

outports = mido.get_output_names()
inports = mido.get_input_names()
print('Available outports:', outports)
print('Available inports:', inports)

# doing this i can send midi messages to for example garageband
if outports:
    with mido.open_output(outports[1]) as outport:
        msg = mido.Message('note_on', note=60)
        print('Outputting',msg,'to:', outport.name)
        outport.send(msg)
else:
    print('No MIDI outports available')

# If there are any input ports available
if inports:
    # Open the first input port
    with mido.open_input(inports[0]) as inport:
        print('Listening to:', inport.name)
        
        # Continuously listen to the input port
        while True:
            # Wait for a message and print it
            msg = inport.receive()
            print(msg)
