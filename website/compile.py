import sys
import os
from jinja2 import Environment, FileSystemLoader
from model.rank_teams import get_rankings

file_loader = FileSystemLoader(os.getcwd() + '/website/templates')
env = Environment(loader=file_loader)


def make_index_page():
  index_template = env.get_template('index.jinja2')
  rankings = get_rankings()
  teams = list(map(lambda x: {'team': x[0], 'score': x[1]}, rankings))
  static_index = index_template.render(teams=teams)
  os.makedirs(os.getcwd() + '/website/build', exist_ok=True)
  with open(f'website/build/index.html', 'w') as f:
    f.write(static_index)


def build():
  make_index_page()


if __name__ == '__main__':
  build()
