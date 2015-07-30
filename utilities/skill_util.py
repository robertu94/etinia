#!/usr/bin/env python3

import sys
import json
import argparse
import logging

logging.basicConfig(level=logging.DEBUG)

def json_to_tex(jsonstr):
    """
    Function that convers the json format to LaTeX
    input:
        str jsonstr - string containing json to print as the latex
    return:
        str tex - tex converted from json

    """
    """
    tree
        - section_header
        - tree_omega
        - skill
        - elemental
    """
    skills = json.loads(jsonstr)

    converters = {'Knowledge':convert_knowledge,
                  'Magic': convert_magic,
                  'Basic': convert_basic}
    tex = "\\chapter{Skills}\n"
    for tree in sorted(skills):
        logging.info("Starting section %s", tree)
        tex += converters.get(tree, convert_general)(skills[tree], tree)
        logging.info("Finishing section %s", tree)
    return tex

def convert_knowledge(desc, treename):
    """
    Method for converting the knowledge skills section
    """
    logging.info("parsing with convert knowledge")
    tex = convert_section(desc, treename)
    tex += convert_elemental(desc['elemental'])
    tex += convert_skills_knowledge(desc['skills'])
    return tex

def convert_magic(desc, treename):
    """
    Method for converting the magic skills section
    """
    logging.info("parsing with convert magic")
    tex = convert_section_magic(desc, treename)
    tex += convert_elemental_magic(desc['elemental'])
    tex += convert_skills(desc['skills'])
    return tex

def convert_basic(desc, treename):
    """
    Method for converting the basic skills section
    """
    logging.info("parsing with convert basic")
    return desc['section_header']

def convert_general(desc, treename):
    """
    Default method for converting a skill tree to tex
    """
    logging.info("parsing with convert general")
    tex = convert_section(desc, treename)
    tex += convert_elemental(desc['elemental'])
    tex += convert_skills(desc['skills'])
    return tex

def convert_section(desc, treename):
    """
    Default method for converting a section header
    """
    logging.info("parsing with convert section")
    tex = "\\section{{{section_name}}}\\index{{{section_name}}}\n".format(section_name=treename)
    if desc['section_header'] != '':
        tex += "{}\\\\\n".format(desc['section_header'])
    if desc['tree_omega'] != '':
        tex += "$Tree \\Omega$: {}\n".format(desc['tree_omega'])
    return tex

def convert_section_magic(desc, treename):
    """
    Method for converting a section header Magics
    """
    logging.info("parsing with convert section magic")
    tex = "\\section{{{section_name}}}\\index{{{section_name}}}\n".format(section_name=treename)
    tex += "{}\\\\\n".format(desc['section_header'])
    tex += "$Tree \\Omega$: {}\n".format(desc['tree_omega'])
    return tex

def convert_elemental(desc):
    """
    Default Method that represents the standard way of converting elements
    """
    logging.info("parsing with convert elemental")
    tex = "\\subsection{{Elemental Affinity}}\n{}".format(desc['description'])
    desc = {i:desc[i] for i in desc if desc[i] != ''}
    logging.debug("Length of elemental after removing empty elements %d", len(desc))
    if len(desc) > 1:
        tex += '\\begin{itemize}'
    elif len(desc) == 0:
        tex += 'There are currently no elemental affinities for this skill tree.  Coming soon'

    for element in sorted(desc):
        if element == 'description':
            continue
        tex += "\t\\item {element_name}: {ability}\n".format(element_name=element,
                                                             ability=desc[element])
    if len(desc) > 1:
        tex += '\\end{itemize}'
    return tex

def convert_elemental_magic(desc):
    """
    Default Method that represents the standard way of converting elements
    """
    logging.info("parsing with convert elemental magic")
    tex = "\\subsection{{Elemental Affinity}}\n{}".format(desc['description'])
    tex += '\\begin{itemize}\n'
    for element in sorted(desc):
        logging.debug(element)
        if element == 'description':
            continue
        for ability in desc[element]:
            logging.debug(ability)
            tex += "\t\\item {element_name}: {ability} ({difficulty})\n"\
                    .format(element_name=element, ability=ability['Ability'],
                            difficulty=ability['Difficulty'])
    tex += '\\end{itemize}\n'
    return tex


def convert_skills(desc):
    """
    Method that represents the standard way of converting skills
    """
    logging.info("parsing with convert skills")
    tex = ""
    for skill in sorted(desc):
        tex += '\\noindent\n'
        tex += '\\subsection{{{skill_name}}}\\index{{{skill_name}}}\n'.format(skill_name=skill)
        tex += '\\rowcolors{1}{white}{white}\n'
        tex += '\\begin{tabularx}{\\textwidth}{l X}\n'
        tex += '\\textbf{{Level 1:}}& {level1} \\\\\n'.format(level1=desc[skill]['level1'])
        tex += '\\textbf{{Level 2:}}& {level2} \\\\\n'.format(level2=desc[skill]['level2'])
        tex += '\\textbf{{Level 3:}}& {level3} \\\\\n'.format(level3=desc[skill]['level3'])
        tex += '\\textbf{{Level 4:}}& {level4} \\\\\n'.format(level4=desc[skill]['level4'])
        tex += '\\textbf{{Level 5:}}& {level5} \\\\\n'.format(level5=desc[skill]['level5'])
        tex += '\\textbf{{Level $\\Omega$:}}& {level_omega} \\\\\n'\
                .format(level_omega=desc[skill]['omega'])
        tex += '\\end{tabularx}\n'
        tex += '\\ignorespacesafterend\n\n'
    return tex


def convert_skills_knowledge(desc):
    """
    Method that represents the standard way of converting skills
    """
    logging.info("parsing with convert skills knowledge")
    tex = ""
    for skill in sorted(desc):
        tex += '\\noindent\n'
        tex += '\\subsection{{{skill_name}}}\\index{{{skill_name}}}\n'.format(skill_name=skill)
        tex += '\\rowcolors{1}{white}{white}\n'
        tex += '\\begin{tabularx}{\\textwidth}{l X}\n'
        tex += '\\textbf{{Level 1:}}& {level1} \\\\\n'.format(level1=desc[skill]['level1'])
        tex += '\\textbf{{Level 2:}}& {level2} \\\\\n'.format(level2=desc[skill]['level2'])
        tex += '\\textbf{{Level 3:}}& {level3} \\\\\n'.format(level3=desc[skill]['level3'])
        tex += '\\textbf{{Level 4:}}& {level4} \\\\\n'.format(level4=desc[skill]['level4'])
        tex += '\\textbf{{Level 5:}}& {level5} \\\\\n'.format(level5=desc[skill]['level5'])
        tex += '\\textbf{{Level $\\Omega$:}}& {level_omega} \\\\\n'\
                .format(level_omega=desc[skill]['omega'])
        tex += '\\textbf{{Further :}}& {further} \\\\\n'.format(further=desc[skill]['further'])
        tex += '\\textbf{{Greater :}}& {greater} \\\\\n'.format(greater=desc[skill]['greater'])
        tex += '\\end{tabularx}\n'
        tex += '\\ignorespacesafterend\n\n'
    return tex


def parse_args():
    """
    Parse the arguments that come from the command line
    """
    parser = argparse.ArgumentParser(
        description="""A tool that converts the skills file to ini and tex and
        back""")
    parser.add_argument("to", choices=['tex',], default='tex',
                        help="direction of conversion")
    parser.add_argument("infile", type=argparse.FileType('r'),
                        help="file to read in as input")
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'),
                        default=sys.stdout, help="file to read in as input")
    return parser.parse_args()


if __name__ == '__main__':
    ARGS = parse_args()
    infile = ARGS.infile.read()
    if ARGS.to == 'tex':
        ARGS.outfile.write(json_to_tex(infile))
    else:
        raise NotImplementedError
