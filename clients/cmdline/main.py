#!/usr/bin/python

import cmd, shlex, os
from parser import Parser
from engine.reports import generate_individual_student_feedback_report
from engine.feedback_message import save_message, append_feedback

class CmdlineInterface(cmd.Cmd):

	intro = 'EasyMarking v1.0 - Type "help" for help.\n' \
		'Good marking! :)\n'
	prompt = "easyMarker=# "

	def help_newfbmsg(self): Parser.get_parser('newfbmsg').print_help()
	def do_newfbmsg(self, line):
		try:
			parser = Parser.get_parser('newfbmsg')
			args = parser.parse_args(shlex.split(line))
			print save_message(args.alias, args.message, args.mark_value)
		except SystemExit:
			print ""

	def help_mkfb(self): Parser.get_parser('mkfb').print_help()
	def do_mkfb(self, line):
		try:
			parser = Parser.get_parser('mkfb')
			args = parser.parse_args(shlex.split(line))
			print append_feedback(
				args.alias, 
				args.student_id, 
				"COMP 4350", 
				1, 
				100
			)
		except SystemExit:
			print ""	

	#def help_sturep(self): Parser.get_parser('mkfb').print_help()
	def do_sturep(self, line):
		generate_individual_student_feedback_report('umkonkin', "COMP 4350", 1)

	def do_cd(self, line):
		os.chdir(line)

	def default(self, line):
		os.system(line)

	def do_exit(self, line):
		return True;		

	def do_quit(self, line):
		return True;

	def do_EOF(self, line):
		print "\n"
		return True	
