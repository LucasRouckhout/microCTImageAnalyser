#!/usr/bin/env python3

import sys

def ask():
  reply = input(">> ")
  
  if reply == 'quit':
    sys.exit()
  
  return reply
  
