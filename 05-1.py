from utils import read_inputs

inputs = read_inputs("inputday5.txt")

def get_seat_id(seat_hash):
  seat_row = seat_hash[:7] # FBFBBFF
  seat_column = seat_hash[7:] # RLR
  seat_row_binary = "".join(["1" if letter=="B" else "0" for letter in seat_row]) # "010..."
  seat_column_binary = "".join(["1" if letter=="R" else "0" for letter in seat_column]) # "101"
  return int(seat_row_binary, 2) * 8 + int(seat_column_binary, 2)

seat_ids = [get_seat_id(seat_hash) for seat_hash in inputs]
max(seat_ids)

print(max(seat_ids))

my_seat=set(range(min(seat_ids),max(seat_ids)))-set(seat_ids)
print(my_seat)