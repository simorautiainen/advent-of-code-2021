import math
import itertools
import ast
import functools

with open("inputs/day21") as data:
  f = data.readlines()
  player1_starting = int(f[0].split(' ')[-1])
  player2_starting = int(f[1].split(' ')[-1])

def get_loser_score_times_dice_throws(p1_starting: int, p2_starting: int) -> int:
  cube_iter = itertools.cycle(range(1, 100+1))
  player_cur = [p1_starting, p2_starting]
  player_scores=[0, 0]

  die_rolls = 0
  while player_scores[0] < 1000 and player_scores[1] < 1000:
    for i in range(2):
      for _ in range(3):
        cube = next(cube_iter)
        player_cur[i] += cube
      player_cur[i] = (player_cur[i]%10) if (player_cur[i] % 10) != 0 else 10
      player_scores[i] += player_cur[i]
      die_rolls += 3
      if player_scores[i] >= 1000:
        return min(player_scores)*die_rolls


print("Part 1:", get_loser_score_times_dice_throws(player1_starting, player2_starting))

@functools.cache
def rec_cube_ref(cur_player: int, cur_player_score: int, other_player: int, other_player_score: int, is_starting: bool = True) -> tuple[int, int]:
  winners = (0, 0)
  for i in range(1,4):
    for k in range(1, 4):
      for c in range(1, 4):
        cur_iter_player = cur_player + i + k + c
        cur_iter_player = (cur_iter_player % 10) if (cur_iter_player % 10) != 0 else 10
        cur_iter_player_score = cur_player_score + cur_iter_player
        if cur_iter_player_score >= 21:
          winners = (winners[0] + is_starting, winners[1] + (not is_starting))
        else:
          all_this_path_winners = rec_cube_ref(other_player, other_player_score, cur_iter_player, cur_iter_player_score, not is_starting)
          winners = (winners[0]+all_this_path_winners[0], winners[1]+all_this_path_winners[1])
  return winners


print("Part 2", max(rec_cube_ref(player1_starting, 0, player2_starting, 0)))