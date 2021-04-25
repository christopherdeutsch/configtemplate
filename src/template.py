#!/usr/bin/env python3
import sys
import os
import argparse
import yaml
from jinja2 import Template


class StupidTemplate:
  """For when you just need some stupid templates"""
  def __init__(self, template_dirs=[], template_files=[], suffix='.in.yml'):
    self.template_dirs = template_dirs
    self.template_files = template_files
    self.suffix = suffix
    self.root = {}

  def load_templates_from_directories(self, dirs):
    if dirs is None:
      return
    for dir in sorted([item for sublist in dirs for item in sublist]):
      for filename in os.listdir(dir):
        full_filename = os.path.join(dir, filename)
        if full_filename.endswith(self.suffix):
          self.update(full_filename)

  def load_templates_from_files(self, filenames):
    if filenames is None:
      return
    for file in [item for sublist in filenames for item in sublist]:
      self.update(file)

  def update(self, template_filename):
    print("input: {}".format(template_filename), file=sys.stderr)
    self.root.update(yaml.safe_load(open(template_filename, 'r').read()))

  def output(self, filename):
    self.load_templates_from_directories(self.template_dirs)
    self.load_templates_from_files(self.template_files)
    print("output: {}".format(filename), file=sys.stderr)
    outfile = Template(open(filename, 'r').read(), trim_blocks=True)
    print(outfile.render(root=self.root))


p = argparse.ArgumentParser(description='stupid templating, for when nothing else is available')
p.add_argument('-d', '--dir', help='load all files from a directory', action='append', nargs='*')
p.add_argument('-f', '--file', help='load a specific file',  action='append', nargs='*')
p.add_argument('-s', '--suffix', help='suffix of filenames to load from directories', default='.yml')
p.add_argument('input_file', help='input template file')

args = p.parse_args()
st = StupidTemplate(args.dir, args.file, args.suffix)
st.output(args.input_file)
