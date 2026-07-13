# ASCII code for 'A'
char = 'A'
ascii_val = ord(char)  # 65

# CPU uses adders to compute memory address
base_address = 1000
address = base_address + ascii_val  # simulated with addition

# CPU uses multipliers to scale font size
font_size = 2
pixel_position = ascii_val * font_size  # simulated with multiplication

print("Stored at:", address, "Pixel position:", pixel_position)
