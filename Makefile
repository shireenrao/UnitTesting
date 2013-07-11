.PHONY: all type1 type2 type3

all: type1 type2 type3

verbose: type1_verbose type2_verbose type3_verbose

type1:
	cd Type1; make tests

type1_verbose:
	cd Type1; make verbose_tests

type2:
	cd Type2; make tests

type2_verbose:
	cd Type2; make verbose_tests

type3:
	cd Type3; make tests

type3_verbose:
	cd Type3; make verbose_tests

